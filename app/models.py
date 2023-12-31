import cv2
import mediapipe as md
import time

from moviepy.editor import VideoFileClip
import moviepy.video.fx.all as vfx
import constant

def count_pushup(path):
    md_pose = md.solutions.pose 

    count = 0
    position = None 

    # cap = cv2.VideoCapture(path, cv2.CAP_DSHOW)
    cap = cv2.VideoCapture(path)

    # debug
    num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    start_time = time.time()

    with md_pose.Pose(
        min_detection_confidence = 0.7,
        min_tracking_confidence = 0.7
    ) as pose:
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                print('Video not found or ended')
                break
            
            image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
            result = pose.process(image)
            
            imlist = []

            if result.pose_landmarks:
                for id, lm in enumerate(result.pose_landmarks.landmark):
                    h, w, _ = image.shape
                    X, Y = int(lm.x * w), int(lm.y * h)
                    imlist.append([id, X, Y])

            if len(imlist) != 0:
                right = abs(imlist[constant.RIGHT_SHOULDER][2] - imlist[constant.RIGHT_ELBOW][2])
                left = abs(imlist[constant.LEFT_SHOULDER][2] - imlist[constant.LEFT_ELBOW][2])
                if ((left) >= constant.DOWN_HAND_THRESHOLD 
                and (right) >= constant.DOWN_HAND_THRESHOLD):
                    position = "down"
                if ((left) <= constant.UP_HAND_THRESHOLD 
                and (right) <= constant.UP_HAND_THRESHOLD) and position == "down":
                    position = "up"
                    count +=1 
                    print(count)

    # debug
    end_time = time.time()
    time_taken = end_time - start_time
    fps = num_frames / time_taken
    time_per_frame = time_taken / num_frames * 1000

    print(f'Process time: {time_taken:.2f}')
    print(f'Frames per second: {fps:.2f}')
    print(f'Time per frame: {time_per_frame:.2f} ms')

    cap.release()
    return count

def count_squat(path):
    count = 0
    return count

def speedup_video(old, new):
    clip = VideoFileClip(old)
    final = clip.fx(vfx.speedx, constant.SPEED_UP_THRESHOLD)
    final.write_videofile(new)
    return 