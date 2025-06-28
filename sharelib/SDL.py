import ctypes

from .lib import sdl3
from .SDL_events import *  # noqa
from .SDL_mouse import *  # noqa
from .SDL_pixels import *  # noqa
from .SDL_rect import *  # noqa
from .SDL_video import *  # noqa

# region SDL constants

SDL_INIT_AUDIO = 0x00000010  # /**< `SDL_INIT_AUDIO` implies `SDL_INIT_EVENTS` */
SDL_INIT_VIDEO = 0x00000020  # /**< `SDL_INIT_VIDEO` implies `SDL_INIT_EVENTS`, should be initialized on the main thread */
SDL_INIT_JOYSTICK = 0x00000200  # /**< `SDL_INIT_JOYSTICK` implies `SDL_INIT_EVENTS` */
SDL_INIT_HAPTIC = 0x00001000  #
SDL_INIT_GAMEPAD = 0x00002000  # /**< `SDL_INIT_GAMEPAD` implies `SDL_INIT_JOYSTICK` */
SDL_INIT_EVENTS = 0x00004000  #
SDL_INIT_SENSOR = 0x00008000  # /**< `SDL_INIT_SENSOR` implies `SDL_INIT_EVENTS` */
SDL_INIT_CAMERA = 0x00010000  # /**< `SDL_INIT_CAMERA` implies `SDL_INIT_EVENTS` */


SDL_WINDOW_FULLSCREEN = 0x0000000000000001  #    /**< window is in fullscreen mode */
SDL_WINDOW_OPENGL = 0x0000000000000002  #    /**< window usable with OpenGL context */
SDL_WINDOW_OCCLUDED = 0x0000000000000004  #    /**< window is occluded */
SDL_WINDOW_HIDDEN = 0x0000000000000008  #    /**< window is neither mapped onto the desktop nor shown in the taskbar/dock/window list; SDL_ShowWindow() is required for it to become visible */
SDL_WINDOW_BORDERLESS = 0x0000000000000010  #    /**< no window decoration */
SDL_WINDOW_RESIZABLE = 0x0000000000000020  #    /**< window can be resized */
SDL_WINDOW_MINIMIZED = 0x0000000000000040  #    /**< window is minimized */
SDL_WINDOW_MAXIMIZED = 0x0000000000000080  #    /**< window is maximized */
SDL_WINDOW_MOUSE_GRABBED = (
    0x0000000000000100  #    /**< window has grabbed mouse input */
)
SDL_WINDOW_INPUT_FOCUS = 0x0000000000000200  #    /**< window has input focus */
SDL_WINDOW_MOUSE_FOCUS = 0x0000000000000400  #    /**< window has mouse focus */
SDL_WINDOW_EXTERNAL = 0x0000000000000800  #    /**< window not created by SDL */
SDL_WINDOW_MODAL = 0x0000000000001000  #    /**< window is modal */
SDL_WINDOW_HIGH_PIXEL_DENSITY = 0x0000000000002000  #    /**< window uses high pixel density back buffer if possible */
SDL_WINDOW_MOUSE_CAPTURE = 0x0000000000004000  #    /**< window has mouse captured (unrelated to MOUSE_GRABBED) */
SDL_WINDOW_MOUSE_RELATIVE_MODE = (
    0x0000000000008000  #    /**< window has relative mode enabled */
)
SDL_WINDOW_ALWAYS_ON_TOP = (
    0x0000000000010000  #    /**< window should always be above others */
)
SDL_WINDOW_UTILITY = 0x0000000000020000  #    /**< window should be treated as a utility window, not showing in the task bar and window list */
SDL_WINDOW_TOOLTIP = 0x0000000000040000  #    /**< window should be treated as a tooltip and does not get mouse or keyboard focus, requires a parent window */
SDL_WINDOW_POPUP_MENU = 0x0000000000080000  #    /**< window should be treated as a popup menu, requires a parent window */
SDL_WINDOW_KEYBOARD_GRABBED = (
    0x0000000000100000  #    /**< window has grabbed keyboard input */
)
SDL_WINDOW_VULKAN = 0x0000000010000000  #    /**< window usable for Vulkan surface */
SDL_WINDOW_METAL = 0x0000000020000000  #    /**< window usable for Metal view */
SDL_WINDOW_TRANSPARENT = 0x0000000040000000  #    /**< window with transparent buffer */
SDL_WINDOW_NOT_FOCUSABLE = (
    0x0000000080000000  #    /**< window should not be focusable */
)

# endregion

# region Define argument and return types

# void SDL_SetMainReady(void);
sdl3.SDL_SetMainReady.argtypes = []
sdl3.SDL_SetMainReady.restype = None

# bool SDL_SetWindowBordered(SDL_Window *window, bool bordered);
sdl3.SDL_SetWindowBordered.argtypes = [
    ctypes.c_void_p,
    ctypes.c_bool,
]
sdl3.SDL_SetWindowBordered.restype = ctypes.c_bool

# typedef SDL_HitTestResult (SDLCALL *SDL_HitTest)(SDL_Window *win, const SDL_Point *area, void *data);
SDL_HitTest = ctypes.CFUNCTYPE(
    ctypes.c_int,  # Return type (SDL_HitTestResult)
    ctypes.c_void_p,  # Window pointer
    ctypes.POINTER(SDL_Point),  # Mouse position pointer
    ctypes.c_void_p,  # User data
)

# bool SDL_SetWindowOpacity(SDL_Window *window, float opacity);
sdl3.SDL_SetWindowOpacity.argtypes = [
    ctypes.c_void_p,  # SDL_Window* window
    ctypes.c_float,  # float opacity
]
sdl3.SDL_SetWindowOpacity.restype = ctypes.c_bool

# bool SDL_SetWindowHitTest(SDL_Window *window, SDL_HitTest callback, void *callback_data);
sdl3.SDL_SetWindowHitTest.argtypes = [
    ctypes.c_void_p,
    SDL_HitTest,
    ctypes.c_void_p,
]
sdl3.SDL_SetWindowHitTest.restype = ctypes.c_bool

# bool SDL_Init(SDL_InitFlags flags);
sdl3.SDL_Init.argtypes = [ctypes.c_uint32]  # SDL_InitFlags (usually a uint32_t)
sdl3.SDL_Init.restype = ctypes.c_bool  # Returns bool (SDL_TRUE or SDL_FALSE)

# void SDL_Quit(void);
sdl3.SDL_Quit.argtypes = []
sdl3.SDL_Quit.restype = None  # No return value

# SDL_Window * SDL_CreateWindow(const char *title, int w, int h, SDL_WindowFlags flags);
sdl3.SDL_CreateWindow.argtypes = [
    ctypes.c_char_p,  # const char *title
    ctypes.c_int,  # int w
    ctypes.c_int,  # int h
    ctypes.c_uint32,  # SDL_WindowFlags (usually a uint32_t)
]
sdl3.SDL_CreateWindow.restype = ctypes.c_void_p  # SDL_Window* as void pointer

# void SDL_DestroyWindow(SDL_Window *window);
sdl3.SDL_DestroyWindow.argtypes = [ctypes.c_void_p]  # SDL_Window* window
sdl3.SDL_DestroyWindow.restype = None  # No return value

# SDL_Renderer * SDL_CreateRenderer(SDL_Window *window, const char *name);
sdl3.SDL_CreateRenderer.argtypes = [
    ctypes.c_void_p,  # SDL_Window* window
    ctypes.c_char_p,  # const char *name
]
sdl3.SDL_CreateRenderer.restype = ctypes.c_void_p  # SDL_Renderer* as void pointer

# void SDL_DestroyRenderer(SDL_Renderer *renderer);
sdl3.SDL_DestroyRenderer.argtypes = [ctypes.c_void_p]  # SDL_Renderer* renderer
sdl3.SDL_DestroyRenderer.restype = None  # No return value

# bool SDL_SetRenderDrawColor(SDL_Renderer *renderer, Uint8 r, Uint8 g, Uint8 b, Uint8 a);
sdl3.SDL_SetRenderDrawColor.argtypes = [
    ctypes.c_void_p,  # SDL_Renderer* renderer
    ctypes.c_uint8,  # Uint8 r
    ctypes.c_uint8,  # Uint8 g
    ctypes.c_uint8,  # Uint8 b
    ctypes.c_uint8,  # Uint8 a
]
sdl3.SDL_SetRenderDrawColor.restype = (
    ctypes.c_bool
)  # Returns bool (SDL_TRUE or SDL_FALSE)

# bool SDL_RenderPresent(SDL_Renderer *renderer);
sdl3.SDL_RenderPresent.argtypes = [ctypes.c_void_p]  # SDL_Renderer* renderer
sdl3.SDL_RenderPresent.restype = ctypes.c_bool  # Returns bool (SDL_TRUE or SDL_FALSE)

# bool SDL_RenderClear(SDL_Renderer *renderer);
sdl3.SDL_RenderClear.argtypes = [ctypes.c_void_p]
sdl3.SDL_RenderClear.restype = ctypes.c_bool

# bool SDL_RenderTexture(SDL_Renderer *renderer, SDL_Texture *texture, const SDL_FRect *srcrect, const SDL_FRect *dstrect);
sdl3.SDL_RenderTexture.argtypes = [
    ctypes.c_void_p,  # SDL_Renderer* renderer
    ctypes.c_void_p,  # SDL_Texture* texture
    ctypes.POINTER(SDL_FRect),  # const SDL_FRect* srcrect
    ctypes.POINTER(SDL_FRect),  # const SDL_FRect* dstrect
]
sdl3.SDL_RenderTexture.restype = ctypes.c_bool  # Returns bool (SDL_TRUE or SDL_FALSE)

# SDL_Texture * SDL_CreateTextureFromSurface(SDL_Renderer *renderer, SDL_Surface *surface);
sdl3.SDL_CreateTextureFromSurface.argtypes = [
    ctypes.c_void_p,  # SDL_Renderer* renderer
    ctypes.c_void_p,  # SDL_Surface* surface
]
sdl3.SDL_CreateTextureFromSurface.restype = (
    ctypes.c_void_p
)  # SDL_Texture* as void pointer

# bool SDL_GetTextureSize(SDL_Texture *texture, float *w, float *h);
sdl3.SDL_GetTextureSize.argtypes = [
    ctypes.c_void_p,  # SDL_Texture* texture
    ctypes.POINTER(ctypes.c_float),  # float* w
    ctypes.POINTER(ctypes.c_float),  # float* h
]
sdl3.SDL_GetTextureSize.restype = ctypes.c_bool  # Returns bool (SDL_TRUE or SDL_FALSE)

# void SDL_DestroyTexture(SDL_Texture *texture);
sdl3.SDL_DestroyTexture.argtypes = [ctypes.c_void_p]  # SDL_Texture* texture
sdl3.SDL_DestroyTexture.restype = None  # No return value

# void SDL_DestroySurface(SDL_Surface *surface);
sdl3.SDL_DestroySurface.argtypes = [ctypes.c_void_p]  # SDL_Surface* surface
sdl3.SDL_DestroySurface.restype = None  # No return value

# bool SDL_PollEvent(SDL_Event *event);
sdl3.SDL_PollEvent.argtypes = [ctypes.c_void_p]  # SDL_Event* event
sdl3.SDL_PollEvent.restype = ctypes.c_bool  # Returns bool (SDL_TRUE or SDL_FALSE)

# const char * SDL_GetError(void);
sdl3.SDL_GetError.argtypes = []
sdl3.SDL_GetError.restype = ctypes.c_char_p  # Returns a C string (const char*)

# endregion
