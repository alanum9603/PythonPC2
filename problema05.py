def count(text,digit) :
    cont = 0
    for n in text : 
        if n == digit :
            cont += 1
    return cont

def main() :
    numero = int(input('Ingrese un número -> '))
    digito = int(input('Ingrese un digito -> ')[0:1])
    cant = count(str(numero), str(digito))
    print(cant)

main()

    
