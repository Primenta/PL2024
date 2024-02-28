# **Contador On/Off**

Este código é um programa que permite ao utilizador realizar operações de soma interativamente através da linha de comando ou interpretar comandos de soma de um ficheiro de texto.

##**Funcionalidades Principais**

###**Função process_input:**

Esta função processa o input do utilizador ou de um ficheiro de texto, atualizando a soma e o estado de ativação conforme necessário.
Os comandos disponíveis são:
**"quit"**: Sai do programa.
**"off"**: Desativa a soma.
**"on"**: Ativa a soma.
**"="**: Imprime a soma atual.
**Main:**

Se um argumento de linha de comando for fornecido, o programa lê um ficheiro de texto especificado e processa os comandos de soma contidos nele.
Caso contrário, o programa permite ao utilizador inserir comandos de soma através da entrada padrão.
**Loop Principal:**

No caso de entrada do utilizador, o programa entra num loop infinito, onde cada entrada é processada usando a função process_input.
O loop continua até o utilizador digitar "quit" para sair do programa.

**Ficheiro de output**

No final a soma total é escrita num ficheiro texto de output.
