# Recebe a entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função responsável por receber um conceito e retornar sua respectiva descrição.
def descrever_conceito(conceito):
    if conceito == "Azure Cognitive Search":
        return "Sistema de recuperação de informações para conteúdo heterogêneo"
        
    # COMPLETE AQUI: Preencha corretamente cada conceito, considerando as descrições abaixo:
    elif conceito == "Language Studio":
        return "Ferramenta para criar e personalizar modelos de NLP"

    elif conceito == "Azure OpenAI":
        return "Serviço que oferece modelos avançados de IA"

    elif conceito == "Copilot":
        return "Assistente de IA que simplifica operações e gestão na nuvem"

print(descrever_conceito(entrada))