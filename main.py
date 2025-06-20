import random
import tkinter as tk

from exports import save_png
from palettes import generate_random_palette
from motifs import (
    draw_star,    
    draw_paisley,
    draw_leaf,
    draw_flower,
    draw_crescent,
    draw_diamond
)

def design(canvas):
    canvas.delete("all")

    width = int(canvas.cget("width"))
    height = int(canvas.cget("height"))

    rows, cols = 3 , 3
    cell_w = width / cols
    cell_h = height / rows

    palettes = generate_random_palette(count=7)

    motif_func = [
        draw_star,
        draw_paisley,
        draw_leaf,
        draw_flower,
        draw_crescent,
        draw_diamond
    ]

    for row in range(rows):
        for col in range(cols):
            center_x = cell_w * col + cell_w / 2
            center_y = cell_h * row + cell_h / 2

            func = random.choice(motif_func)
            color = random.choice(palettes)

            size = min(
                cell_w,
                cell_h 
            ) * 0.4

            try:
                func(
                    canvas,
                    center_x,
                    center_y,
                    size,
                    color
                )
            except Exception as e:
                print(
                    f"Error drawing motif {func.__name__}: {e}"
                )

def save_file(canvas):
    save_png(canvas)


root = tk.Tk()
root.title("Random Shapes")
root.iconbitmap(r"C:\Code\Code_in_place\project\random_shape\icon.ico")

canvas_w = 800
canvas_h = 600

canvas = tk.Canvas(
    root,
    width=canvas_w,
    height=canvas_h,
    bg="white"
)
canvas.pack()

btn_generate = tk.Button(
    root, 
    text="Generate Design", 
    command=lambda: design(canvas)
)
btn_generate.pack(side=tk.LEFT, padx=10, pady=10)

btn_save = tk.Button(
    root, 
    text="Save Design", 
    command=lambda: save_file(canvas)
)
btn_save.pack(side=tk.LEFT, padx=10, pady=10)

design(canvas)

root.mainloop()