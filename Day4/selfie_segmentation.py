import cv2
import mediapipe as mp
import numpy as np
#Drawing utility
mp_drawing = mp.solutions.drawing_utils
mp_selfie_segmentation = mp.solutions.selfie_segmentation
bg_image = cv2.imread("../images/goku.jpg")

model = mp_selfie_segmentation.SelfieSegmentation(model_selection=1)

cap = cv2.VideoCapture(0)
# C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools
while cap.isOpened():
    flag, frame = cap.read()
    if not flag:
        print("could not accesss camera")
        break

    results = model.process(frame)
    condition = np.stack((results.segmentation_mask,)*3,axis = -1) > 0.5

    if bg_image is None:
        bg_image = np.zeros(frame.shape,dtype=np.uint8)
        bg_image[:] = (0,255,0)

    bg_image = cv2.resize(bg_image,(frame.shape[1],frame.shape[0]))
    output_image = np.where(condition,frame,bg_image)
    cv2.imshow("Frame",results.segmentation_mask)
    # cv2.imshow("Frame",output_image)
    if cv2.waitKey(10) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

