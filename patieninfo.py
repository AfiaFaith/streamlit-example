import tkinter as tk

class PatientInfo:
    def __init__(self, master):
        self.master = master
        self.master.title("Patient Information")
        self.master.geometry("400x400")

        # Create label for disease
        disease_label = tk.Label(master, text="Disease:")
        disease_label.grid(row=0, column=0)
        self.disease_entry = tk.Entry(master)
        self.disease_entry.grid(row=0, column=1)

        # Create label for prescription
        prescription_label = tk.Label(master, text="Prescription:")
        prescription_label.grid(row=1, column=0)
        self.prescription_entry = tk.Entry(master)
        self.prescription_entry.grid(row=1, column=1)

        # Create label for remarks
        remarks_label = tk.Label(master, text="Remarks:")
        remarks_label.grid(row=2, column=0)
        self.remarks_entry = tk.Entry(master)
        self.remarks_entry.grid(row=2, column=1)

        # Create label for date
        date_label = tk.Label(master, text="Date:")
        date_label.grid(row=3, column=0)
        self.date_entry = tk.Entry(master)
        self.date_entry.grid(row=3, column=1)

        # Create label for doctor ID
        docID_label = tk.Label(master, text="Doctor ID:")
        docID_label.grid(row=4, column=0)
        self.docID_entry = tk.Entry(master)
        self.docID_entry.grid(row=4, column=1)

        # Create button to save patient information
        save_button = tk.Button(master, text="Save", command=self.save_info)
        save_button.grid(row=5, column=1)

    def save_info(self):
        disease = self.disease_entry.get()
        prescription = self.prescription_entry.get()
        remarks = self.remarks_entry.get()
        date = self.date_entry.get()
        docID = self.docID_entry.get()

        # Save patient information to database
        # Code for database integration can be added here

        # Clear the input fields after saving
        self.disease_entry.delete(0, tk.END)
        self.prescription_entry.delete(0, tk.END)
        self.remarks_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.docID_entry.delete(0, tk.END)

root = tk.Tk()
app = PatientInfo(root)
root.mainloop()
