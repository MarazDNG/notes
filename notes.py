import tkinter
from tkinter.font import Font
from typing import Text

with open('notes.txt', 'a', encoding='utf-8'):
    pass

with open('notes.txt', 'r', encoding='utf-8') as f:
    lines = f.read()

root = tkinter.Tk()
root.title('Notes')

text = None


def get_text():
    global text
    text = T.get(1.0, "end-1c")
    root.destroy()


root.protocol('WM_DELETE_WINDOW', get_text)

T = tkinter.Text(root, width=25, height=10, bg='#fff44f')

T.insert(1.0, lines)
T.configure(font=('Calibri', 15))
T.tag_configure('bg', background='red')

T.pack()
root.resizable(False, False)


root.mainloop()

print(text)
with open('notes.txt', 'w+', encoding='utf-8') as f:
    f.write(text)
