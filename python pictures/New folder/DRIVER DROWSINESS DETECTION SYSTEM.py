from scipy.spatial import distance as dist
from imutils.video import VideoStream
from imutils import face_utils
from threading import Thread
import numpy as np
import argparse
import imutils
import time
import dlib
import cv2
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from pygame import mixer   
import os
from datetime import datetime
import pygame 
from gtts import gTTS
import keyboard

usermail='ukavitha45@gmail.com'
userpass='kavi@9483'
sendermail='yugarashim2004@gmail.com'

def mail():
    msg=MIMEMultipart()
    msg['Frome']=usermail
    msg['To']=sendermail
    msg['subject']='Drowsiness detected!!'

    msg.attach(MIMEText("Drowsiness Detected!!","plain"))
    filename = './image.jpg'
    file = open(filename,'rb')

    part=MIMEBase('application','octet-stream')
    part.set_payload(file.read())
    part.add_header('content-Disposition', 'attachment; filename='+filename)
    encoders.encode_base64(part)
    msg.attach(part)

    massage=msg.as_string()

    server=smtplib.SMTP('smtp.gmail.com',587)

    server.ehlo()
    server.starttls()
    server.ehlo()
    print("sending email")
    server.login(usermail,userpass)
    server.sendmail(usermail,sendermail,massage)
    server.quit()

    time.sleep(1)
    file.close()
    
# an audio will be played which speaks the test if pyttsx3 recognizes it
def CallAudio(TextPhrase):
    # Language in which you want to convert
    language = 'en'  
    # Passing the text and language to the engine, 
    # here we have marked slow=False. Which tells 
    # the module that the converted audio should 
    # have a high speed
    myobj = gTTS(text=TextPhrase, lang=language, slow=False)      
    # Saving the converted audio in a mp3 file named 
    now = datetime.now() 
    print("now =", now)
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d%m%Y%H%M%S")
    MusicfileName = str("Welcome" + dt_string + ".mp3")
    print(MusicfileName)
    myobj.save(MusicfileName)        
    PlayAudio(MusicfileName)
    print(MusicfileName)
    os.remove(MusicfileName)
        
def PlayAudio(FileName):
    # Starting the mixer
    mixer.init()      
    # Loading the song
    mixer.music.load(FileName)  
    print(FileName)    
    # Setting the volumee
    mixer.music.set_volume(0.7)      
    # Start playing the song
    mixer.music.play()  
    while pygame.mixer.music.get_busy() == True:
        if keyboard.is_pressed('q'):  # if key 'q' is pressed 
            print('You Pressed A Key!')
            break  # finishing the loop
        continue
    # time.sleep(3)
    mixer.music.stop()
    mixer.quit()
    #pygame.event.wait()

def alarm(msg):
    global alarm_status
    global alarm_status2
    global saying

    while alarm_status:
        print('call')
        s = 'espeak "'+msg+'"'
        os.system(s)

    if alarm_status2:
        print('call')
        saying = True
        s = 'espeak "' + msg + '"'
        os.system(s)
        saying = False

def eye_aspect_ratio(eye):
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])

    C = dist.euclidean(eye[0], eye[3])

    ear = (A + B) / (2.0 * C)

    return ear

def final_ear(shape):
    (lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
    (rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

    leftEye = shape[lStart:lEnd]
    rightEye = shape[rStart:rEnd]

    leftEAR = eye_aspect_ratio(leftEye)
    rightEAR = eye_aspect_ratio(rightEye)

    ear = (leftEAR + rightEAR) / 2.0
    return (ear, leftEye, rightEye)

def lip_distance(shape):
    top_lip = shape[50:53]
    top_lip = np.concatenate((top_lip, shape[61:64]))

    low_lip = shape[56:59]
    low_lip = np.concatenate((low_lip, shape[65:68]))

    top_mean = np.mean(top_lip, axis=0)
    low_mean = np.mean(low_lip, axis=0)

    distance = abs(top_mean[1] - low_mean[1])
    return distance


ap = argparse.ArgumentParser()
ap.add_argument("-w", "--webcam", type=int, default=0,
                help="index of webcam on system")
args = vars(ap.parse_args())

EYE_AR_THRESH = 0.3
EYE_AR_CONSEC_FRAMES = 30
YAWN_THRESH = 8
alarm_status = False
alarm_status2 = False
saying = False
COUNTER = 0
YAWNCOUNTER=0
YAWN_AR_CONSEC_FRAMES = 20

print("-> Loading the predictor and detector...")
#detector = dlib.get_frontal_face_detector()
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")    #Faster but less accurate
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')


print("-> Starting Video Stream")
vs = VideoStream(src=args["webcam"]).start()
#vs= VideoStream(usePiCamera=True).start()       //For Raspberry Pi
time.sleep(1.0)

while True:

    frame = vs.read()
    frame = imutils.resize(frame, width=450)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #rects =:
    rects = detector.detectMultiScale(gray, scaleFactor=1.1, 
	minNeighbors=5, minSize=(30, 30),
	flags=cv2.CASCADE_SCALE_IMAGE)

    #for rect in rects:
    for (x, y, w, h) in rects:
        rect = dlib.rectangle(int(x), int(y), int(x + w),int(y + h))
        
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)

        eye = final_ear(shape)
        ear = eye[0]
        leftEye = eye [1]
        rightEye = eye[2]

        distance = lip_distance(shape)

        leftEyeHull = cv2.convexHull(leftEye)
        rightEyeHull = cv2.convexHull(rightEye)
        cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
        cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)

        lip = shape[48:60]
        cv2.drawContours(frame, [lip], -1, (0, 255, 0), 1)

        if ear < EYE_AR_THRESH:
            COUNTER += 1
            print("Drowsiness count "+str(COUNTER))
            if COUNTER >= EYE_AR_CONSEC_FRAMES:
                if alarm_status == False:
                    alarm_status = True
                    #t = Thread(target=alarm, args=('wake up sir',))
                    #t.deamon = True
                    #t.start()
                    CallAudio("Wake up")
                    PlayAudio("Buzzersound.mp3")
                    

                cv2.putText(frame, "DROWSINESS ALERT!", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                cv2.imwrite('./image.jpg',frame)
                mail()
                COUNTER = 0

        else:
            COUNTER = 0
            alarm_status = False

        if (distance > YAWN_THRESH):
                YAWNCOUNTER+=1
                print("Yawn count "+str(YAWNCOUNTER))
                if YAWNCOUNTER >= YAWN_AR_CONSEC_FRAMES:
                    cv2.putText(frame, "Yawn Alert", (10, 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                    if alarm_status2 == False and saying == False:
                        alarm_status2 = True
                        #t = Thread(target=alarm, args=('take some fresh air sir',))
                        #t.deamon = True
                        #t.start()
                        cv2.imwrite('./image1.jpg',frame)
                        CallAudio("Wake up yawning detected")
                        mail()
                        YAWNCOUNTER=0
        else:
            YAWNCOUNTER=0
            alarm_status2 = False

        cv2.putText(frame, "EAR: {:.2f}".format(ear), (300, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        cv2.putText(frame, "YAWN: {:.2f}".format(distance), (300, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)


    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

cv2.destroyAllWindows()
vs.stop()