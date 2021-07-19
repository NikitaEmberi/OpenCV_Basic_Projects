#DAY 3
import cv2

cap = cv2.VideoCapture(0)
image = cv2.imread("images/background.jpg")
while True:
    flag, frame = cap.read()
    if not flag:
        print("Couldn't access camera")
        break
    
    k = cv2.waitKey(50)
    image = cv2.resize(image,(frame.shape[1],frame.shape[0]))
    blended_frame = cv2.addWeighted(image,0.0,frame,1.0,gamma=0.2)
    cv2.imshow("Blended Frame",blended_frame)
  
    if k & 0xff == ord('1'):
        image = cv2.imread("images/background1.jpg")
    if k & 0xff == ord('2'):
        image = cv2.imread("images/background2.jpg")
    if k & 0xff == ord('3'):
        image = cv2.imread("images/background3.jpg")
    if k & 0xff == ord('4'):
        image = cv2.imread("images/background4.jpg")
    if k & 0xff == ord('5'):
        image = cv2.imread("images/background5.jpg")
    if k & 0xff == ord('6'):
        image = cv2.imread("images/background6.jpg")

    if k & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

