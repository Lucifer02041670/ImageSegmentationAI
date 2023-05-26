import customtkinter as ST
import main
from PIL import Image


class App(ST.CTk):

    def Start_segmentation(self):
        Img = self.entry_path.get()
        ImgTo = self.entry_path2.get()
        print(Img)
        main.Start(Img, ImgTo)


    def __init__(self):
        super().__init__()

        self.geometry("1280x1024")
        self.title("Сегментация обьектов")
        self.resizable(False, False)

        self.font = ST.CTkImage(dark_image=Image.open("Font.jpg"), size=(1280, 1024))
        self.font_label = ST.CTkLabel(master=self, text="", image=self.font)
        self.font_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.Image_path = ST.CTkFrame(master=self, fg_color="transparent")
        self.Image_path.grid(row=1, column=0, padx=(200, 240),pady=(300, 0), sticky="nsew")

        self.Inf = ST.CTkLabel(master=self.Image_path, text="Путь к изображению:")
        self.Inf.grid(row=0, column=0, padx=(0, 0))

        self.entry_path = ST.CTkEntry(master=self.Image_path, width=800, height=50)
        self.entry_path.grid(row=0, column=2, padx=(0, 0))



        self.Image_Topath = ST.CTkFrame(master=self, fg_color="transparent")
        self.Image_Topath.grid(row=2, column=0, padx=(200, 240),pady=(20, 0), sticky="nsew")

        self.Inf2 = ST.CTkLabel(master=self.Image_Topath, text="Путь сохранения:")
        self.Inf2.grid(row=0, column=0, padx=(0, 0))

        self.entry_path2 = ST.CTkEntry(master=self.Image_Topath, width=800, height=50)
        self.entry_path2.grid(row=0, column=2, padx=(24, 0))



        self.Start_segmentate = ST.CTkFrame(master=self, fg_color="transparent")
        self.Start_segmentate.grid(row=3, column=0, padx=(20, 20), pady=(20, 0))

        self.btn_segment = ST.CTkButton(master=self.Start_segmentate, text="Start", width=300,
                                        command=self.Start_segmentation)
        self.btn_segment.grid(row=0, column=0)







if __name__ == "__main__":
    app = App()
    app.mainloop()