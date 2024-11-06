import tkinter as tk
from tkinter import messagebox

class AlzheimerChanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Avaliação de Chance de Alzheimer")
        
        self.root.configure(bg="#F7F7FF")
        width = 600
        height = 240
        self.root.geometry(f"{width}x{height}")

        # Calculate the position to center the window on the screen
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.root.geometry(f"{width}x{height}+{x}+{y}") 
        
        self.chance = 0
        
        self.perguntas = [
            ("A pessoa apresenta perda de memória?", 1),
            ("A pessoa apresenta mudanças de humor ou personalidade?", 1),
            ("A pessoa tem dificuldade em realizar tarefas básicas?", 1),
            ("A pessoa já teve caso de AVC/Derrame?", 2),
            ("A pessoa possui algum tipo de doença crônica \n(diabetes, hipertensão, colesterol elevado)?", 1),
            ("Há histórico de Alzheimer em parentes próximos da pessoa?", 2),
            ("A pessoa mantém hábitos saudáveis? \n(responda 'não' se os hábitos forem ruins)", 1),
            ("Informe a idade da pessoa:", "idade")
        ]
        
        self.indice_pergunta = 0
        self.resultado_label = None

        self.exibir_pergunta()

    def exibir_pergunta(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        progresso_label = tk.Label(self.root, text=f"Pergunta {self.indice_pergunta + 1} de {len(self.perguntas)}", bg="#F7F7FF", font=("Helvetica", 10))
        progresso_label.pack(pady=(10, 5))

        pergunta, valor = self.perguntas[self.indice_pergunta]
        pergunta_label = tk.Label(self.root, text=pergunta, wraplength=500, bg="#F7F7FF", font=("Helvetica", 14))
        pergunta_label.pack(pady=10)

        if valor == "idade":
            self.entrada_idade = tk.Entry(self.root, font=("Helvetica", 14), width=10)
            self.entrada_idade.pack(pady=5)
            self.entrada_idade.focus()
            proximo_button = tk.Button(self.root, text="Próximo", command=self.validar_idade, bg="#3F826D", fg="white", font=("Helvetica", 12), padx=10)
            proximo_button.pack(pady=(10, 20))
        else:
            button_frame = tk.Frame(self.root)
            button_frame.pack(pady=(10, 20))

            sim_button = tk.Button(button_frame, text="Sim", command=lambda: self.incrementar_chance(valor), bg="#3F826D", fg="white", font=("Helvetica", 12), relief="raised", bd=2, padx=10)
            sim_button.pack(side=tk.LEFT, padx=5)

            nao_button = tk.Button(button_frame, text="Não", command=self.proxima_pergunta, bg="#C03221", fg="white", font=("Helvetica", 12), relief="raised", bd=2, padx=10)
            nao_button.pack(side=tk.LEFT, padx=5)

    def validar_idade(self):
        try:
            idade = int(self.entrada_idade.get())
            if idade >= 65:
                self.chance += 1
            self.proxima_pergunta()
        except ValueError:
            messagebox.showerror("Erro de entrada", "Por favor, insira uma idade válida.")

    def incrementar_chance(self, valor):
        self.chance += valor
        self.proxima_pergunta()

    def proxima_pergunta(self):
        self.indice_pergunta += 1
        if self.indice_pergunta < len(self.perguntas):
            self.exibir_pergunta()
        else:
            self.exibir_resultado()

    def exibir_resultado(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        resultado_texto = self.sint_chance(self.chance)
        resultado_label = tk.Label(self.root, text=resultado_texto, wraplength=500, bg="#F7F7FF", font=("Helvetica", 14, "bold"))
        resultado_label.pack(pady=(30, 10))

        reiniciar_button = tk.Button(self.root, text="Reiniciar", command=self.reiniciar, bg="#648DBA", fg="white", font=("Helvetica", 12), relief="raised", bd=2, padx=10)
        reiniciar_button.pack(pady=(10, 20))

    def reiniciar(self):
        self.chance = 0
        self.indice_pergunta = 0
        self.exibir_pergunta()

    def sint_chance(self, chance):
        if chance <= 3:
            return "Baixa chance de Alzheimer. \nMonitoramento é recomendado."
        elif 4 <= chance <= 5:
            return "Moderada chance de Alzheimer. \nConsulta com especialista é recomendada."
        else:
            return "Alta chance de Alzheimer. \nConsulta com especialista é altamente recomendada."

root = tk.Tk()
app = AlzheimerChanceApp(root)
root.mainloop()