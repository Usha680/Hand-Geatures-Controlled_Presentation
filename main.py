import cv2
import os
from cvzone.HandTrackingModule import HandDetector

# Variables
width, height = 1280, 720
folderPath = "Presentation"

# Camera Setup
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

# Get slide images
pathImages = sorted(os.listdir(folderPath), key=len)

# Variables
imgNumber = 0
hs, ws = int(120 * 3), int(213 * 3)
gestureThreshold = 450
buttonPressed = False
buttonCount = 0
buttonDelay = 10
annotations = [[]]
annotationNumber = 0
annotationStart = False

# Hand Detector
detector = HandDetector(detectionCon=0.8, maxHands=1)

while True:

    success, img = cap.read()

    if not success:
        break

    img = cv2.flip(img, 1)

    pathFullImage = os.path.join(folderPath, pathImages[imgNumber])
    imgCurrent = cv2.imread(pathFullImage)

    hands, img = detector.findHands(img, flipType=False)

    cv2.line(
        img,
        (0, gestureThreshold),
        (width, gestureThreshold),
        (0, 255, 0),
        10
    )

    if hands and buttonPressed is False:

        hand = hands[0]
        fingers = detector.fingersUp(hand)

        cx, cy = hand['center']
        lmList = hand['lmList']

        indexFinger = lmList[8][0], lmList[8][1]

        if cy <= gestureThreshold:

            annotationStart = False

            # Next Slide
            if fingers == [1, 0, 0, 0, 0]:

                if imgNumber < len(pathImages) - 1:

                    buttonPressed = True
                    annotations = [[]]
                    annotationNumber = 0
                    imgNumber += 1

            # Previous Slide
            if fingers == [0, 0, 0, 0, 1]:

                if imgNumber > 0:

                    buttonPressed = True
                    annotations = [[]]
                    annotationNumber = 0
                    imgNumber -= 1

        # Pointer
        if fingers == [0, 1, 1, 0, 0]:

            cv2.circle(
                imgCurrent,
                indexFinger,
                12,
                (0, 0, 255),
                cv2.FILLED
            )

            annotationStart = False

        # Draw
        if fingers == [0, 1, 0, 0, 0]:

            if annotationStart is False:

                annotationStart = True
                annotationNumber += 1
                annotations.append([])

            cv2.circle(
                imgCurrent,
                indexFinger,
                12,
                (0, 0, 255),
                cv2.FILLED
            )

            annotations[annotationNumber].append(indexFinger)

        else:
            annotationStart = False

        # Erase
        if fingers == [0, 1, 1, 1, 0]:

            if annotations:

                annotations.pop(-1)
                annotationNumber -= 1
                buttonPressed = True

    else:
        annotationStart = False

    # Button Delay
    if buttonPressed:

        buttonCount += 1

        if buttonCount > buttonDelay:

            buttonCount = 0
            buttonPressed = False

    # Draw annotations
    for i in range(len(annotations)):

        for j in range(len(annotations[i])):

            if j != 0:

                cv2.line(
                    imgCurrent,
                    annotations[i][j - 1],
                    annotations[i][j],
                    (0, 0, 200),
                    12
                )

    # Webcam overlay
    imgSmall = cv2.resize(img, (ws, hs))

    h, w, _ = imgCurrent.shape

    imgCurrent[0:hs, w - ws:w] = imgSmall

    cv2.imshow("Webcam", img)
    cv2.imshow("Slides", imgCurrent)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()