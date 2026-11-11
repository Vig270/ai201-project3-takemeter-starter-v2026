import os
import pandas as pd
from sklearn.model_selection import train_test_split
from datasets import Dataset
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    TrainingArguments,
    Trainer,
    set_seed,
)

LABELS = ["guide_analysis", "help_question", "opinion_reaction"]
BASE_MODEL = "distilbert-base-uncased"
SEED = 42
EPOCHS = 3
LEARNING_RATE = 2e-5
BATCH_SIZE = 16
MAX_LENGTH = 128

# Load original and experimental datasets
original = pd.read_csv("wizard101_datasets_m5.csv")
experimental = pd.read_csv("wizard101_datasets_experimental.csv")

# Recreate the original notebook split
rest, test = train_test_split(
    original,
    test_size=0.15,
    random_state=SEED,
    stratify=original["label"],
)

train_df, val_df = train_test_split(
    rest,
    test_size=0.15 / 0.85,
    random_state=SEED,
    stratify=rest["label"],
)

# Identify new examples and add ONLY to training data
new_examples = experimental[
    ~experimental["text"].isin(original["text"])
].copy()

if len(new_examples) != 20:
    raise ValueError(f"Expected 20 new examples, found {len(new_examples)}")

if set(new_examples["text"]) & set(test["text"]):
    raise ValueError("Test-set overlap detected. Stopping.")

train_df = pd.concat([train_df, new_examples], ignore_index=True)

print("Training examples:", len(train_df))
print("Validation examples:", len(val_df))
print("Test examples reserved:", len(test))

# Prepare labels
def to_ids(df):
    lookup = {label: i for i, label in enumerate(LABELS)}
    out = df.copy()
    out["labels"] = out["label"].astype(str).str.strip().map(lookup)

    if out["labels"].isna().any():
        raise ValueError("Unknown label found.")

    return out[["text", "labels"]]

set_seed(SEED)

tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL)

model = AutoModelForSequenceClassification.from_pretrained(
    BASE_MODEL,
    num_labels=len(LABELS),
    id2label={i: label for i, label in enumerate(LABELS)},
    label2id={label: i for i, label in enumerate(LABELS)},
)

def tokenize(batch):
    return tokenizer(
        batch["text"],
        truncation=True,
        padding="max_length",
        max_length=MAX_LENGTH,
    )

train_ds = Dataset.from_pandas(to_ids(train_df)).map(
    tokenize, batched=True
)
val_ds = Dataset.from_pandas(to_ids(val_df)).map(
    tokenize, batched=True
)

args = TrainingArguments(
    output_dir="./takemeter_experimental_training",
    num_train_epochs=EPOCHS,
    learning_rate=LEARNING_RATE,
    per_device_train_batch_size=BATCH_SIZE,
    per_device_eval_batch_size=BATCH_SIZE,
    eval_strategy="epoch",
    save_strategy="no",
    logging_steps=10,
    seed=SEED,
    report_to="none",
)

trainer = Trainer(
    model=model,
    args=args,
    train_dataset=train_ds,
    eval_dataset=val_ds,
)

print("\nStarting experimental training...")
trainer.train()

# Save to a NEW folder, not the original model folder
output_dir = "./takemeter_out_experimental/final_model"
os.makedirs(output_dir, exist_ok=True)

trainer.save_model(output_dir)
tokenizer.save_pretrained(output_dir)

print("\nExperimental model saved successfully!")
print("Location:", output_dir)
