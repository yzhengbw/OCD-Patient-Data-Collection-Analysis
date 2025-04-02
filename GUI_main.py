import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import csv
import os
from tkinterdnd2 import TkinterDnD, DND_FILES
import datetime

# Function to handle "Other" selection
def check_other_selection(event):
    if previous_diagnosis.get() == "Other, please specify->":
        other_entry_pre_dia.config(state="normal")  # Enable text entry for custom input
    else: 
        other_entry_pre_dia.delete(0, tk.END)
        other_entry_pre_dia.config(state="disabled")  # Disable text entry
    if medications.get() == "Other, please specify->":
        other_entry_med.config(state="normal")
    else:
        other_entry_med.delete(0, tk.END)
        other_entry_med.config(state="disabled")

# Validation Function
def validate_input():
    errors = []

    # Check if required fields are filled
    required_fields = ["Patient ID", "Age", "OCD Diagnosis Date", "Duration of Symptoms (months)", "Y-BOCS Score (Obsession)", "Y-BOCS Score (Compulsion)"]
    for field in required_fields:
        if not entries[field].get().strip():
            errors.append(f"{field} cannot be empty!")
    if not file_path.get():
        errors.append("Please select a file to save the data!")

    # Ensure age, duration, and Y-BOCS scores are numeric
    numeric_fields = ["Age", "Duration of Symptoms (months)", "Y-BOCS Score (Obsession)", "Y-BOCS Score (Compulsion)"]
    for field in numeric_fields:
        value = entries[field].get().strip()
        if value and not value.isdigit():
            errors.append(f"{field} must be a valid number!")

    # Ensure OCD Diagnosis Date is in the correct format
    if entries["OCD Diagnosis Date"].get().strip():
        try:
            datetime.datetime.strptime(entries["OCD Diagnosis Date"].get().strip(), '%Y/%m/%d')
        except ValueError:
            errors.append("OCD Diagnosis Date must be in YYYY/MM/DD format!")

    # Ensure Y-BOCS scores are within 0-40
    ybocs_fields = ["Y-BOCS Score (Obsession)", "Y-BOCS Score (Compulsion)"]
    for field in ybocs_fields:
        value = entries[field].get().strip()
        if value and value.isdigit():
            score = int(value)
            if score < 0 or score > 40:
                errors.append(f"{field} must be between 0 and 40!")

    # Ensure age is within 0-130
    age_value = entries["Age"].get().strip()
    if age_value and age_value.isdigit():
        age = int(age_value)
        if age < 0 or age > 120:
            errors.append("Age must be between 0 and 120!")

    # Ensure dropdown selections are made
    dropdown_fields = ["Gender", "Ethnicity", "Marital Status", "Education Level", "Family History", "Obsession Type", "Compulsion Type", "Depression", "Anxiety"]
    for field in dropdown_fields:
        if not entries[field].get():
            errors.append(f"Please select an option for {field}!")
    if not previous_diagnosis.get():
        errors.append("Please select a previous diagnosis!")
    if not medications.get():
        errors.append("Please select a medication!")

    # Ensure "Other" fields are filled if selected
    if previous_diagnosis.get() == "Other, please specify->" and not other_entry_pre_dia.get().strip():
        errors.append("Please specify the previous diagnosis!")
    if medications.get() == "Other, please specify->" and not other_entry_med.get().strip():
        errors.append("Please specify the medication!")

    # Show errors if any
    if errors:
        messagebox.showerror("Input Error", "\n".join(errors))
        return False

    return True

# Browse File Function
def browse_file():
    file = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if file:
        file_path.set(os.path.normpath(file))


# Submit Function
def submit():
    if validate_input():
        data = {key: entry.get() for key, entry in entries.items()}

        # Get "Other" entries
        if previous_diagnosis.get() == "Other, please specify->":
            data["Previous Diagnosis"] = other_entry_pre_dia.get().strip()
        else:
            data["Previous Diagnosis"] = previous_diagnosis.get()

        if medications.get() == "Other, please specify->":
            data["Medications"] = other_entry_med.get().strip()
        else:
            data["Medications"] = medications.get()

        # Define column order
        custom_column_order = [
            "Patient ID", "Age", "Gender", "Ethnicity", "Marital Status", "Education Level", 
            "OCD Diagnosis Date", "Duration of Symptoms (months)", "Previous Diagnosis", "Family History",
            "Obsession Type", "Compulsion Type", "Y-BOCS Score (Obsession)", "Y-BOCS Score (Compulsion)",
            "Depression", "Anxiety", "Medications"
        ]

        # Reorder data according to custom_column_order
        ordered_data = {key: data[key] for key in custom_column_order}

        # Write data to CSV file
        try:
            with open(file_path.get(), mode='a', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=ordered_data.keys())
                # If file is empty, write the header
                if file.tell() == 0:
                    writer.writeheader()
                writer.writerow(ordered_data)
            
            messagebox.showinfo("Success", "Form submitted successfully and saved to CSV!")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while saving to CSV: {e}", "Please try to store in local and close the csv file.")


# Create main window
root = TkinterDnD.Tk()
root.title("OCD Patient Information Input System")
root.geometry("620x650")

# Define labels and entry fields
fields = [
    ("Patient ID", tk.Entry),
    ("Age", tk.Entry),
    ("Gender", ttk.Combobox, ["Female", "Male", "Other"]),
    ("Ethnicity", ttk.Combobox, ["Hispanic", "African", "Asian", "Caucasian"]),
    ("Marital Status", ttk.Combobox, [ "Married", "Divorced", "Single"]),
    ("Education Level", ttk.Combobox, ["Secondary School", "High school", "Some College", "College Degree", "Graduate Degree"]),
    ("OCD Diagnosis Date", tk.Entry),
    ("Duration of Symptoms (months)", tk.Entry),
    ("Family History", ttk.Combobox, ["Yes", "No"]),
    #("Previous Diagnosis", ttk.Combobox, ["GAD", "MDD", "Panic Disorder", "PTSD", "None", "Other, please specify"]),
    ("Obsession Type", ttk.Combobox, ["Contamination", "Harm Related", "Religious", "Hoarding", "Symmetry"]),
    ("Compulsion Type", ttk.Combobox, ["Checking", "Counting", "Ordering", "Washing", "Praying"]),
    ("Y-BOCS Score (Obsession)", tk.Entry),
    ("Y-BOCS Score (Compulsion)", tk.Entry),
    ("Depression", ttk.Combobox, ["Yes", "No"]),
    ("Anxiety", ttk.Combobox, ["Yes", "No"])
    #("Medications", ttk.Combobox, ["SSRI", "SNRI", "Benzodiazepine", "None", "Other, please specify"])
]

# Deal with 'other,please specify->'
# For 'previous diagnosis'
ttk.Label(root, text = "Previous Diagnosis").grid(column = 0, row = 16, sticky="w", padx = 10, pady = 5) 
previous_diagnosis = ttk.Combobox(root, values=["GAD", "MDD", "Panic Disorder", "PTSD", "Other, please specify->"])
previous_diagnosis.config(state="readonly")
previous_diagnosis.grid(row=16, column=1, padx=10, pady=5)
# Bind the selection event
previous_diagnosis.bind("<<ComboboxSelected>>", check_other_selection)
# Create an Entry widget for the "Other" specification, initially disabled
other_entry_pre_dia = tk.Entry(root, state="disabled")
other_entry_pre_dia.grid(row=16, column=2, padx=10, pady=5)

# Deal with 'medications', same process
ttk.Label(root, text = "Medications").grid(column = 0, row = 17, sticky="w", padx = 10, pady = 5)
medications = ttk.Combobox(root, values=["SSRI", "SNRI", "Benzodiazepine", "Other, please specify->"])
medications.config(state="readonly")
medications.grid(row=17, column=1, padx=10, pady=5)
medications.bind("<<ComboboxSelected>>", check_other_selection)
other_entry_med = tk.Entry(root, state="disabled")
other_entry_med.grid(row=17, column=2, padx=10, pady=5)


# Layout configuration
entries = {}
for row_num, (label_text, widget_type, *options) in enumerate(fields):
    tk.Label(root, text=label_text).grid(row=row_num, column=0, sticky="w", padx=10, pady=5)
    
    if widget_type == ttk.Combobox:
        entry = widget_type(root, values=options[0])
        entry.config(state="readonly")  # Make combobox non-editable
    else:
        entry = widget_type(root)
    
    entry.grid(row=row_num, column=1, padx=10, pady=5)
    entries[label_text] = entry

# File path entry for dragging the file
ttk.Label(root, text="Where do you want to store? Enter a csv file:").grid(row=len(fields) + 3, column=0, sticky="w", columnspan=2, pady=10)
file_path = tk.StringVar()
file_entry = ttk.Entry(root, textvariable=file_path, state="normal")
file_entry.grid(row=len(fields) + 3, column=1, columnspan=2, padx=10, pady=5)

# Enable drag-and-drop functionality on the entry field
file_entry.drop_target_register(DND_FILES)
file_entry.dnd_bind('<<Drop>>', lambda e: file_path.set(e.data))  # When a file is dropped, set the file path

# Browse button
browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.grid(row=len(fields) + 3, column=2, columnspan=2, pady=10)

# Submit button
tk.Button(root, text="Submit", command=submit).grid(row=len(fields)+4, column=0, columnspan=2, pady=10)

# Run the GUI loop
root.mainloop()