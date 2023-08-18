# QR Code Generator & Scanner

QR Code Generator & Scanner is a simple and user-friendly application that allows users to generate custom QR codes and scan existing QR code images. With a clean and modern interface, it's designed for both personal and professional use.

## Features

1. **Generate Custom QR Codes:** Create QR codes with custom content and color. Simply input the desired URL, choose the color, and generate a QR code that can be saved as a PNG image.
2. **Scan QR Code Images:** Upload and scan existing QR code images to decode the embedded content.
3. **Easy-to-Use Interface:** A sleek and intuitive GUI makes generating and scanning QR codes a breeze.

## Installation

This application requires Python 3.x and the following libraries:

- `qrcode`
- `pyzbar`
- `PIL`
- `ttkthemes`

You can install these dependencies using pip:

```bash
pip install qrcode[pil] pyzbar pillow ttkthemes
```

## How to Use

1. **Generate QR Code:**
   - Enter the URL in the provided text field.
   - (Optional) Choose the color of the QR code using the "Choose QR Code Color" button.
   - Enter a custom file name.
   - Click the "Generate & Save QR Code" button to save the QR code as a PNG image.

2. **Scan QR Code:**
   - Click the "Scan QR Code Image" button to upload a QR code image.
   - The decoded content will be displayed in the text area.

## License

This project is open-source and available for personal, educational, or commercial use.
