from tkinter import filedialog

root = Tk()
root.title("P 165")
root.geometry("500x500")
root.configure(background="lavenderblush")


root.configure(background = "black")

label_image = Label(root, bg="white", highlightthickness=5)

    img_path = filedialog.askopenfilename(title="Open Text File", filetypwa=[("Image Files","*.jpg;*.gif;*.jpg;;*.png;*txt")])
    
img = ImageTk.PhotoImage(Image.open(image_path))
label_image["image"] = img

img = Image.open(img_path)
rotated_img = img.rotate(180)
img = ImageTk.PhotoImage(rotated_img)







img.close()






root.mainloop() 
