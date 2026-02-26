class AutorDao:

    def getAutores(self):
        autorSQL = """
        SELECT id_autor, nombre
        FROM autor
        ORDER BY nombre
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(autorSQL)
            autores = cur.fetchall()
            return [{
                'id_autor': a[0],
                'nombre': a[1]
            } for a in autores]
        except Exception as e:
            app.logger.error(f"Error al obtener autores: {str(e)}")
            return []
        finally:
            cur.close()
            con.close()
