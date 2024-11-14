from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline
import json

# Load Hugging Face model and tokenizer
model_name = "distilbert-base-uncased-distilled-squad"
model = AutoModelForQuestionAnswering.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
nlp_pipeline = pipeline("question-answering", model=model, tokenizer=tokenizer)

# Load FAQs for faster responses to common questions
with open("data/tax_faq.json") as f:
    tax_faq = json.load(f)

def get_answer(question):
    # Check if question is in our FAQ
    question_lower = question.lower()
    if question_lower in tax_faq:
        return tax_faq[question_lower]
    
    # Otherwise, use DistilBERT to answer
    context = " ".join(tax_faq.values())  # Use FAQs as context for DistilBERT
    result = nlp_pipeline({"question": question, "context": context})
    return result["answer"]
