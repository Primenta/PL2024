import csv

# Nestas listas vão ser armazenadas todas as modalidades, idades e atletas inaptos.
modalidades = []
idades = []
inaptos = []
# Neste dicionário vão ser armazenados a contagem de atletas por escalão
escaloes = {}

# Este comando irá abrir o ficheiro CSV em modo leitura.
with open('emd.csv', newline='') as csvfile:
    # Então precisamos de criar um leitor para o nosso ficheiro CSV.
    reader = csv.reader(csvfile)
    # Este pequena linha dá next pois nós não queremos interpretar a linha que tem o nome dos atributos.
    next(reader)
    # Este ciclo for vai fazendo iterações sobre as linhas do ficheiro CSV.
    for row in reader:
        # Com o comando "extend" estamos a adicionar cada modalidade à lista modalidades criada em cima.
        # Usamos um split para separar os atributos numa pequena lista em que o oitavo indice é onde estão as modalidades
        modalidades.extend(row[8].split(';'))
        
        idades.extend(row[5].split(';'))
        
        inaptos.extend(row[12].split(';'))

# Função que ordena as modalidades por ordem alfabética. 
# Adiciona-mos a função "set" nas modalidades para ter-mos uma lista sem duplicados.
sorted_modalidades = sorted(set(modalidades))

# Vão ser dados os prints dos nomes das modalidades linha a linha
print("***LISTA ORDENADA ALFABETICAMENTE DAS MODALIDADES DESPORTIVAS!***\n")
for modalidade in sorted_modalidades:
    print(modalidade)

# Este loop faz a contagem do número de 'false' que há na coluna "resultado" para mais tarde sabermos quantos estão aptos e inaptos.
count_inp = 0
for inapto in inaptos:
    if inapto == 'false':
        count_inp += 1

# Vão ser feitos os prints e as devidas conversões para percentagem.
print("\n***PERCENTAGEM DE ATLETAS APTOS E INAPTOS PARA A PRÁTICA DESPORTIVA!***")
aux = count_inp        
count_inp = count_inp / 300 * 100
print("\n"+ str(count_inp) + " per cent dos atletas estão inaptos.")
count_pt = 300 - aux
count_pt = count_pt / 300 * 100
print(str(count_pt) + " per cent dos atletas estão aptos.")

# Este ciclo for vai iterar na lista 'idades' que contêm as idades dos atletas.
for idade in idades:
    # Calcula o escalão etário para a idade atual, dividindo-a por 5 e arredondando para baixo para o múltiplo de 5 mais próximo.
    escalao = (int(idade) // 5) * 5
    # Incrementa a contagem de atletas no escalão etário correspondente no dicionário escaloes.
    escaloes[escalao] = escaloes.get(escalao, 0) + 1
    
# Vão ser dados os prints do intervalo de idade para o escalão etário atual, junto com o número de atletas nesse escalão.
print("\n***DISTRIBUIÇÃO DOS ATLETAS POR ESCALÃO ETÁRIO!***")
for escalao, count in sorted(escaloes.items()):
    print(f"[{escalao}-{escalao+4}]: {count}")

# Abre o ficheiro 'result.txt' em modo de escrita.
# O ficheiro será criado se não existir, ou 'truncado' se já existir.
# Dentro deste ficheiro será introduzido todas as informações interpretadas acima.
with open('result.txt', 'w') as txtfile:
    txtfile.write("***LISTA ORDENADA ALFABETICAMENTE DAS MODALIDADES DESPORTIVAS!***\n\n")
    for modalidade in sorted_modalidades:
        txtfile.write(modalidade + '\n')

    txtfile.write("\n***PERCENTAGEM DE ATLETAS APTOS E INAPTOS PARA A PRÁTICA DESPORTIVA!***\n\n")
    txtfile.write(str(count_inp) + " per cent dos atletas estão inaptos.\n")
    txtfile.write(str(count_pt) + " per cent dos atletas estão aptos.\n")

    txtfile.write("\n***DISTRIBUIÇÃO DOS ATLETAS POR ESCALÃO ETÁRIO!***\n\n")
    for escalao, count in sorted(escaloes.items()):
        txtfile.write(f"[{escalao}-{escalao+4}]: {count}\n")