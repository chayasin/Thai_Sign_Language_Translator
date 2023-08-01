import cv2
import mediapipe as mp

cam_source = 0 # might need to change this for spesific number of cameras eg. 1,2,3 etc
cap = cv2.VideoCapture(cam_source) 

success, img = cap.read()
H, W, C = img.shape

# Import Draw Hands module
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils # You need this line to draw the hand_landmarks and HAND_CONNECTIONS

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            # Uncomment the following line to draw the hand_landmarks and HAND_CONNECTIONS
            # mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
            for index, lm in enumerate(handLms.landmark):
                if index == 8:
                    print("x:", round(lm.x,4), "y:", round(lm.y,4), "depth:", round(lm.z,5))
                    # positions containing x: horizontal position, y: vertical position, z: depth position
                    # x \in [0,1]
                    # y \in [0,1]
                    cx, cy = int(lm.x * W), int(lm.y * H)
                    cv2.circle(img, (cx, cy), 20, (255, 0, 255), cv2.FILLED)
                    
    cv2.imshow("Image", cv2.flip(img, 1))
    cv2.waitKey(1)