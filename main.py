import threading

from ursina import *
import time
import cv2
import mediapipe


def CalcLandMarks():
    ret, img = cap.read()
    rgbImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(rgbImg)  # results is a list of Hand objects
    # print(results.multi_hand_landmarks) # This will show the landmarks of all hands

    all_hands = []
    if results.multi_hand_landmarks:  # if results is not empty
        new_hand = []
        for hand in results.multi_hand_landmarks:  # For each hand in result
            new_hand = []
            for id, lm in enumerate(hand.landmark):  # For each landmark in hand
                hand_marks = [id, lm.x, lm.y, lm.z]
                new_hand.append(hand_marks)  # Append the landmark to new_hand

                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print(cx, cy)
                # new_hand_mk = [id, cx, cy]
                # new_hand.append(new_hand_mk)

                if id == 4: cv2.circle(img, (cx, cy), 10, (0, 255, 255), -1)
                if id == 8: cv2.circle(img, (cx, cy), 15, (0, 0, 255), -1)
                if id == 12: cv2.circle(img, (cx, cy), 15, (255, 0, 0), -1)
                if id == 16: cv2.circle(img, (cx, cy), 10, (0, 255, 0), -1)
                if id == 20: cv2.circle(img, (cx, cy), 10, (255, 255, 0), -1)

            mpDraw.draw_landmarks(img, hand, mpHands.HAND_CONNECTIONS)  # Draw the landmarks
            all_hands.append(new_hand)  # Append the new_hand to all_hands

            # print("Hand : ", new_hand)

    img = cv2.flip(img, 1)  # Flip the frame horizontally
    img = cv2.resize(img, (640, 480))  # increase frame size
    cv2.imshow('frame', img)  # Show the frame

    return all_hands


def PlotHand():
    all_hands = CalcLandMarks()  # Calculate landmarks for all hands

    for new_hand in all_hands:
        for hand_mk in new_hand:
            # using if is 10x faster than using other method (new_hand[3][1], new_hand[4][1])
            pass


def update():
    # player.position = mouse.position
    # player.x = mouse.x
    player.x += held_keys['d'] * 0.1
    player.x -= held_keys['a'] * 0.1
    player.y += held_keys['e'] * 0.1
    player.y -= held_keys['q'] * 0.1
    player.z += held_keys['w'] * 0.1
    player.z -= held_keys['s'] * 0.1

    player.rotation_x += held_keys['r'] * 5
    player.rotation_y += held_keys['f'] * 5
    player.rotation_z += held_keys['t'] * 5

    # cube.rotation_x += 0.25
    # cube.rotation_y += 0.25

def run_ursin():
    update()

def run_cv():
    print("New calculation\n\n")
    count = 0
    t = time.time()

    PlotHand()  # In here Hands are extracted from CalcLandMarks() and plotted.

    time_diff = time.time() - t
    count += 1
    time_avg = time_diff / count
    print("Time taken : ", time_diff)
    print("Average time taken : ", time_avg)


if __name__ == '__main__':

    app = Ursina()
    # cube = Entity(model='cube', scale=2, color=color.red)
    # player = Entity(model='cube', scale=2, color=color.green)
    player = Entity(model='Objects/dragon.obj', scale=2, color=color.green)

    cap = cv2.VideoCapture(0)

    mpHands = mediapipe.solutions.hands
    hands = mpHands.Hands()
    mpDraw = mediapipe.solutions.drawing_utils  # For drawing landmarks

    # create thread
    #th1 = threading.Thread(target=run_ursin, args=(10,))
    #th2 = threading.Thread(target=run_cv, args=(10,))

    # start thread
    ##th1.start()
    #th2.start()

    app.run()

    while True:

        # wait for thread to finish
        #.join()
        #th2.join()

        # run_ursin()
        run_cv()

        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press q to quit
            break





    cap.release()
    cv2.destroyAllWindows()



