from PIL import Image
import numpy as np
from utils.steganography_utils import message_to_bin, bin_to_message

def hide_message(image_path, message, output_path):
    """
    Hide a message inside an image using the least significant bit steganography technique.
    """
    # Convert the message to binary
    binary_message = message_to_bin(message)
    binary_message += '1111111111111110'  # Delimiter to indicate end of message

    # Load the image
    img = Image.open(image_path)
    pixels = np.array(img)
    flat_pixels = pixels.flatten()

    # Check if the image can hold the message
    if len(binary_message) > len(flat_pixels):
        raise ValueError("The message is too long to be hidden in the provided image.")

    # Hide the message in the image
    for i in range(len(binary_message)):
        flat_pixels[i] = flat_pixels[i] & ~1 | int(binary_message[i])

    # Reshape the pixels back to the original image shape
    new_pixels = flat_pixels.reshape(pixels.shape)

    # Save the new image with the hidden message
    new_img = Image.fromarray(new_pixels.astype('uint8'), img.mode)
    new_img.save(output_path)

def reveal_message(image_path):
    """
    Reveal the hidden message from an image.
    """
    # Load the image
    img = Image.open(image_path)
    pixels = np.array(img)
    flat_pixels = pixels.flatten()

    # Extract the least significant bits
    binary_message = ''.join([str(pixel & 1) for pixel in flat_pixels])

    # Find the delimiter indicating the end of the message
    delimiter = binary_message.find('1111111111111110')
    if delimiter == -1:
        raise ValueError("No hidden message found.")

    # Extract the message up to the delimiter
    binary_message = binary_message[:delimiter]

    # Convert the binary message to a string
    message = bin_to_message(binary_message)
    return message

if __name__ == "__main__":
    # Example usage:
    # To hide a message:
    # hide_message('input_image.png', 'Secret Message', 'output_image.png')

    # To reveal a message:
    # revealed_message = reveal_message('output_image.png')
    # print(revealed_message)
    pass
