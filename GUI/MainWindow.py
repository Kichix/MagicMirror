import tkinter
from tkinter import ttk


class Adder(ttk.Frame):
    """The adders gui and functions."""

    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.init_gui()

    def init_gui(self):
        """Builds GUI."""
        self.root.title('Number Adder')


if __name__ == '__main__':
    root = tkinter.Tk()
    Adder(root)
    root.mainloop()