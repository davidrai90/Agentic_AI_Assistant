"""
llm_manager.py
---------------
This module connects to an open-source Hugging Face model (FLAN-T5)
and provides a text generation function that also integrates memory context.
"""

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
from core.memory_manager import MemoryManager  # ✅ Import memory class

# 🔹 Step 1: Load a lightweight open-source model
MODEL_NAME = "google/flan-t5-small"

print(f"🔄 Loading model: {MODEL_NAME} ...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
print("✅ Model loaded successfully!\n")

# 🔹 Step 2: Initialize MemoryManager
memory = MemoryManager(max_memory=5)


def generate_text(user_input: str, max_tokens: int = 150) -> str:
    """
    Generate a response using the model with conversational context.
    """
    # Get recent context from memory
    context = memory.get_context()
    prompt = f"Conversation so far:\n{context}\n\nUser: {user_input}\nAI:"

    # Tokenize and generate response
    inputs = tokenizer(prompt, return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(**inputs, max_new_tokens=max_tokens)

    response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

    # Save interaction in memory
    memory.add_to_memory(user_input, response)
    return response


# 🔹 Example run
if __name__ == "__main__":
    print("🧠 Agentic AI Chat Started!\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Exiting Agentic Chat.")
            break
        ai_reply = generate_text(user_input)
        print(f"AI: {ai_reply}\n")

