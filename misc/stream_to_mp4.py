# Grab training video from webcam
import cv2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--device","-d",help="device number",type=int,default=0)
parser.add_argument("--output","-o",help="output name"  ,type=str,default="output.mp4")
args = parser.parse_args()

cap = cv2.VideoCapture(args.device)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

frame_width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps          = 20.0 

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out    = cv2.VideoWriter(args.output, fourcc, fps, (frame_width, frame_height))

print("Recording... Press 'q' to stop.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to grab frame.")
        break
    out.write(frame)
    cv2.imshow('Recording', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

