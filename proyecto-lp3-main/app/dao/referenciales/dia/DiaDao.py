# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion


class DiaLocalDao:

    # ===============================
    # OBTENER TODOS LOS DIAS
    # ===============================
    def getDias(self):

        diaSQL = """
        SELECT id_dia, nombre_dia, abierto, observacion
        FROM dia_local
        ORDER BY id_dia
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(diaSQL)
            dias = cur.fetchall()

            return [{
                'id_dia': d[0],
                'nombre_dia': d[1],
                'abierto': d[2],
                'observacion': d[3]
            } for d in dias]

        except Exception as e:
            app.logger.error(f"Error al obtener días del local: {str(e)}")
            return []

        finally:
            cur.close()
            con.close()


    # ===============================
    # ACTUALIZAR DIA
    # ===============================
    def updateDia(self, id_dia, abierto, observacion):

        updateSQL = """
        UPDATE dia_local
        SET abierto = %s,
            observacion = %s
        WHERE id_dia = %s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updateSQL, (abierto, observacion, id_dia))
            filas = cur.rowcount
            con.commit()
            return filas > 0

        except Exception as e:
            app.logger.error(f"Error al actualizar día: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()


    # ===============================
    # VERIFICAR SI HOY ESTA ABIERTO
    # ===============================
    def estaAbiertoHoy(self, nombre_dia):

        sql = """
        SELECT abierto
        FROM dia_local
        WHERE nombre_dia = %s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(sql, (nombre_dia,))
            resultado = cur.fetchone()

            if resultado:
                return resultado[0]
            else:
                return False

        except Exception as e:
            app.logger.error(f"Error al verificar día: {str(e)}")
            return False

        finally:
            cur.close()
            con.close()
