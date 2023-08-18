import tkinter as tk
from tkinter import filedialog, colorchooser
import qrcode
from pyzbar.pyzbar import decode
from PIL import Image
from ttkthemes import ThemedTk
from tkinter import ttk
import os

def pick_color():
    color = colorchooser.askcolor(title="Choose Color")
    if color[1]:
        color_code.set(color[1])

def generate_qr():
    url = url_entry.get().strip()
    qr_color = color_code.get() or "black"
    if url:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)
        img_qr = qr.make_image(fill_color=qr_color, back_color="white")

        # Select save path
        folder_path = filedialog.askdirectory()
        file_name = file_name_entry.get().strip()

        if folder_path and file_name:
            full_path = os.path.join(folder_path, file_name + ".png")
            img_qr.save(full_path)
            result_text.insert(tk.END, f"QR Code saved to {full_path}\n")

def scan_qr():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        image = Image.open(file_path)
        decoded_objects = decode(image)
        for obj in decoded_objects:
            qr_data = obj.data.decode('utf-8')
            result_text.insert(tk.END, f"Scanned QR Code data: {qr_data}\n")

# GUI setup
root = ThemedTk(theme="arc")
root.title("QR Code Generator & Scanner")
root.geometry("700x450")

title_label = ttk.Label(root, text="QR Code Generator & Scanner", font=("Arial", 24, "bold"), foreground="#4a90e2")
title_label.pack(pady=20)

url_label = ttk.Label(root, text="Please enter URL:", font=("Arial", 16))
url_label.pack(pady=5)
url_entry = ttk.Entry(root, width=60, font=("Arial", 14))
url_entry.pack(pady=5)

color_code = tk.StringVar()
pick_color_button = tk.Button(root, text="Choose QR Code Color", command=pick_color)
pick_color_button.pack(pady=5)

file_name_label = ttk.Label(root, text="Please enter custom file name:", font=("Arial", 16))
file_name_label.pack(pady=5)
file_name_entry = ttk.Entry(root, width=60, font=("Arial", 14))
file_name_entry.pack(pady=5)

button_frame = ttk.Frame(root)
button_frame.pack(pady=10)
generate_button = ttk.Button(button_frame, text="Generate & Save QR Code", command=generate_qr, width=25)
generate_button.grid(row=0, column=0, padx=10)
scan_button = ttk.Button(button_frame, text="Scan QR Code Image", command=scan_qr, width=25)
scan_button.grid(row=0, column=1, padx=10)

result_text = tk.Text(root, height=6, wrap=tk.WORD, font=("Arial", 12))
result_text.pack(pady=10, padx=20, fill=tk.BOTH)

root.mainloop()
