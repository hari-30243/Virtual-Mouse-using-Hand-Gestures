import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import time

# -------------------- CONFIG --------------------
pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0

SCREEN_W, SCREEN_H = pyautogui.size()
CLICK_COOLDOWN = 1.0
SCROLL_SPEED = 2
DEADZONE = 5
# ------------------------------------------------

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

prev_x, prev_y = 0, 0
last_click_time = 0

cv2.namedWindow("Gesture Control", cv2.WINDOW_NORMAL)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    finger_count = 0

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            lm = hand_landmarks.landmark

            # Count fingers (ignore thumb)
            for tip in [8, 12, 16, 20]:
                if lm[tip].y < lm[tip - 2].y:
                    finger_count += 1

            ix, iy = int(lm[8].x * w), int(lm[8].y * h)
            mx, my = int(lm[12].x * w), int(lm[12].y * h)

            # -------- MOVE MOUSE --------
            if finger_count == 1:
                sx = np.interp(ix, [0, w], [0, SCREEN_W])
                sy = np.interp(iy, [0, h], [0, SCREEN_H])
                pyautogui.moveTo(sx, sy)
                cv2.putText(frame, "MOVE", (30, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # -------- SCROLL UP / DOWN --------
            elif finger_count == 2:
                dy = iy - prev_y
                if abs(dy) > DEADZONE:
                    pyautogui.scroll(int(-dy * SCROLL_SPEED))
                cv2.putText(frame, "SCROLL V", (30, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

            # -------- SCROLL LEFT / RIGHT --------
            elif finger_count == 3:
                dx = ix - prev_x
                if abs(dx) > DEADZONE:
                    pyautogui.hscroll(int(dx * SCROLL_SPEED))
                cv2.putText(frame, "SCROLL H", (30, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

            # -------- STOP --------
            elif finger_count == 0:
                cv2.putText(frame, "STOP", (30, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            # -------- CLICK --------
            dist = np.hypot(ix - mx, iy - my)
            if dist < 30 and time.time() - last_click_time > CLICK_COOLDOWN:
                pyautogui.click()
                last_click_time = time.time()
                cv2.putText(frame, "CLICK", (30, 100),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)

            prev_x, prev_y = ix, iy

    cv2.imshow("Gesture Control", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
