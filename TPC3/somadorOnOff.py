import sys

def process_input(user_input, count, aux):
    for word in user_input:
        if word.lower() == "quit":
            sys.exit(0)
        elif word.lower() == "off" or "off" in word.lower():
            aux = False
        elif word.lower() == "on" or "on" in word.lower():
            aux = True
        elif word.lower() == "=":
            print(count)
        elif aux:
            if word.isdigit():
                count += int(word)
    return count, aux

def main():
    count = 0
    aux = True

    if len(sys.argv) > 1:
        try:
            file_path = sys.argv[1]
            with open(file_path, 'r') as file:
                for line in file:
                    line_input = line.strip().split()
                    count, aux = process_input(line_input, count, aux)
                print(count)
        except FileNotFoundError:
            print("Ficheiro não encontrado:", file_path)
            sys.exit(1)
    else:
        print("\n\n***PODE INSTRODUZIR NÚMEROS***.\n\nPara parar a soma use \"Off\".\nPara continuar a soma use"
              + "\"On\".\nPara saber a soma até agora use \"=\".\nUse \"quit\" para sair.\n")
        while True:
            user_input = input().split()
            count, aux = process_input(user_input, count, aux)

if __name__ == "__main__":
    main()
