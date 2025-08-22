
from mysql.connector import pooling
from mysql.connector import Error

class Conexion:
    DATABASE = 'zona_fit_db' # variables de clase para nuestra Class Conexion
    USERNAME = 'root'
    PASSWORD = 'admin'
    DB_PORT = 3306
    HOST = 'localhost'
    POOL_SIZE = 5
    POOL_NAME = 'zona_fit_pool'
    pool = None
    
    # Metodo para obtener el pool de conexiones
    @classmethod
    def obtener_pool(cls):
        if cls.pool is None:
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name=cls.POOL_NAME,
                    pool_size=cls.POOL_SIZE,
                    host=cls.HOST,
                    port=cls.DB_PORT,
                    database=cls.DATABASE,
                    user=cls.USERNAME,
                    password=cls.PASSWORD
                )
                print(f'Nombre del pool: {cls.pool.pool_name}')
                print(f'Tamanio del pool: {cls.pool.pool_size}')
                return cls.pool
            except Error as e:
                print(f'Ourrio un error al obtener el pool:c {e}')
        else:
            return cls.pool

    # Metodo para obtener la conexion 
    @classmethod
    def obtener_conexion(cls):
        print('Conexion del Pool'.center(50, '-'))
        return cls.obtener_pool().get_connection()

    # Metodo para liberar la conexion 
    @classmethod
    def liberar_conexion(cls, conexion):
        print('Conexion liberada')
        conexion.close()

if __name__ == '__main__':
    # Creacion del objeto pool
    #pool = Conexion.obtener_pool()
    #print(pool)
    # Obtener un objeto conexion
    cnx1 = Conexion.obtener_conexion()
    print(cnx1)
    # Liberacion de la conexion 
    Conexion.liberar_conexion(cnx1)
    