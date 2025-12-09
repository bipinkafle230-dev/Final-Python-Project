# Start the project
"""This project flashcard for 
routine work flow for study.
"""
# Assignment of Python projects
# console based
# Description of project: Your project needs to have one compulsory main function 
# and at least 4 functions or classes. 
# The project should be CLI based. Feel free to be creative. 
# Submit the project through git repository in the dedicated google sheet.
# readme file is compulsory

# Flashcard CLI App 

# Flashcard structure
class Flashcard:
    def __init__(self, topic, question, answer):
        self.topic = topic
        self.question = question
        self.answer = answer
        self.correct = 0
        self.incorrect = 0

# Function 1: Add a flashcard
def add_flashcard(deck):
    print("\n➕ Add New Flashcard")
    topic = input("Topic: ").strip()
    question = input("Question: ").strip()
    answer = input("Answer: ").strip()
    if topic and question and answer:
        deck.append(Flashcard(topic, question, answer))
        print("✅ Flashcard added.")
    else:
        print("❌ All fields are required.")

# Function 2: Review all flashcards
def review_flashcards(deck):
    print("\n📚 Review All Flashcards")
    if not deck:
        print("No flashcards to review.")
        return
    for i, card in enumerate(deck, 1):
        print(f"\n[{i}] Topic: {card.topic}")
        print(f"Q: {card.question}")
        print(f"A: {card.answer}")
        print(f"Stats: ✅ {card.correct} | ❌ {card.incorrect}")

# Function 3: Manual shuffle (Fisher-Yates without random)
def manual_shuffle(deck):
    print("\n🔀 Shuffling cards manually...")
    for i in range(len(deck) - 1, 0, -1):
        j = (i * 3) % len(deck)  # Simple deterministic swap index
        deck[i], deck[j] = deck[j], deck[i]
    return deck

# Function 4: Start quiz
def start_quiz(deck):
    print("\n🎯 Start Quiz")
    if not deck:
        print("No flashcards to quiz.")
        return
    quiz_deck = manual_shuffle(deck.copy())
    for i, card in enumerate(quiz_deck, 1):
        print(f"\nCard {i}/{len(quiz_deck)}")
        print(f"Topic: {card.topic}")
        print(f"Q: {card.question}")
        user_input = input("Your answer: ").strip()
        if user_input.lower() == card.answer.lower():
            print("✅ Correct!")
            card.correct += 1
        else:
            print(f"❌ Incorrect. Correct answer: {card.answer}")
            card.incorrect += 1
        input("Press Enter to continue...")

# Function 5: Show statistics
def show_stats(deck):
    print("\n📊 Flashcard Stats")
    total = len(deck)
    correct = sum(card.correct for card in deck)
    incorrect = sum(card.incorrect for card in deck)
    attempts = correct + incorrect
    print(f"Total Cards: {total}")
    print(f"Attempts: {attempts}")
    print(f"Correct: {correct}")
    print(f"Incorrect: {incorrect}")
    if attempts > 0:
        print(f"Accuracy: {correct / attempts * 100:.1f}%")

# Main function
def main():
    deck = []
    while True:
        print("\n" + "=" * 40)
        print("FLASHCARD MENU")
        print("1. Add Flashcard")
        print("2. Review Flashcards")
        print("3. Start Quiz")
        print("4. Show Stats")
        print("5. Exit")
        choice = input("Choose (1-5): ").strip()
        if choice == '1':
            add_flashcard(deck)
        elif choice == '2':
            review_flashcards(deck)
        elif choice == '3':
            start_quiz(deck)
        elif choice == '4':
            show_stats(deck)
        elif choice == '5':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.")

# Entry point
if __name__ == "__main__":
    main()


# end of Program !!
