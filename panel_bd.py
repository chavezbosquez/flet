import flet as ft

import componentes as cm


class PanelBD(ft.Pagelet):
    borrar = None

    def recargar_archivo(self):
        self.borrar = cm.crear_texto_markdown_formateado('assets/ui.md', self)
        self.page.update()


    def __init__(self):
        super().__init__(self)
        self.padding = 20
        self.bgcolor='#f5f5f5'
        self.appbar = cm.crear_appbar(ft.icons.FOLDER, 'Base de datos')

        #mkd_texto = ft.Markdown(
        #    cm.leer_archivo("assets/componentes.md"),
        #    selectable=True,
        #    extension_set="gitHubWeb",
        #    code_theme="atom-one-dark",
        #    code_style=ft.TextStyle(font_family="RobotoMono", size=16),
        #    on_tap_link=lambda e: self.page.launch_url(e.data),
        #)
        mkd_texto = cm.crear_texto_markdown_formateado('assets/bd.md', self)
        self.borrar = mkd_texto
        #mkd_texto = cm.crear_texto_markdown_("assets/bd.md", self)

        #codigo  = cm.leer_archivo("vista_bd.py")
        #mkd_codigo = ft.Markdown(
        #    "```python\n" + codigo + "\n```",
        #    selectable=True,
        #    extension_set="gitHubWeb",
        #    code_theme="atom-one-dark",
        #    code_style=ft.TextStyle(font_family="RobotoMono", size=16)
        #)

        codigo, mkd_codigo = cm.crear_codigo_markdown('vista_bd.py', 'python')

        txt_copiar = ft.Markdown('Código fuente', selectable=True)
        ico_copiar = ft.IconButton(
            ft.icons.COPY,
            tooltip='Copiar script',
            on_click=lambda e: self.page.set_clipboard(codigo)
        )

        self.content = ft.Column(
            controls=[
                ft.Container(mkd_texto, bgcolor='#f5f5f5', padding=10, clip_behavior='antiAlias'),
                ft.Row([txt_copiar, ico_copiar]),
                ft.Container(mkd_codigo, margin=ft.margin.only(right=50), padding=ft.padding.only(right=50), clip_behavior='antiAlias')
            ],
            scroll='always'
        )


if __name__ == '__main__':
    pnl_bd = PanelBD()

    def main(page: ft.Page):
        page.theme_mode = ft.ThemeMode.LIGHT
        page.window.height = 800
        page.padding = 20
        btn_recargar = ft.IconButton('palette')
        cnt_principal = ft.Container(content=pnl_bd, expand=True)
        page.add(btn_recargar)
        page.add(cnt_principal)

    ft.app(target=main)
