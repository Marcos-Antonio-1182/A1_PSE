#caracteristicas: 
#- Perda de memoria 
#- Mudança de humor/personalidade 
#- Dificuldade em tarefas básicas
#- AVC/Derrame
#- Doenças Crônicas
#- Histórico 
#- Saúde e rotina
#- Idade


def sint_chance(chance):
    if chance <= 3:
        print("Baixa chance de Alzheimer, Monitoramento é recomendado.")
    elif 4 <= chance <= 5:
        print("Moderada chance de Alzheimer, Consulta com especialista para melhor avaliação é recomendada.")
    elif chance >= 6:
        print("Alta chance de Alzheimer, Consulta com especialista para melhor avaliação/tratamento é altamente recomendada.")
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
        #AVC/derrame aumentam em 80% o desenvolvimento de demências
        chance += 2
    return chance

def sint_illness(illness, chance): 
    if illness == "sim":
        chance += 1
    return chance
    
def sint_famhist(famhist, chance): 
    if famhist == "sim":
        #histórico familiar de alzheimer aumenta as chances
        chance += 2
    return chance

def sint_health(health, chance):
    if health == "nao" or health == "não":
        chance += 1
    return chance

def sint_age(age, chance):
    if age >= 65:
        chance += 1
    return chance

def main():
    chance = 0
    # Pergunta para cada característica
    print("\nSintomas: \n")
    memloss = input("A pessoa apresenta perda de memória? (sim/não): ").lower()
    mood = input("A pessoa apresenta mudanças de humor ou personalidade? (sim/não): ").lower()
    tasks = input("A pessoa tem dificuldade em realizar tarefas básicas? (sim/não): ").lower()
    
    print("\nVida/Saúde: \n")
    AVC = input("A pessoa já teve caso de AVC/Derrame? (sim/não): ").lower()
    illness = input("A pessoa possui algum tipo de doença crônica (diabetes, hipertensão, colesterol elevado)? (sim/não): ").lower()
    famhist = input("Há histórico de Alzheimer em parentes próximos da pessoa? (sim/não): ").lower()
    health = input("A pessoa mantém hábitos saudáveis? (sim/não): ").lower()
    age = int(input("Informe a idade da pessoa: "))
    
    # Atualiza chance com cada função de sintoma
    chance = sint_memloss(memloss, chance)
    chance = sint_mood(mood, chance)
    chance = sint_tasks(tasks, chance)
    chance = sint_AVC(AVC, chance)
    chance = sint_illness(illness, chance)
    chance = sint_famhist(famhist, chance)
    chance = sint_health(health, chance)
    chance = sint_age(age, chance)
    
    print("Chance =", sint_chance(chance))

main()
