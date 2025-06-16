import ctypes
import os
import platform
import pathlib

script_dir = pathlib.Path(__file__).parent.resolve()
dlls_dir = script_dir / "dlls"

sdl3_libname = "libSDL3.so.0"
sdl3_ttf_libname = "libSDL3_ttf.so.0"
if platform.system() == "Windows":
    # 修改 os.environ['PATH'] 没有作用，需要使用 os.add_dll_directory
    # https://github.com/python/cpython/issues/87339
    os.add_dll_directory(str(dlls_dir))
    os.add_dll_directory(r"C:\msys64\ucrt64\bin")
    sdl3_libname = "SDL3.dll"
    sdl3_ttf_libname = "SDL3_ttf.dll"
elif platform.system() == "Darwin":
    sdl3_libname = "libSDL3.0.dylib"
    sdl3_ttf_libname = "libSDL3_ttf.0.dylib"
sdl3 = ctypes.CDLL(str(dlls_dir / sdl3_libname))
sdl3_ttf = ctypes.CDLL(str(dlls_dir / sdl3_ttf_libname))
