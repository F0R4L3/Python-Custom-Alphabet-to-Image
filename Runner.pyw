from PIL import Image
from tkinter import Tk, Text, Button, Label, Entry, StringVar

size = [5500, 5500]
xy_offset = [60, 60]
space_length = 50
letter_spacing = 20
new_line_spacing = 100
max_char_per_line = 40
background = '#fff'

def Write(text: str, chars_per_line: int):
    paper = Image.new('RGB', (size[0], size[1]), color=background)

    x_offset = xy_offset[0]
    y_offset = xy_offset[1]

    for i, character in enumerate(text):
        try:
            if i > 0 and i % chars_per_line == 0:
                x_offset = xy_offset[0]
                y_offset += new_line_spacing
            if character == ' ' and i == chars_per_line:
                x_offset = xy_offset[0]
            elif character == ' ':
                x_offset += space_length
            else:
                x_offset += letter_spacing
                image = Image.open(f"./Images/{character.upper()}_.png")
                paper.paste(image, (x_offset, y_offset))
                x_offset += image.width
        except:
            pass

    paper.show()

# ========================================================= STYLE SECTION ==========================================

def update_variables():
    global space_length, letter_spacing, new_line_spacing, max_char_per_line, background

    background = str(bacgrkound_entry.get())
    size[0] = int(width_entry.get())
    size[1] = int(height_entry.get())
    xy_offset[0] = int(x_offset_entry.get())
    xy_offset[1] = int(y_offset_entry.get())
    space_length = int(space_length_entry.get())
    letter_spacing = int(letter_spacing_entry.get())
    new_line_spacing = int(new_line_spacing_entry.get())
    max_char_per_line = int(max_char_per_line_entry.get())

    # You can print or use the updated variables as needed
    print("Updated variables:", size, xy_offset, space_length, letter_spacing, new_line_spacing, max_char_per_line)

from tkinter import Tk, Label, Entry, Button, Text, StringVar
from tkinter.font import Font

# Create the main window
root = Tk()
root.title("Variable Modifier")
root.configure(bg='lightgrey')

# Define a font for the labels and buttons
font = Font(family="Helvetica", size=10, weight="bold")

# Create entry widgets with padding and custom font
width_label = Label(root, text="Width:", bg='lightgrey', font=font)
width_entry = Entry(root)
height_label = Label(root, text="Height:", bg='lightgrey', font=font)
height_entry = Entry(root)
x_offset_label = Label(root, text="X Offset:", bg='lightgrey', font=font)
x_offset_entry = Entry(root)
y_offset_label = Label(root, text="Y Offset:", bg='lightgrey', font=font)
y_offset_entry = Entry(root)
space_length_label = Label(root, text="Each word spacing:", bg='lightgrey', font=font)
space_length_entry = Entry(root)
letter_spacing_label = Label(root, text="Each alphabet Spacing:", bg='lightgrey', font=font)
letter_spacing_entry = Entry(root)
new_line_spacing_label = Label(root, text="Each Line Spacing:", bg='lightgrey', font=font)
new_line_spacing_entry = Entry(root)
max_char_per_line_label = Label(root, text="Max Characters Per Line:", bg='lightgrey', font=font)
max_char_per_line_entry = Entry(root)
bacgrkound_label = Label(root, text="Paper background (RGB):", bg='lightgrey', font=font)
bacgrkound_entry = Entry(root)

# Set default values in entry widgets
width_entry.insert(0, size[0])
height_entry.insert(0, size[1])
x_offset_entry.insert(0, xy_offset[0])
y_offset_entry.insert(0, xy_offset[1])
space_length_entry.insert(0, space_length)
letter_spacing_entry.insert(0, letter_spacing)
new_line_spacing_entry.insert(0, new_line_spacing)
max_char_per_line_entry.insert(0, max_char_per_line)
bacgrkound_entry.insert(0, background)

# Create button to update variables with custom font
update_button = Button(root, text="Update Variables", command=update_variables, font=font)

# Arrange widgets in the grid with padding
width_label.grid(row=0, column=0, padx=5, pady=5)
width_entry.grid(row=0, column=1, padx=5, pady=5)
height_label.grid(row=0, column=2, padx=5, pady=5)
height_entry.grid(row=0, column=3, padx=5, pady=5)
x_offset_label.grid(row=1, column=0, padx=5, pady=5)
x_offset_entry.grid(row=1, column=1, padx=5, pady=5)
y_offset_label.grid(row=1, column=2, padx=5, pady=5)
y_offset_entry.grid(row=1, column=3, padx=5, pady=5)
space_length_label.grid(row=2, column=0, padx=5, pady=5)
space_length_entry.grid(row=2, column=1, padx=5, pady=5)
letter_spacing_label.grid(row=3, column=0, padx=5, pady=5)
letter_spacing_entry.grid(row=3, column=1, padx=5, pady=5)
new_line_spacing_label.grid(row=4, column=0, padx=5, pady=5)
new_line_spacing_entry.grid(row=4, column=1, padx=5, pady=5)
max_char_per_line_label.grid(row=5, column=0, padx=5, pady=5)
max_char_per_line_entry.grid(row=5, column=1, padx=5, pady=5)
bacgrkound_label.grid(row=2, column=2, padx=5, pady=5)
bacgrkound_entry.grid(row=2, column=3, padx=5, pady=5)
update_button.grid(row=6, columnspan=4, padx=5, pady=5)

# Create a Text widget
text_widget = Text(root)
text_widget.grid(row=7, column=0, columnspan=4, padx=5, pady=5)

def on_button_press():
    text = text_widget.get("1.0", "end-1c")  # Get the text from the text widget
    Write(text, max_char_per_line)

# Create a Button widget with custom font
button = Button(root, text="Cipher", command=on_button_press, font=font)
button.grid(row=8, column=0, columnspan=4, padx=5, pady=5)

# Start the Tkinter event loop
root.mainloop()
