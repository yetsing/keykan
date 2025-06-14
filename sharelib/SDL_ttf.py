import ctypes

from .lib import sdl3_ttf
from .SDL_pixels import SDL_Color

# bool TTF_Init(void);
sdl3_ttf.TTF_Init.argtypes = []
sdl3_ttf.TTF_Init.restype = ctypes.c_bool  # Returns bool (SDL_TRUE or SDL_FALSE)

# void TTF_Quit(void);
sdl3_ttf.TTF_Quit.argtypes = []
sdl3_ttf.TTF_Quit.restype = None  # No return value

# TTF_Font *TTF_OpenFont(const char *file, float ptsize);
sdl3_ttf.TTF_OpenFont.argtypes = [
    ctypes.c_char_p,  # const char *file
    ctypes.c_float,  # float ptsize
]
sdl3_ttf.TTF_OpenFont.restype = ctypes.c_void_p  # TTF_Font* as void pointer

# SDL_Surface * TTF_RenderText_Solid(TTF_Font *font, const char *text, size_t length, SDL_Color fg);
sdl3_ttf.TTF_RenderText_Solid.argtypes = [
    ctypes.c_void_p,  # TTF_Font* font
    ctypes.c_char_p,  # const char *text
    ctypes.c_size_t,  # size_t length
    SDL_Color,  # SDL_Color fg
]

# SDL_Surface * TTF_RenderText_Blended(TTF_Font *font, const char *text, size_t length, SDL_Color fg);
sdl3_ttf.TTF_RenderText_Blended.argtypes = [
    ctypes.c_void_p,  # TTF_Font* font
    ctypes.c_char_p,  # const char *text
    ctypes.c_size_t,  # size_t length
    SDL_Color,  # SDL_Color fg
]
sdl3_ttf.TTF_RenderText_Blended.restype = (
    ctypes.c_void_p
)  # SDL_Surface* as void pointer

# void TTF_CloseFont(TTF_Font *font);
sdl3_ttf.TTF_CloseFont.argtypes = [ctypes.c_void_p]  # TTF_Font* font
sdl3_ttf.TTF_CloseFont.restype = None  # No return value
