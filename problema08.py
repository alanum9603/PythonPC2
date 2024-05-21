def calc_factorial(num) :
    if num < 0 :
        res = num * -1
    return res

def main() :
    n = int(input('Digite un número -> '))
    factorial = calc_factorial(n)
    print(f'Factorial de {n} -> {factorial}')

main()