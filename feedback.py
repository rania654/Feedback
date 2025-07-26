import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root = tk.Tk()
root.geometry("600x600")
root.config(bg="#201E59")
root.title("Event Feedback")


heading = ttk.Label(root, text="Event Feedback Form", font=("Segoe UI",25,"bold"), background="#201E59", foreground="white")
heading.place(anchor="n", rely=0.03, relx=0.5)

separator = tk.Frame(root, height=1, bg="white")
separator.place(relwidth=1.0, rely=0.13)


# age_label = ttk.Label(root, text="Enter Age:", font=("Segoe UI",20), background="#201E59", foreground="white")
# age_label.place(rely=0.15, relx=0.02)
# age_spinbox = ttk.Spinbox(root, from_=5, to=150, font=("Segoe UI",10))
# age_spinbox.place(rely=0.25, relx=0.02, relwidth=0.9)


activity_label = ttk.Label(root, text="Select your favourite(Compulsory)", font=("Segoe UI",20), background="#201E59", foreground="white")
activity_label.place(rely=0.15, relx=0.02)
activity_listbox = tk.Listbox(root, height=5)
activity_listbox.place(rely=0.25, relx=0.02, relwidth=0.9)
activity_listbox.insert(tk.END, "Workshops")
activity_listbox.insert(tk.END, "Stalls")
activity_listbox.insert(tk.END, "Cafeteria")
activity_listbox.insert(tk.END, "Talk")


rating_label = ttk.Label(root, text="Rate the event(Compulsory)", font=("Segoe UI",20), background="#201E59", foreground="white")
rating_label.place(rely=0.40, relx=0.02)

var = tk.StringVar()
var.set("")

rating_radiobutton = tk.Radiobutton(root, text="Poor", variable="rating", value="A", font=("Segoe UI",15), background="#201E59", foreground="white", indicatoron=1, relief='flat', borderwidth=0, highlightthickness=0, selectcolor="#201E59")
rating_radiobutton.place(rely=0.48, relx=0.05)
rating_radiobutton = tk.Radiobutton(root, text="Average", variable="rating", value="B", font=("Segoe UI",15), background="#201E59", foreground="white", indicatoron=1, relief='flat', borderwidth=0, highlightthickness=0, selectcolor="#201E59")
rating_radiobutton.place(rely=0.48, relx=0.2)
rating_radiobutton = tk.Radiobutton(root, text="Excellent", variable="rating", value="C", font=("Segoe UI",15), background="#201E59", foreground="white", indicatoron=1, relief='flat', borderwidth=0, highlightthickness=0, selectcolor="#201E59")
rating_radiobutton.place(rely=0.48, relx=0.42)


feedback_label = ttk.Label(root, text="Enter feedback(Compulsory)", font=("Segoe UI",20), background="#201E59", foreground="white" )
feedback_label.place(rely=0.55, relx=0.02)
feedback_textbox = tk.Text(root, font=("Segoe UI",15), foreground="#201E59", height=3)
feedback_textbox.place(relwidth=0.9, rely=0.65, relx=0.02)


def submit():
    index = activity_listbox.curselection()
    rating = var.get()
    feedback = feedback_textbox.get()
    if len(index) == 0 or rating == "" or feedback == "":
         messagebox.showinfo("ERROR", "Please enter all fields")
    else:
        messagebox.showinfo("Thank You!", "Thanks for filling this!")
        root.destroy()

submit_button = tk.Button(root, text="Submit", command=submit, font=("Segoe UI",20), background="#201E59", foreground="white")
submit_button.place(anchor="s", relx=0.5, rely=0.97)


root.mainloop()

