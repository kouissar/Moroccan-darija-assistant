"""
This module contains unit tests for the Moroccan Darija Assistant application.

The tests verify the translation functionality with different inputs and expected outputs,
as well as edge cases such as empty inputs or invalid model selections.
"""

import unittest
from app import translate_text

class TestTranslation(unittest.TestCase):
    def test_valid_translation(self):
        """
        Test the translation function with a valid English input and expected Moroccan Darija output.
        """
        english_text = "Hello, how are you?"
        expected_output = "السلام عليكم، كيفاش رايك؟" # Replace with the actual expected output
        translated_text = translate_text(english_text, "text2text-generation", "Vrspi/EnglishToDarija")
        self.assertEqual(translated_text, expected_output)

    def test_empty_input(self):
        """
        Test the translation function with an empty input.
        """
        empty_text = ""
        translated_text = translate_text(empty_text, "text2text-generation", "Vrspi/EnglishToDarija")
        self.assertEqual(translated_text, "")

    def test_invalid_model(self):
        """
        Test the translation function with an invalid model selection.
        """
        english_text = "Hello, how are you?"
        translated_text = translate_text(english_text, "text2text-generation", "invalid_model")
        self.assertIsNone(translated_text)

if __name__ == "__main__":
    unittest.main()
