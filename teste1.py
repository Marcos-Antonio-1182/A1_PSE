import tkinter as tk
from tkinter import messagebox
class AlzheimerChanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Avaliação de Chance de Alzheimer")
        self.root.geometry("400x200")  # Tamanho fixo da janela
        self.chance = 0
        
        # Perguntas e variáveis de respostas
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
        
        # Índice da pergunta atual
        self.indice_pergunta = 0
        # Exibe a primeira pergunta
        self.exibir_pergunta()
    def exibir_pergunta(self):
        # Limpa a janela
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Exibe a pergunta atual
        pergunta, funcao = self.perguntas[self.indice_pergunta]
        pergunta_label = tk.Label(self.root, text=pergunta, wraplength=350)
        pergunta_label.pack(pady=20)
        # Adiciona botões apenas se não for a última pergunta
        if self.indice_pergunta < len(self.perguntas) - 1:
            # Frame para os botões
            button_frame = tk.Frame(self.root)
            button_frame.pack(side=tk.BOTTOM, anchor=tk.SE, padx=20, pady=(10, 20))  # Botões no canto inferior direito
            # Botões de resposta "Sim" e "Não"
            sim_button = tk.Button(button_frame, text="Sim", command=lambda: funcao("sim"))
            sim_button.pack(side=tk.LEFT, padx=10)
            nao_button = tk.Button(button_frame, text="Não", command=lambda: funcao("não"))
            nao_button.pack(side=tk.LEFT, padx=10)
        else:
            # Pergunta sobre idade com entrada de número
            self.age_entry = tk.Entry(self.root)
            self.age_entry.pack(pady=(20, 10))
            # Frame para o botão "Enviar"
            enviar_frame = tk.Frame(self.root)
            enviar_frame.pack(side=tk.BOTTOM, anchor=tk.SE, padx=20, pady=(10, 20))
            enviar_button = tk.Button(enviar_frame, text="Enviar", command=self.registrar_idade)
            enviar_button.pack()
    def registrar_idade(self):
        # Verifica se a idade é um número inteiro
        try:
            idade = int(self.age_entry.get())
            self.sint_age(idade)
            self.exibir_resultado()
        except ValueError:
            messagebox.showwarning("Entrada Inválida", "Por favor, insira uma idade válida (número inteiro).")
    def exibir_resultado(self):
        # Mostra a avaliação final baseada na pontuação de chance
        resultado = self.sint_chance(self.chance)
        messagebox.showinfo("Resultado", resultado)
        self.root.destroy()
    # Funções de avaliação de chance
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
# Inicializa a janela do Tkinter
root = tk.Tk()
app = AlzheimerChanceApp(root)
root.mainloop()