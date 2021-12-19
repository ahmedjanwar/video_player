import cv2
import numpy as np

new_cap = cv2.VideoCapture("sample.mp4")

#if(new_cap.isOpened == false):
    #print("error opning file")
while(new_cap.isOpened()):
    ret, frame = new_cap.read()
    if ret == True:
        cv2.imshow("Video_player",frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

new_cap.release()
cv2.destroyAllWindows()
