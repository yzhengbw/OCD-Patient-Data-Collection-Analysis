# 🧠 OCD Patient Form GUI (Python + Tkinter)

This is a graphical user interface (GUI) application designed for entering and validating clinical information from OCD (Obsessive-Compulsive Disorder) patients. Data is saved directly into a CSV file, with support for field validation, dropdown menus, and drag-and-drop file selection.

## 🔧 Technologies Used

- Python `tkinter` (GUI development)
- `tkinterDnD2` (drag and drop support)
- `csv` for data storage
- `datetime` for date validation

## ✨ Features

- GUI form with multiple input types: Entry, Dropdowns, "Other" custom input
- Drag-and-drop CSV path input using `tkinterDnD2`
- Field validation (e.g., numeric input, date format, score range)
- CSV saving with header auto-detection
- User-friendly error popups and success messages

## 📸 Preview

![image](https://github.com/user-attachments/assets/33cca62f-302c-47e8-9e82-44a2b7de6c66)


## 🚀 How to Run

1. Make sure you have Python installed
2. Install tkinterDnD2:
   ```bash
   pip install tkinterdnd2
