# Final-Python-Project

# Flashcard CLI Application

# Overview 
 - This is flashcard Command line interface application for study and  help you memorize and
 - study information efficiently. This program uses a simple CSV-based storage system
 - to manage flashcards across topics, track your learning progress with statistics,
 - and provide interactive progress.

# Features

1. Create Flashcards: Add new flashcards with topics, questions, and answers
2. Review Mode: View all flashcards with their answers and statistics
3. Interactive Quiz: Test your knowledge with randomized quizzes
4. Learning Statistics: Track correct/incorrect attempts and identify problem areas
5. Persistent Storage: Automatically saves flashcards to CSV file
6. Progress Tracking: Each flashcard tracks your performance over time


# Project Structure:

 DocumentCSV.py        # Main application file
 flashcards.csv        # Data storage file (Example)


 # Installation & Setup
 
  Requirements:
  
  -Python 3.6 or higher
  -No external dependencies required (uses built-in modules only)

# Run the program:
  DocumentCSV.py




# How the program  running based on: 

- First appear :
  
==============================
MAIN MENU
==============================
1. Add new flashcard
2. Review all flashcards
3. Start quiz (random)
4. View statistics
5. Save and exit
6. Exit without saving
==============================


 # Adding Flashcards
   
   Select option 1 from the menu

   Enter:
   
   Topic: Category/subject (e.g., "Python", "Biology")
   Question: What you want to remember
   Answer: The correct answer
   

# Reviewing Flashcards

  Select option 2

  Displays all flashcards with questions, answers, and performance stats
  Useful for studying without testing
  

# Taking a Quiz

  Select option 3

  Flashcards are presented in random order
  Type your answer and press Enter
  Type exit during quiz to return to main menu
  Results are tracked automatically
  

# Viewing Statistics
   
Select option 4

Shows overall performance metrics
Highlights cards you're struggling with
Displays success percentages


# Saving Your Progress

Option 5: 
Saves all changes and exits


Option 6:
Exits without saving changes

X Auto-save reminder: 
The program only saves when you choose option 5!



# Technical Architecture

  Classes
  
  Flashcard Class
  The core data model representing individual flashcards.
  

  Attributes:

  topic: Category of the flashcard
  question: The question to answer
  answer: Correct answer
  correct: Number of correct attempts
  incorrect: Number of incorrect attempts
  

  Methods:

  to_list(): Converts flashcard to list for CSV storage
  display(show_answer): Prints flashcard with optional answer reveal
  

  FlashcardApp Class
  The main application controller managing the flashcard system.
  

  Key Methods:

  load_flashcards(): Reads flashcards from CSV file
  save_flashcards(): Writes flashcards to CSV file
  add_flashcard(): Interactive flashcard creation
  review_all(): Display all flashcards
  start_quiz(): Interactive testing session
  show_stats(): Performance analytics
  run(): Main application loop

# Data Storage
  CSV Structure:

  csv
  topic,question,answer,correct,incorrect
  Python,"What does PEP stand for?","Python Enhancement Proposal",5,2
  Science,"H2O is?","Water",10,1
  File Location:

  Default: flashcards.csv in the same directory

  Creates new file if none exists
  UTF-8 encoding for international character support


# Improvement

Want to improve this project? Here are some ideas:

Add export/import functionality
Implement scoring system with points/levels
Add multimedia support (images in questions)
Create GUI version using Tkinter
Add cloud synchronization

# Conclusion 
This is my final project of python for python fundamental basic study.
Happy Learning !!



