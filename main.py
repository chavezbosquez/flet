import flet as ft

def main(page: ft.Page):

    page.title = 'Tutorial de programación avanzada en Flet'
    page.theme_mode = 'light'
    page.add( ft.Text('King Henry') )
    page.update()

if __name__ == '__main__':
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)

