import os
import time

memo_text = """\
📚 Academic Tracker 📓

Name        : Sirisha
Date        : 01 July 2025
Subject     : Python & Java intern
Focus       : On technical skills like java,python,C

Progress Note:
- C,java and python are programming languages
- C is an important language
- java is used to develop web applications
- python is very easy to understand

💡 Keep learning,Good job!
"""
filename = "StudyMemo.txt"
with open(filename, "w", encoding="utf-8") as f:
    f.write(memo_text)

print("Memo saved as", filename)
time.sleep(1) 
os.system(f"start notepad {filename}")