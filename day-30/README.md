
# Days 29–30 — Password Manager 🔐

## Project Overview

A desktop Password Manager application built using Python and Tkinter as part of Dr. Angela Yu's 100 Days of Code Python Bootcamp on Udemy.

The application allows users to generate random passwords, save login information locally, and search for previously saved credentials.

## Features

- 🔐 Generate random passwords
- 📋 Copy generated passwords to the clipboard
- 💾 Save website, email, and password details in JSON format
- 🔍 Search for saved credentials by website name
- ⚠️ Handle missing files and unavailable entries using exception handling
- 🖥️ Graphical user interface built with Tkinter

## Concepts Practiced

- Tkinter GUI development
- JSON file handling
- Python dictionaries
- Exception handling with `try`, `except`, and `else`
- Reading and writing files
- Functions and event-driven programming
- Input validation

## Project Files

- `main.py` — Main application code
- `logo.png` — Application logo (if used)
- `data.json` — Locally generated credential storage (not uploaded)

## How to Run

1. Make sure Python 3 and Tkinter are installed.
2. Install the required dependency:

   ```bash
   pip install pyperclip
   ```

3. Open the project folder.
4. Run:

   ```bash
   python3 main.py
   ```

5. Generate, save, and search for passwords.

## Security Note

This project is for educational purposes only.

Passwords are stored in plaintext inside a local JSON file without encryption. Do not use it for real credentials.

The `data.json` file should be excluded from GitHub.

## What I Learned

This project helped me understand how to work with JSON data, handle exceptions, and connect multiple functions to a graphical interface.

One of the most interesting challenges was implementing the password search feature and handling missing files or website entries.

## Course

**100 Days of Code: The Complete Python Pro Bootcamp**

Instructor: Dr. Angela Yu  
Platform: Udemy  
Progress: Day 30/100 completed
