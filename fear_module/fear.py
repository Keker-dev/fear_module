import os
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from tkinter import *
from tkinter import ttk
import pygame
import keyboard as kb

pygame.init()
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
sys_vol = cast(interface, POINTER(IAudioEndpointVolume))


class FearClassException(Exception):
    pass


class Fear:
    def __init__(self, fullscreen=True, title="Выбрался всё таки", sleep=30, main_text="Ваши действия?", main_image="",
                 kb_block=True, volume=100):
        self.wind = Tk()
        self.wind.title(title)
        self.w_size = (self.wind.winfo_screenwidth(), self.wind.winfo_screenheight())
        self.wind.geometry(f"{self.w_size[0]}x{self.w_size[1]}")
        self.wind.attributes('-fullscreen', fullscreen)
        sys_vol.SetMute(0, None)
        if volume < 0 or volume > 100:
            raise FearClassException("The volume should be between 0 and 100.")
        sys_vol.SetMasterVolumeLevelScalar(volume / 100, None)

        self.scenes = {"main": Frame(self.wind), }
        self.buttons = {}
        self.state, self.sleep = "main", sleep
        self.main_text, self.main_image = main_text, PhotoImage(main_image)
        self.running, self.block = False, kb_block
        self.on_quit = lambda: os.system("shutdown /s /t 1")

    def setup(self):
        for scene in self.scenes.keys():
            if scene == "main":
                lb = ttk.Label(self.scenes["main"], text=self.main_text, font=("Arial", 30), compound="bottom",
                               justify=CENTER, anchor="center", image=self.main_image if self.main_image else None)
            else:
                lb = ttk.Label(self.scenes[scene], image=None, justify=CENTER, anchor="center", compound="bottom",
                               text="")
            lb.pack()

    def run(self):
        if not self.running:
            self.running = True
            self.setup()
            if self.sleep < 0:
                raise FearClassException("The sleep time should be >= 0.")
            if self.block:
                Fear.block_keyboard()
            self.wind.after(self.sleep * 1000, self.on_quit)
            self.wind.after(self.sleep * 1000 + 1, self.wind.quit)
            self.wind.mainloop()

    def add_scene(self):
        pass

    @staticmethod
    def block_keyboard():
        for i in range(150):
            kb.block_key(i)
