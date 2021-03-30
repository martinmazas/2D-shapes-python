# Ex 1
# Niv Swisa 307929257 and Martin Mazas 329834857

import math
from tkinter import *

# Global variables
click_number = x0 = y0 = x1 = y1 = x2 = y2 = x3 = y3 = radius = 0
height = width = 700
flag_line = flag_curve = flag_circle = 0

# Graphic window global variables
window = Tk()
window.title("Ex 1")
window.geometry("700x700")
canvas = Canvas(window, width=width, height=height, bg='grey')
img = PhotoImage(width=width, height=height)
canvas.create_image((width // 2, height // 2), image=img, state="normal")


def main():
    # Set the points for the selected shape. Each point came from the click event on the screen
    def click_event(event):
        global click_number, x0, y0, x1, y1, x2, y2, x3, y3, radius
        # Line shape is activated
        if flag_line:
            if click_number == 0:
                x0 = event.x
                y0 = event.y
                click_number = 1
            else:
                x1 = event.x
                y1 = event.y
                my_line(x0, y0, x1, y1)
                click_number = 0
        # Circle shape is activated
        elif flag_circle:
            if click_number == 0:
                x0 = event.x
                y0 = event.y
                click_number = 1
            else:
                x1 = event.x
                y1 = event.y
                my_circle(x0, y0, x1, y1)
                click_number = 0
        # Curve shape is activated
        elif flag_curve:
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
                my_curve(x0, y0, x1, y1, x2, y2, x3, y3)
                click_number = 0

    # Draw a single pixel
    def draw_pixel(x, y):
        global img
        if x < 0 or y < 0:
            pass
        img.put("#000", (x, y))

    # Draw a line
    def my_line(xx0, yy0, xx1, yy1):
        global x0, y0, x1, y1, click_number
        x0 = xx0
        y0 = yy0
        x1 = xx1
        y1 = yy1

        # DDA Algorithm
        delta_x = x0 - x1
        delta_y = y0 - y1
        _range = max(abs(delta_x), abs(delta_y))
        dx = delta_x / _range
        dy = delta_y / _range
        x = x1
        y = y1
        for i in range(_range):
            draw_pixel(round(x), round(y))
            x += dx
            y += dy

    # Draw line activation
    def activate_line():
        global flag_line, flag_curve, flag_circle
        flag_line = 1
        flag_circle = flag_curve = 0
        canvas.grid(row=3, column=3)
        canvas.bind('<Button-1>', click_event)

    # Draw circle activation
    def activate_circle():
        global flag_line, flag_curve, flag_circle
        flag_circle = 1
        flag_curve = flag_line = 0
        canvas.grid(row=3, column=3)
        canvas.bind('<Button-1>', click_event)

    # Draw curve activation
    def activate_curve():
        global flag_line, flag_curve, flag_circle
        flag_curve = 1
        flag_circle = flag_line = 0
        canvas.grid(row=3, column=3)
        canvas.bind('<Button-1>', click_event)

    # Clear activation
    def activate_clear():
        global canvas, img, flag_curve, flag_line, flag_circle
        canvas.delete(img)
        img = PhotoImage(width=width, height=height)
        canvas.create_image((width // 2, height // 2), image=img, state="normal")
        flag_line = flag_curve = flag_circle = 0

    # Radius calculation
    def calculate_radius(xx0, xx1, yy0, yy1):
        x_minus_x = pow((xx0 - xx1), 2)
        y_minus_y = pow((yy0 - yy1), 2)
        return math.sqrt((x_minus_x + y_minus_y))

    # Draw circle pixel
    def draw_pixel_circle(x_center, y_center, x, y):
        draw_pixel(round(x_center + x), round(y_center + y))
        draw_pixel(round(x_center - x), round(y_center + y))
        draw_pixel(round(x_center + x), round(y_center - y))
        draw_pixel(round(x_center - x), round(y_center - y))
        draw_pixel(round(x_center + y), round(y_center + x))
        draw_pixel(round(x_center - y), round(y_center + x))
        draw_pixel(round(x_center + y), round(y_center - x))
        draw_pixel(round(x_center - y), round(y_center - x))

    # Draw circle
    def my_circle(xx0, yy0, xx1, yy1):
        global click_number, x0, x1, y0, y1, radius
        x0 = xx0
        y0 = yy0
        x1 = xx1
        y1 = yy1
        radius = calculate_radius(x0, x1, y0, y1)
        x = 0
        y = radius
        p = 3 - 2 * radius
        # Bresenham's algorithm
        while x < y:
            draw_pixel_circle(x0, y0, x, y)
            if p < 0:
                p = p + 4 * x + 6
            else:
                draw_pixel_circle(x0, y0, x + 1, y)
                p = p + 4 * (x - y) + 10
                y -= 1
            x += 1
        if x == y:
            draw_pixel_circle(x0, y0, x, y)

    # def my_curve(xx0, yy0, xx1, yy1, xx2, yy2, xx3, yy3):
    #     canvas.create_line(xx0, yy0, xx1, yy1)
    #     canvas.create_line(xx2, yy2, xx3, yy3)
    #     canvas.create_line(xx2, yy2, xx1, yy1)

    # Draw curve
    def my_curve(xx0, yy0, xx1, yy1, xx2, yy2, xx3, yy3):
        global x0, y0, x1, y1, x2, y2, x3, y3
        x0 = xx0
        y0 = yy0
        x1 = xx1
        y1 = yy1
        x2 = xx2
        y2 = yy2
        x3 = xx3
        y3 = yy3

        my_line(x0, y0, x1, y1)
        my_line(x2, y2, x3, y3)
        my_line(x1, y1, x2, y2)



    # Buttons
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
