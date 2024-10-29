#sintomas: 
#- Perda de memoria recente
#- Mudança de humor/personalidade 
#- Dificuldade em tarefas básicas
#- AVC/Derrame
#- Idade
def sint_chance(chance):
    if chance <= 2:
        print("Baixa chance de Alzheimer")
    elif chance == 3:
        print("Moderada chance de Alzheimer")
    elif chance >= 4:
        print("Alta chance de Alzheimer")
    return chance

def sint_memloss(memloss, chance):
    if memloss == "sim":
        chance += 1
    return chance

def sint_mood(mood, chance):
    if mood == "sim":
        chance += 1
    return chance

def sint_tasks(tasks, chance):
    if tasks == "sim":
        chance += 1
    return chance

def sint_AVC(AVC, chance): 
    if AVC == "sim":
        #AVC/derrame aumentam em 80% o desenvolvimento de demencias
        chance += 2
    return chance

def sint_age(age, chance):
    if age >= 65:
        chance += 1
    return chance

def main():
    chance = 0
    # Pergunta para cada sintoma
    memloss = input("Perda de memória? (sim/não): ").lower()
    mood = input("Mudança de humor/personalidade? (sim/não): ").lower()
    tasks = input("Dificuldade em tarefas básicas? (sim/não): ").lower()
    AVC = input("Já teve caso de AVC/Derrame? (sim/não): ").lower()
    age = int(input("informe sua idade: "))
    
    # Atualiza chance com cada função de sintoma
    chance = sint_memloss(memloss, chance)
    chance = sint_mood(mood, chance)
    chance = sint_tasks(tasks, chance)
    chance = sint_AVC(AVC, chance)
    chance = sint_age(age, chance)
    
    print("Chance =", sint_chance(chance))

main()
