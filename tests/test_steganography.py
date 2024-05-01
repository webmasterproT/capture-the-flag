import unittest
from steganography import hide_message, reveal_message
from utils.steganography_utils import is_message_hidden

class TestSteganography(unittest.TestCase):

    def setUp(self):
        self.test_image_path = "data/test_image.png"
        self.test_message = "TopSecret"
        self.test_output_image_path = "data/test_output_image.png"

    def test_hide_message(self):
        # Test hiding a message in an image
        hide_message(self.test_image_path, self.test_message, self.test_output_image_path)
        self.assertTrue(is_message_hidden(self.test_output_image_path), "Message was not hidden successfully")

    def test_reveal_message(self):
        # Test revealing the message from the image
        hide_message(self.test_image_path, self.test_message, self.test_output_image_path)
        revealed_message = reveal_message(self.test_output_image_path)
        self.assertEqual(revealed_message, self.test_message, "The revealed message does not match the original message")

    def test_hide_and_reveal_message(self):
        # Test the full cycle of hiding and revealing a message
        hide_message(self.test_image_path, self.test_message, self.test_output_image_path)
        revealed_message = reveal_message(self.test_output_image_path)
        self.assertEqual(revealed_message, self.test_message, "The full cycle of hiding and revealing the message failed")

if __name__ == '__main__':
    unittest.main()