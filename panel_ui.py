import flet as ft
#import ui_profesor
import componentes as cm
# Marca error en las últimas versiones de Flet:
# from flet_multi_page import subPage


class PanelUI(ft.Pagelet):

    def __init__(self):
        super().__init__(self)
        self.padding = 20
        self.appbar = cm.crear_appbar(ft.icons.GRID_VIEW_SHARP, 'UI (User Inteface)')

        #mkd_texto = ft.Markdown(
        #    cm.leer_archivo("assets/componentes.md"),
        #    selectable=True,
        #    extension_set="gitHubWeb",
        #    code_theme="atom-one-dark",
        #    code_style=ft.TextStyle(font_family="RobotoMono", size=16),
        #    on_tap_link=lambda e: self.page.launch_url(e.data),
        #)
        #mkd_texto = cm.crear_texto_markdown("assets/ui.md", self)
        mkd_texto = cm.crear_texto_markdown_formateado('assets/ui.md', self)


        #btn_mostrar_ui = ft.FilledButton(
            #"Mostrar UI",
            #icon=ft.icons.ARROW_OUTWARD,
            #width=200,
            #on_click=lambda e: subPage(target=ui_profesor.main).start()
        #)

        #codigo  = cm.leer_archivo("ui_licenciatura.py")
        #mkd_codigo = ft.Markdown("```python\n" + codigo + "\n```",
        #                        selectable=True,
        #                        extension_set="gitHubWeb",
        #                        code_theme="atom-one-dark",
        #                        code_style=ft.TextStyle(font_family="RobotoMono", size=16)
        #                    )

        codigo, mkd_codigo = cm.crear_codigo_markdown('vista.py', 'python')
        #codigo = cm.crear_codigo_plano("ui_profesor.py")
        #mkd_codigo = ft.Text(codigo)

        txt_copiar = ft.Markdown('Código fuente para crear la UI.', selectable=True)
        ico_copiar = ft.IconButton(
            ft.icons.COPY,
            tooltip='Copiar código fuente',
            on_click=lambda e: self.page.set_clipboard(codigo)
        )

        self.content = ft.Column(
            controls=[
                mkd_texto,
                #btn_mostrar_ui,
                ft.Row([txt_copiar, ico_copiar]),
                ft.Container(
                    mkd_codigo,
                    margin=ft.margin.only(right=50),
                    padding=ft.padding.only(right=50),
                    clip_behavior='antiAlias'
                )
            ],
            scroll='always'
        )

if __name__ == '__main__':

    def main(page: ft.Page):
        page.theme_mode = 'light'
        cnt_principal = ft.Container(content=PanelUI(), expand=True)
        page.add(cnt_principal)

    ft.app(target=main)
