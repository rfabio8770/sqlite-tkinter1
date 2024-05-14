import sqlite3

class Comunicacion:

    def __init__(self) -> None:
        self.conexion = sqlite3.connect("estudiante.db")

    def insertar_datos(self, nombre, edad, correo, telefono):
        cursor = self.conexion.cursor()
        sql = f"INSERT INTO datos (NOMBRE, EDAD, CORREO, TELEFONO) VALUES('{nombre}', '{edad}', '{correo}', '{telefono}')"
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()

    def mostrar_datos(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM datos"
        cursor.execute(sql)
        data = cursor.fetchall()
        return data
    

    def eliminar_registro(self, nombre):
        cursor = self.conexion.cursor()
        sql = f"DELETE FROM datos WHERE nombre = '{nombre}'"
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()

    def actualizar_datos(self, id, nombre, edad, correo, telefono):
        cursor = self.conexion.cursor()
        sql = '''UPDATE datos set NOMBRE = '{}', EDAD = '{}', CORREO = '{}', TELEFONO = '{}'  
         WHERE ID = '{}' '''.format(nombre, edad, correo, telefono, id)
        cursor.execute(sql)
        dato = cursor.rowcount
        self.conexion.commit()
        cursor.close()

        return dato
    

def main():
    datab = Comunicacion()
    # datab.insertar_datos("juan", 20, "juan@gmail.com", "098151256")
    # datab.insertar_datos("pedro", 25, "pedro@gmail.com", "096150256")
    # datab.insertar_datos("jose", 27, "jose@gmail.com", "097259256")
    datab.actualizar_datos(3, "laura", 22, "laura@hotmail.com", "098178221")
    datos = datab.mostrar_datos()

    for x in datos:
        print(x)


if __name__ == "__main__":
    main()