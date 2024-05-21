def esPrimo(num) :
    primo = True
    for n in range(2, (num - 1)) :
        if (num % n) == 0 :
            primo = False
            break
    return primo

def main() :
    numero = int(input('Digite un número -> '))
    resultado = esPrimo(numero)
    if resultado :
        print(f'{numero} SI es primo')
    else :
        print(f'{numero} NO es primo')

main()