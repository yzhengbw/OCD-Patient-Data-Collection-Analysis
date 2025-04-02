# 🧠 OCD Clinical Data Collection & Visualization Pipeline

This project showcases a complete data pipeline for OCD (Obsessive-Compulsive Disorder) patient data — from **data entry GUI**, to **CSV storage**, and **interactive dashboard visualization** using **Power BI**.

---

## 📌 Components

### 1️⃣ Data Entry: Python GUI (Tkinter)

- Built with `tkinter` and `tkinterDnD2`  
- Allows structured input of patient information (age, gender, diagnosis date, symptoms, medications, etc.)
- Features include:
  - Form validation (age/date/score range)
  - Custom input via "Other, please specify"
  - Drag-and-drop CSV file path entry
  - Instant save to CSV

👉 File: [`GUI_main.py`](./GUI_main.py)

---

### 2️⃣ Data Visualization: Power BI Dashboard

- Analyzed and visualized collected patient data
- Dashboard includes:
  - Gender/Age/Diagnosis distribution
  - Obsession vs Compulsion type mapping
  - Medication breakdown
  - Y-BOCS score trends and severity analysis
  - Interactive filters (e.g. by education level, family history, etc.)

👉 File: `OCD_dashboard.pbix`  

---

## 🚀 Future Work

- Insight python data analysis towards the data

