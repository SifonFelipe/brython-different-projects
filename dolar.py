seleccion_def = input('Pasar dolares a pesos o pesos a dolares: (dolares/pesos)')
peso_arg = 64.91

def pasar_dolares_a_pesos(dolar):
    return dolar * peso_arg

def pasar_pesos_a_dolares(pesos):
    return pesos / peso_arg

print(seleccion_def)
if seleccion_def in ['dolares', 'pesos']:
    if seleccion_def == 'dolares':
        dolar_moneda = int(input('Cantidad De Dolares:'))
        print(dolar_moneda)
        print(pasar_dolares_a_pesos(dolar_moneda))

    if seleccion_def == 'pesos':
        peso_moneda = int(input('Cantidad De Pesos:'))
        print(peso_moneda)
        print(pasar_pesos_a_dolares(peso_moneda))

    seleccion_def = ''

else:
    print('dolares o pesos')
