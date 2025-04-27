import random

caracteristicas = {
    "classe": ["Guerreiro", "Mago", "Ladino", "Arqueiro", "Druida"],
    "raça": ["Elfo", "Anão", "Humano", "Orc", "Goblin"],
    "personalidade": ["Corajoso", "Sábio", "Astuto", "Brincalhão", "Misterioso"],
    "arma": ["Espada", "Cajado", "Adaga", "Arco e flecha", "Machado"]
}

def gerar_personagem():
    personagem = {chave: random.choice(valores) for chave, valores in caracteristicas.items()}
    return personagem

def main():
    print("Gerador de Personagem!\n")
    personagem = gerar_personagem()
    for atributo, valor in personagem.items():
        print(f"{atributo.capitalize()}: {valor}")

if __name__ == "__main__":
    main()
