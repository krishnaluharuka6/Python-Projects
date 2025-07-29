from itertools import cycle
from PIL import Image, ImageTk
import time
import tkinter as tk

root = tk.Tk()
root.title("Image Slideshow Viewer")

image_paths = [  
               
               r"C:\Users\Dell\Desktop\KRISHNA_WORK\krishnaa\photo\krishna\IMG_20220805_163308_555 (1).jpg",
               r"C:\Users\Dell\Desktop\KRISHNA_WORK\krishnaa\photo\krishna\IMG_20220826_224315_983.jpg",
               r"C:\Users\Dell\Desktop\KRISHNA_WORK\krishnaa\photo\krishna\IMG_20220927_151252_751.jpg",
               r"C:\Users\Dell\Desktop\KRISHNA_WORK\krishnaa\photo\krishna\IMG_20221103_202419_509.jpg",
               r"C:\Users\Dell\Desktop\KRISHNA_WORK\krishnaa\photo\krishna\IMG_20230101_180945_657.jpg",
            ]

image_size = (500,500)
images = [Image.open(path).resize(image_size) for path in image_paths]
photo_images = [ImageTk.PhotoImage(image) for image in images]

label = tk.Label(root)
label.pack()

def update_image():
    for photo_image in photo_images:
        label.config(image = photo_image)
        label.update()
        time.sleep(3)

slideshow = cycle(photo_images)

def start_slideshow():
    for _ in range(len(image_paths)):
        update_image()

play_button = tk.Button(root, text='Play Slideshow', command=start_slideshow)
play_button.pack()

root.mainloop()