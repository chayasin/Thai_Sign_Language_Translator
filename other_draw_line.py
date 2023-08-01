import cv2
import mediapipe as mp

import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

# stime = time.now()

points_arr = []
lines_array = []

def draw_lines(img):
    for line in lines_array:
        draw_line(line)

def draw_line(img):
    if not points_arr:
        return
    if len(points_arr) <= 2:
        return
    for x, y in zip(points_arr[:-1], points_arr[1:]):
        cv2.line(img, x, y, (255,0,0), 5)
        
def add_point(point):
    if now_time - start_time > 1:
        return
    points_arr.append(point)

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for index, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                if index == 8 and lm.z < -0.05:
                    cv2.circle(img, (cx, cy), 20, (255, 0, 255), cv2.FILLED)
                    points_arr.append((cx, cy))
        
            
    draw_line(img)
    cv2.imshow("Image", cv2.flip(img, 1))
    cv2.waitKey(1)