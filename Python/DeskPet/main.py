import tkinter as tk

class Pet:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(self.master, width=300, height=300)
        self.canvas.pack()
        self.image = tk.PhotoImage(file="pet.png")  # 请替换为你自己的图片文件路径
        self.canvas.create_image(150, 150, image=self.image)

    def move(self, x, y):
        self.canvas.move(self.image, x, y)

def main():
    root = tk.Tk()
    pet = Pet(root)
    root.mainloop()

if __name__ == "__main__":
    main()
