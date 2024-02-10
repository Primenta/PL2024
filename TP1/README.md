**RESUMO SOBRE TP1**

**DESCRIÇÃO DO PROCESSAMENTO DE DADOS DOS ATLETAS**
Este pequeno trabalho consiste num codigo Python responsável por processar um conjunto de dados relacionados aos atletas, incluindo informações sobre as modalidades que praticam, as suas idades e a sua aptidão. O objetivo principal é analisar e apresentar os dados de forma organizada e compreensível.

**PROCESSAMENTO DOS DADOS**
O codigo utiliza a biblioteca csv para ler os dados de um ficheiro CSV chamado 'emd.csv'. A cada iteração sobre as linhas deste ficheiro, são extraídas as modalidades desportivas, idades e informações sobre a aptidão dos atletas. Estas informações são armazenadas em listas e dicionários para análise.

**LISTAGEM DAS MODALIDADES DESPORTIVAS**
As modalidades desportivas são organizadas numa lista e ordenadas alfabeticamente. De seguida, o codigo imprime cada modalidade numa linha separada, apresentando uma lista ordenada alfabeticamente das modalidades desportivas, sem repetições.

**ANÁLISE DA APTIDÃO DOS ATLETAS**
O codigo conta o número de atletas inaptos com base na informação de aptidão fornecida no ficheiro. Em seguida, calcula a percentagem de atletas aptos e inaptos em relação ao total de atletas.

**DISTRIBUIÇÃO POR FAIXA ETÁRIA**
As idades dos atletas são utilizadas para determinar o escalão etário de cada atleta. As idades são agrupadas em faixas etárias de 5 anos, e o número de atletas em cada faixa etária é contabilizado. O resultado é apresentado como a distribuição dos atletas por faixa etária, mostrando o intervalo de idade e o número de atletas nessa faixa.

**EXPORTAÇÃO PARA UM ARQUIVO DE TEXTO**
Todos os resultados são exportados para um arquivo de texto chamado 'result.txt'. Este ficheiro '.txt' contém uma representação escrita de todas as informações processadas, incluindo a lista de modalidades desportivas, a percentagem de atletas aptos e inaptos, e a distribuição dos atletas por faixa etária.
