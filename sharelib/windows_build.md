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

cd 到 sharelib

```shell
cp SDL/build/SDL3.dll SDL_ttf/build/SDL3_ttf.dll dlls

# 可选，复制其他第三方依赖
cp /ucrt64/bin/libintl-8.dll \
  /ucrt64/bin/libharfbuzz-0.dll \
  /ucrt64/bin/libfreetype-6.dll \
  /ucrt64/bin/libgcc_s_seh-1.dll \
  /ucrt64/bin/libgraphite2.dll \
  /ucrt64/bin/libglib-2.0-0.dll \
  /ucrt64/bin/libbrotlidec.dll \
  /ucrt64/bin/libstdc++-6.dll \
  /ucrt64/bin/libbz2-1.dll \
  /ucrt64/bin/libpng16-16.dll \
  /ucrt64/bin/zlib1.dll \
  /ucrt64/bin/libwinpthread-1.dll \
  /ucrt64/bin/libbrotlicommon.dll \
  /ucrt64/bin/libpcre2-8-0.dll \
  /ucrt64/bin/libiconv-2.dll dlls
```
