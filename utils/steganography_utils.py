from PIL import Image
import stepic
import io

def hide_message(image_path, message, output_path):
    """
    Hide a message inside an image using steganography.
    
    :param image_path: Path to the original image.
    :param message: The message to hide.
    :param output_path: Path to save the modified image.
    """
    # Open the image
    image = Image.open(image_path)
    
    # Convert the message to bytes
    message_bytes = bytes(message, 'utf-8')
    
    # Use stepic to encode the message into the image
    encoded_image = stepic.encode(image, message_bytes)
    
    # Save the modified image
    encoded_image.save(output_path, 'PNG')

def reveal_message(image_path):
    """
    Reveal the hidden message from an image.
    
    :param image_path: Path to the steganographic image.
    :return: The hidden message.
    """
    # Open the image
    image = Image.open(image_path)
    
    # Use stepic to decode the message from the image
    message_bytes = stepic.decode(image)
    
    # Convert the message from bytes to a string
    message = message_bytes.decode('utf-8')
    
    return message

def hide_message_in_memory(image_bytes, message):
    """
    Hide a message inside an image represented as bytes using steganography.
    
    :param image_bytes: Bytes of the original image.
    :param message: The message to hide.
    :return: Bytes of the modified image.
    """
    # Load the image from bytes
    image = Image.open(io.BytesIO(image_bytes))
    
    # Convert the message to bytes
    message_bytes = bytes(message, 'utf-8')
    
    # Use stepic to encode the message into the image
    encoded_image = stepic.encode(image, message_bytes)
    
    # Save the modified image to a bytes buffer
    img_byte_arr = io.BytesIO()
    encoded_image.save(img_byte_arr, format='PNG')
    
    # Return the bytes of the modified image
    return img_byte_arr.getvalue()

def reveal_message_from_memory(encoded_image_bytes):
    """
    Reveal the hidden message from an image represented as bytes.
    
    :param encoded_image_bytes: Bytes of the steganographic image.
    :return: The hidden message.
    """
    # Load the image from bytes
    image = Image.open(io.BytesIO(encoded_image_bytes))
    
    # Use stepic to decode the message from the image
    message_bytes = stepic.decode(image)
    
    # Convert the message from bytes to a string
    message = message_bytes.decode('utf-8')
    
    return message
