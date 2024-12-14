import customtkinter
from tkinter import filedialog
from PIL import Image

from convert import convert

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("ASCII Converter - :)")
        self.geometry("800x600")
        self.iconbitmap('icon.ico')

        self.select_image_btn = customtkinter.CTkButton(self, text="Select Image", command=self.select_file)
        self.select_image_btn.pack(padx=10, pady=10)
        
        self.image_file = customtkinter.CTkEntry(self)
        self.image_file.pack(padx=10, pady=10)


        self.convert_btn = customtkinter.CTkButton(self, text="Convert", command=self.on_click)
        self.convert_btn.pack(padx=10, pady=10)

        #self.image_preview = customtkinter.CTkImage(self, light_image=Image.open(self.image_file.get()),
        #                                            dark_image=Image.open(self.image_file.get()),
        #                                            size=(30, 30))
        
        #self.image_preview_label = customtkinter.CTkLabel(self, image=self.image_preview, text="")

    def on_click(self):
        print(self.image_file.get())

    def select_file(self):
        filetypes = (
            ('JPEG', '*.jpg'),
            ('PNG', '*.png'),
            ('All files', '*.*')
        )
        filename = filedialog.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes
        )

        if filename:
            # Do something with the selected file
            print("Selected file:", filename)

if __name__ == "__main__":
    app = App()
    app.mainloop()