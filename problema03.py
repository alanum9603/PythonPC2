def calc_par_impar() :
    list = []
    npar = 0
    nimpar = 0
    x = 'SI'
    while x == 'SI' : 
        n = int(input('Ingrese un número entero -> '))
        list.append(n)
        if n % 2 :
            npar += 1
        else :
            nimpar +=1
        x = input('¿Desea ingresar otro número? (SI - NO) -> ')
        x = x.upper()
    return list, npar, nimpar

def main() :
    numeros = []
    pares = 0
    impares = 0
    numeros, pares, impares = calc_par_impar()
    print(f'Números ingresados: {numeros} \nCantidad de números impares: {pares} \nCantidad de números pares: {impares}')

main()