import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tkinter as tk

from calculator.postfix_to_resault import Postfix_to_Answer
from calculator.infix_to_postfix import Infix_To_Postfix 

class SimpleCalcGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.resizable(False, False)

        self.expr = tk.StringVar(value="")

        entry = tk.Entry(root, textvariable=self.expr, font=("DejaVu Sans", 14), width=26)
        entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        entry.focus()

        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", "^", "(", ")",
            "+", "=", "C", "⌫"
        ]

        r, c = 1, 0
        for b in buttons:
            btn = tk.Button(root, text=b, width=6, height=2,
                            command=lambda x=b: self.on_press(x))
            btn.grid(row=r, column=c, padx=5, pady=5)
            c += 1
            if c == 4:
                c = 0
                r += 1

        root.bind("<Return>", lambda e: self.evaluate())
        root.bind("<Enter>", lambda e: self.evaluate())
        root.bind("<BackSpace>", lambda e: self.backspace())

    def exit_fullscreen(self, event=None):
        self.root.attributes("-fullscreen", False)
        self.root.overrideredirect(False)

    def on_press(self, ch):
        if ch == "=":
            self.evaluate()
        elif ch == "C":
            self.expr.set("")
        elif ch == "⌫":
            self.backspace()
        else:
            self.expr.set(self.expr.get() + ch)

    def backspace(self):
        s = self.expr.get()
        self.expr.set(s[:-1])

    def evaluate(self):
        expression = self.expr.get()
        try:
            result = Postfix_to_Answer(Infix_To_Postfix(expression))
            self.expr.set(str(result))
        except Exception:
            self.expr.set("There is an error")


if __name__ == "__main__":
    root = tk.Tk()
    SimpleCalcGUI(root)
    root.mainloop()
