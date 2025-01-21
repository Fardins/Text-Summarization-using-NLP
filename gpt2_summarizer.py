from summarizer import TransformerSummarizer

class GPT2Summarizer:
    def __init__(self):
        self.model = TransformerSummarizer(transformer_type="GPT2", transformer_model_key="gpt2-medium")

    def summarize(self, text, min_length=60):
        return ''.join(self.model(text, min_length=min_length))
