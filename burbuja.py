import flet as ft
from random import randint
import time

def main(page: ft.page):

    def create_containers(numbers):
        container_list = []
        for _ in range(numbers):
            container_list.append(ft.Container(content = ft.Text(value = randint(0,999)),
                        alignment=ft.alignment.center,
                        width = 50,
                        height = 50,
                        bgcolor= ft.colors.TEAL,
                        border_radius = 25))
        return container_list

    row = ft.Row(controls=create_containers(10))
    page.add(row)
    time.sleep(2)

    #Logica
    array = row.controls
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            array[j].bgcolor = ft.colors.RED
            array[j+1].bgcolor = ft.colors.RED
            time.sleep(1)
            page.update()
            if array[j].content.value > array[j+1].content.value:
                array[j] , array[j+1] = array[j+1] , array[j]
            array[j].bgcolor = ft.colors.TEAL
            array[j + 1].bgcolor = ft.colors.TEAL
        array[n-i-1].bgcolor = ft.colors.GREEN_ACCENT


    page.update()



ft.app(target=main)

