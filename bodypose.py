import cv2  ## pip install opencv-contrib-python
from ursina import *  ## pip install ursina
import mediapipe as mp  ## pip install mediapipe


class poseDetector():

    def __init__(self, mode=False, upBody=False, smooth=True,
                 detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.upBody = upBody
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose


# Here Choose video (0 for webcam or choose Your own file):
# cap = cv2.VideoCapture("C://video//breakdance.mp4")
cap = cv2.VideoCapture(0)

spd = 10
app = Ursina()

nose = Entity(model='sphere', color=color.blue, scale_x=0.5, scale_y=0.5, scale_z=0.5)
left_shoulder = Entity(model='sphere', color=color.red, scale_x=0.5, scale_y=0.5, scale_z=0.5)
right_shoulder = Entity(model='sphere', color=color.red, scale_x=0.5, scale_y=0.5, scale_z=0.5)

left_elbow = Entity(model='sphere', color=color.red, scale_x=0.5, scale_y=0.5, scale_z=0.5)
right_elbow = Entity(model='sphere', color=color.red, scale_x=0.5, scale_y=0.5, scale_z=0.5)

left_wrist = Entity(model='sphere', color=color.red, scale_x=0.5, scale_y=0.5, scale_z=0.5)
right_wrist = Entity(model='sphere', color=color.red, scale_x=0.5, scale_y=0.5, scale_z=0.5)

left_hip = Entity(model='sphere', color=color.red, scale_x=0.5, scale_y=0.5, scale_z=0.5)
right_hip = Entity(model='sphere', color=color.red, scale_x=0.5, scale_y=0.5, scale_z=0.5)

left_knee = Entity(model='sphere', color=color.red, scale_x=0.5, scale_y=0.5, scale_z=0.5)
right_knee = Entity(model='sphere', color=color.red, scale_x=0.5, scale_y=0.5, scale_z=0.5)

left_ankle = Entity(model='sphere', color=color.red, scale_x=0.5, scale_y=0.5, scale_z=0.5)
right_ankle = Entity(model='sphere', color=color.red, scale_x=0.5, scale_y=0.5, scale_z=0.5)

EditorCamera()
Sky()

EditorCamera(rotation=(0, 180, 0))

detector = poseDetector()


def update():
    success, img = cap.read()


    camera_control()


def camera_control():
    camera.z += held_keys["w"] * spd * time.dt
    camera.z -= held_keys["s"] * spd * time.dt
    camera.x += held_keys["d"] * spd * time.dt
    camera.x -= held_keys["a"] * spd * time.dt
    camera.y += held_keys["e"] * spd * time.dt
    camera.y -= held_keys["q"] * spd * time.dt


window.fullscreen_resolution = (640, 480)

window.screen_resolution = (300, 300)
window.center_on_screen = True
window.fullscreen = False
window.fps_counter.enabled = True

app.run()
