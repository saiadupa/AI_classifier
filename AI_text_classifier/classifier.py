from transformers import pipeline
import re

def chunk_text(text, chunk_size=200):
    chunks = []
    words = re.findall(r'\b\w+\b', text)
    for i in range(0, len(words), chunk_size):
        chunk = ' '.join(words[i:i+chunk_size])
        chunks.append(chunk)
    return chunks

def classify_text(text_chunks):
    pipe = pipeline("text-classification", model="roberta-base-openai-detector")
    total_score = 0.0
    labels = []
    for chunk in text_chunks:
        result = pipe(chunk)
        label = result[0]['label']
        score = result[0]['score']
        total_score += score
        labels.append(label)
    avg_score = total_score / len(text_chunks)
    return avg_score, labels

def classify_and_print(text):
    words = re.findall(r'\b\w+\b', text)
    if len(words) < 120:
        print("Need at least 120 words to process to maintain accuracy.")
        return
    chunks = chunk_text(text)
    score, labels = classify_text(chunks)
    avg_label = max(set(labels), key=labels.count) 
    confidence_type = "AI confidence" if avg_label == "REAL" else "Human confidence"
    print(f"The text is '{avg_label}' with {score * 100:.2f}% confidence.")
    print(f"This is {confidence_type}.")
