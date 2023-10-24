import cv2
import mediapipe as md

def count_pushup(path):
    md_pose = md.solutions.pose 

    count = 0
    position = None 

    cap = cv2.VideoCapture(path)

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
                left = abs(imlist[12][2] - imlist[14][2])
                right = abs(imlist[11][2] - imlist[13][2])
                if ((left) >= 75 and (right) >= 75):
                    position = "down"
                if ((left) <= 50 and (right) <= 50) and position == "down":
                    position = "up"
                    count +=1 
                    print(count)

    cap.release()
    return count