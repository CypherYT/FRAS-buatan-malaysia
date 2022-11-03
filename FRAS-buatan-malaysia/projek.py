import face_recognition
import cv2
import numpy as np
import csv
import os
from datetime import datetime
from colorama import Fore, Back, Style


kelas = input(Fore.LIGHTYELLOW_EX+' Enter Class/Meeting Name:'+Style.RESET_ALL)
print(Fore.GREEN+"Starting"+ Style.RESET_ALL)

#start video capture
video_capture = cv2.VideoCapture(0)
print(Back.GREEN+"Program Started!"+Style.RESET_ALL)


#source of photos(make sure to add students later just copy naqi_image and naqi_encoding into soemthing else)
naqi_image = face_recognition.load_image_file("photos/naqi.jpg")
naqi_encoding = face_recognition.face_encodings(naqi_image)[0]

amir_image = face_recognition.load_image_file("photos/amir.jpg")
amir_encoding = face_recognition.face_encodings(amir_image)[0]

anas_image = face_recognition.load_image_file("photos/anas.jpg")
anas_encoding = face_recognition.face_encodings(anas_image)[0]

cg1_image = face_recognition.load_image_file("photos/cg1.jpg")
cg1_encoding = face_recognition.face_encodings(cg1_image)[0]


fahim_image = face_recognition.load_image_file("photos/fahim.jpg")
fahim_encoding = face_recognition.face_encodings(fahim_image)[0]

hmzh_image = face_recognition.load_image_file("photos/hmzh.jpg")
hmzh_encoding = face_recognition.face_encodings(hmzh_image)[0]


known_face_encoding = [
    naqi_encoding,
    amir_encoding,
    anas_encoding,
    cg1_encoding,
    fahim_encoding,
    hmzh_encoding
    
]


known_faces_names = [
"Harith Anaqi Bin Mohd Hanafi ",
"Mohd. Amir Hadi Bin Mahrizal",
"Muhd Anas Lutfi",
"Hidayati Othman",
"Abdullah Fahim Bin Abdul Razak",
"Ahmad Hamzah bin Azrul"
]




students = known_faces_names.copy()

#listttttt
face_locations = []
face_encodings = []
face_names = []
s=True


#for date on csv
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")



#making a csv file with a writer class instance using open method
f =open(kelas + current_date+'.csv','w+',newline = '')
lnwriter = csv.writer(f)


#loop starts here
while True:
    #read to extract video data aka catch data from webcam
    _,frame = video_capture.read()
    print(Back.GREEN+"AI CURRENTLY RUNNING! PRESS Q TO EXIT AND SAVE DATA."+ Style.RESET_ALL)
    #resizes input from webcam(cv2 takes input from bgr format)
    small_frame = cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
    rgb_small_frame = small_frame[:,:,::-1]
    #s is true *as declared over line 31
    if s:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame,face_locations)
        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.face_distance(known_face_encoding,face_encoding)
            name=''
            face_distance = face_recognition.face_distance(known_face_encoding, face_encoding)
            #to get the best fit, we use np.argmin 
            best_match_index = np.argmin(face_distance)
            if matches[best_match_index]:
                name = known_faces_names[best_match_index]
                 

#appending face names in the csv file 
            face_names.append(name)
            if name in known_faces_names:
                if name in students:
                    #removing duplicates when multiple frames are taken
                    students.remove(name)
                    print(students)
                    current_time = now.strftime("%H:%M:%S")
                    lnwriter.writerow([name,current_time])


                    
#last touch adding a break to the loop i have created
#showing output to the user
    cv2.imshow("attendance system",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print(Back.BLUE+"FILE SAVED AS "+ kelas +" AT "+ current_time +". CSV file updated, Exiting Program!"+ Style.RESET_ALL )
        break


#release video capture
video_capture.release()
cv2.destroyAllWindows()
f.close()
