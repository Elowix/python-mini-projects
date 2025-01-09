# Recommendations:
# change 'fill_color' and 'black_color' may make diagnosis difficult.
# excessive increase in 'logo_size' can lead to issues in recognizing the QR code,
# so it is recommended to choose a size within the range of 100 to 160.

import qrcode
from PIL import Image
import os

link = input('enter your link: ')

add_logo = input('do you want to add a logo to the QR code? (yes/no): ').strip().lower()


qr = qrcode.QRCode(version=3, box_size=15, border=4)
qr.add_data(link)
qr.make(fit=True)


img = qr.make_image(fill_color='black', back_color='white')
if add_logo == 'yes':
    logo_path = input('enter the path to your logo image: ').strip()
    file_format = logo_path[-3:]
    logo_size_input = (input('enter the logo size (press Enter = default = 130): ').strip())

    if os.path.exists(logo_path):

        logo = Image.open(logo_path)
        logo = logo.convert('RGBA')


        if logo_size_input == '':
            logo_size = 130
        elif logo_size_input.isdigit():
            logo_size = int(logo_size_input)
        else:
            logo_size = 130        
    
        logo = logo.resize((logo_size, logo_size))


        qr_width, qr_height = img.size
        logo_position = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)

        img.paste(logo, logo_position, logo)
    else:
        print('logo file not found, the process is runnig without a logo')


current_directory = os.path.dirname(os.path.abspath(__file__))

output_path = os.path.join(current_directory, f"my_qrcode.{file_format}")
img.save(output_path)

print(f"QR code saved as: '{output_path}'")