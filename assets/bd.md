Corregir:
- Comillas simples en todo el tutorial (y en el código)
- ¿Usar 'vista' para la ui y 'modelo' para el archivo de la conexión a la BD?

&nbsp;
# 1  Base de datos

Ahora crearemos una base de datos local usando el Sistema Manejador de Base de Datos (SMBD) más utilizado en la galaxia: [SQLite](https://www.sqlite.org/#:~:text=SQLite%20is%20the%20most%20used%20database%20engine%20in%20the%20world.)

SQLite es tan sensacional que no requiere ningún software o servicio o servidor para funcionar. Permite crear bases de datos "empotradas" en nuestra aplicación, de tal manera que tenemos un mecanismo de persistencia seguro y robusto como cualquier base de datos SQL.

Lo que sí que usaremos es una interfaz para crear nuestra base de datos. Nosotros recomendamos DB Browser (WEB), aunque SQLite Studio (WEB) es también una buena opción.

Descarga DB Browser para Linux (también hay versiones para Mac OS o Güindows). Puedes instalarlo o descargar la versión portable. Cualquiera que sea el caso, ejecuta DB Browser para que te aparezca la siguiente interfaz:

![DB Browser](img/db-browser.png)

Primero, para crear la base de datos deberás ingresar al menú **Archivo ➔ Nueva base de datos** (también hay un botón en la barra de tareas):

![Nueva base de datos](img/bd0.png)

Posteriormente en el cuadro de diálogo de archivos deberás seleccionar el directorio de tu proyecto y escribir el nombre de la base de datos con todo y extensión:

![Archivo de la base de datos](img/bd1.png)

Inmediatamente después aparecerá una ventana para crear tu primera tabla:

![Ventana Nueva tabla](img/bd2.png)

Nota: En caso de que no te aparezca esta ventana simplemente seleccionala desde la barra de herramientas:

![Nueva tabla](img/bd3.png)

 Ahora agrega los siguientes campos en DB Browser así:

![Tabla `division`](img/bd4.png)

Da clic en el botón **Aceptar** y listo. Ya puedes ver tu tabla en la UI. ¡No olvides presionar el botón **Guardar cambios**!

![Guardar cambios](img/bd5.png)

De cualquier manera, si olvidas guardar los cambios entonces BD Browser te enviará el siguiente mensaje cuando quieras salir de la aplicación:

![Confirmación](img/bd6.png)

Revisa que tu base de datos contenga la tabla junto con su estructura justo así:

![Guardar cambios](img/bd7.png)

Finalmente, importa los datos de las Divisiones de tu Alma Máter que se encuentran en el archivo _divisiones.csv_. Tranqui, ya hemos capturado los datos por tí:

![divisiones.csv](img/csv1.png)

## 1.1 Describir que es un CSV

Regresa a DB Browser y selecciona el menú **Archivo ➔ Importar ➔ Tabla de archivo CSV...***

![Importar Divisiones](img/csv2.gif)

Luego coloca el nombre de la tabla a donde vamos a insertar los datos. ¡Debe ser exactamente el mismo nombre! Como separador de campos coloca el "**;**", ya que usamos el punto y coma (;) como el separador de caracteres porque el domicilio de cada División tiene comas. Las demás opciones las puedes dejar como están:

![Importar Divisiones](img/csv3.png)


Al presionar el botón **Aceptar** te aparecerá una ventana de confirmación indicando que ya existe la tabla. Esto es correcto:

![Importar](img/csv4.png)

Ya para terminar esta actividad revisa que los datos estén correctos en la tabla y presiona el botón **Guardar cambios**:

![divisiones.csv](img/csv5.png)

## 1.2  Peewee ORM

Sensacional. ¡Ya que tenemos los datos de todas las Divisiones de nuestra UJAT ahora toca turno de cargar estos datos nuestro componente `DropDown` en la UI. Para ello utilizaremos una técnica conocida como ORM (_Object-relational mapping_, <https://ed.team/blog/que-es-un-orm>).

Un ORM es una herramienta que permite "vincular" los objetos de nuestra aplicación con nuestra base de datos. Sus siglas significan  _Mapeo Relacional de Objetos_, de tal manera que podemos abstraer la base de datos y realizar consultas sin utilizar el lenguaje SQL.

En primer lugar vamos a instalar el módulo `peewee`:

```
pip install peewee
```

Después de unos segundos y unos cuantos MB de descarga ya estamos listos par ensuciarnos las manos.

Vamos a crear un nuevo archivo para crear nuestra conexión a la base de datos. Nombrémosle al archivo _modelo.py_ y dentro vamos a definir nuestro archivo de base de datos. La conexión a SQLite desde Python es directa porque el módulo `sqlite3` se incluye en la instalación predeterminada de Python. En este caso que el archivo de la base de datos se encuentra en el mismo directorio que nuestro código por lo que no necesitamos escribir la ruta completa al archivo.

```python
import peewee as pw

base_datos = pw.SqliteDatabase('bd_ujat.sqlite3')
```

Ahora la clase para acceder a los datos queda de la siguente manera. El nombre de la clase debe ser el mismo que el nombre de nuestra tabla en la base de datos, solamente comenzando con mayúscula para respetar la convención de nombramiento de Python. Esta clase debe heredar sí o sí de `pw.Model` para que Peewee haga el trabajo sucio por nosotros. Los atributos de la clase deben nomnbrarse exactamente igual que los campos de la tabla, y debemos mencionar el tipo de dato con objetos predefinidos de Peewee. Nota los parámetros para especificar la llave primaria y el atributo que puede contener valores nulos.

Al final debemos incluir una clase `Meta` la cual tiene el atributo `database`. Sin esta clase o sin este atributo Peewee nunca podrá hacer su labor de ORM.

```python
class Division(pw.Model):
    clave = pw.TextField(primary_key=True)
    nombre = pw.TextField()
    ubicacion = pw.TextField(null=True)
    class Meta:
        database = base_datos
```

## 1.3  Cargar datos

¡Ya falta poco! En el código de la vista vamos a importar la clase que acabamos de crear:

```python
from modelo import Division
```

La siguiente función "extrae" las Divisiones desde la base datos. Usaremos la clave de cada División para construir un objeto de tipo `Option` porque un Dropdown de Flet únicamente puede mostrar objetos de este tipo. Observa que creamos una lista con todos los Options que corresponden a ada División.

```python
    def get_divisiones() -> list:
        lista = []
        for d in Division.select():
            lista.append( ft.dropdown.Option(text=d.clave) )
        return lista
```

Ahora simplemente tenemos que asignar esta lista al Dropdown en su propiedad `options` y listo:

```python
    # División Académica
    drp_division = ft.Dropdown(
        label='División Académica',
        options=get_divisiones(),
        width=400
    )
```

¿Que tal quedó?

![](img/video.gif)

<!--
[Deployed to a public web host](https://flet.dev/docs/guides/python/deploying-web-app) and be accessible via HTTPS with domain name.
\
&nbsp;
-->