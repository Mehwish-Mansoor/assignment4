import tkinter as tk

def create_canvas_grid(canvas, rows, cols, cell_size):
    """Creates a grid of blue cells on the canvas."""
    for row in range(rows):
        for col in range(cols):
            x1 = col * cell_size
            y1 = row * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size
            canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="black", tags="cell")

def erase(event):
    """Erases cells by setting them to white when the eraser touches them."""
    x, y = event.x, event.y
    overlapping_items = canvas.find_overlapping(x - eraser_size, y - eraser_size, x + eraser_size, y + eraser_size)
    for item in overlapping_items:
        canvas.itemconfig(item, fill="white")

def move_eraser(event):
    """Moves the eraser rectangle and erases cells."""
    canvas.coords(eraser, event.x - eraser_size, event.y - eraser_size, event.x + eraser_size, event.y + eraser_size)
    erase(event)

# Create the main window
root = tk.Tk()
root.title("Eraser on Canvas")

# Canvas settings
canvas_width = 400
canvas_height = 400
cell_size = 20
eraser_size = 10

canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()

# Create the grid of blue cells
rows = canvas_height // cell_size
cols = canvas_width // cell_size
create_canvas_grid(canvas, rows, cols, cell_size)

# Create the eraser rectangle
eraser = canvas.create_rectangle(0, 0, eraser_size * 2, eraser_size * 2, fill="gray", outline="black")

# Bind mouse motion to move the eraser
canvas.bind("<B1-Motion>", move_eraser)

# Run the application
root.mainloop()