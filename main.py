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

        x_values = list(range(1,16))
        green_line = [1.2,1.5,2.0,8,3.2,5,2.0,2.5,5,10,2.1,4,2.0,6,1.7]
        red_line = [1.8,8,1.5,7,1.6,1.8,2.0,10,1.8,3,2.0,2.2,5,2.0,9]

        bottom_axis = ft.ChartAxis(labels_size=25,labels_interval=3,show_labels=True)
        left_axis = ft.ChartAxis(labels_size=25,labels_interval=5,show_labels=True)

        self.chart_data = ft.LineChart(
            tooltip_bgcolor='transparent',
            data_series=[
                ft.LineChartData(
                    data_points=[ft.LineChartDataPoint(x, y, selected=(x == 8)) for x, y in zip(x_values, green_line)],
                    color=ft.colors.GREEN,
                    stroke_width=1,
                    curved=True,
                    below_line_bgcolor=ft.colors.with_opacity(0.2, ft.colors.GREEN)
                ),
                ft.LineChartData(
                    data_points=[ft.LineChartDataPoint(x, y, selected=(x == 8)) for x, y in zip(x_values, red_line)],
                    color=ft.colors.RED,
                    stroke_width=1,
                    curved=True,
                    below_line_bgcolor=ft.colors.with_opacity(0.2, ft.colors.RED)
                ),
            ],
            min_x=0,
            min_y=0,  # Ajustando o eixo Y para incluir os dados corretamente
            expand=True,
            border=ft.Border(
                bottom=ft.BorderSide(1, ft.colors.with_opacity(0.3, ft.colors.WHITE)),
                left=ft.BorderSide(1, ft.colors.with_opacity(0.3, ft.colors.WHITE))
            ),
            bottom_axis=bottom_axis,
            left_axis=left_axis,
        )
        self.header =  ft.Container(
            height=50,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                controls=[
                    ft.IconButton(icon=ft.Icons.ARROW_BACK_IOS,icon_color='white'),
                    ft.Dropdown(
                        width=150,
                        hint_text= "Mês Atual",
                        hint_style=ft.TextStyle(color='white'),  # Define a cor do hint_text
                        border_color=self.container2_color,
                        suffix_icon=ft.Icons.KEYBOARD_ARROW_DOWN,
                        bgcolor=self.bg_color,
                        border_radius=10,
                        icon_enabled_color="transparent",
                        text_style=ft.TextStyle(color='white'),
                        color='white',
                        options=[
                            ft.dropdown.Option('Dezembro'),
                            ft.dropdown.Option('Janeiro'),
                            ft.dropdown.Option('Fevereiro'),

                        ]
                    ),
                    ft.Image(src="assets/face_port.png",height=40,width=40,border_radius=20)
                ]
            )
        )   

        self.title = ft.Container(
            alignment=ft.alignment.center,
            height=20, padding=0,
            content=ft.Text(
                value="6 de fevereiro de 2025, 15 de março de 2025",
                color=ft.Colors.with_opacity(0.5, 'white')
            )
        )

        self.row_1 = ft.Container(
            content=ft.Row([
                ft.Container(
                    height=80,
                    padding=5,expand=True,
                    bgcolor=self.container2_color,
                    border_radius=10,
                    content=ft.Column(
                        controls=[
                            ft.Row(
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                controls=[
                                    ft.Text("Entradas"),
                                    ft.Container(
                                        alignment=ft.alignment.center,
                                        height=10,width=10,border_radius=5,
                                        bgcolor='green'
                                    )
                                ]
                            ),
                            ft.Text("$ 74, 900",size=25 , weight='bold')
                        ]
                    )
                ),
                ft.Container(
                    height=80,
                    padding=5,expand=True,
                    bgcolor=self.container2_color,
                    border_radius=10,
                    content=ft.Column(
                        controls=[
                            ft.Row(
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                controls=[
                                    ft.Text("Saídas"),
                                    ft.Container(
                                        alignment=ft.alignment.center,
                                        height=10,width=10,border_radius=5,
                                        bgcolor='red'
                                    )
                                ]
                            ),
                            ft.Text("$ 44, 782",size=25 , weight='bold')
                        ]
                    )
                )
            ])
        )

        self.row_2 = ft.Container(
            bgcolor=self.container2_color,
            border_radius=10,
            height=250,  # Aumentando a altura para o gráfico ter espaço
            padding=10,
            expand=True,
            content=ft.Column(
                expand=True,
                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Text('Diferença'),
                            ft.Text("R$ 18,290", size=15, weight='bold')
                        ]
                    ),
                    ft.Container(expand=True, content=self.chart_data)  # Adicionando expand ao gráfico
                ]
            )
        )


        self.page.add(
            ft.Column(
                expand=True,scroll="auto",
                controls=[
                   self.header,
                   self.title,
                   self.row_1,
                   self.row_2
                ]
            )
        )


ft.app(target=SpendingApp)