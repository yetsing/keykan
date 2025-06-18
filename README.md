# keykan

Show the keys you pressed 展示你按下的键

# 运行

## 安装工具

需要安装 uv git

```shell
# pull SDL SDL_ttf
git submodule update --init
uv sync
```

## 编译动态库

### Ubuntu

```shell
sudo apt-get install build-essential cmake
sudo apt-get install libfreetype6 zlib1g libpng16-16t64 libbrotli1
uv run sharelib/build_lib.py
```

### MacOS

```shell
brew install freetype harfbuzz
uv run sharelib/build_lib.py
```

### Windows

参照 sharelib/windows_build.md

## 运行

```shell
uv run main.py
```
