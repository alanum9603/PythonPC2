def triangle(n) :
    cont = 1
    ast = '* '
    text = ''
    rango = (n * 2) - 1
    for x in range(rango) :
        for y in range(cont) :
            text += ast
        text += '\n'
        if x < (n - 1) :
            cont += 1
        else : 
            cont -= 1
    return text

def main() :
    n = int(input('Digite el ancho del triangulo -> '))
    t = triangle(n)
    print(t)

main()
