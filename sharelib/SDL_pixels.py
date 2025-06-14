import ctypes


class SDL_Color(ctypes.Structure):
    _fields_ = [
        ("r", ctypes.c_uint8),  # Red component
        ("g", ctypes.c_uint8),  # Green component
        ("b", ctypes.c_uint8),  # Blue component
        ("a", ctypes.c_uint8),  # Alpha component
    ]
