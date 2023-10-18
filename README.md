# Pushup-counter

This project is a Python server that receives a video from a client, processes the video, and returns some data.

## Installation

1. Clone the repository
2. Install the dependencies with `pip install -r requirements.txt`
3. Run the server with `python app/main.py`

## Usage

Send a POST request to `http://localhost:8000/process_video` with the video data in the request body. The server will process the video and return the processed data in the response.

### How to install a FastAPI server

1. Install Python 3.6 or later
2. Install pip
3. Install FastAPI with `pip install fastapi`
4. Install uvicorn with `pip install uvicorn`
5. Run the server with `uvicorn main:app --reload`
You can now access the server at http://localhost:8000/.