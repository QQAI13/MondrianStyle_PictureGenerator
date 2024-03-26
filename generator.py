import random
import tkinter

# red, yellow, blue, white ...
color_array = ['#CD3333' , '#FFD700' , '#0000FF' , 'white' , 'black' , 'gray' , 'white']


def print_colored_text(text, color_code=37):
    '''
    Color Codes:
    30 - Black
    31 - Red
    32 - Green
    33 - Yellow
    34 - Blue
    35 - Magenta
    36 - Cyan
    37 - White
    '''
    print(f"\033[{color_code}m{text}\033[0m")

root = tkinter.Tk() # lefttop is (0 , 0)
root.geometry(f'800x800')
square_nums = -1
counter = 1
canvas = tkinter.Canvas(root , height=600 , width=600)

def window_generator():
    global root
    root.title("Mondrian Style Generator by QQAI")
    btn = tkinter.Button(root, text='Re-generate', command=canvas_generator)
    btn.pack(pady=50)
    root.mainloop()

def canvas_generator():
    print_colored_text("Re-generate the picture ..." , 32)
    global root, square_nums, counter, canvas
    counter += 1
    random.seed( random.random() * counter )
    if square_nums == -1 or square_nums == None:
        square_nums = random.randint(5 , 13)
    else:
        square_nums = random.randint(5 , 13)
    canvas.delete("all")
    min_height = 0
    max_height = 600
    min_width = 0
    max_width = 600
    line_width = 4
    canvas.configure(bg='white')
    square_recursive(canvas, square_nums, left = min_width, right = max_width, \
                     top = min_height, bot = max_height, n=0)
    canvas.pack()
    

def square_recursive(canvas, max, left, right, top, bot, n):
    print_colored_text(f"# Square recursive ... step {n}\n {left}, {right}, {top}, {bot}" , 33)
    if n == max:
        print_colored_text(f"# of squares exceed ... Finished!" , 31)
        return
    dir = random.randint(1 , 3)
    depth_dir = random.randint(1 , 3)
    color_code = random.randint(0 , 5)
    color = color_array[color_code]
    width = random.randint( 2 , 13 )
    if dir % 2 == 0: 
        # Horizontal
        try:
            midpoint = random.randint(top + 10 , bot)
        except:
            return
        print_colored_text(f"Midpoint for horizontal is {midpoint}", 30)
        canvas.create_line(left, midpoint, right, midpoint, width=width, fill="black")
        if depth_dir % 2 == 0: # Lower block
            canvas.create_rectangle(left, midpoint, right, bot, fill=color , outline="black")
            square_recursive(canvas, max, left, right, midpoint, bot, n+1)
        else: # Upper block
            canvas.create_rectangle(left, top, right, midpoint, fill=color , outline="black")
            square_recursive(canvas, max, left, right, top, midpoint, n+1)
    else: 
        # Vertical
        try:
            midpoint = random.randint(left + 10 , right)
        except:
            return
        print_colored_text(f"Midpoint for vertical is {midpoint}", 30)
        canvas.create_line(midpoint, top, midpoint, bot, width=width, fill="black")
        if depth_dir % 2 == 0: # Left-side block
            canvas.create_rectangle(left, top, midpoint, bot, fill=color , outline="black")
            square_recursive(canvas, max, left, midpoint, top, bot, n+1)
        else: # Right-side block
            canvas.create_rectangle(midpoint, top, right, bot, fill=color , outline="black")
            square_recursive(canvas, max, midpoint, right, top, bot, n+1)