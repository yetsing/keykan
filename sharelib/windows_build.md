https://github.com/libsdl-org/SDL/blob/main/docs/INTRO-mingw.md

安装 [MSYS2](https://www.msys2.org/) ，打开 MSYS2 UCRT64

```
pacman -S mingw-w64-ucrt-x86_64-gcc mingw-w64-ucrt-x86_64-ninja mingw-w64-ucrt-x86_64-cmake mingw-w64-ucrt-x86_64-sdl3
# 安装 SDL_ttf 的依赖
pacman -S mingw-w64-ucrt-x86_64-harfbuzz mingw-w64-ucrt-x86_64-freetype
```

cd 到 sharelib/SDL 下

```
cmake -S . -B build
cmake --build build
```

cd 到 sharelib/SDL_ttf 下

```
cmake -S . -B build -DCMAKE_PREFIX_PATH=../SDL/build
cmake --build build
```
