from djitellopy import tello
import cv2
from cvzone.cvzone import FaceDetectionModule

detector = FaceDetectionModule()
drone=tello.Tello()

drone.connect()
drone.streamon()
drone.takeoff()
drone.move_up(80)

while True:
    img = drone.get_frame_read()
    img, bbox = detector.findFaces(img, draw=True)
    cv2.imshow("image", img)
    drone.rotate_clockwise(45)
    drone.move_forward(50)
    if cv2.waitKey(5) & 0xFF == ord('q'):
      break
drone.land()

