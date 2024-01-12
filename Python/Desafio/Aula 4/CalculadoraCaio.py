import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora")

        # Cria a tela de entrada
        self.entry = tk.Entry(master, width=30, justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Cria os bot�es num�ricos
        self.create_button("7", 1, 0)
        self.create_button("8", 1, 1)
        self.create_button("9", 1, 2)
        self.create_button("4", 2, 0)
        self.create_button("5", 2, 1)
        self.create_button("6", 2, 2)
        self.create_button("1", 3, 0)
        self.create_button("2", 3, 1)
        self.create_button("3", 3, 2)
        self.create_button("0", 4, 0)
        self.create_button(".", 4, 1)

        # Cria os bot�es de opera��o
        self.create_button("+", 1, 3)
        self.create_button("-", 2, 3)
        self.create_button("*", 3, 3)
        self.create_button("/", 4, 3)
        self.create_button("C", 4, 2)
        self.create_button("=", 5, 3)

        # Define a express�o e o resultado como vazios
        self.expression = ""
        self.result = ""

    def create_button(self, text, row, column):
        # Cria um bot�o com o texto fornecido, na linha e coluna fornecidas
        button = tk.Button(self.master, text=text, width=7, height=2, command=lambda: self.button_click(text))
        button.grid(row=row, column=column, padx=5, pady=5)

    def button_click(self, text):
        if text == "C":
            # Limpa a tela
            self.expression = ""
            self.result = ""
            self.entry.delete(0, tk.END)
        elif text == "=":
            # Calcula o resultado da express�o
            try:
                self.result = str(eval(self.expression))
            except:
                self.result = "Erro"
            self.entry.delete(0, tk.END)
            self.entry.insert(0, self.result)
            self.expression = self.result
        else:
            # Adiciona o texto do bot�o � express�o
            self.expression += text
            self.entry.insert(tk.END, text)

# Cria a janela principal e a calculadora
root = tk.Tk()
calculator = Calculator(root)

# Inicia o loop do tkinter
root.mainloop()