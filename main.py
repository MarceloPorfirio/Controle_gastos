import flet as ft

class SpendingApp(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__(expand=True)
        self.page = page
        self.bg_color = "#30304b"
        self.page.bgcolor = self.bg_color
        self.blue_color = "#88ddfb"
        self.container_color = "#23243d"
        self.container2_color = "#484a66"


        self.header =  ft.Container(
            height=50,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                controls=[
                    ft.IconButton(icon=ft.Icons.ARROW_BACK_IOS,icon_color='white'),
                    ft.Dropdown(
                        width=150,
                        hint_text= "Mês Atual",
                        border_color=self.container2_color,
                        suffix_icon=ft.icons.KEYBOARD_ARROW_DOWN,
                        bgcolor=self.bg_color,
                        border_radius=10,
                        icon_enabled_color="transparent",
                        text_style=ft.TextStyle(color='white')
                    ),
                    ft.Image(src="assets/face_port.png",height=40,width=40,border_radius=20)
                ]
            )
        )   

        self.page.add(
            ft.Column(
                expand=True,scroll="auto",
                controls=[
                   self.header
                ]
            )
        )


ft.app(target=SpendingApp)