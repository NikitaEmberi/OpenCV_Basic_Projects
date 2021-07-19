import cv2
import mediapipe as mp

#Drawing utility
mp_drawing = mp.solutions.drawing_utils
#face detection utility
mp_face_detection = mp.solutions.face_detection

drawing_spec = mp_drawing.DrawingSpec((255,0,0),thickness=1,circle_radius=1)
#FACE MASH
mp_face_mesh = mp.solutions.face_mesh

#face mesh model
model_facemesh = mp_face_mesh.FaceMesh()

#model for detecting the face
model_detection = mp_face_detection.FaceDetection()

cap = cv2.VideoCapture(0)

while cap.isOpened():
    flag, frame = cap.read()
    if not flag:
        print("Could not access camera")
        break

#####################FOR DETECTION ONLY#################################       
    # results = model_detection.process(frame)
    # for landmark in results.detections:
    #     mp_drawing.draw_detection(frame,landmark)    
               #print(mp_face_detection.get_key_point(landmark))
    # print(results.detections)

###########FOR WRITING TEXT###########################################
    # cv2.putText(frame,"Nikita",
    # (261,157),
    # cv2.FONT_HERSHEY_COMPLEX,
    # 3,
    # (0,255,0), 2
    # )
    # cv2.rectangle(frame,(260,10),(560,100),(255,0,0),2)
################################################################### 

#########FOR MESHING ONLY##############
    results = model_facemesh.process(frame)
    print(results)
    for landmark in results.multi_face_landmarks:
        mp_drawing.draw_landmarks(
            image = frame,
            landmark_list = landmark,
            connections = mp_face_mesh.FACE_CONNECTIONS,
            landmark_drawing_spec = drawing_spec,
            connection_drawing_spec = drawing_spec
            )
        

    cv2.imshow('Frame',frame)
    if cv2.waitKey(10) and 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

