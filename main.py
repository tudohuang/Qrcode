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

def update_fields():
    selected_type = qr_type.get()
    url_label.pack_forget()
    url_entry.pack_forget()
    wifi_frame.pack_forget()
    sms_frame.pack_forget()
    text_frame.pack_forget()
    if selected_type == "URL":
        url_label.pack(pady=5)
        url_entry.pack(pady=5)
    elif selected_type == "WiFi":
        wifi_frame.pack(pady=5)
    elif selected_type == "SMS":
        sms_frame.pack(pady=5)
    elif selected_type == "Text":
        text_frame.pack(pady=5)

def generate_qr():
    qr_color = color_code.get() or "black"
    qr_size = size_scale.get()
    data = ""
    selected_type = qr_type.get()
    if selected_type == "URL":
        data = url_entry.get().strip()
    elif selected_type == "WiFi":
        ssid = wifi_ssid_entry.get().strip()
        password = wifi_password_entry.get().strip()
        encryption = wifi_encryption_var.get()
        if encryption == "No Encryption":
            encryption = "nopass"
        data = f"WIFI:T:{encryption};S:{ssid};P:{password};;"
    elif selected_type == "SMS":
        phone_number = sms_phone_entry.get().strip()
        message = sms_message_entry.get().strip()
        data = f"SMSTO:{phone_number}:{message}"
    elif selected_type == "Text":
        data = text_entry.get("1.0", tk.END).strip()

    if data:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=qr_size,
            border=4,
        )
        qr.add_data(data)
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
root.geometry("800x600")

title_label = ttk.Label(root, text="QR Code Generator & Scanner", font=("Arial", 24, "bold"), foreground="#4a90e2")
title_label.pack(pady=20)

qr_type = tk.StringVar()
qr_type.set("URL")
type_frame = ttk.LabelFrame(root, text="QR Code Type")
type_frame.pack(pady=5)
type_options = [("URL", "URL"), ("WiFi", "WiFi"), ("SMS", "SMS"), ("Text", "Text")]
for text, value in type_options:
    ttk.Radiobutton(type_frame, text=text, variable=qr_type, value=value, command=update_fields).pack(side=tk.LEFT, padx=10)

url_label = ttk.Label(root, text="Please enter URL:", font=("Arial", 16))
url_entry = ttk.Entry(root, width=60, font=("Arial", 14))

wifi_frame = ttk.LabelFrame(root, text="WiFi Connection")
wifi_ssid_label = ttk.Label(wifi_frame, text="SSID:")
wifi_ssid_entry = ttk.Entry(wifi_frame, font=("Arial", 14))
wifi_password_label = ttk.Label(wifi_frame, text="Password:")
wifi_password_entry = ttk.Entry(wifi_frame, font=("Arial", 14), show="*")
wifi_encryption_var = tk.StringVar(value="WPA/WPA2")
wifi_encryption_wpa = ttk.Radiobutton(wifi_frame, text="WPA/WPA2", variable=wifi_encryption_var, value="WPA/WPA2")
wifi_encryption_wep = ttk.Radiobutton(wifi_frame, text="WEP", variable=wifi_encryption_var, value="WEP")
wifi_encryption_none = ttk.Radiobutton(wifi_frame, text="No Encryption", variable=wifi_encryption_var, value="No Encryption")
wifi_ssid_label.grid(row=0, column=0, padx=5, pady=5)
wifi_ssid_entry.grid(row=0, column=1, padx=5, pady=5)
wifi_password_label.grid(row=1, column=0, padx=5, pady=5)
wifi_password_entry.grid(row=1, column=1, padx=5, pady=5)
wifi_encryption_wpa.grid(row=2, column=0, padx=5, pady=5)
wifi_encryption_wep.grid(row=2, column=1, padx=5, pady=5)
wifi_encryption_none.grid(row=2, column=2, padx=5, pady=5)

sms_frame = ttk.LabelFrame(root, text="SMS")
sms_phone_label = ttk.Label(sms_frame, text="Phone Number:")
sms_phone_entry = ttk.Entry(sms_frame, font=("Arial", 14))
sms_message_label = ttk.Label(sms_frame, text="Message:")
sms_message_entry = ttk.Entry(sms_frame, font=("Arial", 14))
sms_phone_label.grid(row=0, column=0, padx=5, pady=5)
sms_phone_entry.grid(row=0, column=1, padx=5, pady=5)
sms_message_label.grid(row=1, column=0, padx=5, pady=5)
sms_message_entry.grid(row=1, column=1, padx=5, pady=5)

text_frame = ttk.LabelFrame(root, text="Plain Text")
text_entry = tk.Text(text_frame, wrap=tk.WORD, font=("Arial", 14), width=50, height=4)
text_entry.pack(padx=5, pady=5)

color_code = tk.StringVar()
pick_color_button = tk.Button(root, text="Choose QR Code Color", command=pick_color)
pick_color_button.pack(pady=5)

size_scale = tk.Scale(root, from_=1, to=20, orient=tk.HORIZONTAL, label="QR Code Size")
size_scale.set(10)  # Default value
size_scale.pack(pady=5)

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

update_fields()  # Initialize fields based on the default selection

root.mainloop()
