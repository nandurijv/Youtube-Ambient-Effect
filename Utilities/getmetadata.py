import cv2

def get_meta_data(vid_path):
    print(vid_path)
    #read the input video
    cap = cv2.VideoCapture(vid_path)

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
    FPS = cap.get(cv2.CAP_PROP_FPS)
    n_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    #stop the file from being used.
    cap.release()

    return [int(n_frames),int(FPS*2)]
