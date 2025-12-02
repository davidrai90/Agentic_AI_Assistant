"""
planner.py
-----------
This module analyzes user input and decides which agent
or workflow should handle the task.
"""

from core.llm_manager import generate_text

class Planner:
    def __init__(self):
        self.available_agents = ["task", "email", "report"]

    def decide_next_action(self, user_input: str) -> str:
        """
        Use a small reasoning prompt to decide what to do.
        """
        reasoning_prompt = f"""
        You are a planning assistant.
        The user said: "{user_input}"
        Decide which agent to use: task, email, report, or chat only.
        Answer in one word.
        """
        decision = generate_text(reasoning_prompt)
        return decision.lower().strip()

# Example usage
if __name__ == "__main__":
    planner = Planner()
    while True:
        text = input("You: ")
        if text.lower() in ["exit", "quit"]:
            break
        action = planner.decide_next_action(text)
        print(f"🧭 Planner decided: {action}")
