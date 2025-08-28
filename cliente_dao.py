'''
PATRON DE DISENIO DAO (DATA ACCESS OBJECT)

Un patron de disenio son soluciones ya concidas a problemas que nos encontramos comunmente al crear aplicaciones.
Cada patron es como un plano que podemos usar y personalizar para resolver un problema al diseniar una aplicacion.

Se va a encargar de acceder a los datos que nos interesa recuperar de la tabla cliente
se utiliza para acceder a la informacion de una entidad de nuestra apliacion (cliente)
en nuestra db tenemos la tabla cliente con los atributos de (id, nombre, etc..)

CLIENTE_DAO: se encarga de administrar la informacion de la entidad de cliente, por eso tiene las operaciones:
- listar_cliente
- insertar_cliente
- actualizar cliente
- eliminar_cliente
Se encarga de administrar la informacion de la entidad CLIENTEA

Este patrón se utiliza para acceder a la informacion de una entidad de nuestra aplicacion(clase cliente)

'''


from conexion import Conexion
from cliente import Cliente


class ClienteDAO:
    SELECCIONAR = 'SELECT * FROM cliente'
    INSERTAR = 'INSERT INTO cliente(nombre_cliente, apellido_cliente, membrecia_cliente) VALUES(%s, %s, %s)'
    ACTUALIZAR = 'UPDATE cliente SET  nombre_cliente=%s, apellido_cliente=%s, membrecia_cliente=%s WHERE id_cliente = %s'
    ELIMINAR = 'DELETE FROM cliente WHERE id_cliente = %s'

    @classmethod
    def seleccionar(cls):
        try:
          conexion = None
          conexion = Conexion.obtener_conexion()
          cursor = conexion.cursor()
          cursor.execute(cls.SELECCIONAR)
          registros = cursor.fetchall()
          clientes = []
          for registro in registros:
            cliente = Cliente(registro[0], registro[1], registro[2], registro[3])
            clientes.append(cliente)
          return clientes
        except Exception as e:
            print(f'Ocurrio un error al seleccionar clientes {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def insertar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre_cliente, cliente.apellido_cliente, cliente.membrecia_cliente)
            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e: 
            print(f'Ocurrio un error al insertar cliente {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def actualizar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre_cliente, cliente.apellido_cliente, cliente.membrecia_cliente, cliente.id_cliente) 
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
             print(f'Ocurrio un error al actualizar cliente {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def eliminar(cls,cliente):
        try:
            conexion = None
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.id_cliente,)
            cursor.execute(cls.ELIMINAR,valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al eliminar cliente {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)




if __name__ == '__main__':

    clientes = ClienteDAO.seleccionar()
    for cliente in clientes: 
        print(cliente)


    '''
    INSERTAR CLIENTE
    cliente1 = Cliente('nombre_cliente=mario', 'apellido_cliente=batista', 'membrecia_cliente=100' )
    cliente_insertado = ClienteDAO.insertar(cliente1)
    print(f'Cliente insetado {cliente_insertado}')

    ACTUALIZAR CLIENTE
    cliente_actualizar = Cliente(6,'ricardo','dioncio',502)
    clientes_actualizados = ClienteDAO.actualizar(cliente_actualizar)
    print(f'Cliente actualizado {clientes_actualizados}')

    ELIMINAR CLIENTE
    cliente1 = Cliente(id_cliente = 4)
    cliente_eliminado = ClienteDAO.eliminar(cliente1)
    print(f'Cliente eliminado: {cliente_eliminado}')

    SELECCIONAR CLIENTE
    #clientes = ClienteDAO.seleccionar()
    #for cliente in clientes:
    #    print(cliente)

    '''





    