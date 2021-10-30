import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
img = Image.open("path//to//imgage.jpg")
img = img.resize((250, 250))
tkimage = ImageTk.PhotoImage(img)
tk.Label(root, image=tkimage).grid()