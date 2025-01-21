import tkinter as tk
from tkinter import scrolledtext
from bert_summarizer import BertSummarizer
from gpt2_summarizer import GPT2Summarizer
from xlnet_summarizer import XLNetSummarizer

# Initialize summarizers
bert_summarizer = BertSummarizer()
gpt2_summarizer = GPT2Summarizer()
xlnet_summarizer = XLNetSummarizer()

def summarize_text():
    input_text = input_box.get("1.0", tk.END).strip()
    if not input_text:
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, "Please enter some text to summarize.")
        return

    selected_model = model_var.get()
    if selected_model == "BERT":
        summary = bert_summarizer.summarize(input_text, min_length=60)
    elif selected_model == "GPT2":
        summary = gpt2_summarizer.summarize(input_text, min_length=60)
    elif selected_model == "XLNet":
        summary = xlnet_summarizer.summarize(input_text, min_length=60)
    else:
        summary = "Invalid model selection."

    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, summary)

# Create GUI
root = tk.Tk()
root.title("Text Summarization")

# Input Text Label and Box
tk.Label(root, text="Enter Text to Summarize:").pack(pady=5)
input_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=10)
input_box.pack(pady=5)

# Model Selection
tk.Label(root, text="Select Model:").pack(pady=5)
model_var = tk.StringVar(value="BERT")
tk.Radiobutton(root, text="BERT", variable=model_var, value="BERT").pack(anchor="w", padx=20)
tk.Radiobutton(root, text="GPT2", variable=model_var, value="GPT2").pack(anchor="w", padx=20)
tk.Radiobutton(root, text="XLNet", variable=model_var, value="XLNet").pack(anchor="w", padx=20)

# Summarize Button
summarize_button = tk.Button(root, text="Summarize", command=summarize_text)
summarize_button.pack(pady=10)

# Output Text Label and Box
tk.Label(root, text="Summary:").pack(pady=5)
output_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=10)
output_box.pack(pady=5)

# Run the GUI
root.mainloop()
