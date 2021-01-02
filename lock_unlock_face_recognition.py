import cv2
import sys
import numpy as np
import pyautogui
import ctypes
import os
import datetime
import time
from PIL import Image 
# import datetime
def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)
        
counter_correct = 0  #counter variable to count number of times loop runs
counter_wrong = 0

now = datetime.datetime.now()  #extract current time     
now = now.second        #we need only seconds

recognizer = cv2.face.LBPHFaceRecognizer_create()

assure_path_exists("F:/LockUnlock/lock/trainer/")

recognizer.read('F:/LockUnlock/lock/trainer/trainer.yml')  #load training model

cascadePath = "F:/LockUnlock/lock/haarcascade_frontalface_default.xml"  #cascade path

faceCascade = cv2.CascadeClassifier(cascadePath);  #load cascade

font = cv2.FONT_HERSHEY_COMPLEX_SMALL  # Set the font style

# cam = cv2.VideoCapture(0)
cam=cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    
    now1 = datetime.datetime.now()          #program will lock station after 5 seconds if it doesn't see any faces.
    now1 = now1.second
    if(now1 > now + 8):
        cam.release()
        cv2.destroyAllWindows()
        ctypes.windll.user32.LockWorkStation()
        sys.exit()

    ret, im =cam.read()
    temp=im
    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray, 1.3,5)

    for(x,y,w,h) in faces:

        cv2.rectangle(im, (x-20,y-20), (x+w+20,y+h+20), (0,255,0), 4)       

        Id, confidence = recognizer.predict(gray[y:y+h,x:x+w])   # Recognize the face belongs to which ID

        #if(Id == 1):    # Check the ID if exist 
         #   Id = "{0:.2f}%".format(round(100 - confidence, 2)) 
 
        if(confidence>60):                 #confidence usually comes greater than 80 for strangers
            counter_wrong += 1
            print("Wrong")
            Id = "Unknown + {0:.2f}%".format(round(100 - confidence, 2)) 
            print(confidence)
            print("counter_wrong - " + str(counter_wrong))
            cv2.rectangle(im, (x-22,y-90), (x+w+22, y-22), (0,0,255), -1)
            cv2.putText(im, str(Id), (x,y-40), font, 1, (0,0,0), 2)
        else:                              #confidence usually comes less than 80 for correct user(s)
            Id = "Risha + {0:.2f}%".format(round(100 - confidence, 2)) 
            print("Verified")
            print(confidence)
            counter_correct += 1
            print("counter_correct - " + str(counter_correct))
            cv2.rectangle(im, (x-22,y-90), (x+w+22, y-22), (255,255,255), -1)
            cv2.putText(im, str(Id), (x,y-40), font, 1, (0,0,0), 2)

                
        if(counter_wrong == 3):
            # pyautogui.moveTo(48,748)
            # pyautogui.click(48,748)
            cv2.imwrite("stranger/temp.png",temp)
            pyautogui.alert('Hello Stranger!!! The System is being locked....!',timeout=3000)
            # pyautogui.typewrite("Hello Stranger!!! Whats Up.")
            # time.sleep(3)
            # pyautogui.moveTo(778,440,duration=3)
            # pyautogui.PAUSE(3)
            # pyautogui.click(778,440,clicks=2)
            cam.release()
            del(cam)
            cv2.destroyAllWindows()
            ctypes.windll.user32.LockWorkStation()
            sys.exit()


        if(counter_correct == 6):    #if counter = 6 then program will terminate as it has recognized correct user for 6 times. 
            # add=os.getcwd()
            # print(add)
            
            if (os.path.exists('F:/LockUnlock/stranger/temp.png')):
                ans=pyautogui.confirm('A Stranger tried to enter into the System..\nDo you want to see or delete?', buttons=['See', 'Delete'])
                if ans=='See':
                    stranger=cv2.imread('F:/LockUnlock/stranger/temp.png')
                    cv2.imshow('Stranger', stranger)
                    cv2.waitKey()
                    home = os.path.expanduser('~')
                    print(home)
                    directory=os.path.join(home,'Pictures\Stranger')
                    print(directory)
                    if not os.path.exists(directory):
                        os.makedirs(directory)
                    m1 = Image.open("F:/LockUnlock/stranger/temp.png")  
                    now=datetime.datetime.now().strftime("%Hhrs-%Mmin-%Ssec")
                    pic="Time-"+str(now)+".png"
                    directory=os.path.join(directory,pic)
                    print(directory)
                    m1.save(directory) 
                    os.remove('F:/LockUnlock/stranger/temp.png')
                else:
                    os.remove('F:/LockUnlock/stranger/temp.png') 
            cam.release()
            del(cam)
            cv2.destroyAllWindows()           
            sys.exit()

    cv2.imshow('Webcam',im) 

    if cv2.waitKey(10) & 0xFF == ord('*'):      # If '*' is pressed, terminate the  program
        break

cam.release()

cv2.destroyAllWindows()
# os.remove(cv2)
