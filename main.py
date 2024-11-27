import flet as ft

class PanelInicio(ft.Pagelet):

    def __init__(self):
        super().__init__(self)
        img_ujat = ft.Image(src="img/dacyti.png", width=200, fit=ft.ImageFit.CONTAIN)
        txt_sistema = ft.Text("Tutorial de programación avanzada en Flet", size=30,
                              font_family="RobotoSlab", weight=ft.FontWeight.W_500,
                              color=ft.colors.GREEN_700)
        txt_version = ft.Text("Versión 1.0", size=20,
                              font_family="RobotoSlab", weight=ft.FontWeight.W_500,
                              color=ft.colors.GREEN_700)
        txt_info = ft.Text("Desarrollado con ❤️ por XYZ",
                           theme_style=ft.TextThemeStyle.BODY_LARGE)

        self.content=ft.Row([ft.Column([img_ujat, txt_sistema, txt_version, txt_info],
                                       alignment=ft.MainAxisAlignment.CENTER,
                                       horizontal_alignment=ft.CrossAxisAlignment.CENTER)],
                            alignment=ft.MainAxisAlignment.CENTER,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER)

def main(page: ft.Page):

    def set_pantalla(e: ft.ControlEvent):
        cnt_principal.content = lst_pantallas[e.control.selected_index]
        page.update()

    page.title = 'Tutorial de programación avanzada en Flet'
    page.theme_mode = ft.ThemeMode.LIGHT

    # Pantalla principal
    cnt_principal = ft.Container(content=PanelInicio(), expand=True)

    lst_pantallas = [
        ft.Text('Inicio'),
        ft.Text('Configuración'),
        ft.Text('UI'),
        ft.Text('Base de datos'),
        ft.Text('En la nube'),
        ft.Text('¿Ayuda?'),
    ]

    nav_rail = ft.NavigationRail(
        bgcolor=ft.colors.GREEN_200,
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=400,
        group_alignment=-1,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.HOME_OUTLINED,
                selected_icon=ft.icons.HOME,
                label='Inicio'
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.SETTINGS_OUTLINED,
                selected_icon=ft.icons.SETTINGS,
                label='Configuración'
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.GRID_VIEW_OUTLINED,
                selected_icon=ft.icons.GRID_VIEW_SHARP,
                label='UI'
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.FOLDER_OUTLINED,
                selected_icon=ft.icons.FOLDER,
                label='Base de datos'
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.CLOUD_OUTLINED,
                selected_icon=ft.icons.CLOUD,
                label='En la nube'
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.HELP_OUTLINE,
                selected_icon=ft.icons.HELP,
                label='Ayuda'
            )
        ],
        on_change=set_pantalla
    )

    page.add(
        ft.Row(
            [
                nav_rail,
                ft.VerticalDivider(width=1),
                ft.Column(
                    [cnt_principal],
                    alignment=ft.MainAxisAlignment.START,
                    expand=True
                )
            ],
            expand=True
        )
    )

if __name__ == '__main__':
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)

