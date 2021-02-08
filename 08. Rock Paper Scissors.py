# rewrite this with functions and with a counter for the winner

player1 = input("Ola Jogador 1, qual o teu nome?\n")
player2 = input("Ola Jogador 2, qual o teu nome?\n")

vencedor = False


while vencedor == False:

    escolha1 = input(f"{player1}, escolhe Pedra, Papel ou Tesoura:\n")
    escolha2 = input(f"{player2}, escolhe Pedra, Papel ou Tesoura:\n")

    if escolha1 == "Pedra":
        if escolha2 == "Tesoura":
            print(f"Pedra parte Tesoura: {player1} ganha o jogo!")
            vencedor = True
        elif escolha2 == "Papel":
            print(f"Papel tapa a Pedra: {player2} ganha o jogo!")
            vencedor = True
        else:
            print(f"Pedra = Pedra: Empate!!")
    
    elif escolha1 == "Papel":
        if escolha2 == "Tesoura":
            print(f"Tesoura corta Papel: {player2} ganha o jogo!")
            vencedor = True
        elif escolha2 == "Pedra":
            print(f"Papel tapa a Pedra: {player1} ganha o jogo!")
            vencedor = True
        else:
            print(f"Papel = Papel: Empate!!")

    elif escolha1 == "Tesoura":
        if escolha2 == "Papel":
            print(f"Tesoura corta Papel: {player1} ganha o jogo!")
            vencedor = True
        elif escolha2 == "Pedra":
            print(f"Pedta parte Tesoura tapa a Pedra: {player2} ganha o jogo!")
            vencedor = True
        else:
            print(f"Tesoura = Tesoura: Empate!!")
        

        
