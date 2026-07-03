import tkinter as tk
from sequence_analysis import sequence_analysis

def menu_analysis(menu):
    window = tk.Toplevel(menu)
    window.title("DNA sequence analysis")
    window.geometry("500x500")
    window.configure(background="#EAF4FC")

    tk.Label(window, text= "Welcome to the DNA sequence analysis program!", font=("Arial", 25, "bold"),
             bg="#EAF4FC", fg="#0B4F6C").pack(pady=20)

    tk.Label(window, text="🧬Provide the DNA sequence🧬", font=("Arial", 15, "bold"),
                      bg= "#EAF4FC", fg="#0B4F6C").pack(pady=10)
    scroll = tk.Scrollbar(window)
    scroll.pack(side="right", fill="y")
    entry1 = tk.Text(window, height=8, width=50, font=("Arial", 15), yscrollcommand=scroll.set)
    entry1.pack(pady=10)
    scroll.config(command=entry1.yview)

    def on_click():
        seq = entry1.get("1.0", tk.END).strip()
        result = sequence_analysis(seq)
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, result)


    button_style = {
        "font": ("Arial", 14, "bold"),
        "width": 28,
        "height": 1,
        "bg": "#2E86DE",
        "fg": "white",
        "activebackground": "#1B4F72",
        "cursor": "hand2"
    }

    tk.Button(window, text="Analyze", command=on_click, **button_style).pack(pady=10)

    def go_back():
        window.destroy()
        menu.deiconify()

    result_text = tk.Text(window, height=10, width=50, font=("Arial", 15))
    result_text.pack(pady=10)
    tk.Button(window, text="Return", command=go_back, **button_style).pack(pady=10)



