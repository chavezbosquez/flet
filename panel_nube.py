import flet as ft
import componentes as cm

class PanelNube(ft.Pagelet):

    def __init__(self):
        super().__init__(self)
        self.padding = 20
        self.appbar = cm.crear_appbar(ft.icons.CLOUD, 'Base de datos en la nube')

        mkd_texto = cm.crear_texto_markdown_formateado('assets/nube.md', self)

        self.content = ft.Row(
            controls=[
                ft.Column(
                    controls=[mkd_texto],
                    scroll=ft.ScrollMode.ALWAYS,
                    expand=True)
            ]
        )

if __name__ == "__main__":
    pnl_nube = PanelNube()

    def main(page: ft.Page):
        page.theme_mode = 'light'
        cnt_principal = ft.Container(content=pnl_nube, expand=True)
        page.add(cnt_principal)

    ft.app(target=main)
