import mysql.connector

class ConexionBD:
    # Constructor vacío
    def __init__(self):
        self.conexion = None
        pass

    def AbrirConexion(self,baseDeDatos):
        host = 'localhost'
        usuario  = 'root'
        password = ''

        try:
            # Url de conexión
            url = f"mysql+mysqlconnector://{usuario}:{password}@{host}/{baseDeDatos}"

            # Establecimiento de la conexión
            self.conexion = mysql.connector.connect(
                host = host,
                user = usuario,
                password = password,
                database = baseDeDatos
            )
            print(f'Conexión a {baseDeDatos} realizada con éxito')
            return True
        except mysql.connector.Error as e:
            print(f'Error al conectar a la BBDD: {e} ')
            return False
        
    def CerrarConexion(self):
        if self.conexion is not None:
            self.conexion.close()
            print("Se ha cerrado la conexión.")
        
if __name__ == "__main__":
    # Crear una instancia de ConexionBD
    conexion_bd = ConexionBD()

    # Establecemos la conexion a la BBDD introducida
    exito = conexion_bd.AbrirConexion('MasLeads')

    # Cierre de la conexion
    if exito:
        conexion_bd.CerrarConexion()

