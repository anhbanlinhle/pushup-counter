import os
import datetime

def process_video(video_data):
    file_name = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    path = f"../data/{file_name}.mp4"
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "wb") as f:
        f.write(video_data)

    processed_data = count_pushup(path)

    return processed_data


def count_pushup(path):
    count = 0
    return count