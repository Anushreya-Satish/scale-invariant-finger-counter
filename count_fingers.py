"""
Real-Time Hand Landmark Tracking and Finger Counter Application.
Powered by OpenCV and MediaPipe.
"""

import cv2
import mediapipe as mp
import math

def count_fingers(image, hand_landmarks, tip_ids, hand_no=0):
    """
    Calculates the number of extended fingers based on hand landmark coordinates.
    Uses distance-based scaling for the thumb to ensure scale-invariance.
    """
    if not hand_landmarks:
        return

    h, w, _ = image.shape
    landmarks = hand_landmarks[hand_no].landmark
    fingers = []
    
    # Thumb Detection (Distance-Based Ratio)
    thumb_tip = (int(landmarks[4].x * w), int(landmarks[4].y * h))
    pinky_base = (int(landmarks[17].x * w), int(landmarks[17].y * h))
    knuckle_5 = (int(landmarks[5].x * w), int(landmarks[5].y * h))
    
    thumb_to_pinky_dist = math.sqrt((thumb_tip[0] - pinky_base[0])**2 + (thumb_tip[1] - pinky_base[1])**2)
    palm_width = math.sqrt((knuckle_5[0] - pinky_base[0])**2 + (knuckle_5[1] - pinky_base[1])**2)
    
    # Scale factor threshold for an extended thumb
    if thumb_to_pinky_dist > (palm_width * 1.1):
        fingers.append(1)
    else:
        fingers.append(0)
        
    # Remaining 4 Fingers Detection (Vertical Knuckle Comparison)
    for lm_index in tip_ids[1:]:
        finger_tip_y = landmarks[lm_index].y
        finger_base_y = landmarks[lm_index - 2].y
        
        if finger_tip_y < finger_base_y:
            fingers.append(1)   
        else:
            fingers.append(0)   
            
    total_fingers = fingers.count(1)
    
    # Render the dynamic text overlay
    cv2.putText(
        image, 
        f'Total fingers: {total_fingers}', 
        (50, 50), 
        cv2.FONT_HERSHEY_SIMPLEX, 
        1, 
        (255, 0, 0), 
        2
    ) 

def main():
    """Main execution loop for capturing video frames and processing hand data."""
    cap = cv2.VideoCapture(0)

    mp_hands = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils
    hands = mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5)

    # MediaPipe Landmark IDs for finger tips
    tip_ids = [4, 8, 12, 16, 20]

    while True:
        success, image = cap.read()
        if not success:
            continue

        image = cv2.flip(image, 1)
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_image)

        if results.multi_hand_landmarks:
            for hand_lms in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(image, hand_lms, mp_hands.HAND_CONNECTIONS)
            
            count_fingers(image, results.multi_hand_landmarks, tip_ids)

        cv2.imshow("Media Controller", image)

        # Exit safely when Spacebar (ASCII 32) is pressed
        if cv2.waitKey(1) == 32:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()