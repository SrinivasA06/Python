import cv2
import numpy as np
import math
import pyttsx3
import os

# Load the YOLOv3 object detection model and its configuration files
config_file = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
frozen_model = 'frozen_inference_graph.pb'
net = cv2.dnn_DetectionModel(frozen_model, config_file)

# Load the class labels for the model
classes = []
file_name = 'coco.txt'
with open(file_name, 'rt') as fpt:
    classes = fpt.read().rstrip('\n').split('\n')

# Set up text-to-speech engine
engine = pyttsx3.init()

# Set up the video capture
cap = cv2.VideoCapture(0)
print(cap)

# Set the threshold distance for object detection
threshold = 100

while True:
    # Read a frame from the video input
    success, frame = cap.read()
    
    # Convert the frame to a blob for input to the model
    blob = cv2.dnn.blobFromImage(frame, 1/255.0, (416, 416), [0,0,0],1, crop=False)
    # Set the input for the model and perform a forward pass
    
    layerNames = net.getLayerNames()
    outputNames = [layerNames[i-1] for i in net.getUnconnectedOutLayers()]
    outputs = net.forward(outputNames)
    
    #outs = net.forward(net.getUnconnectedOutLayersNames())
    
    # Loop over the output detections and draw bounding boxes on the frame
    for out in outputs:
        for det in out:
            scores = det[5:]
            
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            
            if confidence > 0.5:
                center_x = int(det[0] * frame.shape[1])
                center_y = int(det[1] * frame.shape[0])
                width = int(det[2] * frame.shape[1])
                height = int(det[3] * frame.shape[0])
                left = int(center_x - width/2)
                top = int(center_y - height/2)
                
    

                # Draw the bounding box on the frame
                cv2.rectangle(frame, (left, top),(left+width, top+height), (255, 0, 0), 2)
                cv2.putText(frame, classes[class_id], (left, top-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)
                # Calculate the distance to the object
                distance = math.sqrt((center_x - frame.shape[1]/2)**2 + (center_y - frame.shape[0]/2)**2)
                print(distance)
                # Speak a distance alert if the object is close enough
                if distance < threshold:
                    print("voice")
                    engine.say(f"{classes[class_id]} at {int(distance)} centimeters.")
                    engine.runAndWait()

    # Display the resulting frame
    cv2.imshow("Output", frame)
    #print("Image displayed successfully")

    # Exit if the user presses the "q" key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()
