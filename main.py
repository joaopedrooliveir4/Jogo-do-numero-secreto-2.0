import random

def escolher_dificuldade():
    print("\nEscolha o nível de dificuldade:")
    print("1 - Fácil (1 a 10)")
    print("2 - Médio (1 a 20)")
    print("3 - Difícil (1 a 50)")
    
    while True:
        try:
            dificuldade = int(input("Digite o número correspondente ao nível de dificuldade: "))
            if dificuldade in [1, 2, 3]:
                return dificuldade
            else:
                print("Opção inválida! Por favor, escolha 1, 2 ou 3.")
        except ValueError:
            print("Entrada inválida. Digite um número entre 1 e 3.")

def configurar_jogo(dificuldade):
    ranges = {1: 10, 2: 20, 3: 50}
    return random.randint(1, ranges[dificuldade]), ranges[dificuldade]

def calcular_pontuacao(dificuldade, tentativas):
    base_pontos = {1: 10, 2: 20, 3: 30}
    return max((base_pontos[dificuldade] * 10) - (tentativas - 1) * base_pontos[dificuldade], base_pontos[dificuldade])

def jogar():
    print("Bem-vindo ao Jogo do Número Secreto!")
    total_pontos = 0
    
    while True:
        dificuldade = escolher_dificuldade()
        numero_secreto, limite = configurar_jogo(dificuldade)
        tentativas, max_tentativas = 1, 3
        
        print(f"\nTente adivinhar o número secreto entre 1 e {limite}. Você tem {max_tentativas} chances!")
        
        while tentativas <= max_tentativas:
            try:
                chute = int(input(f"Tentativa {tentativas} - Digite um número entre 1 e {limite}: "))
                
                if chute < 1 or chute > limite:
                    print(f"Por favor, digite um número dentro do intervalo de 1 a {limite}.")
                    continue
                
                if chute == numero_secreto:
                    tentativa_str = "tentativa" if tentativas == 1 else "tentativas"
                    pontos = calcular_pontuacao(dificuldade, tentativas)
                    total_pontos += pontos
                    
                    print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} {tentativa_str}!")
                    print(f"Você ganhou {pontos} pontos nesta rodada. Pontuação total: {total_pontos}")
                    break
                elif chute > numero_secreto:
                    print("O número secreto é menor.")
                else:
                    print("O número secreto é maior.")
                
                tentativas += 1

            except ValueError:
                print("Entrada inválida. Por favor, digite um número válido.")
        
        if tentativas > max_tentativas:
            print(f"\nGAME OVER. O número secreto era {numero_secreto}.")
        
        jogar_novamente = input("Deseja jogar novamente? (Sim/Não): ").strip().lower()
        if jogar_novamente != "sim":
            print(f"\nEncerrando o jogo. Pontuação final: {total_pontos}. Obrigado por jogar!")
            break

if __name__ == "__main__":
    jogar()
