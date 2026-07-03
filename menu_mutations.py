import tkinter as tk
from mutation_analysis import mutation_analysis

def menu_mutations(menu):
    window = tk.Toplevel(menu)
    window.title("Mutation analysis")
    window.geometry('650x550')
    window.configure(bg="#EAF4FC")


    title = tk.Label(window, text= "Welcome to the mutation analysis program!", font=("Arial", 30, "bold"), bg="#EAF4FC",
        fg="#0B4F6C")
    title.pack(pady=10)

    label1 = tk.Label(window, text="🧬Provide the reference DNA sequence🧬", font=("Arial", 15), bg="#EAF4FC",fg="#444444")
    label1.pack(pady=5)

    entry1 = tk.Text(window, height=5, width=60, font=("Arial", 15))
    entry1.pack(pady=5)

    label2 = tk.Label(window, text="🧬Provide the sequences for DNA analysis🧬", font=("Arial", 15),bg="#EAF4FC",fg="#444444")
    label2.pack(pady=5)

    entry2 = tk.Text(window, height=5, width=60, font=("Arial", 15))
    entry2.pack(pady=5)

    def on_click1():
        R_Seq = entry1.get("1.0", tk.END).strip()
        A_seq = entry2.get("1.0", tk.END).strip()
        result = mutation_analysis(R_Seq,A_seq)
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

    tk.Button(window, text="Compare", command=on_click1, **button_style).pack(pady=10)


    def go_back():
        window.destroy()
        menu.deiconify()
    result_text = tk.Text(window, height= 10, width= 50,  font=("Arial", 15))
    result_text.pack(pady=10)
    tk.Button(window, text="Return",command=go_back, **button_style).pack(pady=10)



