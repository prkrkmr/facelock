from subprocess import Popen
import face_recognition
import cv2

def image_matching(temp_image):
    video_capture = cv2.VideoCapture(0)
    image = face_recognition.load_image_file(temp_image)
    a_face_encoding = face_recognition.face_encodings(image)[0]
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True
    while True:
        ret, frame = video_capture.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        if process_this_frame:
            face_locations = face_recognition.face_locations(small_frame)
            face_encodings = face_recognition.face_encodings(small_frame, face_locations)
            face_names = []
            for face_encoding in face_encodings:
                match = face_recognition.compare_faces([a_face_encoding], face_encoding,
                                                       tolerance = 0.4)
                name = "Unknown"
                if match[0]:
                    return True
                face_names.append(name)
        process_this_frame = not process_this_frame
        cv2.imshow('Video', frame)
        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video_capture.release()
    cv2.destroyAllWindows()
