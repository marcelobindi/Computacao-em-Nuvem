import cv2
import face_recognition

def capture_and_recognize():
    video_capture = cv2.VideoCapture(0)
    known_faces = [...]  # Carregar rostos conhecidos aqui

    while True:
        ret, frame = video_capture.read()
        rgb_frame = frame[:, :, ::-1]

        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_faces, face_encoding)

            if True in matches:
                print("Presença confirmada!")
                # Enviar dados para o servidor
                break

        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

capture_and_recognize()