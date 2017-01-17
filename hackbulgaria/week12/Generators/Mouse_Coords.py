from Xlib import display

def mouse_coords():
    data = display.Display().screen().root.query_pointer()._data
    return data["root_x"], data["root_y"]
