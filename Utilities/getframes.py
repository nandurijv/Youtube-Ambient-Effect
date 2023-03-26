import pandas as pd
import numpy as np
import cv2
import matplotlib.pyplot as plt
from glob import glob
import os
#read the input video
cap = cv2.VideoCapture('./TestData/demo.mp4')

#printing meta data of the video
print("META DATA: ")

#print the frames available
print(f'FRAMES AVAILABLE: {cap.get(cv2.CAP_PROP_FRAME_COUNT)}')
print()
#print the height and width available
print(f'HEIGHT : {cap.get(cv2.CAP_PROP_FRAME_HEIGHT)}')
print(f'WIDTH : {cap.get(cv2.CAP_PROP_FRAME_WIDTH)}')
print()
#print the frames available
print(f'FPS(FRAMES PER SECOND): {cap.get(cv2.CAP_PROP_FPS):0.2f}')

#stop the file from being used.
cap.release()

#display multiple frames from the video
def read_frames(vid_path,frame_factor):
    # Open the video file
    cap = cv2.VideoCapture(vid_path)

    # Check if the video file was opened successfully
    if not cap.isOpened():
        print("Error opening video file")

    # Read and display each frame of the video
    img_idx = -1
    while img_idx!=cap.get(cv2.CAP_PROP_FRAME_COUNT):
        # Capture a frame from the video
        ret, frame = cap.read()
        img_idx += 1
        # If frame is read correctly, ret is True
        if ret and img_idx%(int(cap.get(cv2.CAP_PROP_FPS)*frame_factor)) == 0:
            print(img_idx)
            # Display the frame
            cv2.imshow('frame', frame)

            out_path = "./TestData/Frames"
            frame_name = 'Frame'+str(img_idx)+'.jpg'
            cv2.imwrite(os.path.join(out_path, frame_name), frame)

            # Wait for 25 milliseconds and check if the user wants to quit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            print(img_idx)
            continue

    # Release the video capture object and close all windows
    cap.release()
    cv2.destroyAllWindows()