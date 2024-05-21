def calc_num_div_5_7 () :
    list = []
    cont = 0;
    for n in range (1500,2701) : 
        if (n % 7) == 0 and (n % 5) == 0 :
            list.append(n)
            cont += 1
    return cont, list

def main() :
    a, b = calc_num_div_5_7 ()
    print(f'Cantidad de números divisibles entre 7 y múltiplos de 5 entre 1500 y 2700 -> {a} \nNúmeros -> {b}')

main()
