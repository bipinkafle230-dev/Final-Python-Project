# Start the project
"""This project flashcard for 
routine work flow for study.
"""

import csv
import random
import os

class Flashcard:
    def __init__(self, topic, question, answer, correct=0, incorrect=0):
        self.topic = topic
        self.question = question
        self.answer = answer
        self.correct = int(correct)
        self.incorrect = int(incorrect)

    def to_list(self):
        return [self.topic, self.question, self.answer, str(self.correct), str(self.incorrect)]

    def display(self, show_answer=False):
        print(f"\nTopic: {self.topic}")
        print(f"Q: {self.question}")
        if show_answer:
            print(f"A: {self.answer}")
            print(f"Stats: ✅ {self.correct} | ❌ {self.incorrect}")

class FlashcardApp:
    def __init__(self, filename='flashcards.csv'):
        self.filename = filename
        self.flashcards = []
        self.load_flashcards()

    def load_flashcards(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', newline='', encoding='utf-8') as f:
                    reader = csv.reader(f)
                    next(reader, None)  # Skip header
                    self.flashcards = [Flashcard(*row) for row in reader]
                print(f"✅ Loaded {len(self.flashcards)} flashcards from {self.filename}")
            except Exception as e:
                print(f"❌ Error loading flashcards: {e}")
        else:
            print("📁 No existing flashcard file found. Starting fresh.")

    def save_flashcards(self):
        try:
            with open(self.filename, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['topic', 'question', 'answer', 'correct', 'incorrect'])
                for card in self.flashcards:
                    writer.writerow(card.to_list())
            print(f"💾 Saved {len(self.flashcards)} flashcards to {self.filename}")
        except Exception as e:
            print(f"❌ Error saving flashcards: {e}")

    def add_flashcard(self):
        print("\n➕ ADD NEW FLASHCARD")
        topic = input("Enter topic: ").strip()
        question = input("Enter question: ").strip()
        answer = input("Enter answer: ").strip()

        if topic and question and answer:
            self.flashcards.append(Flashcard(topic, question, answer))
            print("✅ Flashcard added successfully!")
        else:
            print("❌ All fields are required!")

    def review_all(self):
        print("\n📚 REVIEW ALL FLASHCARDS")
        if not self.flashcards:
            print("No flashcards available. Add some first!")
            return

        for i, card in enumerate(self.flashcards, 1):
            print(f"\n[{i}/{len(self.flashcards)}]")
            card.display(show_answer=True)

    def start_quiz(self):
        print("\n🎯 START QUIZ")
        if not self.flashcards:
            print("No flashcards available. Add some first!")
            return

        quiz_cards = self.flashcards.copy()
        random.shuffle(quiz_cards)

        print(f"Quiz starting with {len(quiz_cards)} cards. Type 'exit' to quit early.\n")

        for i, card in enumerate(quiz_cards, 1):
            print(f"\nCard {i}/{len(quiz_cards)}")
            print(f"Topic: {card.topic}")
            print(f"Q: {card.question}")

            user_answer = input("Your answer: ").strip()

            if user_answer.lower() == 'exit':
                print("Exiting quiz early.")
                break

            if user_answer.lower() == card.answer.lower():
                print("✅ Correct!")
                card.correct += 1
            else:
                print(f"❌ Incorrect. The correct answer is: {card.answer}")
                card.incorrect += 1

            input("Press Enter to continue...")

        print("\n📊 Quiz completed!")
        self.show_stats()

    def show_stats(self):
        print("\n📊 FLASHCARD STATISTICS")
        if not self.flashcards:
            print("No flashcards available.")
            return

        total_correct = sum(card.correct for card in self.flashcards)
        total_incorrect = sum(card.incorrect for card in self.flashcards)
        total_attempts = total_correct + total_incorrect

        print(f"Total Flashcards: {len(self.flashcards)}")
        print(f"Total Attempts: {total_attempts}")
        print(f"Correct: {total_correct} ({total_correct/total_attempts*100:.1f}%)" if total_attempts > 0 else "Correct: 0")
        print(f"Incorrect: {total_incorrect}")

        problematic = sorted(self.flashcards, key=lambda x: x.incorrect, reverse=True)[:3]
        if any(card.incorrect > 0 for card in problematic):
            print("\n⚠️  Cards needing review (most incorrect):")
            for card in problematic:
                if card.incorrect > 0:
                    print(f"  - {card.question[:50]}... (❌ {card.incorrect} wrong)")

    def run(self):
        print("=" * 50)
        print("🎴 FLASHCARD CLI APP - CSV Edition")
        print("=" * 50)

        while True:
            print("\n" + "=" * 30)
            print("MAIN MENU")
            print("=" * 30)
            print("1. Add new flashcard")
            print("2. Review all flashcards")
            print("3. Start quiz (random)")
            print("4. View statistics")
            print("5. Save and exit")
            print("6. Exit without saving")
            print("=" * 30)

            choice = input("\nEnter your choice (1-6): ").strip()

            if choice == '1':
                self.add_flashcard()
            elif choice == '2':
                self.review_all()
            elif choice == '3':
                self.start_quiz()
            elif choice == '4':
                self.show_stats()
            elif choice == '5':
                self.save_flashcards()
                print("👋 Goodbye!")
                break
            elif choice == '6':
                print("👋 Exiting without saving.")
                break
            else:
                print("❌ Invalid choice. Please enter 1-6.")

# Start the program
if __name__ == "__main__":
    app = FlashcardApp()
    app.run()

# end of Program !!