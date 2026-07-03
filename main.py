import tkinter as tk
from menu_sequence import menu_analysis
from menu_protein import menu_protein
from menu_mutations import menu_mutations
from menu_info import menu_info

def menu():
    menu = tk.Tk()
    menu.title('BioAnalyzer')
    menu.geometry('650x550')
    menu.configure(bg="#EAF4FC")

    title=tk.Label(menu, text= "Welcome to BioAnalyzer!!!", font=("Arial", 30, "bold"), bg="#EAF4FC",
        fg="#0B4F6C")
    title.pack(pady=10)

    subtitle = tk.Label(menu, text="Bioinformatics toolkit for DNA, protein\nand mutation analysis",
                        font=("Arial", 13), bg="#EAF4FC",fg="#444444",justify="center")
    subtitle.pack(pady=10)

    def open_seq_menu():
        menu.withdraw()
        menu_analysis(menu)


    def open_protein_menu():
        menu.withdraw()
        menu_protein(menu)


    def open_mutation_menu():
        menu.withdraw()
        menu_mutations(menu)


    def open_info_menu():
        menu.withdraw()
        menu_info(menu)


    button_style = {
        "font": ("Arial", 14, "bold"),
        "width": 28,
        "height": 3,
        "bg": "#2E86DE",
        "fg": "white",
        "activebackground": "#1B4F72",
        "cursor": "hand2"
    }

    tk.Button(menu, text="🧬 DNA sequence analysis 🧬", command=open_seq_menu, **button_style).pack(pady=10)
    tk.Button(menu, text="🧪 Protein analysis 🧪", command=open_protein_menu, **button_style).pack(pady=10)
    tk.Button(menu, text="🧬 Mutation analysis 🧬", command=open_mutation_menu, **button_style).pack(pady=10)
    tk.Button(menu, text="ℹ️ About the program ℹ️", command=open_info_menu, **button_style).pack(pady=10)
    menu.mainloop()

menu()