import tkinter as tk
from tkinter import filedialog, messagebox
from solvemaze import solveMazeBFS, solveMazeDFS

fileFlag = False

def chooseFile():
    window.filename = filedialog.askopenfilename(initialdir = "/", title = "Choose a file", filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    fileFlag = True
    return window.filename


window = tk.Tk(className="pyMazeSolver")
window.geometry("900x500")
window['background'] = 'yellow'

welcome = tk.Label(window, pady=10, text="Hello, this is our maze solving program. To get started, you can either upload your own maze, or choose a default maze to solve")
welcome.pack(fill="x")

pickMaze = tk.Button(window, pady=10, text="Upload Maze to solve", command=lambda : chooseFile())
pickMaze.pack()

BFS = tk.Button(window, text="BFS User Maze", command=lambda : solveMazeBFS(window.filename))
BFS.pack(fill="x")

DFS = tk.Button(window, text="DFS User Maze", command=lambda : solveMazeDFS(window.filename))
DFS.pack(fill="x")


BFSdefault = tk.Button(window, text="BFS Hard Maze", command=lambda : solveMazeBFS("maze_hard.png"))
BFSdefault.pack(fill="x")

DFSdefault = tk.Button(window, text="DFS Hard Maze", command=lambda : solveMazeDFS("maze_hard.png"))
DFSdefault.pack(fill="x")

BFSez = tk.Button(window, text="BFS Easy Maze", command=lambda : solveMazeBFS("squirrel.jpg"))
BFSez.pack(fill="x")

DFSez = tk.Button(window, text="DFS Easy Maze", command=lambda : solveMazeDFS("squirrel.jpg"))
DFSez.pack(fill="x")




window.mainloop()

