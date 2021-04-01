#!/usr/bin/env python
# Ex 1
# Niv Swisa 307929257 and Martin Mazas 329834857

import math
from tkinter import *

# Global variables
click_number = x0 = y0 = x1 = y1 = x2 = y2 = x3 = y3 = radius = 0
height = width = 1000
flag_line = flag_curve = flag_circle = 0

# Graphic window global variables
window = Tk()
window.title("Ex 1")
window.geometry("1000x1000")
canvas = Canvas(window, width=width, height=height)
img = PhotoImage(width=width, height=height)
canvas.create_image((width // 2, height // 2), image=img, state="normal")
lines_number = Label(window, text="Number of lines").place(x=210)
lines_entry_number = Entry(window)
lines_entry_number.place(x=320)


def main():
    # Draw a single pixel
    def draw_pixel(x, y):
        global img
        # Check that the point is on the window
        if x < 0 or y < 0:
            return
        img.put("#000", (x, y))

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

    # Draw line activation
    def activate_line():
        global flag_line, flag_curve, flag_circle

        # Change line_btn to selected button and activate flag_line
        line_btn.configure(highlightbackground="grey")
        curve_btn.configure(highlightbackground="white")
        circle_btn.configure(highlightbackground="white")
        flag_line = 1
        flag_circle = flag_curve = 0
        canvas.grid(row=3, column=3)
        canvas.bind('<Button-1>', click_event)

    # Draw circle activation
    def activate_circle():
        global flag_line, flag_curve, flag_circle

        # Change circle_btn to selected button and activate flag_circle
        line_btn.configure(highlightbackground="white")
        curve_btn.configure(highlightbackground="white")
        circle_btn.configure(highlightbackground="grey")
        flag_circle = 1
        flag_curve = flag_line = 0
        canvas.grid(row=3, column=3)
        canvas.bind('<Button-1>', click_event)

    # Draw curve activation
    def activate_curve():
        global flag_line, flag_curve, flag_circle

        # Change curve_btn to selected button and activate flag_curve
        line_btn.configure(highlightbackground="white")
        curve_btn.configure(highlightbackground="grey")
        circle_btn.configure(highlightbackground="white")
        flag_curve = 1
        flag_circle = flag_line = 0
        canvas.grid(row=3, column=3)
        canvas.bind('<Button-1>', click_event)

    # Clear activation
    def activate_clear():
        global canvas, img, flag_curve, flag_line, flag_circle, click_number
        canvas.delete(img)
        img = PhotoImage(width=width, height=height)
        canvas.create_image((width // 2, height // 2), image=img, state="normal")
        click_number = 0

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
        if _range == 0:
            return
        else:
            dx = delta_x / _range
            dy = delta_y / _range
            x = x1
            y = y1
            for i in range(_range):
                draw_pixel(round(x), round(y))
                x += dx
                y += dy

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
        global x0, y0, x1, y1, radius
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

        num_of_lines = lines_entry_number.get()

        # default number of lines is 4
        if num_of_lines == '':
            num_of_lines = 4
        else:
            num_of_lines = int(num_of_lines)

        # Bezier curves
        dt = 1 / num_of_lines
        ax = -x0 + 3 * x1 - 3 * x2 + x3
        bx = 3 * x0 - 6 * x1 + 3 * x2
        cx = -3 * x0 + 3 * x1
        dx = x0

        ay = -y0 + 3 * y1 - 3 * y2 + y3
        by = 3 * y0 - 6 * y1 + 3 * y2
        cy = -3 * y0 + 3 * y1
        dy = y0

        f_x, f_y = x0, y0
        t = dt
        while t < 1.0:
            xt, yt = int(ax * pow(t, 3) + bx * pow(t, 2) + cx * t + dx), int(ay * pow(t, 3) + by * pow(t, 2) + cy * t + dy)
            my_line(f_x, f_y, xt, yt)
            f_x, f_y = xt, yt
            t += dt
        my_line(xt, yt, x3, y3)

    # Buttons
    line_btn = Button(window, text="Line", command=activate_line)
    line_btn.grid(row=0, column=1)

    circle_btn = Button(window, text="Circle", command=activate_circle)
    circle_btn.grid(row=0, column=1)
    circle_btn.place(x=70)

    curve_btn = Button(window, text="Curve", command=activate_curve)
    curve_btn.grid(row=0, column=1)
    curve_btn.place(x=140)

    clear_btn = Button(window, text="Clear", command=activate_clear)
    clear_btn.grid(row=0, column=1)
    clear_btn.place(x=550)

    window.mainloop()


if __name__ == '__main__':
    main()
