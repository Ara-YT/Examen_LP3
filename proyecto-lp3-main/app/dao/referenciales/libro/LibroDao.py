class LibroDao:

    def getLibros(self):
        libroSQL = """
        SELECT l.id_libro, l.titulo, a.nombre, l.precio, l.stock
        FROM libro l, autor a
        WHERE l.id_autor = a.id_autor
        ORDER BY l.titulo
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(libroSQL)
            libros = cur.fetchall()
            return [{
                'id_libro': l[0],
                'titulo': l[1],
                'autor': l[2],
                'precio': l[3],
                'stock': l[4]
            } for l in libros]
        except Exception as e:
            app.logger.error(f"Error al obtener libros: {str(e)}")
            return []
        finally:
            cur.close()
            con.close()
