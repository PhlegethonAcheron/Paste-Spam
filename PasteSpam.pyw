import sys
import pyautogui
import tkinter as tk
import tkinter.ttk as ttk
import time
window = tk.Tk()
window.title = "Word Sender"
v1 = tk.PhotoImage(file='v1.png')
window.iconphoto(False, v1)
pyautogui.FAILSAFE = True
x = 0
try:
    screenWidth, screenHeight = pyautogui.size()
    window.geometry('400x100')
    label = ttk.Label(window, text="To Use: Copy the thing to the clipboard\nPress the button when you're ready.\nThere will be a 2 second delay before the script starts.", font=('Times New Roman', 13))
    label.pack(anchor='nw', side='top')
   # print(ShuffledSongs)

    def stop():
        x = 100
    def sendem():
        time.sleep(2)
        while x<1:
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(0.1)
            pyautogui.press('enter')
            time.sleep(0.5)

    btn1 = tk.Button(window,text="Start the Script!", font=('Times New Roman',13), command = sendem)
    btn1.pack(anchor = 'n', side=tk.LEFT)
    btn2 = tk.Button(window, text="Stop the Script!", font=('Times New Roman', 13), command=stop)
    btn2.pack(anchor = 'n', side = tk.RIGHT)
    window.mainloop()
except KeyboardInterrupt:
    sys.exit()
