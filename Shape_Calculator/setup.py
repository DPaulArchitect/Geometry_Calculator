# setup.py

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from shapes import Square, Rectangle, Triangle, Circle, Ellipse, Parallelogram, Trapezoid


class GeometryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Geometry Calculator")

        # Create a notebook (tabbed interface)
        self.tabControl = ttk.Notebook(root)

        # Add tabs for each shape
        self.square_tab = ttk.Frame(self.tabControl)
        self.rectangle_tab = ttk.Frame(self.tabControl)
        self.triangle_tab = ttk.Frame(self.tabControl)
        self.circle_tab = ttk.Frame(self.tabControl)
        self.ellipse_tab = ttk.Frame(self.tabControl)
        self.parallelogram_tab = ttk.Frame(self.tabControl)
        self.trapezoid_tab = ttk.Frame(self.tabControl)

        self.tabControl.add(self.square_tab, text="Square")
        self.tabControl.add(self.rectangle_tab, text="Rectangle")
        self.tabControl.add(self.triangle_tab, text="Triangle")
        self.tabControl.add(self.circle_tab, text="Circle")
        self.tabControl.add(self.ellipse_tab, text="Ellipse")
        self.tabControl.add(self.parallelogram_tab, text="Parallelogram")
        self.tabControl.add(self.trapezoid_tab, text="Trapezoid")

        self.tabControl.pack(expand=1, fill="both")

        # Create widgets for Square tab
        self.square_label = ttk.Label(self.square_tab, text="Enter side length:")
        self.square_label.pack(pady=10)
        self.square_entry = ttk.Entry(self.square_tab)
        self.square_entry.pack()
        self.square_button = ttk.Button(self.square_tab, text="Calculate", command=self.calculate_square)
        self.square_button.pack(pady=10)
        self.square_result_label = ttk.Label(self.square_tab, text="")
        self.square_result_label.pack(pady=10)

        # Create widgets for Rectangle tab
        self.rectangle_label1 = ttk.Label(self.rectangle_tab, text="Enter length:")
        self.rectangle_label1.pack(pady=10)
        self.rectangle_entry1 = ttk.Entry(self.rectangle_tab)
        self.rectangle_entry1.pack()
        self.rectangle_label2 = ttk.Label(self.rectangle_tab, text="Enter width:")
        self.rectangle_label2.pack()
        self.rectangle_entry2 = ttk.Entry(self.rectangle_tab)
        self.rectangle_entry2.pack()
        self.rectangle_button = ttk.Button(self.rectangle_tab, text="Calculate", command=self.calculate_rectangle)
        self.rectangle_button.pack(pady=10)
        self.rectangle_result_label = ttk.Label(self.rectangle_tab, text="")
        self.rectangle_result_label.pack(pady=10)

        # Create widgets for Triangle tab
        self.triangle_label1 = ttk.Label(self.triangle_tab, text="Enter side 1:")
        self.triangle_label1.pack(pady=10)
        self.triangle_entry1 = ttk.Entry(self.triangle_tab)
        self.triangle_entry1.pack()
        self.triangle_label2 = ttk.Label(self.triangle_tab, text="Enter side 2:")
        self.triangle_label2.pack()
        self.triangle_entry2 = ttk.Entry(self.triangle_tab)
        self.triangle_entry2.pack()
        self.triangle_label3 = ttk.Label(self.triangle_tab, text="Enter side 3:")
        self.triangle_label3.pack()
        self.triangle_entry3 = ttk.Entry(self.triangle_tab)
        self.triangle_entry3.pack()
        self.triangle_label4 = ttk.Label(self.triangle_tab, text="Enter base:")
        self.triangle_label4.pack()
        self.triangle_entry4 = ttk.Entry(self.triangle_tab)
        self.triangle_entry4.pack()
        self.triangle_label5 = ttk.Label(self.triangle_tab, text="Enter height:")
        self.triangle_label5.pack()
        self.triangle_entry5 = ttk.Entry(self.triangle_tab)
        self.triangle_entry5.pack()
        self.triangle_button = ttk.Button(self.triangle_tab, text="Calculate", command=self.calculate_triangle)
        self.triangle_button.pack(pady=10)
        self.triangle_result_label = ttk.Label(self.triangle_tab, text="")
        self.triangle_result_label.pack(pady=10)

        # Create widgets for Circle tab
        self.circle_label = ttk.Label(self.circle_tab, text="Enter radius:")
        self.circle_label.pack(pady=10)
        self.circle_entry = ttk.Entry(self.circle_tab)
        self.circle_entry.pack()
        self.circle_button = ttk.Button(self.circle_tab, text="Calculate", command=self.calculate_circle)
        self.circle_button.pack(pady=10)
        self.circle_result_label1 = ttk.Label(self.circle_tab, text="Area:")
        self.circle_result_label1.pack()
        self.circle_result_label2 = ttk.Label(self.circle_tab, text="")
        self.circle_result_label2.pack()
        self.circle_result_label3 = ttk.Label(self.circle_tab, text="Circumference:")
        self.circle_result_label3.pack()
        self.circle_result_label4 = ttk.Label(self.circle_tab, text="")
        self.circle_result_label4.pack()

        # Create widgets for Ellipse tab
        self.ellipse_label1 = ttk.Label(self.ellipse_tab, text="Enter semi-major axis:")
        self.ellipse_label1.pack(pady=10)
        self.ellipse_entry1 = ttk.Entry(self.ellipse_tab)
        self.ellipse_entry1.pack()
        self.ellipse_label2 = ttk.Label(self.ellipse_tab, text="Enter semi-minor axis:")
        self.ellipse_label2.pack()
        self.ellipse_entry2 = ttk.Entry(self.ellipse_tab)
        self.ellipse_entry2.pack()
        self.ellipse_button = ttk.Button(self.ellipse_tab, text="Calculate", command=self.calculate_ellipse)
        self.ellipse_button.pack(pady=10)
        self.ellipse_result_label = ttk.Label(self.ellipse_tab, text="")
        self.ellipse_result_label.pack(pady=10)

        # Create widgets for Parallelogram tab
        self.parallelogram_label1 = ttk.Label(self.parallelogram_tab, text="Enter base:")
        self.parallelogram_label1.pack(pady=10)
        self.parallelogram_entry1 = ttk.Entry(self.parallelogram_tab)
        self.parallelogram_entry1.pack()
        self.parallelogram_label2 = ttk.Label(self.parallelogram_tab, text="Enter side:")
        self.parallelogram_label2.pack()
        self.parallelogram_entry2 = ttk.Entry(self.parallelogram_tab)
        self.parallelogram_entry2.pack()
        self.parallelogram_label3 = ttk.Label(self.parallelogram_tab, text="Enter height:")
        self.parallelogram_label3.pack()
        self.parallelogram_entry3 = ttk.Entry(self.parallelogram_tab)
        self.parallelogram_entry3.pack()
        self.parallelogram_button = ttk.Button(self.parallelogram_tab, text="Calculate",
                                               command=self.calculate_parallelogram)
        self.parallelogram_button.pack(pady=10)
        self.parallelogram_result_label = ttk.Label(self.parallelogram_tab, text="")
        self.parallelogram_result_label.pack(pady=10)

        # Create widgets for Trapezoid tab
        self.trapezoid_label1 = ttk.Label(self.trapezoid_tab, text="Enter base 1:")
        self.trapezoid_label1.pack(pady=10)
        self.trapezoid_entry1 = ttk.Entry(self.trapezoid_tab)
        self.trapezoid_entry1.pack()
        self.trapezoid_label2 = ttk.Label(self.trapezoid_tab, text="Enter base 2:")
        self.trapezoid_label2.pack()
        self.trapezoid_entry2 = ttk.Entry(self.trapezoid_tab)
        self.trapezoid_entry2.pack()
        self.trapezoid_label3 = ttk.Label(self.trapezoid_tab, text="Enter side 1:")
        self.trapezoid_label3.pack()
        self.trapezoid_entry3 = ttk.Entry(self.trapezoid_tab)
        self.trapezoid_entry3.pack()
        self.trapezoid_label4 = ttk.Label(self.trapezoid_tab, text="Enter side 2:")
        self.trapezoid_label4.pack()
        self.trapezoid_entry4 = ttk.Entry(self.trapezoid_tab)
        self.trapezoid_entry4.pack()
        self.trapezoid_label5 = ttk.Label(self.trapezoid_tab, text="Enter height:")
        self.trapezoid_label5.pack()
        self.trapezoid_entry5 = ttk.Entry(self.trapezoid_tab)
        self.trapezoid_entry5.pack()
        self.trapezoid_button = ttk.Button(self.trapezoid_tab, text="Calculate", command=self.calculate_trapezoid)
        self.trapezoid_button.pack(pady=10)
        self.trapezoid_result_label = ttk.Label(self.trapezoid_tab, text="")
        self.trapezoid_result_label.pack(pady=10)

    def calculate_square(self):
        try:
            side_length = float(self.square_entry.get())
            square = Square(side_length)
            perimeter = square.square_perimeter()
            area = square.square_area()
            self.square_result_label.config(text=f"Perimeter: {perimeter}, Area: {area}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for side length.")

    def calculate_rectangle(self):
        try:
            length = float(self.rectangle_entry1.get())
            width = float(self.rectangle_entry2.get())
            rectangle = Rectangle(length, width)
            perimeter = rectangle.rectangle_perimeter()
            area = rectangle.rectangle_area()
            self.rectangle_result_label.config(text=f"Perimeter: {perimeter}, Area: {area}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for length and width.")

    def calculate_triangle(self):
        try:
            side1 = float(self.triangle_entry1.get())
            side2 = float(self.triangle_entry2.get())
            side3 = float(self.triangle_entry3.get())
            base = float(self.triangle_entry4.get())
            height = float(self.triangle_entry5.get())
            triangle = Triangle(side1, side2, side3, base, height)
            perimeter = triangle.triangle_perimeter()
            area = triangle.triangle_area()
            self.triangle_result_label.config(text=f"Perimeter: {perimeter}, Area: {area}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for all sides, base, and height.")

    def calculate_circle(self):
        try:
            radius = float(self.circle_entry.get())
            circle = Circle(radius)
            area = circle.circle_area()
            circumference = circle.circle_circumference()
            self.circle_result_label2.config(text=f"{area:.2f}")
            self.circle_result_label4.config(text=f"{circumference:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for radius.")

    def calculate_ellipse(self):
        try:
            semi_major_axis = float(self.ellipse_entry1.get())
            semi_minor_axis = float(self.ellipse_entry2.get())
            ellipse = Ellipse(semi_major_axis, semi_minor_axis)
            area = ellipse.ellipse_area()
            self.ellipse_result_label.config(text=f"Area: {area:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for semi-major and semi-minor axes.")

    def calculate_parallelogram(self):
        try:
            base = float(self.parallelogram_entry1.get())
            side = float(self.parallelogram_entry2.get())
            height = float(self.parallelogram_entry3.get())
            parallelogram = Parallelogram(base, side, height)
            perimeter = parallelogram.parallelogram_perimeter()
            area = parallelogram.parallelogram_area()
            self.parallelogram_result_label.config(text=f"Perimeter: {perimeter}, Area: {area}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for base, side, and height.")

    def calculate_trapezoid(self):
        try:
            base1 = float(self.trapezoid_entry1.get())
            base2 = float(self.trapezoid_entry2.get())
            side1 = float(self.trapezoid_entry3.get())
            side2 = float(self.trapezoid_entry4.get())
            height = float(self.trapezoid_entry5.get())
            trapezoid = Trapezoid(base1, base2, side1, side2, height)
            perimeter = trapezoid.trapezoid_perimeter()
            area = trapezoid.trapezoid_area()
            self.trapezoid_result_label.config(text=f"Perimeter: {perimeter}, Area: {area}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for all dimensions.")


def run_gui():
    root = tk.Tk()
    app = GeometryApp(root)
    root.mainloop()


# Entry point for running the GUI
if __name__ == "__main__":
    run_gui()
