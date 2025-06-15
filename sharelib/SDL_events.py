import ctypes

SDL_EVENT_QUIT = 0x100

#  Mouse events
SDL_EVENT_MOUSE_MOTION = 0x400  # /**< Mouse moved */
SDL_EVENT_MOUSE_BUTTON_DOWN = 0x401  # /**< Mouse button pressed */
SDL_EVENT_MOUSE_BUTTON_UP = 0x402  # /**< Mouse button released */
SDL_EVENT_MOUSE_WHEEL = 0x403  # /**< Mouse wheel motion */
SDL_EVENT_MOUSE_ADDED = 0x404  # /**< A new mouse has been inserted into the system */
SDL_EVENT_MOUSE_REMOVED = 0x405  # /**< A mouse has been removed */


class SDL_MouseButtonEvent(ctypes.Structure):
    _fields_ = [
        (
            "type",
            ctypes.c_int,
        ),  # SDL_EVENT_MOUSE_BUTTON_DOWN or SDL_EVENT_MOUSE_BUTTON_UP
        ("reserved", ctypes.c_uint32),
        (
            "timestamp",
            ctypes.c_uint64,
        ),  # In nanoseconds, populated using SDL_GetTicksNS()
        ("windowID", ctypes.c_uint32),  # The window with mouse focus, if any
        (
            "which",
            ctypes.c_uint32,
        ),  # The mouse instance id in relative mode, SDL_TOUCH_MOUSEID for touch events, or 0
        ("button", ctypes.c_uint8),  # The mouse button index
        ("down", ctypes.c_bool),  # true if the button is pressed
        ("clicks", ctypes.c_uint8),  # 1 for single-click, 2 for double-click, etc.
        ("padding", ctypes.c_uint8),
        ("x", ctypes.c_float),  # X coordinate, relative to window
        ("y", ctypes.c_float),  # Y coordinate, relative to window
    ]


class SDL_Event(ctypes.Union):
    _fields_ = [
        ("type", ctypes.c_int),
        ("button", SDL_MouseButtonEvent),  # Mouse button event
        ("padding", ctypes.c_uint8 * 128),
    ]
