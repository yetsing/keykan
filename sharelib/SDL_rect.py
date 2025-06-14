import ctypes


class SDL_Rect(ctypes.Structure):
    _fields_ = [
        ("x", ctypes.c_int),  # x coordinate of the rectangle
        ("y", ctypes.c_int),  # y coordinate of the rectangle
        ("w", ctypes.c_int),  # width of the rectangle
        ("h", ctypes.c_int),  # height of the rectangle
    ]


class SDL_FRect(ctypes.Structure):
    _fields_ = [
        ("x", ctypes.c_float),  # x coordinate of the rectangle
        ("y", ctypes.c_float),  # y coordinate of the rectangle
        ("w", ctypes.c_float),  # width of the rectangle
        ("h", ctypes.c_float),  # height of the rectangle
    ]
