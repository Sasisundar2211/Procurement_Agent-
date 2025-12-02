# Procurement Agent with Gemini

This project is a procurement agent that uses Gemini to detect price drifts in purchase orders.

## Running with Docker

1.  **Build the Docker image:**

    ```bash
    docker build -t procurement-agent .
    ```

2.  **Run the Docker container:**

    ```bash
    docker run -p 8000:8000 procurement-agent
    ```

Open your browser and navigate to `http://localhost:8000` to use the application.