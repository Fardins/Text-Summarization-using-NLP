from summarizer import Summarizer

class BertSummarizer:
    def __init__(self):
        self.model = Summarizer()

    def summarize(self, text, min_length=60):
        return ''.join(self.model(text, min_length=min_length))