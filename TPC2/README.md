# **Conversor de Markdown para HTML**

Este código converte texto em formato Markdown para HTML. Este pode ser executado a partir da linha de comando, fornecendo como argumento o texto em Markdown ou o caminho para um ficheiro Markdown.

## **Funcionalidades**

### **1. Conversão de Formatação de Texto**

**Cabeçalhos**: Converte os cabeçalhos Markdown (#, ##, ###, etc.) para tags HTML <h1>, <h2>, <h3>, etc.

**Negrito**: Converte texto envolto por ** para a tag HTML <strong>.

**Itálico**: Converte texto envolto por * para a tag HTML <em>.

**Citação em Bloco**: Converte linhas começando com > para a tag HTML <blockquote>.

**Lista Ordenada**: Converte os elementos de listas ordenadas para a tag HTML <ol>.

**Lista Não Ordenada**: Converte os elementos de listas não ordenadas para a tag HTML <ul>.

**Código**: Converte texto envolto por ` para a tag HTML <code>.

**Linha Horizontal**: Converte sequências de --- numa linha para a tag HTML <hr>.

**Link**: Converte links Markdown [texto](URL) para a tag HTML <a>.

**Imagem**: Converte imagens Markdown ![texto](URL) para a tag HTML <img>.

### **2. Verificação e Conversão de Arquivos**

O código verifica se o argumento fornecido é um ficheiro existente.

Se for um ficheiro, ele lê o conteúdo do ficheiro Markdown, converte para HTML e escreve num novo ficheiro chamado output.html.

Se for um texto diretamente fornecido como argumento, ele converte o texto Markdown para HTML e imprime.

### **3. Uso**

O código pode ser executado usando o seguinte comando:

python3 TPC2.py <"MarkdownText"/MarkdownFile.md>

"<"MarkdownText"/MarkdownFile.md>": Este é o argumento esperado pelo código. Pode ser um texto entre aspas duplas ou o caminho para um ficheiro Markdown.

