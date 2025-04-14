import tkinter as tk

CELL_SIZE = 40
ROWS, COLS = 10, 10

def erase(event):
    ex1, ey1, ex2, ey2 = canvas.coords(eraser)
    for rect, coords in cells.items():
        if ex1 < coords[2] and ex2 > coords[0] and ey1 < coords[3] and ey2 > coords[1]:
            canvas.itemconfig(rect, fill="white")

# Initialize window
root = tk.Tk()
canvas = tk.Canvas(root, width=COLS * CELL_SIZE, height=ROWS * CELL_SIZE, bg="white")
canvas.pack()

# Draw grid
cells = {}
for row in range(ROWS):
    for col in range(COLS):
        x1, y1 = col * CELL_SIZE, row * CELL_SIZE
        x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE
        rect = canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="black")
        cells[rect] = (x1, y1, x2, y2)

# Create eraser
eraser = canvas.create_rectangle(0, 0, 50, 50, fill="gray", outline="black")
canvas.bind("<B1-Motion>", lambda e: (canvas.coords(eraser, e.x-25, e.y-25, e.x+25, e.y+25), erase(e)))

root.mainloop()
