import tkinter as tk
import ttkbootstrap as ttk
from tkinter import messagebox
from tkinter import filedialog
import cv2
import main


window = ttk.Window(themename="journal")
window.title("Aadhaar Card Reader")
window.geometry("1200x720")
window.resizable(False, False)



# add icon
icon = tk.PhotoImage(file='Images\icon1.png')
window.iconphoto(False, icon)


front_image_path = ""
back_image_path = ""

def select_front_image():
    global front_image_path
    front_image_path = filedialog.askopenfilename( title="Select Front Image", filetypes=(("jpeg files", "*.jpg"), ("png files", "*.png")))
    # messagebox.showinfo("Front Image Selected", "Front Image Selected Successfully")

def select_back_image():
    global back_image_path
    back_image_path = filedialog.askopenfilename( title="Select Back Image", filetypes=(("jpeg files", "*.jpg"), ("png files", "*.png")))
    # messagebox.showinfo("Back Image Selected", "Back Image Selected Successfully")

def image_preprocessing(front, back):

    global front_image, back_image

    # reading images
    front_image = cv2.imread(front)
    back_image = cv2.imread(back)

    # process front image
    front_image = cv2.resize(front_image, (600, 400), interpolation=cv2.INTER_CUBIC)
    front_image = cv2.cvtColor(front_image, cv2.COLOR_BGR2GRAY)
    var_f = cv2.Laplacian(front_image, cv2.CV_64F).var()

    if var_f < 50:
        messagebox.showerror("Error", "Front Image is Too Blurry")
        exit(1)

    # process back image
    back_image = cv2.resize(back_image, (600, 400), interpolation=cv2.INTER_CUBIC)
    back_image = cv2.cvtColor(back_image, cv2.COLOR_BGR2GRAY)
    var_b = cv2.Laplacian(back_image, cv2.CV_64F).var()

    if var_b < 50:
        messagebox.showerror("Error", "Back Image is Too Blurry")
        exit(1)




def extract():
    global  front_image_path, back_image_path
    global front_image , back_image

    if front_image_path == "" or back_image_path == "":
        messagebox.showerror("Error", "Please Select Both Images")
    else:


        image_preprocessing(front_image_path, back_image_path)

        output = main.extract(front_image, back_image)

        id_type_textarea.delete("1.0", tk.END)
        name_textarea.delete("1.0", tk.END)
        dob_textarea.delete("1.0", tk.END)
        gender_textarea.delete("1.0", tk.END)
        aadhaar_number_textarea.delete("1.0", tk.END)
        pin_code_textarea.delete("1.0", tk.END)
        address_textarea.delete("1.0", tk.END)


        id_type_textarea.insert(tk.END, output['ID Type'])
        name_textarea.insert(tk.END, output['Name'])
        dob_textarea.insert(tk.END, output['Date of Birth'])
        gender_textarea.insert(tk.END, output['Sex'])
        aadhaar_number_textarea.insert(tk.END, output['Adhaar Number'])
        pin_code_textarea.insert(tk.END, output['Pin Code'])
        address_textarea.insert(tk.END, output['Address'])


# Adhaar OCR Label
aadhaar_ocr_label = ttk.Label(window, text="Aadhaar Card OCR", font=("Lucida Calligraphy", 30, "bold", 'underline'))
aadhaar_ocr_label.pack(pady=20)



# input frame
input_frame = ttk.Frame(window)
input_frame.pack(side = tk.LEFT, padx=150)

# output frame
output_frame = ttk.Frame(window)
output_frame.pack(side=tk.LEFT, padx=50, ipadx=150)


# buttons
f_img = ttk.Button(input_frame, text="Select Front Image", command=select_front_image)
f_img.pack(pady=50, padx=60)

b_img = ttk.Button(input_frame, text="Select Back Image", command=select_back_image)
b_img.pack(pady=50, padx=60)

extract = ttk.Button(input_frame, text="Extract Image Data", command=extract)
extract.pack(pady=50, padx=60)

# Id Type Label
id_type_label = ttk.Label(output_frame, text="ID Type:")
id_type_label.grid(row=1, column=2, pady=10, padx=10)

# id type textarea
id_type_textarea = tk.Text(output_frame, height=1, width=30)
id_type_textarea.grid(row=1, column=3, pady=10, padx=10)

# name label
name_label = ttk.Label(output_frame, text="Name:")
name_label.grid(row=2, column=2, pady=10, padx=10)

# name textarea
name_textarea = tk.Text(output_frame, height=1, width=30)
name_textarea.grid(row=2, column=3, pady=10, padx=10)

# DOB label
dob_label = ttk.Label(output_frame, text="DOB:")
dob_label.grid(row=3, column=2, pady=10, padx=10)

# DOB textarea
dob_textarea = tk.Text(output_frame, height=1, width=30)
dob_textarea.grid(row=3, column=3, pady=10, padx=10)

# Gender label
gender_label = ttk.Label(output_frame, text="Gender:")
gender_label.grid(row=4, column=2, pady=10, padx=10)

# gender textarea
gender_textarea = tk.Text(output_frame, height=1, width=30)
gender_textarea.grid(row=4, column=3, pady=10, padx=10)

# Aadhaar Number label
aadhaar_number_label = ttk.Label(output_frame, text="Aadhaar Number:")
aadhaar_number_label.grid(row=5, column=2, pady=10, padx=10)

# Aadhaar Number textarea
aadhaar_number_textarea = tk.Text(output_frame, height=1, width=30)
aadhaar_number_textarea.grid(row=5, column=3, pady=10, padx=10)

# Address label
address_label = ttk.Label(output_frame, text="Address:")
address_label.grid(row=7, column=2, pady=10, padx=10)

# Address textarea
address_textarea = tk.Text(output_frame, height=5, width=30)
address_textarea.grid(row=7, column=3, pady=10, padx=10)

# Pin Code label
pin_code_label = ttk.Label(output_frame, text="Pin Code:")
pin_code_label.grid(row=6, column=2, pady=10, padx=10)

# Pin Code textarea
pin_code_textarea = tk.Text(output_frame, height=1, width=30)
pin_code_textarea.grid(row=6, column=3, pady=10, padx=10)



window.mainloop()