#modulo prototipo programado

import flet as ft
import pandas as pd

#Función para menú principal
def menu(page):
    page.add(
        ft.Row(controls=[
        ft.ElevatedButton(text="Crear mi CV"),
        ft.ElevatedButton(text="Guía para crear mi CV"),
        ft.ElevatedButton(text="Manuales de herramientas básicas"),
        ft.ElevatedButton(text="Recomendaciones")
    ])
    )



def prueba_funcion(page):
   with open('prueba.txt', 'r') as file:
       print(file.read())
       page.add(
           ft.Text(file.read())
       )


#Función para mostrar los texto de la pantalla de inicio
def texto_principal(value = "", color = "", weight = "", size = 0):
    pass