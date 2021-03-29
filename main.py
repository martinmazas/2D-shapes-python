# Ex 1
# Niv Swisa 307929257 and Martin Mazas 329834857
import math
from tkinter import *
import re
import sys
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
click_number = 0
x0 = 0
y0 = 0
x1 = 0
y1 = 0
radius = 0
height = 700
width = 700

window = Tk()
window.title("Ex 1")
canvas = Canvas(window, width=width, height=height, bg='grey')
img = PhotoImage(width=width, height=height)
canvas.create_image((width // 2, height // 2), image=img, state="normal")


def main():
    # Draw a single pixel
    def draw_pixel(x, y):
        global canvas, img
        if x < 0 or y < 0:
            pass
        img.put("white", (x, y))

    def my_line(event):
        # DDA algorithm
        global x0, y0, x1, y1, click_number
        if click_number == 0:
            x0 = event.x
            y0 = event.y
            click_number = 1
        else:
            x1 = event.x
            y1 = event.y
            delta_x = x0-x1
            delta_y = y0-y1
            _range = max(abs(delta_x), abs(delta_y))
            dx = delta_x/_range
            dy = delta_y/_range
            x = x1
            y = y1
            for i in range(_range):
                draw_pixel(round(x), round(y))
                x += dx
                y += dy
            click_number = 0

    def activate_line():
        canvas.grid(row=3, column=3)
        canvas.bind('<Button-1>', my_line)

    def activate_circle():
        canvas.grid(row=3, column=3)
        canvas.bind('<Button-1>', my_circle)

    def calculate_radius(xx0, xx1, yy0, yy1):
        x_minus_x = pow((xx0-xx1), 2)
        y_minus_y = pow((yy0-yy1), 2)
        return math.sqrt((x_minus_x + y_minus_y))

    # def my_line(event):
    #     global click_number
    #     global x1, y1
    #     if click_number == 0:
    #         x1 = event.x
    #         y1 = event.y
    #         click_number = 1
    #     else:
    #         x2 = event.x
    #         y2 = event.y
    #         my_canvas.create_line(x1, y1, x2, y2, fill='blue', width=7)
    #         click_number = 0

    def my_circle(event):
        global click_number
        global x0, x1, y0, y1, radius
        if click_number == 0:
            x0 = event.x
            y0 = event.y
            click_number = 1
        else:
            x1 = event.x
            y1 = event.y
            radius = calculate_radius(x0, x1, y0, y1)
            canvas.create_oval(x0-radius, y0-radius, x0+radius, y0+radius, width=7)
            click_number = 0

    # my_window = Tk()
    window.geometry("700x700")
    # my_canvas = Canvas(window, width=700, height=700, background='grey')

    linebtn = Button(window, text="Draw Line", command=activate_line)
    linebtn.grid(row=0, column=1)
    linebtn.place(x=250, y=50)
    # linebtn.bind('<Button-1>', my_line)
    circle_btn = Button(window, text="Draw Circle", command=activate_circle)
    circle_btn.grid(row=0, column=1)
    circle_btn.place(x=350, y=50)

    window.mainloop()


if __name__ == '__main__':
    main()
