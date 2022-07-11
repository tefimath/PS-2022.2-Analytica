# P2 

# Questão 1 - Calculadora de ângulo entre ponteiros do relógio 

# ler inputs no horário hh:mm, 24h, zero à esquerda
def q1():
    def num_int(num):
        # tenta converter para inteiro; é o que vamos "tentar" fazer acontecer
        try:
            int(num)
            return True
        # pega a exceção; se não rolar, ele vai printar esse erro no terminal
        except ValueError:
            return False

    while True:
        entrada = input("Insira um horário: ")

        if entrada == 'f':
            print("Fim...")
            break

        if len(entrada) != 5:
            print("Input inválido")
            continue

        tempos = entrada.split(":")

        if len(tempos) != 2 or len(tempos[0]) != 2 or len(tempos[1]) != 2:
            print("Input inválido")
            continue

        horas = tempos[0]
        minutos = tempos[1]

        if num_int(horas) and num_int(minutos) and 0 <= int(horas) <= 23 and 0 <= int(minutos) <= 59:
            horas = int(horas)
            minutos = int(minutos)

            # (valor % total de opções) * (graus totais / total de opções)
            angulo_horas = (horas % 12) * 30
            angulo_minutos = minutos * 6

            # 00:00 -> 0°
            # 00:01 ~ 00:29 -> 1° ~ 179°
            # 00:30 -> 180°
            # 00:31 ~ 00:59 -> 1° 179°

            graus = abs(angulo_horas - angulo_minutos)

            if graus == 180:
                print("O menor ângulo é de 180°")

            else:
                print(f"O menor ângulo é de {graus % 180}°")

        else:
            print("Input inválido")
            continue

q1()

# Questão 2 - Movimentação do cavalo no xadrez

def q2():

    while True:
        entrada = input("jogada: ")

        # se a entrada for 'f', o while acaba
        if entrada == 'f':
            print("Fim...")
            break
        
        # nossa entrada deve ter o tamanho 5 pois o que queremos será algo do tipo: d4 h2. Portanto, ja eliminamos os inputs que fogem desse padrão
        if len(entrada) != 5:
            print("ERRO: INPUT INVÁLIDO")
            continue
        
        # aqui, nos separamos o input por espaços
        posicoes = entrada.split()

        # se o input nao tiver tamanho 2, ou seja, esta separado por 1 espaço entre os caracateres apenas, ou se ele tiver tamanho 2, mas sua primeira parte tiver tamanho diferente de 2 caracteres ou sua segunda parte tiver tamanho diferente de 2 caracteres, ele tbm descarta esses inputs
        if len(posicoes) != 2 or len(posicoes[0]) != 2 or len(posicoes[1]) != 2:
            print("ERRO: INPUT INVÁLIDO")
            continue

        # aqui nós usamos a tabela ASCII e usamos ela para poder filtrar os valores que queremos receber, pois queremos um formato [letra][numero] [letra][número]
        if  97 <= ord(posicoes[0][0].lower()) <= 104 and 49 <= ord(posicoes[0][1]) <= 56 and 97 <= ord(posicoes[1][0].lower()) <= 104 and 49 <= ord(posicoes[1][1]) <= 56:
            
            if abs(ord(posicoes[0][0].lower())) - ord(posicoes[1][0].lower()) == 1 and abs(ord(posicoes[0][1]) - ord(posicoes[1][1])) == 2 or abs(ord(posicoes[0][0].lower()) - ord(posicoes[1][0].lower())) == 2 and abs(ord(posicoes[0][1]) - ord(posicoes[1][1])) == 1:
                print("VÁLIDO")
            
            else:
                print("INVÁLIDO")

        else:
            print("ERRO: INPUT INVÁLIDO")

q2()

# Questão 3 - Calculadora de troco


def q3():

    value = float(input("Valor: "))
    notas = [100, 50, 20, 10, 5, 2]
    moedas = [1, 0.5, 0.25, 0.1, 0.05, 0.01]
    qnt_notas = []
    qnt_moedas = []
    print('\nNOTAS:\n')

    for nota in notas:
        qnt_notas.append(int(value / nota))
        total_notas = int(value / nota)
        value = value % nota
        print('{} nota(s) de R$ {}.00'.format(total_notas, nota))

    print('\nMOEDAS:\n')
    for moeda in moedas:
        # %.2f => o 2f reduz o número a duas casas decimais e o % antes dele arredonda o valor
        value = float('%.2f' % value)
        qnt_moedas.append(int(value / moeda))
        total_moedas = int(value / moeda)
        value = value % moeda
        moeda_formatada = "{:.2f}".format(moeda)
        print('{} moeda(s) de R$ {}'.format(total_moedas, moeda_formatada))
    
q3()


# Questão 4 - Frequência de números

# checa se o valor é um inteiro
def num_int(num):

	try:
		int(num)
		return True

	except ValueError:
		return False

def q4():
 
     # recebe valor inicial de número
    num = input('valor: ')

    # dicionário para armazenar os inputs
    data = {}

    # loop principal, para quando o input for 'f'
    while num != "f":

        # checa se valor é um dígito
        if num_int(num):

            # ele vai salvar a frequencia do valor que colocarmos no input dentro do dicionário basicamente.
            # O data.get() pega o valor e o 0 serve para os valores que nao existiam antes não darem erro no primeiro contato
            # o + 1 é meio q um contador de frequência
            data[num] = data.get(num, 0) + 1
        
        # atualiza o valor do input
        num = input('valor: ')

    # ordena o dicionário pelas chaves 
    sorted_dict = sorted(data.items(), key=lambda x: x[0])

    # printa os resultados
    for k, v in sorted_dict:

        # checa se o valor é maior que 1 e printa com o português correto
        if v > 1:
            print(f'O número {k} apareceu {v} vezes')
        else:
            print(f'O número {k} apareceu {v} vez')

    # printa a mensagem final
    print("Fim...")

q4()