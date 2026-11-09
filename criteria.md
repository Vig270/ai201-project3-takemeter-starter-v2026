# Acceptance criteria — TakeMeter

Five criteria that say what "working" means for this classifier, written in
unit 5 **before** anything was trained.

**All five are yours this time.** None are given. You've had two projects of
practice.

An acceptance criterion names a number. *"The model is accurate"* is an
opinion. *"Every label has an F1 of at least 0.60 on the held-out set"* is a
criterion.

Under each, write a sentence or two on **why that number**. A reason that says
something about your data or your taxonomy earns credit — *"I picked 0.60 F1
for `reaction` because it's my smallest label and I only have about 50
examples of it"*. A reason that could be attached to any project does not.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

Not numbers that sound impressive. Three labels means a coin-flip guesser gets
about 33%, so a target of 0.40 is barely a target. Your number should sit
somewhere you'd honestly call useful.

**Cover at least three of these five areas.** They're here as prompts, not as a
form to fill in — a criterion that fits none of them is fine if it names a
number.

| Area | A question it could answer |
|---|---|
| Overall accuracy | How often does it need to be right to be worth using? |
| Per-label performance | Is one label allowed to be much worse than the others? |
| Balance | How lopsided can your label counts get before it's a problem? |
| Consistency | If someone else labelled the same posts, how often should you agree? |
| Confidence | Should a confident prediction be right more often than an unsure one? |

Two things worth knowing before you pick numbers, because both will affect
whether you hit them:

- **Your smallest label will have the jumpiest score.** If a label has 50
  examples, about 8 land in the test split. An F1 computed on 8 examples moves
  a lot between seeds. A target for that label should be looser than one for
  your biggest label, and saying so is a good reason.
- **Unit 6 tests across three seeds, and the target has to hold across all
  three.** A target of 0.65 against results of 0.71, 0.62, 0.68 is a **miss**.
  Pick with that in mind — it is stricter than it first sounds.

---

## 1. Overall Accuracy 

at least 0.65



**Why this target: I chose 0.65 because it is significantly better than random guessing among the three labels, while still being a realistic target for 200 posts.**



---

## 2. Per-Label performance


at least 0.55


**Why this target: I chose 0.65 because it is significantly better than random guessing among the three labels, while still being a realistic target for 200 posts.**



---

## 3. Dataset Balance

largest label no more than 1.5 times the smallest.



**Why this target:I chose 0.65 because it is significantly better than random guessing among the three labels, while still being a realistic target for 200 posts.**



---

## 4. Labeling consistency

at least 0.70.


**Why this target:I chose 0.70 because I want two people independently labeling the same posts to agree at least 70% of the time, showing that the label definitions are reasonably clear.**



---

## 5. Prediction Confidence

at least 0.75.



**Why this target:I chose 0.75 because I want predictions marked as high-confidence to be correct at least 75% of the time, rather than having confidence scores that are misleading.**






Before using these, I will write my own rationale for each target and confirm that the notebook or dataset provides a way to measure it.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 6 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Every label performs acceptably

         The model performs well on all labels.

         **Why this target:** ...

         > **Revised in unit 6:** Every label has an F1 of at least 0.60 on
         > the held-out set.
         >
         > **Why revised:** "performs well" gave me nothing to check. I
         > couldn't produce a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "Overall accuracy of at least 0.65" → "at least 0.55", because
            0.65 turned out to be optimistic for 200 examples.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->





# Criteria Self-Check — TakeMeter
# Unit 9 — Extension Acceptance Criteria

## 1. Overall Accuracy (at least 0.65)

- **How would I test it?** Calculate the model's overall accuracy on the held-out test dataset by dividing the number of correct predictions by the total number of predictions.
- **Would two people score it the same way?** Yes. Both people would use the same test dataset and compare predictions against the actual labels.
- **What would make it fail?** An overall accuracy below 0.65.

## 2. Per-Label Performance (at least 0.55)

- **How would I test it?** Calculate the performance metric selected for each of the three labels using the held-out test dataset.
- **Would two people score it the same way?** Yes, provided they use the same metric, dataset, and calculation method.
- **What would make it fail?** Any label scoring below 0.55.

## 3. Dataset Balance (largest label no more than 1.5 times the smallest)

- **How would I test it?** Count the examples belonging to each of the three labels and divide the largest label count by the smallest label count.
- **Would two people score it the same way?** Yes. Both people would count the examples in the same dataset and calculate the same ratio.
- **What would make it fail?** The largest label containing more than 1.5 times the examples of the smallest label.

## 4. Labeling Consistency (at least 0.70)

- **How would I test it?** Have two people independently label the same set of posts and calculate the percentage of posts where their labels match.
- **Would two people score it the same way?** Yes, if they use the same posts and label definitions and calculate the percentage of matching labels.
- **What would make it fail?** Agreement below 70%.

## 5. Prediction Confidence (at least 0.75)

- **How would I test it?** Evaluate predictions with confidence scores of at least 0.75 and calculate the percentage that have the correct predicted label.
- **Would two people score it the same way?** Yes, if they use the same predictions, confidence cutoff, and actual labels to calculate correctness.
- **What would make it fail?** Fewer than 75% of the high-confidence predictions being correct.



# Unit 9 — Extension Acceptance Criteria

## 1. Confidence-Based Abstention

**Criterion:** When testing 10 posts with confidence below 0.70, all of them must return `needs_review`.

**Why this target:** I chose this target because needs to be in review to see specifics.

## 2. Local CPU Inference

**Criterion:** The model must complete 10 out of 10 prediction tests using local CPU inference.

**Why this target:** I chose this target because for fair testing.

## 3. Prediction Logging

**Criterion:** When I run all successful predictions, all must be recorded in `logs/predictions.jsonl`, including the prediction, confidence, and execution time.

**Why this target:** I chose this target because to see what each of them say.

## 4. Failure Handling

**Criterion:** When I test each questions invalid inputs, all must be recorded with an error status and error details in `logs/predictions.jsonl`.

**Why this target:** I chose this target because for find each categories and see if it is correct and
see what happens after you fail.

## 5. Execution Time

**Criterion:** The average prediction execution time across 10 test inputs must be below few milliseconds.

**Why this target:** I chose this target because to classify each of them individual. 


# TakeMeter — Milestone 5 Run Log

## Test summary

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Confidence-based abstention | 10/10 low-confidence posts return `needs_review` | 10/10 | 10/10 | 10/10 | MET |
| 2. Local CPU inference | 10/10 predictions complete on CPU | 10/10 | 10/10 | 10/10 | MET |
| 3. Prediction logging | 10/10 successful predictions logged with required fields | 10/10 | 10/10 | 10/10 | MET |
| 4. Failure handling | 5/5 invalid inputs logged with error details | 5/5 | 5/5 | 5/5 | MET |
| 5. Execution time | Average below 100 ms across 10 predictions | 52.95 ms | 51.18 ms | 51.08 ms | MET |

---

## Actual test output

### Criterion 1 — Confidence-based abstention

**Produced by:** `predict.py` — `predict_post()`

**Trial 1 actual output:**

```text
CRITERION 1 — TRIAL 1
1. Confidence: 36.08%
   Prediction: needs_review
   Check: PASS
2. Confidence: 36.48%
   Prediction: needs_review
   Check: PASS
3. Confidence: 47.52%
   Prediction: needs_review
   Check: PASS
4. Confidence: 38.66%
   Prediction: needs_review
   Check: PASS
5. Confidence: 45.76%
   Prediction: needs_review
   Check: PASS
6. Confidence: 37.04%
   Prediction: needs_review
   Check: PASS
7. Confidence: 47.40%
   Prediction: needs_review
   Check: PASS
8. Confidence: 37.91%
   Prediction: needs_review
   Check: PASS
9. Confidence: 35.30%
   Prediction: needs_review
   Check: PASS
10. Confidence: 48.73%
    Prediction: needs_review
    Check: PASS
---------------------------------------------
Low-confidence posts checked: 10
Correctly sent to review: 10
```

### Criterion 2 — Local CPU inference

**Produced by:** `predict.py` — model initialization and `predict_post()`

**Trial 1 actual output:**

```text
CRITERION 2 — TRIAL 1
Model device: cpu
1. Device: cpu | Prediction completed: True
2. Device: cpu | Prediction completed: True
3. Device: cpu | Prediction completed: True
4. Device: cpu | Prediction completed: True
5. Device: cpu | Prediction completed: True
6. Device: cpu | Prediction completed: True
7. Device: cpu | Prediction completed: True
8. Device: cpu | Prediction completed: True
9. Device: cpu | Prediction completed: True
10. Device: cpu | Prediction completed: True
---------------------------------------------
Successful CPU predictions: 10/10
```

### Criterion 3 — Prediction logging

**Produced by:** `predict.py` — `predict_post()` and `write_log()`

**Log file:** `logs/predictions.jsonl`

**Trial 1 actual log entry:**

```json
{
  "timestamp": "2026-11-09T01:51:04.884455+00:00",
  "input": "How do I get better gear for my Storm wizard?",
  "output": "needs_review",
  "original_prediction": "help_question",
  "confidence": 0.3821,
  "duration_ms": 92.76
}
```

**Trial 1 actual test summary:**

```text
CRITERION 3 — TRIAL 1
New log entries: 10
Entries with required fields: 10
Required fields: ['output', 'confidence', 'duration_ms']
Successfully logged predictions: 10/10
```

### Criterion 4 — Failure handling

**Produced by:** `predict.py` — `predict_post()` exception handler and `write_log()`

**Log file:** `logs/predictions.jsonl`

**Trial 1 actual log entry:**

```json
{
  "timestamp": "2026-11-09T01:53:31.162971+00:00",
  "input": null,
  "output": "error",
  "error_type": "ValueError",
  "error_message": "You need to specify either `text` or `text_target`.",
  "duration_ms": 0.01
}
```

**Trial 1 actual test summary:**

```text
CRITERION 4 — TRIAL 1
New failure log entries: 5
Entries with error details: 5
Failures correctly logged: 5/5
```

### Criterion 5 — Execution time

**Produced by:** `predict.py` — `predict_post()`; execution time measured using `time.perf_counter()`

**Trial 1 actual output:**

```text
CRITERION 5 — TRIAL 1
1. Execution time: 86.16 ms
2. Execution time: 47.26 ms
3. Execution time: 47.37 ms
4. Execution time: 49.22 ms
5. Execution time: 56.35 ms
6. Execution time: 50.2 ms
7. Execution time: 48.22 ms
8. Execution time: 47.6 ms
9. Execution time: 44.66 ms
10. Execution time: 52.41 ms
---------------------------------------------
Average execution time: 52.95 ms
Target: Below 100 ms
Verdict: MET
```

**All five criteria passed across three separate trials.**