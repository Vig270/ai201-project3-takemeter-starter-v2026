
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch.nn.functional as F

# Location of the saved TakeMeter model
MODEL_DIR = "./takemeter_out/final_model"

# Confidence threshold
CONFIDENCE_THRESHOLD = 0.70

# Load the trained model and tokenizer
tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_DIR)

# Use CPU for local execution
model.to("cpu")
model.eval()


def predict_post(text):
    """Predict a Wizard101 post or request human review if confidence is low."""

    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding="max_length",
        max_length=128
    )

    with torch.no_grad():
        outputs = model(**inputs)
        probabilities = F.softmax(outputs.logits, dim=-1)

    confidence, predicted_id = torch.max(probabilities, dim=-1)

    confidence = confidence.item()
    predicted_id = predicted_id.item()

    predicted_label = model.config.id2label[predicted_id]

    if confidence < CONFIDENCE_THRESHOLD:
        final_label = "needs_review"
    else:
        final_label = predicted_label

    return {
        "prediction": final_label,
        "original_prediction": predicted_label,
        "confidence": round(confidence, 4)
    }


if __name__ == "__main__":
    post = input("Enter a Wizard101 post: ")
    result = predict_post(post)

    print("\nTakeMeter Result")
    print("----------------")
    print(f"Prediction: {result['prediction']}")
    print(f"Original prediction: {result['original_prediction']}")
    print(f"Confidence: {result['confidence']:.2%}")
