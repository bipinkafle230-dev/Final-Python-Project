# Final Python Project: Flashcard CLI App

## Overview
A command-line flashcard app to help memorize and review topics efficiently. Uses CSV for storage, tracks progress, and offers interactive quizzes.

## Features
1. **Add Flashcards**: Input topic, question, and answer  
2. **Review Mode**: View all cards with stats  
3. **Quiz Mode**: Randomized Q&A with performance tracking  
4. **Stats**: View correct/incorrect counts and weak areas  
5. **Auto Save**: Saves to CSV (option 5)  
6. **Progress Tracking**: Tracks performance per card  

## Structure
- `DocumentCSV.py`: Main script  
- `flashcards.csv`: Data file  

## Setup
- Python 3.6+  
- No external libraries  

**Run**: `python DocumentCSV.py`

## Menu Options
```
1. Add new flashcard  
2. Review all flashcards  
3. Start quiz  
4. View statistics  
5. Save and exit  
6. Exit without saving  
```

## Usage
- **Add**: Enter topic, question, answer  
- **Review**: View all cards and stats  
- **Quiz**: Random questions, type answers, type `exit` to quit  
- **Stats**: View performance summary  
- **Save**: Use option 5 (auto-save not enabled)  

## Architecture

### Flashcard Class
- **Attributes**: topic, question, answer, correct, incorrect  
- **Methods**: `to_list()`, `display(show_answer)`

### FlashcardApp Class
- **Methods**: `load_flashcards()`, `save_flashcards()`, `add_flashcard()`, `review_all()`, `start_quiz()`, `show_stats()`, `run()`

## CSV Format
```
topic,question,answer,correct,incorrect  
Python,"What does PEP stand for?","Python Enhancement Proposal",5,2  
Science,"H2O is?","Water",10,1  
```
- File: `flashcards.csv` (auto-created if missing)  
- Encoding: UTF-8  

## Future Ideas
- Import/export  
- Scoring system  
- Image support  
- GUI (Tkinter)  
- Cloud sync  

## Conclusion
A simple Python CLI flashcard tool for learning and revision.  
**Happy Learning!** 🎓





