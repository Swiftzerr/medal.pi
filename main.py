import cv2
import os.path
from threading import Thread, Event
from vidgear.gears import WriteGear
import time
import numpy
from time import gmtime, strftime

# START CONFIG

clip_length = 30  # The clip length in seconds

file_path = "/Users/admin/Desktop/clips/"  # The folder where the clips will be saved

# END CONFIG


webcam = cv2.VideoCapture(0)
cam_fps = webcam.get(cv2.CAP_PROP_FPS)
cam_width = webcam.get(cv2.CAP_PROP_FRAME_WIDTH)
cam_height = webcam.get(cv2.CAP_PROP_FRAME_HEIGHT)
Frames = []


def save_clip():
    da_frames = Frames
    print("Starting clipping")
    if not os.path.isdir(file_path):
        os.mkdir(file_path)
    output_params = {"-vcodec": "libx264", "-crf": 0, "-preset": "fast"}
    writer = WriteGear(output_filename='output.mp4', logging=True, **output_params)
    for Frame in da_frames:
        writer.write(Frame)
    print("Done clipping")
    writer.close()


def webcam_loop(Frames):
    while True:
        result, cur_frame = webcam.read()
        Frames.append(cur_frame)
        if event.is_set(): break

event = Event()
cam_thread = Thread(target=webcam_loop, args=(Frames, ))
cam_thread.start()

print("Medal.pi is running. Press enter to clip")
while True:
    input("")
    save_clip()
    output_file = cv2.VideoWriter((file_path + "clip-" + str(os.listdir(file_path))), cv2.VideoWriter_fourcc(*'MP4V'), cam_fps, (int(cam_width),int(cam_height)))
