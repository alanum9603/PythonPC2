def obtener_Fecha(fecha) :
    nfecha = ''
    if fecha.find('/') > 0 :
        m,d,y = fecha.split('/')
        d = int(d)
        m = int(m)
        y = int(y)
        nfecha = f'{y:04}-{m:02}-{d:02}'
    elif fecha.find(',') > 0:
        meses = ['ENERO', 'FEBRERO', 'MARZO', 'ABRIL', 'MAYO', 'JUNIO', 'JULIO', 'AGOSTO', 'SEPTIEMBRE', 'OCTUBRE', 'NOVIEMBRE', 'DICIEMBRE']
        m,d,y = fecha.split(' ')
        m = m.upper()
        d = int(d[0])
        y = int(y)
        for cont, mes in enumerate(meses):
            if m == mes : 
                m = cont + 1
        nfecha = f'{y:04}-{m:02}-{d:02}'
    return nfecha

def main() : 
    text = input('Digite la fecha\nFormatos adminitos: 09/08/2020 | Septiembre 8, 2020 \n -> ')
    res = obtener_Fecha(text)
    print(res)

main()