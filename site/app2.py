from flask import Flask,render_template,Response
import cv2
import pickle
import cvzone
import numpy as np
from pynput.keyboard import Key, Controller
import keyboard


app=Flask(__name__)


def generate_frames(): 
    cap = cv2.VideoCapture('F:/Programming/Hackathon/Hashcode/hashcode-meandthebois/inputcounter/carPark.mp4')
    while True: 
        ## read the camera frame
        success,frame=cap.read()
        if not success:
            break
        else:
            with open('CarParkPos', 'rb') as f:
                posList = pickle.load(f)
                
            width, height = 107, 48
            def checkParkingSpace(framePro):
                spaceCounter = 0
                for pos in posList:
                    x, y = pos
                    frameCrop = framePro[y:y + height, x:x + width]
                    # cv2.imshow(str(x * y), frameCrop)
                    count = cv2.countNonZero(frameCrop)
                    
                    if count < 900:
                        color = (0, 255, 0)
                        thickness = 5
                        spaceCounter += 1
                    else:
                        color = (0, 0, 255)
                        thickness = 2
                        
                    cv2.rectangle(frame, pos, (pos[0] + width, pos[1] + height), color, thickness)
                    cvzone.putTextRect(frame, str(count), (x, y + height - 3), scale=1,
                           thickness=2, offset=0, colorR=color)

                cvzone.putTextRect(frame, f'Free: {spaceCounter}/{len(posList)}', (100, 50), scale=3,
                                        thickness=5, offset=20, colorR=(0,200,0))
            while True:

                    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
                        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                    success, frame = cap.read()
                    frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    frameBlur = cv2.GaussianBlur(frameGray, (3, 3), 1)
                    frameThreshold = cv2.adaptiveThreshold(frameBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                                        cv2.THRESH_BINARY_INV, 25, 16)
                    frameMedian = cv2.medianBlur(frameThreshold, 5)
                    kernel = np.ones((3, 3), np.uint8)
                    frameDilate = cv2.dilate(frameMedian, kernel, iterations=1)    
                    checkParkingSpace(frameDilate)
                    
    #cv2.imshow("ImageBlur", frameBlur)
    #cv2.imshow("ImageThres", frameMedian)
                    ret,buffer=cv2.imencode('.jpg',frame)
                    frame=buffer.tobytes()

                    yield(b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=="__main__":
    app.run(debug=False)