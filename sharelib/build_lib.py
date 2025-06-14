#!/usr/bin/env python3

import os
import pathlib
import shutil
import subprocess

script_dir = pathlib.Path(__file__).parent.resolve()


def check_env():
    cmake = shutil.which("cmake")
    if cmake is None:
        raise EnvironmentError("CMake is not installed or not found in PATH.")


def build_sdl():
    cmake = shutil.which("cmake")
    assert cmake is not None, "CMake must be installed to build SDL."
    curdir = os.getcwd()
    libname = "libSDL3.so.0"
    try:
        os.chdir(script_dir / "SDL")
        subprocess.check_call([cmake, "-S", ".", "-B", "build"])
        subprocess.check_call([cmake, "--build", "build"])
        shutil.copyfile(pathlib.Path("build") / libname, script_dir / libname)
    finally:
        os.chdir(curdir)


def build_sdl_ttf():
    cmake = shutil.which("cmake")
    assert cmake is not None, "CMake must be installed to build SDL_ttf."
    curdir = os.getcwd()
    libname = "libSDL3_ttf.so.0"
    try:
        os.chdir(script_dir / "SDL_ttf")
        subprocess.check_call(
            [
                cmake,
                "-S",
                ".",
                "-B",
                "build",
                f"-DCMAKE_PREFIX_PATH={script_dir / 'SDL' / 'build'}",
            ]
        )
        subprocess.check_call([cmake, "--build", "build"])
        shutil.copyfile(pathlib.Path("build") / libname, script_dir / libname)
    finally:
        os.chdir(curdir)


def main():
    check_env()
    build_sdl()
    build_sdl_ttf()


if __name__ == "__main__":
    main()
