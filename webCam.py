#!/usr/bin/env python
'''
This module takes image from the webcam and compares it with
the image taken during setup.
'''
import cv2
import face_recognition

def image_matching(temp_image):
    '''
    Records the image from the camera and process every frame to
    find a match with the temp image if the image matches then
    returns true as the value otherwise waits for the q key to
    exit the video capture.
    '''
    video_capture = cv2.VideoCapture(0)
    image = face_recognition.load_image_file(temp_image)
    temp_face_encoding = face_recognition.face_encodings(image)[0]
    face_locations = []
    face_encodings = []
    process_this_frame = True
    while True:
        ret, frame = video_capture.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        if process_this_frame:
            face_locations = face_recognition.face_locations(small_frame)
            face_encodings = face_recognition.face_encodings(small_frame, face_locations)
            for face_encoding in face_encodings:
                match = face_recognition.compare_faces([temp_face_encoding], face_encoding,
                                                       tolerance = 0.4)
                if match[0]:
                    return True
        process_this_frame = not process_this_frame
        cv2.imshow('Video', frame)
        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video_capture.release()
    cv2.destroyAllWindows()
