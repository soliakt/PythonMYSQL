import mysql.connector

class DominioDAO:
    def __init__(self, conexion):
        self.conexion = conexion

    def mostrarIdPropietarioProveedor(self):
        self.muestraExitosamente = False
        cursor = self.conexion.cursor()
        try:
            cursor.execute("SELECT id, email, propietario, proveedor FROM Dominios")
            dominios = cursor.fetchall()
            if dominios:
                for dominio in dominios:
                    print(dominio)
            self.muestraExitosamente = True
        except mysql.connector.Error as e:
            print(f'Error al obtener los dominios: {e}')
        finally:
            cursor.close()
        
        return self.muestraExitosamente
        