# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class VentaDao:

    def getVentas(self):
        ventaSQL = """
        SELECT 
            v.id_venta,
            c.nombre,
            c.apellido,
            l.titulo,
            v.precio,
            v.fecha
        FROM ventas v, clientes c, libros l
        WHERE v.id_cliente = c.id_cliente
        AND v.id_libro = l.id_libro
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(ventaSQL)
            ventas = cur.fetchall()

            return [{
                'id_venta': venta[0],
                'nombre': venta[1],
                'apellido': venta[2],
                'titulo': venta[3],
                'precio': venta[4],
                'fecha': venta[5]
            } for venta in ventas]

        except Exception as e:
            app.logger.error(f"Error al obtener todas las ventas: {str(e)}")
            return []

        finally:
            cur.close()
            con.close()


    def getVentaById(self, id_venta):

        ventaSQL = """
        SELECT 
            v.id_venta,
            c.nombre,
            c.apellido,
            l.titulo,
            v.precio,
            v.fecha,
            v.id_cliente,
            v.id_libro
        FROM ventas v, clientes c, libros l
        WHERE v.id_cliente = c.id_cliente
        AND v.id_libro = l.id_libro
        AND v.id_venta = %s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(ventaSQL, (id_venta,))
            ventaEncontrada = cur.fetchone()

            if ventaEncontrada:
                return {
                    "id_venta": ventaEncontrada[0],
                    "nombre": ventaEncontrada[1],
                    "apellido": ventaEncontrada[2],
                    "titulo": ventaEncontrada[3],
                    "precio": ventaEncontrada[4],
                    "fecha": ventaEncontrada[5],
                    "id_cliente": ventaEncontrada[6],
                    "id_libro": ventaEncontrada[7]
                }
            else:
                return None

        except Exception as e:
            app.logger.error(f"Error al obtener venta: {str(e)}")
            return None

        finally:
            cur.close()
            con.close()


    def guardarVenta(self, id_cliente, id_libro, precio):

        insertVentaSQL = """
        INSERT INTO ventas(id_cliente, id_libro, precio, fecha)
        VALUES(%s, %s, %s, NOW())
        RETURNING id_venta
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(insertVentaSQL, (id_cliente, id_libro, precio))
            venta_id = cur.fetchone()[0]
            con.commit()
            return venta_id

        except Exception as e:
            app.logger.error(f"Error al insertar venta: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()


    def updateVenta(self, id_venta, id_cliente, id_libro, precio):

        updateVentaSQL = """
        UPDATE ventas
        SET id_cliente=%s, id_libro=%s, precio=%s
        WHERE id_venta=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updateVentaSQL, (id_cliente, id_libro, precio, id_venta))
            filas_afectadas = cur.rowcount
            con.commit()
            return filas_afectadas > 0

        except Exception as e:
            app.logger.error(f"Error al actualizar venta: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()


    def deleteVenta(self, id_venta):

        deleteVentaSQL = """
        DELETE FROM ventas
        WHERE id_venta=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(deleteVentaSQL, (id_venta,))
            rows_affected = cur.rowcount
            con.commit()
            return rows_affected > 0

        except Exception as e:
            app.logger.error(f"Error al eliminar venta: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()
