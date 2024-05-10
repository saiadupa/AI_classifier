# AI Classifier

AI Classifier is a Python package for text classification using transformer models. It classifies text into two categories: AI generated or human written.

## Installation

You can install AI Classifier via pip:

```bash
pip install AI-classifier
```

## Usage

```python
from AI_text_classifier.classifier import classify_and_print

# Example text to classify
example_text = """
A package for text classification using transformers models which classifies text whether it is AI generated or human written
"""

# Call the classify_and_print function to classify the example text
classify_and_print(example_text)
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
