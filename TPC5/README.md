# TPC5: Vending Machine


## Autor

- Pedro Miguel Costa Azevedo
- A100557


## Descrição Geral

Este código implementa um sistema simples de vendas automatizado através de uma interface de linha de comandos. O sistema permite ao utilizador adicionar moedas, listar produtos disponíveis e selecionar produtos para compra. O sistema também calcula e fornece o troco ao usuário quando o comando `SAIR` é emitido.

## Funcionamento

### Tokens

O analisador léxico, construído com a biblioteca `ply.lex`, reconhece os seguintes tokens:

- `LISTAR`: Mostra todos os produtos disponíveis.
- `MOEDA`: Indica que o utilizador está a adicionar moeda ao saldo.
- `SELECIONAR`: Utilizado para selecionar um produto para compra.
- `ID`: Identificador numérico de um produto.
- `VALOR`: Valor da moeda inserida, em euros (`e`) ou cêntimos (`c`).
- `SAIR`: Termina a sessão atual e devolve o troco.

### Funções Principais

- `adicionar_moeda(valor)`: Adiciona o valor especificado ao saldo atual do usuário.
- `listar_produtos()`: Lista todos os produtos disponíveis com seus respectivos preços em cêntimos.
- `selecionar_produto(id)`: Tenta realizar a compra do produto identificado pelo `id` dado. Verifica se o saldo é suficiente e se o produto existe.
- `processar_entrada(entrada)`: Processa cada linha de entrada do usuário, invocando ações correspondentes aos tokens reconhecidos.


