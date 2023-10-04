jogo = ["pedra","papel","tesoura"]
perg = "s"

while perg.lower() == "s" :
    escolha_1 = int(input('''Jogador 1.Escolha
    0 -pedra
    1 - papel
    2 - tesoura \n:'''))

    escolha_2 = int(input('''Jogador 2.Escolha:
    0 -pedra
    1 - papel
    2 - tesoura \n:'''))

    if escolha_1 == escolha_2:
        print("Empate")
    elif (escolha_1 == 0 and escolha_2 == 2) or (escolha_1 == 1 and escolha_2 == 0) or (escolha_1 == 2 and escolha_2 == 1):
        print("Jogador 1 vence!")
    else:
        print("Jogador 2 vence!")
    perg = input("Deseja continuar (s/n) ? ")



