# Procurement Price-Drift Enforcement Agent

A tool to detect and enforce price-drift in procurement data.

## How to run locally

1.  Generate data:
    ```bash
    python data_generator.py
    ```
    This generates data in `data/private` and `data/public`.

2.  Ingest public data:
    ```bash
    python -c "from src.agents.ingestor import run; run()"
    ```

3.  Start the API:
    ```bash
    uvicorn src.api.fastapi_app:app --reload --port 8000
    ```

4.  Run detection via API:
    ```bash
    curl -X POST http://localhost:8000/run_detection
    ```

## LLM Usage

This project can use a Large Language Model (LLM) for certain tasks. The `LLM_PROVIDER` environment variable controls which provider to use.

-   `LLM_PROVIDER=local`: (Default) Uses a simple, deterministic local fallback that does not make network requests.
-   `LLM_PROVIDER=openai`: Uses the OpenAI API. Requires an `LLM_API_KEY`.

## Compliance

-   For compliance details, see `compliance.md`.
-   For third-party licenses, see `THIRD_PARTY_NOTICES.md`.
-   A template for submission is in `submission_compliance.txt`.

## How to create submission artifact

To create a submission artifact that excludes private data, run the following command:

```bash
python scripts/make_submission_artifact.py
```

## Team Eligibility

-   **Team Members:** `<Your Name(s) / Handle(s)>`
-   Please confirm that all team members meet the competition's residency and export control rules.
