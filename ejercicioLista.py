class ejercicioList:
    def __init__(self):
        self.dato=[]
        print('******* EJERCICIO DE LISTAS ******* ')
    def ingresarDat(self):
        datos=input('ingrese datos por favor:\n')
        print(self.guardarP(datos))
        guardarOtro= input('desea agregar otro dato:y/n \n')
        if (guardarOtro =='y' or guardarOtro=='Y'):
            print(self.ingresarDat())
            print('SE AGREGO LOS DATOS  CORRECTAMENTE')
            self.menu()
    def guardarP(self, dt):
        self.dato.append(dt)
        return 'SE GUARDO CORRECTAMENTE {} '.format(self.dato)
    def menu(self):
        seleccion="""
        ************* EJERCICIO DE LISTAS *************
        1.-MOSTRAR NUMERO SEGUN POSICION
        2.-CANTIDAD DE ELEMENTOS
        3.-POSICION DEL DATO
        4.-SALIR
        """
        print(seleccion)
        opcion=int(input('INGRESE OPCION: \n'))
        if (opcion==1):
            print('DATOS GUARDADOS {} '.format(self.dato))
            digito = int(input('DIGITE POSICION PARA VER EL DATO: \n'))
            print('**EL NUMERO DE LA POSICION QUE DIGITASTE ES EL DATO:*** {} *** '.format(self.dato[digito]))
            print('******************************************************')
            print(self.menu())
        elif (opcion==2):
            print('DATOS GUARDADOS {} '.format(self.dato))
            print('**LA CANTIDAD DE ELEMENTO DE LA LISTA ES : ** {} ** '.format(len(self.dato)))
            print('******************************************************')
            print(self.menu())
        elif (opcion == 3):
            print('DATOS GUARDADOS {} '.format(self.dato))
            digito = input('DIGITE EL DATO A BUSCAR PARA VER EN QUE POSICION ESTA: \n')
            print('**EL NUMERO QUE SELECCIONO ESTA EN LA POSICION :** {} ** '.format(self.dato.index(digito)))
            print('******************************************************')
            print(self.menu())
        elif (opcion == 4):
            print('GRACIAS POR UTILIZAR EL SISTEMA QUE TENGA UN BUEN DIA')
        else:
            return 'SELECCIONE UNA OPCION'

datos=ejercicioList()
datos.ingresarDat()
