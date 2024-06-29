# Moroccan Darija Assistant

Moroccan Darija Assistant is a web application that translates English text into Moroccan Darija (Moroccan Arabic dialect) using pre-trained models from Hugging Face. The app provides a user-friendly interface for text input and translation, with options to select different translation models and tasks.

## Features

- English to Moroccan Darija translation
- Option to select different pre-trained translation models from Hugging Face Hub
- Text-to-text generation task
- User-friendly Streamlit interface

## Getting Started

To run the application locally, follow these steps:

1. Clone the repository:
```
git clone https://github.com/kouissar/Moroccan-darija-assistant.git
```

2. Navigate to the project directory:
```
cd Moroccan-darija-assistant
```

3. Install the required dependencies:
```
pip install -r requirements.txt
```

4. Run the Streamlit app:
```
streamlit run app.py
```

The application will be accessible at `http://localhost:8501` in your web browser.

## Pre-trained Models

The application uses the following pre-trained models from Hugging Face Hub for translation:

- `Vrspi/EnglishToDarija`
- `lachkarsalim/Helsinki-translation-en-moroccann_darija`

These models are loaded and used for the translation task based on the user's selection in the application interface.

## Dependencies

- Python 3.6 or higher
- Streamlit
- Hugging Face Transformers
- Markdown

## Future Improvements

- Add more pre-trained models for translation
- Implement bidirectional translation (Moroccan Darija to English)
- Improve the user interface and experience
- Implement additional features such as speech-to-text and text-to-speech capabilities

## Contributing

Contributions to the project are welcome! If you find any issues or want to add new features, please open an issue or submit a pull request on the [GitHub repository](https://github.com/kouissar/Moroccan-darija-assistant).

## License

This project is licensed under the [MIT License](LICENSE).
