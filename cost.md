# TakeMeter Cost and Execution Measurement

## 1. Model Size

TakeMeter uses a locally saved DistilBERT classification model.

- Base model: `distilbert-base-uncased`
- Model weights file: `model.safetensors`
- Model weights size: approximately 268 MB
- Model location: `takemeter_out/final_model/`

## 2. Execution Environment

- Execution method: Local inference
- Hardware: CPU
- Python version: 3.11.9
- External model API: Not used

## 3. Inference Time

Initial prediction runs recorded the following execution times:

| Test | Execution Time |
|---|---:|
| First logged prediction | 81.85 ms |
| Second logged prediction | 80.45 ms |

These are observed development-machine measurements. Actual execution times may vary depending on hardware and system conditions.

## 4. API and Compute Costs

TakeMeter runs the trained model locally rather than sending requests to an external model API.

- External API charges: $0
- API tokens billed: 0
- Local CPU inference: Used
- Cloud inference charges: $0

Local execution still uses the computer's CPU and electricity, but there are no per-request model API charges.

## 5. Measurement Summary

The system uses approximately 268 MB of model weights and has demonstrated prediction times of approximately 80–82 milliseconds in initial runs.

The local execution approach avoids external API costs and does not require a hosted inference service.