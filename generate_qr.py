import qrcode
from pathlib import Path


# Define the output path for the QR code image
QR_OUTPUT = Path('./QR_code') / 'qr.png'

# Define the URL to be encoded into the QR code
URL = "http://127.0.0.1:8000/"


def generate_qr_code():
    """
    Generate a QR code image from the specified URL and save it to the output path.
    """
    # Generate the QR code image using the specified URL
    qr_image = qrcode.make(URL)

    # Save the QR code image to the output path
    qr_image.save(QR_OUTPUT)


if __name__ == "__main__":
    # If this script is executed directly, call the generate_qr_code function
    generate_qr_code()
