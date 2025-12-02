"""
main.py
--------
Central controller for the Agentic AI Assistant.
It connects Planner, LLM, and Memory modules to form
a working cognitive AI loop.
"""

from core.planner import Planner
from core.llm_manager import generate_text
from core.memory_manager import MemoryManager

# Initialize core components
planner = Planner()
memory = MemoryManager()

print("\n🤖 Agentic AI Assistant Ready!")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("👋 Exiting Agentic AI Assistant.")
        break

    # 🧠 Step 1: Decide what to do next
    action = planner.decide_next_action(user_input)
    print(f"🧭 Planner chose action: {action}")

    # 🧩 Step 2: Get context from memory
    context = memory.get_context()
    prompt = f"Context:\n{context}\n\nUser: {user_input}\nAI:"

    # 💬 Step 3: Generate a response
    ai_response = generate_text(prompt)
    print(f"AI: {ai_response}\n")

    # 🧠 Step 4: Store this interaction
    memory.add_to_memory(user_input, ai_response)
