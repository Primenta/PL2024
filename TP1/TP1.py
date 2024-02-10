import pandas as pd

# Ler o arquivo CSV
df = pd.read_csv('emd.csv')

# Listas para armazenar as modalidades e idades
modalidades = []
idades = []

# Lista para armazenar os atletas inaptos
inaptos = []

# Dicionário para armazenar a contagem de atletas por escalão etário
escaloes = {}

# Iterar sobre as linhas do DataFrame
for index, linha in df.iterrows():
    # Adicionar modalidades à lista
    modalidades.extend(linha['modalidade'].split(';'))
    
    # Tratar a coluna de idade como string e adicionar à lista de idades
    idades.extend(str(linha['idade']).split(';'))

    # Adicionar atletas inaptos à lista
    if linha['resultado'] == False:
        inaptos.append('false')
    else:
        inaptos.append('true')

# Ordenar e obter modalidades únicas
modalidades_unicas = sorted(set(modalidades))

# Calcular a contagem de atletas inaptos
contagem_inaptos = inaptos.count('false')

# Calcular a percentagem de atletas aptos e inaptos
total_atletas = len(inaptos)
percentagem_aptos = (total_atletas - contagem_inaptos) / total_atletas * 100
percentagem_inaptos = contagem_inaptos / total_atletas * 100

# Imprimir modalidades ordenadas
print("\n***LISTA ORDENADA ALFABETICAMENTE DAS MODALIDADES DESPORTIVAS!***\n")
for modalidade in modalidades_unicas:
    print(modalidade)

# Imprimir percentagem de atletas aptos e inaptos
print("\n***PERCENTAGEM DE ATLETAS APTOS E INAPTOS PARA A PRÁTICA DESPORTIVA!***\n")
print("{:.2f}% dos atletas estão aptos.".format(percentagem_aptos))
print("{:.2f}% dos atletas estão inaptos.".format(percentagem_inaptos))

# Iterar sobre as idades para calcular os escalões etários e a contagem de atletas em cada escalão
for idade in idades:
    escalao = (int(idade) // 5) * 5
    escaloes[escalao] = escaloes.get(escalao, 0) + 1

# Imprimir distribuição de atletas por escalão etário
print("\n***DISTRIBUIÇÃO DOS ATLETAS POR ESCALÃO ETÁRIO!***\n")
for escalao, count in sorted(escaloes.items()):
    print(f"[{escalao}-{escalao+4}]: {count}")

# Escrever os resultados em um arquivo de texto
with open('result.txt', 'w') as txtfile:
    txtfile.write("***LISTA ORDENADA ALFABETICAMENTE DAS MODALIDADES DESPORTIVAS!***\n\n")
    for modalidade in modalidades_unicas:
        txtfile.write(modalidade + '\n')

    txtfile.write("\n***PERCENTAGEM DE ATLETAS APTOS E INAPTOS PARA A PRÁTICA DESPORTIVA!***\n\n")
    txtfile.write("{:.2f}% dos atletas estão aptos.\n".format(percentagem_aptos))
    txtfile.write("{:.2f}% dos atletas estão inaptos.\n".format(percentagem_inaptos))

    txtfile.write("\n***DISTRIBUIÇÃO DOS ATLETAS POR ESCALÃO ETÁRIO!***\n\n")
    for escalao, count in sorted(escaloes.items()):
        txtfile.write(f"[{escalao}-{escalao+4}]: {count}\n")
