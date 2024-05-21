def ing_alumn(num) :
    list = []
    for n in range(num) :
        nombre = input('Nombre del alumno: ')
        n1 = float(input('Digite la nota 1: '))
        n2 = float(input('Digite la nota 2: '))
        n3 = float(input('Digite la nota 3: '))
        alumno = {'Alumno':nombre, 'Notas':[n1, n2, n3]}
        list.append(alumno)
    print(list)

def main() :
    lista_alumnos = []
    x = int(input('¿Cuantos alumnos desea ingresar? -> '))
    lista_alumnos = ing_alumn(x)
    print(lista_alumnos)

main()