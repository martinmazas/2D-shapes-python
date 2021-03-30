# Ex 1
# Niv Swisa 307929257 and Martin Mazas 329834857

import math
from tkinter import *
# import re
# import sys
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# Global variables
click_number = x0 = y0 = x1 = y1 = x2 = y2 = x3 = y3 = radius = 0
height = width = 700

window = Tk()
window.title("Ex 1")
window.geometry("700x700")
canvas = Canvas(window, width=width, height=height, bg='grey')
img = PhotoImage(width=width, height=height)
canvas.create_image((width // 2, height // 2), image=img, state="normal")


def main():
    # Draw a single pixel
    def draw_pixel(x, y):
        global img
        if x < 0 or y < 0:
            pass
        img.put("#000", (x, y))

    # Draw a line
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

    # Draw line activation
    def activate_line():
        canvas.grid(row=3, column=3)
        canvas.bind('<Button-1>', my_line)

    # Draw circle activation
    def activate_circle():
        canvas.grid(row=3, column=3)
        canvas.bind('<Button-1>', my_circle)

    def activate_curve():
        canvas.grid(row=3, column=3)
        canvas.bind('<Button-1>', my_curve)

    def activate_clear():
        global canvas, img
        canvas.delete(img)
        img = PhotoImage(width=width, height=height)
        canvas.create_image((width // 2, height // 2), image=img, state="normal")

    # Radius calculation
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

    def draw_pixel_circle(x_center, y_center, x, y):
        draw_pixel(round(x_center + x), round(y_center + y))
        draw_pixel(round(x_center - x), round(y_center + y))
        draw_pixel(round(x_center + x), round(y_center - y))
        draw_pixel(round(x_center - x), round(y_center - y))
        draw_pixel(round(x_center + y), round(y_center + x))
        draw_pixel(round(x_center - y), round(y_center + x))
        draw_pixel(round(x_center + y), round(y_center - x))
        draw_pixel(round(x_center - y), round(y_center - x))

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
            x = 0
            y = radius
            p = 3 - 2 * radius
            while x < y:
                draw_pixel_circle(x0, y0, x, y)
                if p < 0:
                    p = p + 4 * x + 6
                else:
                    draw_pixel_circle(x0, y0, x+1, y)
                    p = p + 4 * (x-y) + 10
                    y -= 1
                x += 1
            if x == y:
                draw_pixel_circle(x0, y0, x, y)
            # draw_pixel_circle(x0, y0, x1, y1)
            # canvas.create_oval(x0-radius, y0-radius, x0+radius, y0+radius, width=7)
            click_number = 0

    # def my_curve(xx0, yy0, xx1, yy1, xx2, yy2, xx3, yy3):
    #     canvas.create_line(xx0, yy0, xx1, yy1)
    #     canvas.create_line(xx2, yy2, xx3, yy3)
    #     canvas.create_line(xx2, yy2, xx1, yy1)
    def my_curve(event):
        global click_number, x0, y0, x1, y1, x2, y2, x3, y3
        if click_number == 0:
            x0 = event.x
            y0 = event.y
            draw_pixel(x0, y0)
            click_number = 1
        elif click_number == 1:
            x1 = event.x
            y1 = event.y
            draw_pixel(x1, y1)
            click_number = 2
        elif click_number == 2:
            x2 = event.x
            y2 = event.y
            draw_pixel(x2, y2)
            click_number = 3
        elif click_number == 3:
            x3 = event.x
            y3 = event.y
            draw_pixel(x3, y3)
            click_number = 0

    # my_window = Tk()

    # my_canvas = Canvas(window, width=700, height=700, background='grey')

    line_btn = Button(window, text="Draw Line", command=activate_line)
    line_btn.grid(row=0, column=1)
    line_btn.place(x=150)
    circle_btn = Button(window, text="Draw Circle", command=activate_circle)
    circle_btn.grid(row=0, column=1)
    circle_btn.place(x=250)
    curve_btn = Button(window, text="Draw Curve", command=activate_curve)
    curve_btn.grid(row=0, column=1)
    curve_btn.place(x=350)
    clear_btn = Button(window, text="Clear", command=activate_clear)
    clear_btn.grid(row=0, column=1)
    clear_btn.place(x=450)

    window.mainloop()


if __name__ == '__main__':
    main()
