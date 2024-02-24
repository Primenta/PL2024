def main():
    count = 0
    aux = True
    print("\n\n***PODE INSTRODUZIR NÚMEROS***.\n\nPara parar a soma use \"Off\".\nPara continuar a soma use \"On\".\nPara saber a soma até agora use \"=\".")
    while True:
        choose = input()
        if choose.lower() == "off":
            aux = False
        elif choose.lower() == "on":
            aux = True
        elif choose.lower() == "=":
            print(count)
        elif aux:
            if choose.isdigit():
                count += int(choose)

if __name__ == "__main__":
    main()