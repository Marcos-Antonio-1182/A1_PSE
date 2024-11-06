import tkinter as tk

class AlzheimerChanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Avaliação de Chance de Alzheimer")
        self.root.geometry("750x270")
        
        self.root.configure(bg="#f0f8ff")
        self.chance = 0
        
        self.perguntas = [
            ("A pessoa apresenta perda de memória?", self.sint_memloss),
            ("A pessoa apresenta mudanças de humor ou personalidade?", self.sint_mood),
            ("A pessoa tem dificuldade em realizar tarefas básicas?", self.sint_tasks),
            ("A pessoa já teve caso de AVC/Derrame?", self.sint_AVC),
            ("A pessoa possui algum tipo de doença crônica (diabetes, hipertensão, colesterol elevado)?", self.sint_illness),
            ("Há histórico de Alzheimer em parentes próximos da pessoa?", self.sint_famhist),
            ("A pessoa mantém hábitos saudáveis?", self.sint_health),
            ("Informe a idade da pessoa:", self.sint_age)
        ]
        
        self.indice_pergunta = 0
        self.resultado_label = None

        self.exibir_pergunta()

    def exibir_pergunta(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        progresso_label = tk.Label(self.root, text=f"Pergunta {self.indice_pergunta + 1} de {len(self.perguntas)}", bg="#f0f8ff", font=("Helvetica", 10))
        progresso_label.pack(pady=(10, 5))

        pergunta, funcao = self.perguntas[self.indice_pergunta]
        pergunta_label = tk.Label(self.root, text=pergunta, wraplength=350, bg="#f0f8ff", font=("Helvetica", 12))
        pergunta_label.pack(pady=10)

        if self.indice_pergunta < len(self.perguntas) - 1:
            button_frame = tk.Frame(self.root, bg="#f0f8ff")
            button_frame.pack(side=tk.BOTTOM, anchor=tk.SE, padx=20, pady=(10, 20))

            sim_button = tk.Button(button_frame, text="Sim", command=lambda: funcao("sim"), bg="#4CAF50", fg="white", font=("Helvetica", 10), relief="raised", bd=2)
            sim_button.pack(side=tk.LEFT, padx=10)

            nao_button = tk.Button(button_frame, text="Não", command=lambda: funcao("não"), bg="#f44336", fg="white", font=("Helvetica", 10), relief="raised", bd=2)
            nao_button.pack(side=tk.LEFT, padx=10)
        else:
            self.age_entry = tk.Entry(self.root, bg="white", font=("Helvetica", 10))
            self.age_entry.pack(pady=(10, 5))

            nota_label = tk.Label(self.root, text="Pessoas acima dos 65 anos possuem maior chance de desenvolverem Alzheimer.", bg="#f0f8ff", fg="grey", font=("Helvetica", 10), wraplength=350)
            nota_label.pack(pady=(5, 10))

            enviar_frame = tk.Frame(self.root, bg="#f0f8ff")
            enviar_frame.pack(side=tk.BOTTOM, anchor=tk.SE, padx=20, pady=(10, 20))

            enviar_button = tk.Button(enviar_frame, text="Enviar", command=self.registrar_idade, bg="#2196F3", fg="white", font=("Helvetica", 10), relief="raised", bd=2)
            enviar_button.pack()

    def registrar_idade(self):
        try:
            idade = int(self.age_entry.get())
            self.sint_age(idade)
            self.exibir_resultado()
        except ValueError:
            self.exibir_erro("Por favor, insira uma idade válida (número inteiro).")

    def exibir_resultado(self):
        resultado = self.sint_chance(self.chance)
        
        if self.resultado_label:
            self.resultado_label.destroy()
        
        self.resultado_label = tk.Label(self.root, text=resultado, bg="#f0f8ff", fg="black", font=("Helvetica", 12, "bold"))
        self.resultado_label.pack(pady=10)

        reiniciar_button = tk.Button(self.root, text="Reiniciar", command=self.reiniciar, bg="#FF9800", fg="white", font=("Helvetica", 10), relief="raised", bd=2)
        reiniciar_button.pack(pady=(10, 20))

    def reiniciar(self):
        self.chance = 0
        self.indice_pergunta = 0
        self.exibir_pergunta()

    def sint_chance(self, chance):
        if chance <= 3:
            return "Baixa chance de Alzheimer. Monitoramento é recomendado."
        elif 4 <= chance <= 5:
            return "Moderada chance de Alzheimer. Consulta com especialista é recomendada."
        else:
            return "Alta chance de Alzheimer. Consulta com especialista é altamente recomendada."

    def sint_memloss(self, resposta):
        if resposta == "sim":
            self.chance += 1
        self.proxima_pergunta()

    def sint_mood(self, resposta):
        if resposta == "sim":
            self.chance += 1
        self.proxima_pergunta()

    def sint_tasks(self, resposta):
        if resposta == "sim":
            self.chance += 1
        self.proxima_pergunta()

    def sint_AVC(self, resposta):
        if resposta == "sim":
            self.chance += 2
        self.proxima_pergunta()

    def sint_illness(self, resposta):
        if resposta == "sim":
            self.chance += 1
        self.proxima_pergunta()

    def sint_famhist(self, resposta):
        if resposta == "sim":
            self.chance += 2
        self.proxima_pergunta()

    def sint_health(self, resposta):
        if resposta == "não":
            self.chance += 1
        self.proxima_pergunta()

    def sint_age(self, idade):
        if idade >= 65:
            self.chance += 1

    def proxima_pergunta(self):
        self.indice_pergunta += 1
        self.exibir_pergunta()

    def exibir_erro(self, mensagem):
        if self.resultado_label:
            self.resultado_label.destroy()
        erro_label = tk.Label(self.root, text=mensagem, fg="red", bg="#f0f8ff", font=("Helvetica", 10))
        erro_label.pack(pady=10)


root = tk.Tk()
app = AlzheimerChanceApp(root)
root.mainloop()