# ai_integration.py
from typing import List
from transformers import pipeline

# ----------------------------
# Lightweight summarization model for local testing
# ----------------------------
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

# ----------------------------
# AI Functions
# ----------------------------
def ai_summarize(text: str) -> str:
    """Summarize the LoM using the lightweight model."""
    try:
        summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        print("Summarization error:", e)
        return "\n".join(text.splitlines()[:3])

def ai_extract_keywords(text: str) -> List[str]:
    """Extract simple keywords."""
    words = text.replace("\n", " ").split()
    unique_words = list(dict.fromkeys(words))
    return unique_words[:10]

def ai_strengths_analysis(text: str) -> List[str]:
    """Return 3 inferred strengths using simple keyword logic."""
    strengths_keywords = ["Analytical", "Motivated", "Creative", "Detail-Oriented"]
    return [kw for kw in strengths_keywords if kw.lower() in text.lower()] or ["Analytical", "Motivated", "Detail-Oriented"]
