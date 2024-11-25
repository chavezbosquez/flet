import flet as ft
from click import style


def recargar_archivo(e:ft.ControlEvent):
    e.control.data.mkd_texto = crear_texto_markdown_formateado('assets/ui.md', e.control.data.pagelet)
    e.control.data.mkd_texto.update()
    print('Markdown actualizado')


class MiAppBar(ft.AppBar):
    archivo   = ""
    mkd_texto = None
    pagelet   = None

    def __init__(self, icono, texto, archivo, mkd_texto, pagelet):
        super().__init__()
        self.leading = ft.Icon(icono)
        self.title = ft.Text(texto)
        self.bgcolor = ft.colors.GREEN_200
        self.pagelet = pagelet
        #
        self.archivo   = archivo
        self.mkd_texto = mkd_texto
        self.actions = [ft.IconButton("palette",data=self, on_click=recargar_archivo)]


def crear_appbar(icono, texto):
    """"""
    return ft.AppBar(
        leading=ft.Icon(icono),
        title=ft.Text(texto, size=26),
        bgcolor=ft.colors.GREEN_200
    )


def leer_archivo(archivo):
    """"""
    return open(archivo, 'r').read()


#def crear_texto_markdown(archivo, pagelet):
#    ""
#    return ft.Markdown(
#            leer_archivo(archivo),
#            selectable=True,
#            on_tap_link=lambda e: pagelet.page.launch_url(e.data)
#        )


def crear_texto_markdown_formateado(archivo, pagelet):
    """"""
    return ft.Markdown(
        leer_archivo(archivo),
        selectable=True,
        md_style_sheet=ft.MarkdownStyleSheet(p_text_style=ft.TextStyle(size=16)),
        extension_set='gitHubWeb',
        code_theme='atom-one-dark',
        code_style=ft.TextStyle(font_family='RobotoMono', size=16),
        #code_style_sheet=ft.TextStyle(font_family="RobotoMono", size=16),
        on_tap_link=lambda e: pagelet.page.launch_url(e.data)
    )


def crear_codigo_markdown(archivo, lenguaje):
    """ Crea un componente Markdown y devuelve el contenido del archivo en texto plano """
    codigo  = leer_archivo(archivo)
    return codigo, ft.Markdown(f"```{lenguaje}\n" + codigo + "\n```",
                                selectable=True,
                                extension_set="gitHubWeb",
                                code_theme="atom-one-dark",
                                code_style=ft.TextStyle(font_family="RobotoMono", size=16)
                            )

def crear_codigo_plano(archivo):
    return "Hola mundo!" + archivo