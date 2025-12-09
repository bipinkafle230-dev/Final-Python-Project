## Final Python Project

# Flashcard Quiz App

A simple command-line flashcard application to help you study, quiz yourself, and track your learning progress.

# Overview

This Python-based CLI tool allows users to create, review, and quiz themselves on flashcards. It tracks correct and incorrect answers per card and provides performance statistics.

# Features

 Add Flashcards: Input topic, question, and answer
 Review Mode: View all flashcards with performance stats
 Quiz Mode: Manually shuffled Q&A with scoring
 Statistics: Track total attempts, correct/incorrect answers, and accuracy
 Manual Shuffle: Deterministic shuffle without using random
 Progress Tracking: Per-card performance tracking

# Structure

 flashcard_app.py: Main script containing all logic
 No external files or libraries required

 # Setup

  Python 3.6 


 # Run the App

   project0.py

# Menu Options

1. Add Flashcard
2. Review Flashcards
3. Start Quiz
4. Show Stats
5. Exit

# Usage

Add Flashcard: Enter topic, question, and answer when prompted
Review: Displays all flashcards with stats (correct/incorrect)
Quiz: Presents shuffled questions; tracks your answers
Stats: Shows total cards, attempts, correct/incorrect counts, and accuracy

 
 # Code Architecture

Class: Flashcard

Attribute::

Description

topic:

Subject or category of the card

question:

The question to be asked

answer:

The correct answer

correct:

Count of correct responses

incorrect:

Count of incorrect responses

# Functions

add_flashcard(deck)

review_flashcards(deck)

manual_shuffle(deck)

start_quiz(deck)

show_stats(deck)

main()

##  Future Enhancements

CSV import/export

Persistent storage

GUI with Tkinter

Cloud sync and backup

Scoring and leaderboard system

## Conclusion

A simple basic functioning , oop concepts are applied for project.
this is flashcard based on command based interface working .
on progress .
