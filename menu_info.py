import tkinter as tk

def menu_info(menu):
    window = tk.Toplevel(menu)
    window.title("About the program")
    window.geometry("650x550")
    window.configure(bg="#EAF1FF")

    my_text= """🧬 Bioinformatics Analyzer is an application written in Python using the Tkinter library.
     The program was created as an educational project and enables basic bioinformatics analyses.


    Available functions:
    🧬 DNA sequence analysis,
    🧪 protein sequence analysis,
    🧬 detection of basic mutations,
    📊 calculation of GC content,
    🔎 sequence validation,
    🧫 translation of DNA sequences into amino acid sequences."""


    title = tk.Label(window, text= "About the program",font=("Arial", 30, "bold"), bg="#EAF1FF",
        fg="#0B4F6C")
    title.pack(pady=20)
    label1 = tk.Label(window, text=my_text, font=("Arial", 13), bg="#EAF1FF",fg="#313c59",justify="center", wraplength=500)
    label1.pack(pady=10, padx=10)

    button_style = {
        "font": ("Arial", 14, "bold"),
        "width": 28,
        "height": 1,
        "bg": "#2E86DE",
        "fg": "white",
        "activebackground": "#1B4F72",
        "cursor": "hand2"
    }

    def go_back():
        window.destroy()
        menu.deiconify()

    tk.Button(window, text="Return",command=go_back, **button_style).pack(pady=10)



