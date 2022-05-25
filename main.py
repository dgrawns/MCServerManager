import tkinter as tk
from tkinter import filedialog, Text
import os
import subprocess

root = tk.Tk()
root.title("MC Server Manager (v1.0)")
root.iconbitmap("MC.ico")
startFiles = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempFiles = f.read()
        tempFiles = tempFiles.split(',')
        startFiles = [x for x in tempFiles if x.strip()]

def startServer(server):
    os.chdir(server[:-9])
    os.startfile(server)
def addServerButton(file):
    button = tk.Button(frame, text=file[:-9], bg="#AAAAAA", command=(lambda: startServer(file)))
    button.pack()
def addServer():
    filename = filedialog.askopenfilename(initialdir="/", title="Select Server Start File",
                                          filetype=[("Batch", "*.bat")])

    startFiles.append(filename)
    print(filename)
    addServerButton(filename)


canvas = tk.Canvas(root, height=700, width=1000, bg="#212121")
canvas.pack()

frame = tk.Frame(root, bg="#3D3D3D")
frame.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)

openFile = tk.Button(frame, text="Add Server", padx=5, pady=10, fg="white", bg="#212121", command=addServer)
openFile.pack()


for file in startFiles:
    addServerButton(file)
root.mainloop()

with open('save.txt', 'w') as f:
    for sf in startFiles:
        f.write(sf + ',')























