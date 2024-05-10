```markdown
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
Plausibility Solutions is a leading mobile app development company that develops apps on IOS, Android, and Hybrid platforms. We have a dedicated team that specializes in mobile app development. With over a decade of experience, our mobile app developers are well aware of constantly evolving technology stacks and models. Furthermore, we can proudly say that we are featured as the top mobile app development company in Europe according to Clutch. We are also featured in the top consumer, financial, e-commerce, social media, and healthcare mobile app development companies in the USA according to Clutch and Good firm.
"""

# Call the classify_and_print function to classify the example text
classify_and_print(example_text)
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```
