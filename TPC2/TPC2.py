import re
import sys
import os

def markdown_to_html(markdown):
    # Headings
    markdown = re.sub(r'(?m)^(#{1,6})\s+(.*)$', lambda x: f'<h{len(x.group(1))}>{x.group(2)}</h{len(x.group(1))}>', markdown)

    # Bold
    markdown = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', markdown)

    # Italic
    markdown = re.sub(r'__(.*?)__', r'<em>\1</em>', markdown)

    # Blockquote
    markdown = re.sub(r'^>(.*)$', r'<blockquote>\1</blockquote>', markdown, flags=re.MULTILINE)

    # Ordered list
    markdown = re.sub(r'(?<=\n)(\d+\. .*?)(?=\n)', r'<ol>\n<li>\1</li>\n</ol>', markdown)

    # Unordered list
    markdown = re.sub(r'(?<=\n)([*-] .*?)(?=\n)', r'<ul>\n<li>\1</li>\n</ul>', markdown)

    # Code
    markdown = re.sub(r'`(.*?)`', r'<code>\1</code>', markdown)

    # Horizontal rule
    markdown = re.sub(r'^[-_*]{3,}$', r'<hr>', markdown, flags=re.MULTILINE)

    # Link
    markdown = re.sub(r'\[([^\]]+)]\(([^)]+)\)', r'<a href="\2">\1</a>', markdown)

    # Image
    markdown = re.sub(r'!\[([^\]]+)]\(([^)]+)\)', r'<img src="\2" alt="\1">', markdown)

    return markdown

def is_file(path):
    return os.path.isfile(path)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 TPC2.py <\"MarkdownText\"/MarkdownFile.md>")
        sys.exit(1)
        
    if is_file(sys.argv[1]):
        with open(sys.argv[1], 'r') as f:
            markdown_text = f.read()
    
        html_text = markdown_to_html(markdown_text)

        with open('output.html', 'w') as f:
            f.write(html_text)
        print("Ficheiro convertido com sucesso.")
    else:
        output = markdown_to_html(sys.argv[1])
        print(output)

if __name__ == "__main__":
    main()
