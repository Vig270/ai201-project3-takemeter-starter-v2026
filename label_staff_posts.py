
import csv
from pathlib import Path

posts_path = Path("data/staff_posts.csv")
output_path = Path("my_staff_labels.csv")

with posts_path.open("r", encoding="utf-8", newline="") as f:
    posts = list(csv.DictReader(f))

labels = {"analysis", "hot_take", "reaction"}
my_labels = []

print(f"Found {len(posts)} posts.")
print("Choose a label based on data/staff_taxonomy.md.")
print("Enter q to quit and continue later.\n")

for i, post in enumerate(posts, start=1):
    print(f"\nPost {i}/{len(posts)} — {post['id']}")
    print("-" * 60)
    print(post["text"])
    print("-" * 60)

    while True:
        label = input("Label (analysis / hot_take / reaction): ").strip()

        if label.lower() == "q":
            print("Stopped. Your labels have not been saved.")
            raise SystemExit

        if label in labels:
            my_labels.append({
                "text": post["text"],
                "label": label
            })
            break

        print("Please enter analysis, hot_take, or reaction.")

with output_path.open("w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["text", "label"])
    writer.writeheader()
    writer.writerows(my_labels)

print(f"\nSaved {len(my_labels)} labels to {output_path}.")
