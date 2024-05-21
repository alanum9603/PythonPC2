def sec_fibonacci(n) :
    n1 = 0
    n2 = 1
    x = 0
    list_fibonacci = []
    while n1 <= n :
        x = n1 + n2
        list_fibonacci.append(n1)
        n1 = n2
        n2 = x
    return list_fibonacci

def main() :
    list = []
    max = int(input('Digite el límite de la secuencia Fibonacci -> '))
    list = sec_fibonacci(max)
    print(list)

main()
