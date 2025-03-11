from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import imutils

def visualizar():
    global cap
    if cap is not None:
        ret, frame = cap.read()
        if ret == True:
            frame = imutils.resize(frame, width=500)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            im = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image=im)

            lbvideo.config(image=img)
            lbvideo.image = img
            lbvideo.after(10, visualizar)
        else:
            lbinfovideopath.configure(text="No se pudo abrir el video")
            lbvideo.image = ""
            cap.release()
        
def abrirVideo():
    global cap
    
    if cap is not None:
        lbvideo.image=""
        cap.release()
        cap = None
    # Seleccionar el video
    video_path = filedialog.askopenfilename(filetypes=[("all video files", "*.mp4")])
    if len(video_path) > 0:
        lbinfovideopath.config(text=video_path)
        cap = cv2.VideoCapture(video_path)
        visualizar()
    else :
        lbinfovideopath.config(text="Aun no se ha seleccionado un video")

cap = None
root = Tk()

boton = Button(root, text="Abrir video", command=abrirVideo)
boton.grid(row=0, column=0, padx=5, pady=5)

lbinfo1 = Label(root, text="Video de entrada:")
lbinfo1.grid(column=0, row=1)

lbinfovideopath = Label(root, text="Aun no se ha seleccionado un video")
lbinfovideopath.grid(column=1, row=1)

lbvideo = Label(root)
lbvideo.grid(column=0, row=2, columnspan=2)

root.mainloop()
