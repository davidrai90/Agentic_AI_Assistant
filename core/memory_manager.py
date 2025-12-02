"""
memory_manager.py
-----------------
This module provides a simple in-memory context system
for the Agentic AI Assistant. It stores and retrieves 
recent conversation history for contextual understanding.
"""

from typing import List, Dict

class MemoryManager:
    def __init__(self, max_memory: int = 10):
        """
        Initialize memory storage.

        Args:
            max_memory (int): Number of recent interactions to retain.
        """
        self.max_memory = max_memory
        self.memory: List[Dict[str, str]] = []

    def add_to_memory(self, user_input: str, ai_response: str):
        """
        Store a conversation pair in memory.
        Automatically removes oldest memory if limit is reached.
        """
        if len(self.memory) >= self.max_memory:
            self.memory.pop(0)  # remove oldest
        self.memory.append({
            "user": user_input,
            "assistant": ai_response
        })

    def get_context(self, limit: int = 5) -> str:
        """
        Return the recent memory context as a single string.
        Used to provide LLM with background conversation context.
        """
        context_items = self.memory[-limit:]
        context_text = "\n".join(
            [f"User: {m['user']}\nAI: {m['assistant']}" for m in context_items]
        )
        return context_text.strip()

    def clear_memory(self):
        """Clear all stored memory."""
        self.memory = []

    def __repr__(self):
        """Developer-friendly display of memory contents."""
        return f"<MemoryManager: {len(self.memory)} entries>"

# Example run (for testing only)
if __name__ == "__main__":
    memory = MemoryManager(max_memory=3)
    memory.add_to_memory("Hi", "Hello! How can I assist?")
    memory.add_to_memory("What's your name?", "I'm your AI Agent.")
    memory.add_to_memory("Where is the server located?", "In Helsinki data center.")
    print(memory.get_context())
