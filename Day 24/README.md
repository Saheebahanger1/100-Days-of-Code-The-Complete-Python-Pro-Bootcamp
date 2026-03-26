# Day 24 – Intermediate  
## Files, Directories, and Paths

## Overview  
On **Day 24** of my **100 Days of Code – The Complete Python Pro Bootcamp**, I focused on persistent data storage and local file management by mastering **Files, Directories, and Paths** in Python. 

I applied these concepts to two distinct projects. First, I upgraded my **Snake Game** so that it remembers the player's highest score even after the game window is closed. Second, I built a **Mail Merge Project** that automates the repetitive task of generating personalized letters from a template and a list of names.

In these projects, I learned how to read data from local files, write new data to files, and navigate complex folder structures using code.

---

## Project Objectives  
- Open, read, and write to local text files using Python  
- Save and retrieve a persistent high score for the Snake Game  
- Understand and navigate absolute and relative file paths  
- Automate file creation for a Mail Merge project  
- Parse text documents and manipulate strings to personalize content  
- Prevent program crashes by handling missing files appropriately  

---

## Concepts I Covered  
- File I/O (Input/Output) operations  
- The `with open()` context manager  
- Reading file contents (`.read()`, `.readlines()`)  
- Writing and appending data (`mode="w"`, `mode="a"`)  
- String manipulation (`.strip()`, `.replace()`)  
- Absolute vs. Relative file paths (`./`, `../`)  
- Handling `FileNotFoundError`  

---

## What I Learned  
- How to persist data so it isn't lost when a program terminates  
- How to safely open and close files using the `with` keyword to prevent data corruption  
- How to automate repetitive administrative tasks, like generating hundreds of personalized text files  
- How Python navigates and interacts with folder structures on a local operating system  
- How to structure projects logically with separate Input and Output directories  
- Debugging pathing issues when files are nested inside different folders  

---

## Day 24 Features  
- **Persistent High Score:** Snake Game saves the highest score to a local text file  
- **Seamless Game Reset:** Snake Game resets automatically on collision without closing the window  
- **Mail Merge Automation:** Script reads a list of invited names from a text file  
- **Template Processing:** Script reads a starting letter template and identifies placeholder text  
- **Batch Output:** Automatically generates and saves a unique, personalized letter for every name on the list  

---

## Files in This Folder  
- `Day24.py` – Main script for the Mail Merge logic  
- `Input/Names/invited_names.txt` – List of names for the mail merge  
- `Input/Letters/starting_letter.txt` – The base template letter  
- `Output/ReadyToSend/` – Directory where the final generated letters are saved  
- `scoreboard.py` – Updated Snake Game class handling the high score file I/O  
- `data.txt` – Text file storing the persistent Snake Game high score  

---

**Challenge:** 100 Days of Code – The Complete Python Pro Bootcamp  
**Level:** Intermediate  
**Project:** Mail Merge & Snake Game High Score
