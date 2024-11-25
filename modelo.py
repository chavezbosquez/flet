import peewee as pw

base_datos = pw.SqliteDatabase('bd_ujat.sqlite3')

class Division(pw.Model):
    clave = pw.TextField(primary_key=True)
    nombre = pw.TextField()
    ubicacion = pw.TextField(null=True)
    class Meta:
        database = base_datos
