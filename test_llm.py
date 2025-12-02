from core.llm_manager import generate_text

if __name__ == "__main__":
    prompt = "Summarize: Server down in Helsinki data center due to power issue."
    result = generate_text(prompt)
    print("Model Output:\n", result)
