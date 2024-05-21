def quitar_vocales(text) :
    res = ''
    vocales = ['a', 'e', 'i', 'o', 'u']
    valor = True
    for t in text :
        for v in vocales :
            if t == v :
                valor = False
                break 
        if valor :
            res += t
        else :
            valor = True
    return res

def main() :
    texto = input('Digite un texto -> ')
    new = quitar_vocales(texto)
    print(new)

main()
