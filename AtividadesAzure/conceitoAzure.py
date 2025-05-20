# Recebe a entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função responsável por receber um conceito e retornar sua respectiva descrição.
def descrever_conceito(conceito):
    if conceito == "Inteligência Artificial":
        return "Simulação da inteligência humana por máquinas"

    # COMPLETE AQUI: Preencha corretamente cada conceito, considerando as descrições abaixo:
    elif conceito == "Processamento de Linguagem Natural":
        return "Análise e geração de linguagem humana"

    elif conceito == "Visão Computacional":
        return "Interpretação e análise de imagens e vídeos"

    elif conceito == "Machine Learning":
        return "Aprendizado de máquina para prever ou decidir com base em dados"
        
# Imprime a descrição do conceito recebido na "entrada" através da função "descrever_conceito".
print(descrever_conceito(entrada))