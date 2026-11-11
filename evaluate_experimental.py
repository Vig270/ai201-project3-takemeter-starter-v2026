import torch
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, classification_report, confusion_matrix
from transformers import AutoTokenizer, AutoModelForSequenceClassification

LABELS = ["guide_analysis", "help_question", "opinion_reaction"]
THRESHOLD = 0.70

# Recreate the original held-out test set
original = pd.read_csv("wizard101_datasets_m5.csv")
_, test = train_test_split(
    original,
    test_size=0.15,
    random_state=42,
    stratify=original["label"],
)

texts = test["text"].tolist()
actual = test["label"].tolist()

def evaluate_model(model_path, model_name):
    print(f"\n{'=' * 55}")
    print(model_name)
    print("=" * 55)

    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForSequenceClassification.from_pretrained(model_path)
    model.eval()

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    predictions = []
    review_count = 0

    with torch.no_grad():
        for start in range(0, len(texts), 16):
            batch = texts[start:start + 16]
            inputs = tokenizer(
                batch,
                truncation=True,
                padding=True,
                max_length=128,
                return_tensors="pt",
            )
            inputs = {key: value.to(device) for key, value in inputs.items()}
            probabilities = torch.softmax(model(**inputs).logits, dim=-1)
            confidence, predicted_ids = probabilities.max(dim=-1)

            predictions.extend(
                model.config.id2label[int(i)] for i in predicted_ids.cpu()
            )
            review_count += int((confidence < THRESHOLD).sum().item())

    print("Accuracy:", round(accuracy_score(actual, predictions), 4))
    print("Macro F1:", round(f1_score(
        actual, predictions, labels=LABELS, average="macro", zero_division=0
    ), 4))
    print("Needs review (<70% confidence):", review_count, "of", len(texts))

    print("\nClassification report:")
    print(classification_report(
        actual, predictions, labels=LABELS, zero_division=0
    ))

    print("Confusion matrix (rows=actual, columns=predicted):")
    print(confusion_matrix(actual, predictions, labels=LABELS))

evaluate_model("takemeter_out/final_model", "ORIGINAL MODEL")
evaluate_model(
    "takemeter_out_experimental/final_model",
    "EXPERIMENTAL MODEL",
)
