import psycopg2

class Conexion:

    """Metodo constructor
    """
    def __init__(self):
        self.con = psycopg2.connect(dbname="EL_LECTOR", user="postgres", password="05032005", host="localhost", port=5432)
     
    """getConexion

        retorno la instancia de la base de datos

     """
   
    
    def getConexion(self):
        return self.con
