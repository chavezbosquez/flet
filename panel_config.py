import flet as ft
import componentes as cm

class PanelConfig(ft.Pagelet):

    def __init__(self):
        super().__init__(self)
        self.padding = 20

        self.content=ft.Text('PanelConfig con: import componentes as cm')
        '''
        self.appbar = cm.crear_appbar(ft.icons.SETTINGS, 'Configuración y puesta a punto')
        
        mkd_texto = cm.crear_texto_markdown_formateado('assets/config.md', self)

        self.content=ft.Row(
            controls=[
                ft.Column(
                    controls=[mkd_texto],
                    scroll=ft.ScrollMode.ALWAYS,
                    expand=True)
            ]
        )
        '''

if __name__ == '__main__':

    def main(page: ft.Page):
        page.theme_mode = 'light'
        cnt_principal = ft.Container(content=PanelConfig(), expand=True)
        page.add(cnt_principal)

    ft.app(target=main)
