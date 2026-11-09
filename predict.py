import os
import json
import time
from datetime import datetime, timezone

import torch
import torch.nn.functional as F
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Location of the saved TakeMeter model
MODEL_DIR = "./takemeter_out/final_model"

# Confidence threshold
CONFIDENCE_THRESHOLD = 0.70

# Location of prediction logs
LOG_FILE = "./logs/predictions.jsonl"

# Create the logs folder if it does not exist
os.makedirs("./logs", exist_ok=True)


def write_log(log_entry):
    """Append one structured entry to the JSONL log."""
    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(json.dumps(log_entry) + "\n")


# Load the trained model and tokenizer
tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_DIR)

model.to("cpu")
model.eval()

# Warm up the model before accepting real predictions
warmup_inputs = tokenizer(
    "TakeMeter warm-up.",
    return_tensors="pt",
    truncation=True,
    padding="max_length",
    max_length=128
)

with torch.no_grad():
    model(**warmup_inputs)

del warmup_inputs


def predict_post(text):
    """Predict a Wizard101 post and log success or failure."""

    start_time = time.perf_counter()

    try:
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

        duration_ms = round(
            (time.perf_counter() - start_time) * 1000, 2
        )

        result = {
            "prediction": final_label,
            "original_prediction": predicted_label,
            "confidence": round(confidence, 4),
            "duration_ms": duration_ms
        }

        # Log successful prediction
        log_entry = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "input": text,
            "output": final_label,
            "original_prediction": predicted_label,
            "confidence": round(confidence, 4),
            "duration_ms": duration_ms
        }

        write_log(log_entry)

        return result

    except Exception as error:
        duration_ms = round(
            (time.perf_counter() - start_time) * 1000, 2
        )

        # Log prediction failure
        log_entry = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "input": text,
            "output": "error",
            "error_type": type(error).__name__,
            "error_message": str(error),
            "duration_ms": duration_ms
        }

        write_log(log_entry)

        raise


if __name__ == "__main__":
    print("TakeMeter - Wizard101 Classifier")
    print("Enter 'exit' when you are finished.\n")

    while True:
        post = input("Enter a Wizard101 post: ")

        if post.lower() == "exit":
            break

        if not post.strip():
            continue

        try:
            result = predict_post(post)

            print("\nTakeMeter Result")
            print("----------------")
            print(f"Prediction: {result['prediction']}")
            print(f"Original prediction: {result['original_prediction']}")
            print(f"Confidence: {result['confidence']:.2%}")
            print(f"Execution time: {result['duration_ms']} ms")
            print(f"Log saved to: {LOG_FILE}\n")

        except Exception as error:
            print("\nPrediction failed.")
            print(f"Error: {type(error).__name__}: {error}")
            print(f"Failure logged to: {LOG_FILE}\n")