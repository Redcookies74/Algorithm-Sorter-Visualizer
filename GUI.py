import tkinter as tk
from tkinter import messagebox

import Algorithms  # Ensure this module exists

# Centers the window of the Game Launcher
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

def createGUI():
    root = tk.Tk()
    root.title("Algorithm Sorter Visualizer")
    root.geometry("720x720")
    center_window(root, 480, 480)
    root.configure(bg="#1e1e2f")

    title_label = tk.Label(root, text="Sorting Algorithm Visualizer", font=("Arial", 20, "bold"), bg="#1e1e2f", fg="white")
    title_label.pack(pady=20)

    dataset_label = tk.Label(root, text="Enter the size of the randomly generated dataset\n 1 to 9999: ", bg="#1e1e2f", fg="white")
    dataset_label.pack(pady=0)

    dataset_input = tk.Entry(root, width=15, bg="black", fg="white", insertbackground="white")  # Fixed: Use Entry instead of Text
    dataset_input.pack(pady=10)

    algorithm_checkbox_header = tk.Label(root, text="Choose the algorithms you wish to see", font=("Arial",12, "bold"), bg="#1e1e2f", fg="white")
    algorithm_checkbox_header.pack(pady=20)

    checkbox_frame = tk.Frame(root, bg="#1e1e2f")
    checkbox_frame.pack()

    cb = tk.Checkbutton(checkbox_frame, text="Bubble Sort", bg="#1e1e2f", fg="white", selectcolor="black")
    cb.grid(row=0, column=0)

    cb = tk.Checkbutton(checkbox_frame, text="Merge Sort", bg="#1e1e2f", fg="white", selectcolor="black")
    cb.grid(row=0, column=1)

    cb = tk.Checkbutton(checkbox_frame, text="Quick Sort", bg="#1e1e2f", fg="white", selectcolor="black")
    cb.grid(row=0, column=2)

    cb = tk.Checkbutton(checkbox_frame, text="Insertion Sort", bg="#1e1e2f", fg="white", selectcolor="black")
    cb.grid(row=1, column=0)

    cb = tk.Checkbutton(checkbox_frame, text="Selection Sort", bg="#1e1e2f", fg="white", selectcolor="black")
    cb.grid(row=1, column=1)

    cb = tk.Checkbutton(checkbox_frame, text="Radix Sort", bg="#1e1e2f", fg="white", selectcolor="black")
    cb.grid(row=1, column=2)



    root.mainloop()

# Run the launcher
if __name__ == "__main__":
    createGUI()
