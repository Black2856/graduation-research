import tkinter as tk
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        #self.overrideredirect(True)  # タイトルバーを非表示にする
        self.title("Transparent window")
        self.geometry("500x300")
        self.config(bg="white")
        self.attributes("-transparentcolor", "white")
        self.attributes('-fullscreen', True)

        canvas = tk.Canvas(self, width=self.winfo_screenwidth(), height=self.winfo_screenheight(), bg="white")
        canvas.configure(background='red')
        canvas.pack()

        canvas.create_text(800, 250, text="エラーコード 0x800F081F：Windows更新プログラムのインストール中に問題が発生しました。", font=("Arial", 20), fill="blue")
if __name__ == "__main__":
    application = Application()
    application.mainloop()



    #Ik3awI_yeKCSI