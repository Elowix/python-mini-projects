# QR Code Generator with Logo📱

This Python script allows you to generate a QR code from a URL or text and, if needed, add a logo to the center of the QR code. You can adjust the logo size and save the generated QR code as an image file. 🖼️

## Prerequisites ⚙️

Before running this script, you need to install a few libraries. There are two scenarios for installation:

### 1. For Virtual Machine Setup 🖥️

If you're working on a virtual machine, you can install the required libraries by using the following command:

```bash
pip install -r requirements.txt
```

### 2. For Regular Setup 🛠️

If you're not using a virtual machine and don't have the `requirements.txt` file, you can directly install the necessary libraries using:

```bash
pip install qrcode[pil] pillow
```

## The output will look like this:

https://ibb.co/cCVhMJ9


## Features ✨

- Generate QR codes from any URL or text.
- Support for all three-letter image formats (PNG, JPG, BMP, etc.).
- Output file retains the same extension as the input format.
- Ability to adjust the logo size to fit nicely in the center of the QR code.
- Saves the final QR code as an image file in the current directory.

## How to Use 🚀

1. Run the script.
2. Enter the URL or text you want to generate the QR code for.
3. Choose whether you want to add a logo to the QR code (yes/no).
4. If "yes," enter the logo's path and size.
5. The script will generate the QR code and save it in the current directory. 📂

## Recommendations 🔧

- **The logo size, according to the predefined scale in the code, it's better if is it between 100 and 160 pixels.** 📏
- **Avoid using excessively large logos**, as they might cause issues with QR code recognition. ❌
