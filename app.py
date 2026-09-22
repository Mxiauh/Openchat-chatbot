import streamlit as st
from openchat.chatbot import ChatBot
from openchat.rag import process_document, augment_prompt

st.set_page_config(page_title="OpenChat Local AI", page_icon="🤖")

# Initialize ChatBot and Session State
if "chatbot" not in st.session_state:
    st.session_state.chatbot = ChatBot()

if "messages" not in st.session_state:
    st.session_state.messages = []

if "context" not in st.session_state:
    st.session_state.context = ""

# --- Sidebar ---
with st.sidebar:
    st.title("⚙️ Settings")

    # Model Selection
    available_models = st.session_state.chatbot.get_available_models()
    selected_model = st.selectbox("Select AI Model", available_models, index=available_models.index("llama3") if "llama3" in available_models else 0)
    st.session_state.chatbot.set_model(selected_model)

    st.divider()

    # RAG - Document Upload
    st.subheader("📚 Knowledge Base")
    uploaded_file = st.file_uploader("Upload PDF or TXT", type=["pdf", "txt"])

    if uploaded_file:
        with st.spinner("Processing document..."):
            st.session_state.context = process_document(uploaded_file)
            st.success("Document processed!")

    st.divider()

    # Clear Chat
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.session_state.context = ""
        st.rerun()

# --- Main Chat Interface ---
st.title("🤖 OpenChat")
st.caption("Powered by Ollama Local AI")

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Ask me anything..."):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)

    # Add user message to chat history
    # Apply RAG augmentation if context exists
    final_prompt = augment_prompt(prompt, st.session_state.context)

    # We store the original prompt in history for the UI,
    # but we send the augmented one to the model.
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        # Create the message list for Ollama (including history)
        # Note: We use augmented prompt for the last message
        ollama_messages = [m for m in st.session_state.messages]
        ollama_messages[-1] = {"role": "user", "content": final_prompt}

        try:
            # Get response from ChatBot
            response_text = st.session_state.chatbot.chat(ollama_messages)
            full_response = response_text
            message_placeholder.markdown(full_response)
        except Exception as e:
            st.error(f"Error communicating with Ollama: {e}")
            full_response = "Sorry, I encountered an error."
            message_placeholder.markdown(full_response)

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
