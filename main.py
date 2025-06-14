import ctypes
import pathlib
from collections import deque

from pynput import keyboard

from sharelib import (
    SDL_EVENT_MOUSE_BUTTON_DOWN,
    SDL_EVENT_QUIT,
    SDL_INIT_VIDEO,
    SDL_BUTTON_RIGHT,
    SDL_WINDOW_ALWAYS_ON_TOP,
    SDL_WINDOW_BORDERLESS,
    SDL_WINDOW_RESIZABLE,
    SDL_WINDOW_TRANSPARENT,
    SDL_Color,
    SDL_Event,
    SDL_FRect,
    sdl3,
    sdl3_ttf,
)

script_dir = pathlib.Path(__file__).parent.resolve()


class KeyDisplayWindow:

    def __init__(self):
        self.window = None
        self.renderer = None
        self.font = None
        self.running = True
        self.key_history = deque(maxlen=5)  # 存储最近个按键

        if not sdl3.SDL_Init(SDL_INIT_VIDEO):
            print(
                f"SDL could not be initialized! SDL_Error: {sdl3.SDL_GetError().decode('utf-8')}"
            )
            raise RuntimeError("SDL initialization failed")

        if not sdl3_ttf.TTF_Init():
            print(
                f"SDL_ttf could not be initialized! SDL_Error: {sdl3.SDL_GetError().decode('utf-8')}"
            )
            raise RuntimeError("SDL_ttf initialization failed")

        font_path = script_dir / "font" / "MapleMonoNormalNL-Bold.ttf"
        self.font = sdl3_ttf.TTF_OpenFont(str(font_path).encode(), 28)
        if not self.font:
            print(
                f"Font could not be loaded! SDL_Error: {sdl3.SDL_GetError().decode('utf-8')}"
            )
            raise RuntimeError("Font loading failed")

    def _run(self):
        title = "Hello SDL".encode("utf-8")  # must be bytes
        width = 500
        height = 50
        flags = (
            SDL_WINDOW_RESIZABLE
            | SDL_WINDOW_TRANSPARENT
            | SDL_WINDOW_ALWAYS_ON_TOP
            | SDL_WINDOW_BORDERLESS
        )

        self.window = sdl3.SDL_CreateWindow(title, width, height, flags)
        if not self.window:
            print(
                f"Window could not be created! SDL_Error: {sdl3.SDL_GetError().decode('utf-8')}"
            )
            raise RuntimeError("Window creation failed")

        self.renderer = sdl3.SDL_CreateRenderer(self.window, None)
        if not self.renderer:
            print(
                f"Renderer could not be created! SDL_Error: {sdl3.SDL_GetError().decode('utf-8')}"
            )
            raise RuntimeError("Renderer creation failed")

        color = SDL_Color(0, 0, 0, 255)  # Black color

        running = True
        prev_text = b""
        while running:
            event = SDL_Event()
            while sdl3.SDL_PollEvent(ctypes.byref(event)):
                if event.type == SDL_EVENT_QUIT:
                    running = False
                elif event.type == SDL_EVENT_MOUSE_BUTTON_DOWN and event.button.button == SDL_BUTTON_RIGHT:
                    running = False

            text = "Press any key...".encode("utf-8")
            if len(self.key_history) > 0:
                text = " ".join(self.key_history).encode("utf-8")
            if text == prev_text:
                continue
            prev_text = text
            surface = sdl3_ttf.TTF_RenderText_Blended(self.font, text, len(text), color)
            texture = sdl3.SDL_CreateTextureFromSurface(self.renderer, surface)
            w = ctypes.c_float()
            h = ctypes.c_float()
            sdl3.SDL_GetTextureSize(texture, ctypes.byref(w), ctypes.byref(h))

            # Clear, copy, and present
            sdl3.SDL_RenderClear(self.renderer)
            dst_rect = SDL_FRect(0, 0, w.value, h.value)
            sdl3.SDL_RenderTexture(self.renderer, texture, None, ctypes.byref(dst_rect))
            sdl3.SDL_RenderPresent(self.renderer)

            # Clean up
            sdl3.SDL_DestroyTexture(texture)
            sdl3.SDL_DestroySurface(surface)

    def _free(self):
        if self.font:
            sdl3_ttf.TTF_CloseFont(self.font)
        if self.renderer:
            sdl3.SDL_DestroyRenderer(self.renderer)
        if self.window:
            sdl3.SDL_DestroyWindow(self.window)
        sdl3_ttf.TTF_Quit()
        sdl3.SDL_Quit()

    def run(self):
        try:
            self._run()
        finally:
            self._free()

    def add_key(self, key: str):
        self.key_history.append(key)


class KeyListener:
    def __init__(self, window: KeyDisplayWindow):
        self.window = window
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()

    def on_press(self, key):
        """处理按键事件"""
        try:
            # 处理普通按键
            if hasattr(key, "char") and key.char:
                key_str = key.char
            # 处理特殊按键
            else:
                key_str = key.name.replace("_", " ").title()
        except AttributeError:
            key_str = str(key)

        self.window.add_key(key_str)


def main():
    window = KeyDisplayWindow()
    # 启动键盘监听
    KeyListener(window)
    window.run()


if __name__ == "__main__":
    main()
