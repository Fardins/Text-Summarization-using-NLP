from summarizer import TransformerSummarizer

class XLNetSummarizer:
    def __init__(self):
        self.model = TransformerSummarizer(transformer_type="XLNet", transformer_model_key="xlnet-base-cased")

    def summarize(self, text, min_length=60):
        return ''.join(self.model(text, min_length=min_length))
