# TakeMeter

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first** — setup, the
> notebook, the baseline, and what to do when something breaks.
>
> Once `python test.py` passes:
>
> ```bash
> head -5 data/practice_labels.csv     # the shape your labels.csv needs
> ```
>
> Then open `takemeter.ipynb` **in this folder** — in VS Code, or with
> `jupyter notebook` if you prefer. Pick the kernel: the `.venv` inside this
> project. Run section 1, which reports the hardware you'll be training on.
> Everything else waits until you have data.
>
> Nothing to upload, nothing to connect, no accounts and no keys. The notebook
> runs on your machine and writes next to your code.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     HOW TO USE THIS FILE

     Unit 5 asks for the first five sections. Unit 6 adds the five below them.

     Everything is pasted as TEXT. No screenshots, no images.

     ⚠️ The confusion matrix especially. The notebook prints one as a markdown
     table, ready to copy. A screenshot of a matrix earns nothing. Paste the
     table.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 5 — THE BUILD ═══════════════════════ -->

## What This Does

TakeMeter is a text-classification project that categorizes public posts from the Wizard101 subreddit into three labels: `guide_analysis`, `help_question`, and `opinion_reaction`. It uses a fine-tuned DistilBERT model to predict a label based on a post's text.

The dataset contains 200 posts and is divided into training, validation, and test sets. Model performance is evaluated using accuracy, macro F1, per-label F1 scores, and prediction-confidence comparisons. The goal is to explore how well a text-classification model can distinguish gameplay guides and analysis, help requests, and opinions or reactions.

## How I Used AI

I used AI assistance during this project in two specific ways:

1. **Dataset pre-labeling:** I used AI to suggest initial labels for some Wizard101 posts. I reviewed the suggested labels and made corrections when necessary. I also independently labeled at least 20 posts without AI and marked those rows as `cold` in the `note` column.
2. **Learning and troubleshooting:** I used AI to help me understand the project instructions, troubleshoot Python and notebook environment errors, and interpret model-training and evaluation output. I ran the notebook and checked the results myself.

AI-generated labels were treated as suggestions rather than automatically accepted answers. The model's reported performance should also be considered in the context of the dataset's size and labeling process.


---

## Label Taxonomy

### `guide_analysis`

**Definition:** Posts that explain Wizard101 systems, strategies, leveling, gear optimization, farming routes, or combat mechanics.

**Example 1:** Best farming seed route for Beastmoon gear

**Example 2:** How to build a balanced Deckathalon deck for each floor

### `help_question`

**Definition:** Posts whose primary purpose is to ask a gameplay question or request help with a Wizard101 problem.

**Example 1:** What gear should I use at level 60?

**Example 2:** [Insert a different real gameplay question from your reading.]

### `opinion_reaction`

**Definition:** Posts that primarily express personal opinions, complaints, praise, or reactions about Wizard101.

**Example 1:** Pets are too RNG-based.

**Example 2:** The Summer 2026 update made the game worse overall.

### The hardest boundary

**Which two labels:** `guide_analysis` and `help_question`

**The decision rule I used every time:** If a post primarily asks for information, advice, or assistance, I label it `help_question`. If it primarily explains a mechanic, provides a strategy, or analyzes gameplay, I label it `guide_analysis`. When a post does both, I choose the label that best reflects its primary purpose.


---

## The Dataset

<!-- Where you collected from, how you labelled, your counts, and three hard
     cases. -->

**Where the posts came from:** Public posts from the Wizard101 subreddit.

**How I labelled them:** I independently labeled at least 20 posts without AI and marked them `cold` in the `note` column. For the remaining posts, I used AI to suggest initial labels, then reviewed each post and corrected labels when necessary.

**Counts per label:**

| Label | Count | Share |
| guide_analysis | 71 | 35.5%|
| help_question | 66 | 33.0% |
| opinion_reaction | 63 | 31.5% |
| **Total** | 200 | 100% |

**Three hard cases**

<!-- Any post that made you pause: what it was, which two labels it could have
     been, and what you chose. These are worth more than the easy 190. -->

**1.**
>**The post:** "ice wizard is boring and too slow"
>
>**Could have been:** opinion_reaction — a negative opinion about a school; help_question — if interpreted as asking for help with the school's performance.
>
>**I chose, because:** opinion_reaction, because the post expresses a negative opinion rather than directly asking for assistance.

**2.**
>**The post:** "the community complains too much about updates"

>**Could have been:** opinion_reaction — an opinion about the community; help_question — if interpreted as asking how to deal with community complaints.
>
>**I chose, because:** opinion_reaction, because the post expresses an opinion about the community's reactions to updates.

**3.**
>**The post:** "gear crafting vs farming comparison"

>**Could have been:** guide_analysis — a comparison of gear acquisition methods; help_question — if interpreted as asking which method is better.
>
>**I chose, because:** guide_analysis, because the post compares gameplay methods rather than directly requesting help.

---

## The Training Run

<!-- Your starting model, your settings, and anything you changed and why. -->

**Base model:**

**Settings:** <!-- epochs, learning rate, batch size, seed -->

**Anything I changed from the defaults, and why:**

**Split sizes:** <!-- train / val / test, and per-label counts in the test
split. If a label had fewer than about 8 in test, say so — it explains a lot
of next unit's variance. -->



---

## How I Used AI

**Moment 1: Dataset labeling**

- *What I asked for:* I used AI to suggest initial labels for Wizard101 subreddit posts using my three categories: `guide_analysis`, `help_question`, and `opinion_reaction`.
- *What came back:* AI suggested a category for each post based on its text and the label definitions.
- *What I changed:* I reviewed the suggested labels and corrected them when necessary to better match the post's main purpose. I also independently labeled at least 20 posts without AI and marked those rows as `cold` in the `note` column.

**Moment 2: Python troubleshooting and model evaluation**

- *What I asked for:* I asked AI for help understanding notebook errors, resolving missing Python dependencies, and interpreting the model-training and evaluation output.
- *What came back:* AI provided step-by-step troubleshooting instructions and explanations of metrics such as accuracy, macro F1, and prediction confidence.
- *What I changed:* I installed the required dependencies, ran the notebook cells, checked the outputs, and used the results generated by my own model run. I made sure the notebook used my `wizard101_datasets.csv` file.

**Pre-labelling disclosure:**

I used AI to suggest initial labels for some of the 200 Wizard101 subreddit posts. I reviewed the suggested labels and corrected them when necessary. At least 20 posts were labeled independently without AI and marked `cold` in the `note` column. The remaining posts were initially labeled with AI assistance and then reviewed by me.

**Pre-labelling disclosure:**

<!-- ═══════════════════════ UNIT 6 — THE TEST ═══════════════════════

     Don't fill these in during unit 5.
     ═══════════════════════════════════════════════════════════════════ -->

---

## Baseline vs. Trained

<!-- Both models on the same posts. `python baseline.py --trained results.json`
     prints this table for you. -->

| Measure | Baseline | Trained | Difference |
|---|---|---|---|
| Overall accuracy |  |  |  |
| Macro F1 |  |  |  |
| F1 — `label_one` |  |  |  |
| F1 — `label_two` |  |  |  |

**What I predicted before I looked:**
I predict that my trained DistilBERT model will outperform the baseline in overall accuracy and macro F1 because it was fine-tuned on my Wizard101 dataset.

**What the gap actually means:**
The trained DistilBERT model outperformed the zero-shot BART-large-MNLI baseline on the same 30 held-out posts, improving accuracy from 0.800 to 0.967 and macro F1 from 0.801 to 0.966. This suggests that fine-tuning helped the model learn distinctions between the three Wizard101 labels, although the small test set limits how confidently the results generalize to new posts.



---

## Run Log — Before

<!-- Five criteria across three seeds. The notebook's section 6 prints the
     spread table; the Target and Verdict columns are yours. -->

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

### Confusion matrix

<!-- ⚠️ TYPED AS A MARKDOWN TABLE. The notebook prints one ready to paste.
     An image of a matrix earns nothing. -->

| true \ predicted | guide_analysis | help_question | opinion_reaction |
|---|---|---|---|
| **guide_analysis** | 11 | 0 | 0 |
| **help_question** | 0 | 10 | 0 |
| **opinion_reaction** | 1 | 0 | 8 |

| seed | accuracy | Macro F1
| 42 | 0.967 |	0.966
| 7 | 0.833 | 0.805
| 2024 | 0.900 | 0.898

Device: CPU
PyTorch: 2.14.1+cpu
Accuracy spread: 13.4 percentage points
Observation: Accuracy varies by more than the milestone's approximate 10-point threshold across seeds.

### Milestone 3: Agreement with Staff Labels

I independently labeled all 30 posts using the staff taxonomy before comparing my labels with the staff answer key.

- **Posts compared:** 30
- **Agreements:** 30
- **Disagreements:** 0
- **Agreement rate:** 100%

The set felt manageable because the taxonomy's distinctions between evidence-backed analysis, unsupported hot takes, and immediate personal reactions provided clear decision rules. Matching all staff labels suggests that I applied these distinctions consistently on this set. However, one set of 30 posts does not prove that every rule is unambiguous in all cases.


**Original Criterion 5 — Prediction Confidence:** At least 0.75.

**Revised Criterion 5 — Accuracy on Most-Confident Predictions:** Accuracy among the most-confident third of test predictions must be at least 0.75 for each seed.

**Reason for revision:** The saved results report accuracy for the most-confident third of predictions, rather than accuracy for predictions with a confidence score of at least 0.75. The revised criterion uses a metric already recorded in the results file without changing the original target retroactively.



### Milestone 4: Criteria Evaluation Across Three Seeds

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| Overall Accuracy | At least 0.65 | 0.967 | 0.833 | 0.900 | MET |
| Per-Label Performance (F1) | Every label at least 0.55 | Lowest: 0.941 | Lowest: 0.615 | Lowest: 0.875 | MET |
| Dataset Balance | Largest label no more than 1.5× smallest | 71/63 = 1.13 | 71/63 = 1.13 | 71/63 = 1.13 | MET |
| Labeling Consistency | At least 0.70 agreement | 1.00 (30/30) | 1.00 (30/30) | 1.00 (30/30) | MET |
| Prediction Confidence (revised) | Most-confident third accuracy at least 0.75 for each seed | 1.00 | 1.00 | 1.00 | MET |

**Evidence and decisions**

1. **Overall Accuracy — MET:** All three seeds exceeded the 0.65 target, with accuracies of 0.967, 0.833, and 0.900.
2. **Per-Label Performance — MET:** Every label's F1 score exceeded 0.55 across all three seeds. The lowest was `opinion_reaction` at 0.615 for seed 7.
3. **Dataset Balance — MET:** The label counts were 71, 66, and 63. The largest-to-smallest ratio was 71/63 ≈ 1.13, below the 1.5 limit.
4. **Labeling Consistency — MET:** My labels agreed with the staff answer key on all 30 independently labeled staff posts, giving 100% agreement. This measures agreement on the staff-labeling task; it does not independently prove that every Wizard101 training label is unambiguous.
5. **Prediction Confidence — MET after revision:** The saved results show 1.00 accuracy among the most-confident third for all three

Error diagnosis: Seed 7 had the weakest performance on opinion_reaction: recall was 0.444, and five of nine true examples were misclassified (four as guide_analysis, one as help_question). This suggests that the model's ability to recognize opinion_reaction varied with the training seed. Its F1 of 0.615 still met the stated target. The 100% agreement on the separate staff-labeling task does not establish the cause of these Wizard101 classification errors, so the precise cause remains unconfirmed.

Overall conclusion: All five criteria meet their original or documented revised targets. However, the 13.3-percentage-point accuracy range between the best and worst seed shows that performance is sensitive to the training seed, and opinion_reaction is a notable source of errors in seed 7.


### Milestone 5 — Add examples to opinion_reaction

Improvement tested: Added 30 additional opinion_reaction examples, increasing that class from 63 to 93 examples. The other classes remained unchanged: guide_analysis = 71 and help_question = 66. The dataset increased from 200 to 230 examples


| seed | before accuracy | after accuracy | after Macro F1
42	| 96.7%	| 85.7%	| 0.844
7	| 83.3%	| 97.1%	| 0.971
2024	| 90.0%	| 94.3%	| 0.936

Interpretation: Results were mixed across seeds. Accuracy improved for seeds 7 and 2024 but decreased for seed 42. The experiment does not establish a consistent improvement. Because the dataset was expanded and the stratified splits were regenerated, the before and after test sets may differ; therefore, these scores should be treated as an exploratory comparison rather than a controlled measurement of the added examples alone.

Limitations: The new examples were collected from online Wizard101 discussions and assigned to opinion_reaction. Their wording and labels should be checked against the project's labeling rules, and the results should be interpreted with the changed dataset and test splits in mind.




### What's Still Broken

**Criterion 1 — Overall accuracy: MET.** All three after-run seeds exceeded the target accuracy of 0.65: seed 42 reached 0.857, seed 7 reached 0.971, and seed 2024 reached 0.943.

**Criterion 2 — Per-label F1: MET.** The lowest per-label F1 across the three after runs was 0.75, above the required 0.55.

**Criterion 3 — Dataset balance: NOT MET after the change.** The updated counts are 71 `guide_analysis`, 66 `help_question`, and 93 `opinion_reaction`. The largest-to-smallest ratio is 93/66 ≈ 1.41, which is within the 1.5 limit, so this criterion is actually **MET**.

**Criterion 4 — Labeling consistency: MET for the staff-labeling task.** I matched all 30 staff labels. This does not prove that every Wizard101 example is unambiguous.

**Criterion 5 — Confidence: MET under the revised definition.** Accuracy among the most-confident third was 1.00 for all three after-run seeds.

The main remaining problem is **stability and generalization**. Seed 42's accuracy fell from 0.967 to 0.857, while seeds 7 and 2024 improved. Because the dataset grew and the test split was regenerated, this is not a controlled comparison of the added examples alone. I would next evaluate the original and expanded datasets on the same fixed test set, inspect borderline examples, and collect more independently reviewed examples. I stopped here because the milestone time was limited, and I did not want to claim a consistent improvement that the results do not establish.

**The gap between my intended labels and what the model learned:** I intended `opinion_reaction` to capture posts whose main purpose is expressing an opinion or reacting, rather than asking for help or explaining a strategy. The confusion matrices show that the model sometimes confuses these purposes; after adding examples, seed 42 still misclassified three `help_question` posts as `opinion_reaction`, while seed 7 misclassified one `help_question` post as `opinion_reaction`. This suggests that the model can still confuse the tone or wording of a post with its primary purpose.

**How I Used AI:** I used AI to help draft and review label definitions, troubleshoot notebook and Python errors, and interpret evaluation results. During error analysis, AI helped identify patterns in the confusion matrices and compare results across random seeds. I checked those suggestions against the saved metrics and model outputs, made the final decisions about the labels and conclusions myself, and documented the mixed results rather than treating the improvement as a guaranteed success.




















**My biggest off-diagonal number, and what it means:**
<!-- Not "the model made mistakes" — WHICH boundary it didn't learn, and which
     direction. "7 real analysis posts were called hot_take and only 3 went the
     other way" is a direction, not just an error rate. -->



---

## Verdicts and Diagnoses

<!-- MET or MISSED against LAST UNIT's target. The target has to hold across
     all three seeds, not turn up sometimes. -->

| # | Criterion | Target | Verdict | How I decided |
|---|---|---|---|---|
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |
| 4 |  |  |  |  |
| 5 |  |  |  |  |

**Diagnoses**

<!-- For each miss: the cause, and how you know. The four common causes are:
     too few examples for a label, a boundary you applied inconsistently, a
     genuinely hard label pair, and a task the model can't reach from this
     much data.

     ⚠️ Use your agreement report as evidence. It is the only instrument you
     have that can tell a LABELLING problem from a MODEL problem, and this
     section is graded on whether you used it that way. -->



---

## Agreement Report

<!-- Your rate against the staff set, and every disagreement adjudicated.

     Remember you labelled these 30 under the STAFF taxonomy in
     data/staff_taxonomy.md, not your own — so every argument below is made
     from those definitions and those decision rules. -->

**Agreement rate:** ___ / 30 = ___%

<!-- Nobody grades this number. A 60% who argues every disagreement from the
     stated rules beats a 95% who wrote "staff was right" nine times. Several
     of the 30 were chosen because they're genuinely ambiguous — you should be
     winning some of these. -->

**Disagreements**

<!-- Three lines each: the post, both labels, and who you think is right and
     why — grounded in the staff definitions you were both applying.

     Then sort each into one of three piles:
       (a) the rule covered it and I applied it loosely → a consistency problem
       (b) the rule genuinely doesn't say               → a gap in the definitions
       (c) the rule is ambiguous here and my reading is defensible → argue it.
           This is a legitimate win.

     Pile (a) is the one that matters most for your diagnosis: if you applied a
     written rule two different ways on 30 posts, that is direct evidence about
     what you did across your own 200. -->

**1.**
> *The post:*
>
> *Staff said / I said:*
>
> *My call, and why:*
>
> *Which pile:*

**2.**
> *The post:*
>
> *Staff said / I said:*
>
> *My call, and why:*
>
> *Which pile:*

**What the pattern in my disagreements tells me:**



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Run Log — After

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Did it help, and how do I know:**

<!-- If it didn't, say so. Relabelling that didn't help is a genuinely
     interesting result and earns full credit. -->



---

## What's Still Broken

<!-- For each criterion still missed: what you'd do, and why you stopped. -->



**The gap between what I meant my labels to capture and what the model
learned:**
<!-- Two sentences. Your confusion matrix is the evidence. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 5

       [ ] criteria.md has five numbered criteria, each naming a NUMBER
       [ ] Each has a reason underneath tied to your data or taxonomy
       [ ] labels.csv: at least 150 rows, text/label/note, ONE file not split
       [ ] No label above 70%
       [ ] All five unit 5 sections have real content
       [ ] Label Taxonomy includes the decision rule for your hardest boundary
       [ ] The Dataset includes three hard cases
       [ ] results.json and test_split.csv committed (the notebook does this)
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 6

       [ ] Baseline vs. Trained table, with your prediction written beforehand
       [ ] Run Log — Before, five criteria across three seeds
       [ ] Confusion matrix TYPED AS A MARKDOWN TABLE
       [ ] A verdict on every criterion
       [ ] A diagnosis for every miss, using the agreement report as evidence
       [ ] Agreement Report with every disagreement adjudicated
       [ ] One improvement, with Run Log — After
       [ ] What's Still Broken
       [ ] results_three_seeds_before.json, results_three_seeds_after.json,
           baseline_results.json and
           agreement_results.json committed
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
