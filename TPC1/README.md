**RESUMO SOBRE TP1**

**DESCRIÇÃO DO PROCESSAMENTO DE DADOS**
Este código em Python tem como objetivo processar um conjunto de dados relacionados aos atletas, fornecendo informações sobre as modalidades desportivas praticadas, as idades dos atletas e a sua aptidão para a prática desportiva.

**PROCESSAMENTO DOS DADOS**
O código utiliza a biblioteca Pandas para ler os dados do ficheiro CSV 'emd.csv'. Ele itera sobre as linhas do DataFrame, extrai as modalidades desportivas, as idades dos atletas e a informação sobre a aptidão de cada atleta, armazenando essas informações em listas e dicionários para posterior análise.

**LISTAGEM DAS MODALIDADES DESPORTIVAS**
As modalidades desportivas são organizadas numa lista e ordenadas alfabeticamente. De seguida, o código imprime cada modalidade numa linha separada, proporcionando uma lista ordenada alfabeticamente das modalidades desportivas, sem repetições.

**ANÁLISE DA APTIDÃO DOS ATLETAS**
O código conta o número de atletas inaptos com base na informação de aptidão fornecida no ficheiro. Ele calcula a percentagem de atletas aptos e inaptos em relação ao total de atletas e imprime essas informações.

**DISTRIBUIÇÃO POR FAIXA ETÁRIA**
As idades dos atletas são utilizadas para determinar os escalões etários de cada atleta. As idades são agrupadas em faixas etárias de 5 anos, e o número de atletas em cada faixa etária é contabilizado. O resultado é apresentado como a distribuição dos atletas por faixa etária, mostrando o intervalo de idade e o número de atletas nessa faixa.

**EXPORTAÇÃO PARA UM ARQUIVO DE TEXTO**
Todos os resultados são exportados para um arquivo de texto denominado 'result.txt'. Este arquivo contém a representação escrita de todas as informações processadas, incluindo a lista de modalidades desportivas, a percentagem de atletas aptos e inaptos e a distribuição dos atletas por faixa etária.
