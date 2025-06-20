import colorsys
import random

def hex_to_rgb(hex_color):

    hex_color = hex_color.lstrip('#')
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    return r / 255.0, g / 255.0, b / 255.0

def rgb_to_hex(rgb):

    r, g, b = rgb
    return '#{:02x}{:02x}{:02x}'.format(
        int(r * 255), int(g * 255), int(b * 255)
    )

def generate_analogous_palette(base_color, count=3, angle=30):

    r, g, b = hex_to_rgb(base_color)
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    
    palette = [base_color]
    angle_fraction = angle / 360.0
    for i in range(1, count):
        new_h = (h + angle_fraction * i) % 1.0
        new_rgb = colorsys.hls_to_rgb(new_h, l, s)
        palette.append(rgb_to_hex(new_rgb))
    return palette

def generate_complementary_palette(base_color):

    r, g, b = hex_to_rgb(base_color)
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    complementary_h = (h + 0.5) % 1.0
    complementary_rgb = colorsys.hls_to_rgb(complementary_h, l, s)
    return [base_color, rgb_to_hex(complementary_rgb)]

def generate_triadic_palette(base_color):

    r, g, b = hex_to_rgb(base_color)
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    palette = []
    for i in range(3):
        new_h = (h + i/3.0) % 1.0
        new_rgb = colorsys.hls_to_rgb(new_h, l, s)
        palette.append(rgb_to_hex(new_rgb))
    return palette

def generate_random_palette(count=5):

    palette = []
    for _ in range(count):
        r, g, b = random.random(), random.random(), random.random()
        palette.append(rgb_to_hex((r, g, b)))
    return palette
