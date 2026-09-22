import ollama

class ChatBot:
    def __init__(self, model="llama3"):
        self.model = model

    def set_model(self, model):
        self.model = model

    def get_available_models(self):
        """Fetch list of available models from Ollama."""
        try:
            models_info = ollama.list()
            # Handle different return types of ollama.list()
            if hasattr(models_info, 'models'):
                return [m.model for m in models_info.models]
            return [m['name'] for m in models_info]
        except Exception as e:
            print(f"Error fetching models: {e}")
            return ["llama3"]

    def chat(self, messages):
        """
        Send messages to Ollama and return the response content.
        'messages' should be a list of {'role': 'user/assistant', 'content': '...'}
        """
        response = ollama.chat(
            model=self.model,
            messages=messages,
        )
        return response['message']['content']
