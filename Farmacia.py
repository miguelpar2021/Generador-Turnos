import Numero_proyecto

def preguntar():
    print('-' * 30)
    print("Bienvenido a Inversiones Parra")
    print('-' * 30)

    while True:
        try:

            print('\n')
            print('Farmacia[f]')
            print('Belleza[b]')
            print('Perfumeria[p]')
            print('Salir[s]')
            eleccion_menu=input("Escoja Categoria: ").lower()
            ['f','b','p','s'].index(eleccion_menu)

        except:
            print("Esa opcion no es valida")

        else:
            break

    Numero_proyecto.decorador(eleccion_menu)

def inicio():
    while True:
        preguntar()
        try:
            otro_turno=input('Quiere agarra otro turno: [S] o [N]: ').upper()
            ['S','N'].index(otro_turno)
        except:
            print("Presione alguna de las 2 opciones")
        else:
            if otro_turno=="N":
                print("Gracias por su visita")
                break


inicio()