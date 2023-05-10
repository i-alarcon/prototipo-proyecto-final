import flet as ft
import pandas as pd
from modulo_proyecto import *

def main(page):
    page.title = "Logralo"

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(title=ft.Text("LOGRALO app!"), bgcolor=ft.colors.SURFACE_VARIANT),
                    ft.Text(value="¡Bienvenido a LOGRALO app!", color="Blue", weight="bold", size=50),
                    ft.Text(value="Donde te ayudaremos en tu busqueda de empleo", color="Black", weight="bold", size=20),
                    ft.Text(value="Para comenzar, selecciona la opción que deseas visualizar", color="Black", size=20),
                    ft.Row(controls=[
                        ft.ElevatedButton("Crear mi CV", on_click=lambda _: page.go("/crearcv")),
                        ft.ElevatedButton("Guia para crear mi CV", on_click=lambda _: page.go("/guiacv")),
                        ft.ElevatedButton("Manuales de Herramientas Básicas", on_click=lambda _: page.go("/manuales")),
                        ft.ElevatedButton("Recomendaciones", on_click=lambda _: page.go("/recomendaciones")),
                    ])

                ],
            )

        )
        if page.route == "/crearcv":
            page.views.append(
                ft.View(
                    "/crearcv",
                    [
                        ft.AppBar(title=ft.Text("Crear CV"), bgcolor=ft.colors.SURFACE_VARIANT),

                    ],
                )
            )
        if page.route == "/guiacv":
            page.views.append(
                ft.View(
                    "/guiacv",
                    [
                        ft.AppBar(title=ft.Text("Guia para hacer mi CV"), bgcolor=ft.colors.SURFACE_VARIANT),

                    ],
                )
            )
        if page.route == "/manuales":
            page.views.append(
                ft.View(
                    "/manuales",
                    [
                        ft.AppBar(title=ft.Text("Manuales de Herramientas Básicas"), bgcolor=ft.colors.SURFACE_VARIANT),

                    ],
                )
            )
        if page.route == "/recomendaciones":
            page.views.append(
                ft.View(
                    "/recomendaciones",
                    [
                        ft.AppBar(title=ft.Text("Recomendaciones"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Container(
                            alignment=ft.alignment.center,
                            padding=25,
                            content=ft.Column(

                                         controls=[
                                             ft.ElevatedButton("¿Qué debo saber sobre el proceso de contratación laboral?", on_click=lambda _: page.go("/recomendaciones/proceso")),
                                             ft.ElevatedButton("Recomendaciones para entrevistas de trabajo",
                                                               on_click=lambda _: page.go("/recomendaciones/entrevistas")),
                                             ft.ElevatedButton("Tips para la busqueda de empleo",
                                                               on_click=lambda _: page.go("/recomendaciones/busqueda")),
                                             ft.ElevatedButton("Plataformas para buscar empleo",
                                                               on_click=lambda _: page.go("/recomendaciones/plataformas")),
                                         ]

                            )

                        )

                    ],
                )
            )
        if page.route == "/recomendaciones/proceso":
            page.views.append(
                ft.View(
                    "/recomendaciones/proceso",
                    [
                        ft.AppBar(
                            leading=ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=lambda _: page.go("/recomendaciones")),
                            leading_width=50,
                            center_title=True,
                            title=ft.Text("Proceso de contratacion laboral"),
                            bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Container(
                            alignment=ft.alignment.center,
                            padding=25,
                            content=ft.Column(
                                controls=[ft.Text("¿Que debo saber sobre el proceso de contratacion laboral?"),
                                ft.Text(
                                    "Buscar empleo puede ser un proceso desafiante, pero es importante que conozcas"),
                                ft.Text("cual es el proceso de contratación laboral:"),
                                ft.Text("Comienza cuando una empresa anuncia una plaza disponible."),
                                ft.Text(
                                    "Aplicación: es el proceso en el que los posibles candidatos envían su información"),
                                ft.Text("para aplicar a la plaza anunciada por la empresa."),
                                ft.Text(
                                    "Selección: El area de reclutamiento de la empresa evalúa la información de los"),
                                ft.Text("candidatos y selecciona los perfiles que considera que se acoplan al puesto."),]

                            )

                        )


                    ]

                )
            )
        if page.route == "/recomendaciones/entrevistas":
            page.views.append(
                ft.View(
                    "/recomendaciones/entrevistas",
                    [
                        ft.AppBar(
                            leading=ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=lambda _: page.go("/recomendaciones")),
                            leading_width=50,
                            center_title=True,
                            title=ft.Text("Recomendaciones para Entrevistas de Trabajo"),
                            bgcolor=ft.colors.SURFACE_VARIANT),

                    ]

                )
            )
        if page.route == "/recomendaciones/busqueda":
            page.views.append(
                ft.View(
                    "/recomendaciones/busqueda",
                    [
                        ft.AppBar(
                            leading=ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=lambda _: page.go("/recomendaciones")),
                            leading_width=50,
                            center_title=True,
                            title=ft.Text("Tips para la Busqueda de Empleo"),
                            bgcolor=ft.colors.SURFACE_VARIANT),

                    ]

                )
            )
        if page.route == "/recomendaciones/plataformas":
            page.views.append(
                ft.View(
                    "/recomendaciones/plataformas",
                    [
                        ft.AppBar(
                            leading=ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=lambda _: page.go("/recomendaciones")),
                            leading_width=50,
                            center_title=True,
                            title=ft.Text("Plataformas para Buscar Empleo"),
                            bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text("Plataformas que existen para encontrar o aplicar a un empleo"),
                        ft.Text("LinkedIn"),
                        ft.Text("Transdoc")


                    ]

                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main, view=ft.WEB_BROWSER)