import json

def menu():
    print("\n === Menu de Filmes ===")
    print("1. Adicionar")
    print("2. Listar")
    print("3. Atualizar")
    print("4. Excluir")
    print("5. Sair")

# Função para escolher tipo de filme
def escolher_categoria():
    print("Tipos de filme \n 1. Romance \n 2. Terror")
    opcao = input("Digite sua escolha: ")

    if opcao == "1":
        return "romance"
    if opcao == "2":
        return "terror"
    
    else:
        print("Opção Invalida, tente novamente")

# Função para ler dados
def ler_dados():
    with open ("filmes.json", "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)
    
def salvar_dados(dados):
    with open ("filmes.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=2, ensure_ascii=False)

# Função 2 - Listar 
