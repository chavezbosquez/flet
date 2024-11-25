import flet as ft


def main(page: ft.Page):
    # Configuración de la página
    page.window.width =400
    page.window.height =480
    page.padding = 25
    page.title = "Alta de profesores"
    page.theme_mode = "light"
    page.appbar = ft.AppBar(
        leading=ft.Icon("person"),
        title=ft.Text("Nuevo profesor"),
        center_title=True,
        bgcolor="blue",
        color="white"
    )

    # Clave del profesor
    txt_clave = ft.TextField(label="Número de empleado", autofocus=True)
    # Nombre del profesor
    txt_nombre = ft.TextField(label="Nombre", width=400)
    # Apellidos
    txt_apellidos = ft.TextField(label="Apellidos", width=400)
    # Grado académico
    rdo_grado = ft.RadioGroup(content=ft.Row([
        ft.Radio(value="Lic.", label="Licenciatura"),
        ft.Radio(value="M.", label="Maestría"),
        ft.Radio(value="Dr.", label="Doctorado")
    ]), value="Dr.")

    # División Académica
    drp_division = ft.Dropdown(
        label="División Académica",
        options=None,
        width=400
    )

    # ¿El profesor cuenta con perfil PRODEP?
    chk_prodep = ft.Checkbox(
        " ¿Es perfil PRODEP?",
        label_position=ft.LabelPosition.RIGHT,
        value=True,
        width=320
    )

    # Botones
    btn_aceptar  = ft.ElevatedButton(text="Guardar",  icon="save",  bgcolor="green", color="white", width=150, on_click=None)
    btn_cancelar = ft.ElevatedButton(text="Cancelar", icon="close", bgcolor="red",   color="white", width=150)

    # Agregar componentes a la UI
    page.add(txt_clave)
    page.add(rdo_grado)
    page.add(txt_nombre)
    page.add(txt_apellidos)
    page.add(chk_prodep)
    page.add(drp_division)
    page.add(ft.Row([btn_aceptar, btn_cancelar], alignment="center"))
    # No olvides actualizar la página
    page.update()


if __name__ == "__main__":
    ft.app(target=main)
