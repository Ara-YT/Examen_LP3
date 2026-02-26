# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class ClienteDao:

    def getClientes(self):
        clienteSQL = """
        SELECT c.id_cliente, c.nombre, c.apellido, c.documento, 
               c.telefono, c.email, ci.nombre
        FROM cliente c, ciudad ci
        WHERE c.id_ciudad = ci.id_ciudad
        ORDER BY c.apellido
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(clienteSQL)
            clientes = cur.fetchall()
            return [{
                'id_cliente': c[0],
                'nombre': c[1],
                'apellido': c[2],
                'documento': c[3],
                'telefono': c[4],
                'email': c[5],
                'ciudad': c[6]
            } for c in clientes]
        except Exception as e:
            app.logger.error(f"Error al obtener clientes: {str(e)}")
            return []
        finally:
            cur.close()
            con.close()
