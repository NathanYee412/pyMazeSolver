import tkinter as tk
from tkinter import filedialog
from solvemaze import solveMazeBFS, solveMazeDFS

def chooseFile():
    window.filename = filedialog.askopenfilename(initialdir = "/", title = "Choose a file", filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    return window.filename




window = tk.Tk(className="pyMazeSolver")
window.geometry("500x500")
window['background'] = 'yellow'

pickMaze = tk.Button(window, text="Choose Maze to solve", command=lambda : chooseFile())
pickMaze.pack(fill="x")
BFS = tk.Button(window, text="BFS User Maze", command=lambda : solveMaze(window.filename))
BFS.pack(fill="x")

BFSdefault = tk.Button(window, text="BFS Hard Maze", command=lambda : solveMazeBFS("maze_hard.png"))
BFSdefault.pack(fill="x")

BFSdefault = tk.Button(window, text="DFS Hard Maze", command=lambda : solveMazeDFS("maze_hard.png"))
BFSdefault.pack(fill="x")

BFSez = tk.Button(window, text="BFS Easy Maze", command=lambda : solveMaze("fish.jpg"))
BFSez.pack(fill="x")


window.mainloop()

