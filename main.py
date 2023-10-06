from DAO.conexionBD import ConexionBD
from DAO.dominioDAO import DominioDAO

if __name__ == "__main__":
    conexion_bd = ConexionBD() # Creamos la instancia de ConexionBD
    creadorDeConexion = conexion_bd.AbrirConexion('MasLeads')
    if creadorDeConexion:
        # Creamos una instancia de DominioDAO pasando la conexión
        dominio_dao = DominioDAO(conexion_bd.conexion)

        muestraLaInfo = dominio_dao.mostrarIdPropietarioProveedor()

        if muestraLaInfo:
            print("Consulta exitosa")
        else:
            print("Error en la consulta")
    
        conexion_bd.CerrarConexion()

