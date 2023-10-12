# extract text from live video

from pytesseract import pytesseract
import cv2

# open video to capture video
video = cv2.VideoCapture(0)

if not video.isOpened():
    print("Error Capturing video")
    exit()


# set video frames
video.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
video.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# read frame from video
while True:
    # current frame
    ret, frame = video.read()

    # c check frame successfully captured
    if ret:
        # convert frame to gray scale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # perform OCR on the grayscale frame
        text = pytesseract.image_to_string(gray_frame)
        print(text)
        cv2.imshow('live video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        print("frame not read")
        break

video.release()
cv2.destroyAllWindows()
