import cv2

import threading
import colorsys
import time
from time import sleep
from tkinter import messagebox


class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y





def BFS(s, e):

    global pic, h, w
    const = 10000
    start = time.time()

    found = False
    queue = []
    visited = [[0 for j in range(w)] for i in range(h)]
    parent = [[Point() for j in range(w)] for i in range(h)]

    queue.append(s)
    visited[s.y][s.x] = 1
    while len(queue) > 0:
        #sleep(0.05)
        p = queue.pop(0)
        for d in dir4:
            cell = p + d
            if (cell.x >= 0 and cell.x < w and cell.y >= 0 and cell.y < h and visited[cell.y][cell.x] == 0 and
                    (pic[cell.y][cell.x][0] != 0 or pic[cell.y][cell.x][1] != 0 or pic[cell.y][cell.x][2] != 0)):
                queue.append(cell)
                visited[cell.y][cell.x] = visited[p.y][p.x] + 1

                pic[cell.y][cell.x] = list(reversed(
                    [i * 255 for i in colorsys.hsv_to_rgb(visited[cell.y][cell.x] / const, 1, 1)])
                )
                parent[cell.y][cell.x] = p
                if cell == e:
                    found = True
                    del queue[:]
                    break

    solutionPath = []
    if found:
        end = time.time()
        p = e
        while p != s:
            solutionPath.append(p)
            p = parent[p.y][p.x]
        solutionPath.append(p)
        solutionPath.reverse()

        for p in solutionPath:
            pic[p.y][p.x] = [255, 255, 255]
        print("Solution Found")
        print("Time taken: ", str(end-start), " seconds!")
        message = 'Time taken: ', str(end-start), ' seconds! Press OK then any key close the maze'
        message = " ".join(message)
        messagebox.showinfo("Total Time", message )
    else:
        print("Solution Not Found")
        messagebox.showinfo("Total Time", "Solution Not Found!" )

def DFS(s, e):

    global pic, h, w
    const = 10000
    start = time.time()

    found = False
    queue = []
    visited = [[0 for j in range(w)] for i in range(h)]
    parent = [[Point() for j in range(w)] for i in range(h)]

    queue.append(s)
    visited[s.y][s.x] = 1
    while len(queue) > 0:
        #sleep(0.05)
        p = queue.pop(len(queue) - 1)
        for d in dir4:
            cell = p + d
            if (cell.x >= 0 and cell.x < w and cell.y >= 0 and cell.y < h and visited[cell.y][cell.x] == 0 and
                    (pic[cell.y][cell.x][0] != 0 or pic[cell.y][cell.x][1] != 0 or pic[cell.y][cell.x][2] != 0)):
                queue.append(cell)
                visited[cell.y][cell.x] = visited[p.y][p.x] + 1  # Later

                pic[cell.y][cell.x] = list(reversed(
                    [i * 255 for i in colorsys.hsv_to_rgb(visited[cell.y][cell.x] / const, 1, 1)])
                )
                parent[cell.y][cell.x] = p
                if cell == e:
                    found = True
                    del queue[:]
                    break

    solutionPath = []
    if found:
        end = time.time()
        p = e
        while p != s:
            solutionPath.append(p)
            p = parent[p.y][p.x]
        solutionPath.append(p)
        solutionPath.reverse()

        for p in solutionPath:
            pic[p.y][p.x] = [0, 0, 0]
        print("Solution Found")
        print("Time taken: ", str(end-start), " seconds!")
        message = 'Time taken: ', str(end-start), ' seconds! Press OK then any key close the maze'
        message = " ".join(message)
        messagebox.showinfo("Total Time", message )
    else:
        print("Solution Not Found")
        messagebox.showinfo("Total Time", "Solution Not Found!" )

def mouse_event(event, pX, pY, flags, param):

    global pic, start, end, p

    if event == cv2.EVENT_LBUTTONUP:
        if p == 0:
            cv2.rectangle(pic, (pX - rw, pY - rw),
                          (pX + rw, pY + rw), (0, 0, 255), -1)
            start = Point(pX, pY)
            print("start = ", start.x, start.y)
            p += 1
        elif p == 1:
            cv2.rectangle(pic, (pX - rw, pY - rw),
                          (pX + rw, pY + rw), (0, 200, 50), -1)
            end = Point(pX, pY)
            print("end = ", end.x, end.y)
            p += 1


def disp():
    global pic
    cv2.imshow("Image", pic)
    cv2.setMouseCallback('Image', mouse_event)
    key = -1
    while key == -1:
        cv2.imshow("Image", pic)
        key = cv2.waitKey(1)
    cv2.destroyAllWindows()


def solveMazeBFS(picName):
    global rw, p, start, end, dir4, pic, h, w, t

    rw = 2
    p = 0
    start = Point()
    end = Point()

    dir4 = [Point(0, -1), Point(0, 1), Point(1, 0), Point(-1, 0)]


    pic = cv2.imread(picName, cv2.IMREAD_GRAYSCALE)
    _, pic = cv2.threshold(pic, 120, 255, cv2.THRESH_BINARY)
    pic = cv2.cvtColor(pic, cv2.COLOR_GRAY2BGR)
    h, w = pic.shape[:2]

    print("Select start and end points : ")


    t = threading.Thread(target=disp, args=())
    t.daemon = True
    t.start()

    while p < 2:
        pass

    BFS(start, end)

    cv2.destroyAllWindows()
    t.join()

def solveMazeDFS(picName):
    global rw, p, start, end, dir4, pic, h, w, t

    rw = 2
    p = 0
    start = Point()
    end = Point()

    dir4 = [Point(0, -1), Point(0, 1), Point(1, 0), Point(-1, 0)]


    pic = cv2.imread(picName, cv2.IMREAD_GRAYSCALE)
    _, pic = cv2.threshold(pic, 120, 255, cv2.THRESH_BINARY)
    pic = cv2.cvtColor(pic, cv2.COLOR_GRAY2BGR)
    h, w = pic.shape[:2]

    print("Select start and end points : ")


    t = threading.Thread(target=disp, args=())
    t.daemon = True
    t.start()

    while p < 2:
        pass

    DFS(start, end)

    cv2.destroyAllWindows()
    t.join()

# def main():
#     solveMaze()

# if __name__ == "__main__":
#     main()