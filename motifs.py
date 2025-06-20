import tkinter as tk
import math


# Star
def draw_star(canvas, x, y, size, color, points=5):
    coords = []
    for i in range(2 * points):
        angle = math.pi / points * i
        radius = size if i % 2 == 0 else size / 2
        coords.extend([
            x + radius * math.cos(angle),
            y + radius * math.sin(angle)
        ])
    canvas.create_polygon(
        coords, 
        fill = color,
        outline = "black")
    
# Paisley 
def draw_paisley(canvas, x, y, size, color, variant=1):
    width = size
    height = size * 1.5

    exp = 0.5 if variant == 1 else 0.3 if variant == 2 else 1.0

    points = []

    for i in range(11):
        t = i / 10.0
        x_offset = - (width / 2) * ((1 - t) ** exp)
        y_coord = (y - height / 2) + t * height
        points.append((x + x_offset, y_coord))
    
    right_points = []

    for i in range(11):
        t = 1 - (i / 10.0)
        x_offset = - (width / 2) * ((1 - t) ** exp)
        y_coord = (y - height / 2) + t * height
        right_points.append((x - x_offset, y_coord))

    polygon_points = points + right_points

    flat_points = [
        coord for point in polygon_points for coord in point]
    
    canvas.create_polygon(
        flat_points, 
        fill=color, 
        outline="black",
        smooth=True)
    
# Leaf 
def draw_leaf(canvas, x, y, size, color):
    width = size
    height = size * 1.5

    left_point = []
    right_point = []

    for i in range(11):
        t = i / 10.0

        x_offset =  - (width / 2) * math.sin(math.pi * t)
        y_coord = y - height / 2 + t * height
        left_point.append((x + x_offset, y_coord))

    for i in range(11):
        t = i / 10.0
        x_offset = (width / 2) * math.sin(math.pi * t)
        y_coord = y - height / 2 + t * height
        right_point.append((x + x_offset, y_coord))

    polygon_points = left_point + right_point[::-1]
    flat_points = [coord for point in polygon_points for coord in point]

    canvas.create_polygon(*flat_points, fill=color, outline="black", smooth=True)

    canvas.create_line(x, y - height / 2, x, y + height / 2, fill="black", width=1)
    

# Flower
def draw_flower(canvas, x, y, size, color, petals=6):
    petal_length = size
    petal_width = size / 2 

    petal_radius = size / 2

    for i in range(petals):
        angle_deg = (360 / petals) * i
        angle_rad = math.radians(angle_deg)

        petal_center_x = x + petal_radius + math.cos(angle_rad)
        petal_center_y = y + petal_radius + math.sin(angle_rad)

        left = petal_center_x - petal_width / 2
        top = petal_center_y - petal_length / 2
        right = petal_center_x + petal_width / 2
        bottom = petal_center_y + petal_length / 2

        canvas.create_oval(
            left,
            top,
            right,
            bottom,
            fill=color,
            outline="black"
        )
    
    center_radius = size / 4
    canvas.create_oval(
        x - center_radius, y - center_radius,
        x + center_radius, y + center_radius,
        fill="yellow",
        outline="black"
    )

# Crescent
def draw_crescent(canvas, x, y, size, color, offset_factor=0.3, num_points=20):
    r = size
    delta = offset_factor * size
    h = math.sqrt(max(0, r**2, - (delta/2)**2))
    alpha = math.atan2(h, delta/2)

    n = num_points

    arc_A = []

    for j in range(n + 1):
        theta = -alpha + (2 * alpha * j / n)
        arc_A.append(
            (
                x + r * math.cos(theta),
                y + r * math.sin(theta)))

    arc_B = []

    for j in range(n + 1):
        theta = (math.pi - alpha) - (
            2 * (math.pi - alpha) * j / n
        )

        arc_B.append(
            (
                (x + delta) + r * math.cos(theta), 
                y + r * math.sin(theta)))
    
    polygon_points = arc_A + arc_B

    flat_points = [
        coords for points in polygon_points for coords in points
    ]

    canvas.create_polygon(
        *flat_points,
        fill=color,
        outline="black",
        smooth=True
    )

# Diamond

def draw_diamond(
        canvas,
        x,
        y,
        size,
        color
):
    half = size / 2

    vertices = [
        (x, y - half),
        (x + half, y),
        (x, y + half),
        (x - half, y)
    ]
    
    flat_points = [
        coord for vertex in vertices for coord in vertex
    ]

    canvas.create_polygon(
        *flat_points,
        fill=color,
        outline="black"
    )

