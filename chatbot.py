# ============================================================
#  DecodeLabs | Batch 2026 | Project 1: Rule-Based AI Chatbot
#  Architecture: IPO Model  |  Lookup: O(1) Dictionary
# ============================================================

# ── KNOWLEDGE BASE ──────────────────────────────────────────
RESPONSES = {
    # Greetings
    "hello":        "Hey there! I'm DecodeBot. How can I help you today?",
    "hi":           "Hi! Welcome to DecodeLabs. What's on your mind?",
    "hey":          "Hey! Ready to build something great today?",

    # Identity
    "who are you":  "I'm DecodeBot — a rule-based AI built at DecodeLabs.",
    "what are you": "I'm a deterministic chatbot powered by pure Python logic. No hallucinations, guaranteed!",
    "your name":    "My name is DecodeBot. Nice to meet you!",

    # DecodeLabs info
    "what is decodelabs": "DecodeLabs is an industrial AI training program that turns interns into professional AI engineers.",
    "about decodelabs":   "DecodeLabs provides hands-on AI project training. You're currently on Project 1!",

    # Project info
    "what is project 1":  "Project 1 is the Rule-Based AI Chatbot — your foundation milestone at DecodeLabs.",
    "project 1":          "Project 1 focuses on control flow, decision-making logic, and basic AI concepts.",

    # Feelings / smalltalk
    "how are you":   "I'm running at 100% uptime — no bugs today! How about you?",
    "i am fine":     "Glad to hear it! Let's get to work.",
    "i am good":     "Great! Let's build something cool.",
    "i am bad":      "Sorry to hear that. Take a breath — coding will cheer you up!",

    # Help
    "help":          "I can answer questions about DecodeLabs, Project 1, or just chat. Try: 'what is AI?' or 'who are you'.",
    "what can you do": "I can respond to greetings, answer questions about DecodeLabs, explain AI concepts, and keep you company!",

    # AI concepts
    "what is ai":           "AI (Artificial Intelligence) is the simulation of human intelligence by machines using logic, data, and learning.",
    "what is machine learning": "Machine Learning is a subset of AI where systems learn patterns from data instead of following explicit rules.",
    "what is a chatbot":    "A chatbot is a program designed to simulate conversation with humans — like me!",
    "what is rule based ai":"Rule-based AI uses explicit if-else logic and dictionaries to respond. It's deterministic — same input, same output, every time.",

    # Farewells
    "bye":       "Goodbye! Keep building. See you next session!",
    "goodbye":   "Farewell, engineer! Project 1 awaits your final submission.",
    "see you":   "See you soon! Don't forget to push your code.",
    "take care": "You too! Keep learning, keep building.",
}

FALLBACK = "I don't have a rule for that yet. Try asking something else, or type 'help'."
EXIT_COMMANDS = {"exit", "quit", "q"}

# ── PHASE 1: INPUT & SANITIZATION ───────────────────────────
def sanitize(raw: str) -> str:
    """Normalize input: lowercase + strip whitespace."""
    return raw.lower().strip()

# ── PHASE 2: PROCESS (Intent Matching) ──────────────────────
def get_response(clean_input: str) -> str:
    """O(1) dictionary lookup with fallback."""
    return RESPONSES.get(clean_input, FALLBACK)

# ── PHASE 3: OUTPUT & FEEDBACK LOOP ─────────────────────────
def run_chatbot():
    print("=" * 55)
    print("  DecodeBot v1.0 | DecodeLabs Industrial Training Kit")
    print("  Type 'exit' or 'quit' to end the session.")
    print("=" * 55)

    while True:                                   # ← THE HEARTBEAT
        raw_input_text = input("\nYou: ")
        clean_input    = sanitize(raw_input_text) # ← SANITIZATION

        if clean_input in EXIT_COMMANDS:          # ← EXIT STRATEGY
            print("\nDecodeBot: Session terminated. Goodbye, engineer!")
            break

        reply = get_response(clean_input)         # ← DICT LOOKUP O(1)
        print(f"DecodeBot: {reply}")

# ── ENTRY POINT ──────────────────────────────────────────────
if __name__ == "__main__":
    run_chatbot()