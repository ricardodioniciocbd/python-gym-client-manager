# CAPA DE PRESENTACION 
from cliente_dao import ClienteDAO
from cliente import Cliente


print('*** Clientes de Zona Fit ***')
opcion = None
while opcion != 5:
    print('''
    1.- Listar clientes
    2.- Agregar cliente
    3.- Modificar cliente
    4.- Eliminar cliente
    5.- Salir
     ''')
    opcion = int(input('Escribe una opcion (1-5): '))
    if opcion == 1: # Listar clientes
        clientes = ClienteDAO.seleccionar()
        for cliente in clientes:
            print(cliente) 
        print(f'Total de clientes {len(clientes)}')
    elif opcion == 2: # Agregar cliente
        nombre_var = input('Escribe el nombre: ')
        apellido_var = input('Escribe el apellido: ')
        membrecia_var = int(input('Escribe la membrecia: '))
        cliente_insertado = ClienteDAO.insertar(Cliente(nombre_cliente=nombre_var, apellido_cliente=apellido_var, membrecia_cliente=membrecia_var))
        print(f'Cliente insertado: {cliente_insertado}\n')
    elif opcion == 3: # Modificar cliente
        id_cliente_var = int(input('Escribe el id del cliente a modificar:'))
        nombre_var = input('Escribe el nombre a modificar: ')
        apellido_var = input('Escribe el apellido a modificar: ')
        membrecia_var = int(input('Escribe la membrecia: '))
        cliente_modificado = ClienteDAO.actualizar(Cliente(id_cliente=id_cliente_var, nombre_cliente=nombre_var, apellido_cliente=apellido_var, membrecia_cliente=membrecia_var))
        print(f'Cliente modificado: {cliente_modificado}\n')
    elif opcion == 4: 
        id_cliente_var = int(input('Escribe el id del cliente a eliminar: '))
        cliente_eliminado = ClienteDAO.eliminar(Cliente(id_cliente=id_cliente_var))
        print(f'Cliente eliminado: {cliente_eliminado}\n')
else:
    print('Saliendo del programa...')
