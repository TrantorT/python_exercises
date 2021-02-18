from colorthief import ColorThief

color_thief = ColorThief("C:/Users/danimmar/Desktop/sky.jpg")
# get the dominant color
dominant_color = color_thief.get_color(quality=1)
palette = color_thief.get_palette(color_count=6)
print(dominant_color)
print(palette)