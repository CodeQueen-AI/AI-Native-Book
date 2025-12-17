# Quickstart: Embed Chatbot UI

This quickstart guide will help you get the embedded chatbot UI up and running.

## Prerequisites

*   Node.js and npm installed.
*   Python and pip installed.
*   A `GEMINI_API_KEY` environment variable set.

## Running the Application

1.  **Run the Backend (FastAPI)**

    You'll need one terminal for the backend.

    1.  **Navigate to the backend directory:**
        ```bash
        cd backend
        ```

    2.  **Install dependencies:**
        ```bash
        pip install -r requirements.txt
        ```

    3.  **Run the FastAPI server:**
        ```bash
        uvicorn src.main:app --reload
        ```

        The server will be running on `http://127.0.0.1:8000`.

2.  **Run the Docusaurus App (Frontend)**

    You'll need a *separate* terminal for the frontend.

    1.  **Navigate to the `book_source` directory:**
        ```bash
        cd book_source
        ```

    2.  **Install dependencies:**
        ```bash
        npm install
        ```

    3.  **Start the Docusaurus app:**
        ```bash
        npm start
        ```

        The application will be running on `http://localhost:3000`.

3.  **Verify the Integration**

    *   Once both the frontend and backend are running, open your browser and navigate to any of the documentation pages.
    *   You should see a circular floating button with a chat bubble icon at the bottom right of the screen.
    *   Click the button to open the chatbot panel.
    *   Try sending a message. You should see the answer from the backend displayed in the chat window, along with the sources.
