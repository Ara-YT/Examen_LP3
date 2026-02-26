# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion


class DisponibilidadHorariaDao:

    # ==================================
    # OBTENER TODAS LAS DISPONIBILIDADES
    # ==================================
    def getDisponibilidades(self):

        disponibilidadSQL = """
        SELECT 
            dh.id_disponibilidad,
            h.dia,
            h.hora_apertura,
            h.hora_cierre,
            dh.disponible,
            dh.observacion
        FROM disponibilidad_horaria dh, horario h
        WHERE dh.id_horario = h.id_horario
        ORDER BY h.id_horario
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(disponibilidadSQL)
            disponibilidades = cur.fetchall()

            return [{
                'id_disponibilidad': d[0],
                'dia': d[1],
                'hora_apertura': d[2],
                'hora_cierre': d[3],
                'disponible': d[4],
                'observacion': d[5]
            } for d in disponibilidades]

        except Exception as e:
            app.logger.error(f"Error al obtener disponibilidad horaria: {str(e)}")
            return []

        finally:
            cur.close()
            con.close()


    # ==================================
    # OBTENER DISPONIBILIDAD POR ID
    # ==================================
    def getDisponibilidadById(self, id_disponibilidad):

        disponibilidadSQL = """
        SELECT 
            dh.id_disponibilidad,
            dh.id_horario,
            dh.disponible,
            dh.observacion
        FROM disponibilidad_horaria dh
        WHERE dh.id_disponibilidad = %s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(disponibilidadSQL, (id_disponibilidad,))
            d = cur.fetchone()

            if d:
                return {
                    "id_disponibilidad": d[0],
                    "id_horario": d[1],
                    "disponible": d[2],
                    "observacion": d[3]
                }
            else:
                return None

        except Exception as e:
            app.logger.error(f"Error al obtener disponibilidad: {str(e)}")
            return None

        finally:
            cur.close()
            con.close()


    # ==================================
    # GUARDAR DISPONIBILIDAD
    # ==================================
    def guardarDisponibilidad(self, id_horario, disponible, observacion):

        insertSQL = """
        INSERT INTO disponibilidad_horaria
        (id_horario, disponible, observacion)
        VALUES (%s, %s, %s)
        RETURNING id_disponibilidad
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(insertSQL, (id_horario, disponible, observacion))
            nuevo_id = cur.fetchone()[0]
            con.commit()
            return nuevo_id

        except Exception as e:
            app.logger.error(f"Error al insertar disponibilidad horaria: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()


    # ==================================
    # ACTUALIZAR DISPONIBILIDAD
    # ==================================
    def updateDisponibilidad(self, id_disponibilidad, disponible, observacion):

        updateSQL = """
        UPDATE disponibilidad_horaria
        SET disponible = %s,
            observacion = %s
        WHERE id_disponibilidad = %s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updateSQL, (disponible, observacion, id_disponibilidad))
            filas_afectadas = cur.rowcount
            con.commit()
            return filas_afectadas > 0

        except Exception as e:
            app.logger.error(f"Error al actualizar disponibilidad horaria: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()


    # ==================================
    # ELIMINAR DISPONIBILIDAD
    # ==================================
    def deleteDisponibilidad(self, id_disponibilidad):

        deleteSQL = """
        DELETE FROM disponibilidad_horaria
        WHERE id_disponibilidad = %s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(deleteSQL, (id_disponibilidad,))
            filas_afectadas = cur.rowcount
            con.commit()
            return filas_afectadas > 0

        except Exception as e:
            app.logger.error(f"Error al eliminar disponibilidad horaria: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()
