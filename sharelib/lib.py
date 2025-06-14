import ctypes
import pathlib

script_dir = pathlib.Path(__file__).parent.resolve()


sdl3 = ctypes.CDLL(str(script_dir / "libSDL3.so.0"))
sdl3_ttf = ctypes.CDLL(str(script_dir / "libSDL3_ttf.so.0"))
