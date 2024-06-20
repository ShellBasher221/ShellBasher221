from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

#button commands

def open_file(window, text_edit):
    filepath = askopenfilename(filetypes=[("text files", "*.txt"),
                                           ("python files", "*.py"),
                                           ("all files", "*.*")])
                                           
    if not filepath:
        return
    text_edit.delete(1.0,END)
    with open(filepath, 'r') as f:
        content = f.read()
        text_edit.insert(END, content)
    window.title(f"Open file: {filepath}")

def save_file(window, text_edit):
    filepath = asksaveasfilename(filetypes=[("text files", "*.txt"),
                                           ("python files", "*.py"),
                                           ("all files", "*.*")])
    
    if not filepath:
        return 
    
    with open(filepath, 'w') as f:
        content = text_edit.get(1.0, END)
        f.write(content)
    window.title(f"Open file: {filepath}")

def darkmode(text_edit):
    text_edit.configure(background="black", foreground="white", insertbackground="white")

def lightmode(text_edit):
    text_edit.configure(background="white", foreground="black", insertbackground="black")

#window and buttons
def main()-> None:
    window = Tk()
    window.title("Text editor")
    window.rowconfigure(0, minsize=400)
    window.columnconfigure(1, minsize=500)

    text_edit = Text(window, font="Helvetica 18")
    text_edit.grid(row=0, column=1)

    frame = Frame(window, relief=RAISED, bd=2)
    save_button = Button(frame, text="Save", command=lambda: save_file(window, text_edit))
    open_button = Button(frame, text="Open", command=lambda: open_file(window, text_edit))
    dark_button = Button(frame, text="Dark mode", command=lambda: darkmode(text_edit))
    light_button = Button(frame, text="Light mode", command=lambda: lightmode(text_edit))

    save_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
    open_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
    dark_button.grid(row=2, column=0, padx=5, pady=5, sticky="ew")
    light_button.grid(row=3, column=0, pady=5, padx=5, sticky="ew")      
    frame.grid(row=0, column=0, sticky="ns")

    window.bind("<Control-s>", lambda x: save_file(window, text_edit))
    window.bind("<Control-o>", lambda x: open_file(window, text_edit))


    window.mainloop()

if __name__ == "__main__":
    main()