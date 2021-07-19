import cv2
import mediapipe as mp

#Drawing Utility
mp_drawing = mp.solutions.drawing_utils

mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)
with mp_hands.Hands() as hands:
  while cap.isOpened():
    flag, frame = cap.read()
    if not flag:
      print("Couldn't access camera")
      break

    # Flip the image horizontally for a later selfie-view display, and convert
    # the BGR image to RGB.
    frame = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)
    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    frame.flags.writeable = False
    results = hands.process(frame)

    # Draw the hand annotations on the image.
    frame.flags.writeable = True
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
      for landmark in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            frame, landmark, mp_hands.HAND_CONNECTIONS)
    cv2.imshow('Frame', frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
      break
cap.release()
