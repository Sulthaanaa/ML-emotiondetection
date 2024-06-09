import cv2
import numpy as np
from keras.models import load_model
from keras.preprocessing.image import img_to_array
import tkinter as tk
from PIL import Image, ImageTk

class FaceScanner:
    def __init__(self, master):
        self.master = master
        self.master.title("Emotion Detection")

        # Load Haar Cascade classifier for face detection
        self.face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        # Load emotion detection model
        self.classifier = load_model('./Emotion_Detection.h5')
        self.class_labels = ['Angry', 'Happy', 'Neutral', 'Sad', 'Surprise']

        # Create a canvas to display the webcam feed
        self.canvas = tk.Canvas(master, width=640, height=480)
        self.canvas.pack()

        # Initialize video capture
        self.cap = cv2.VideoCapture(0)

        # Start updating the canvas
        self.update()

    def update(self):
        # Read a frame from the video capture
        ret, frame = self.cap.read()
        if ret:
            # Convert the frame from BGR to RGB format
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Detect faces in the frame
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_classifier.detectMultiScale(gray, 1.3, 5)

            # Draw rectangles around the faces and display emotion labels
            for (x, y, w, h) in faces:
                roi_gray = gray[y:y + h, x:x + w]
                roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)

                if np.sum([roi_gray]) != 0:
                    roi = roi_gray.astype('float') / 255.0
                    roi = img_to_array(roi)
                    roi = np.expand_dims(roi, axis=0)

                    # Make a prediction on the ROI, then lookup the class
                    preds = self.classifier.predict(roi)[0]
                    label = self.class_labels[preds.argmax()]

                    # Draw rectangle around the face
                    cv2.rectangle(frame_rgb, (x, y), (x + w, y + h), (255, 0, 0), 2)

                    # Display emotion label
                    cv2.putText(frame_rgb, label, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # Convert the frame to a format suitable for displaying in Tkinter
            img = Image.fromarray(frame_rgb)
            img = ImageTk.PhotoImage(image=img)

            # Update the canvas with the new frame
            self.canvas.create_image(0, 0, anchor=tk.NW, image=img)
            self.canvas.img = img

            # Repeat after 10 milliseconds
            self.master.after(10, self.update)

    def close_window(self):
        # Release video capture and close window
        self.cap.release()
        self.master.destroy()

def main():
    root = tk.Tk()
    app = FaceScanner(root)

    # Create another window or perform any other operations here

    # Set close button to stop capturing and close window
    close_button = tk.Button(root, text="Close", command=app.close_window)
    close_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
