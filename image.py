import cv2
import os
import time

def capture_and_save_image(output_dir):
    # Access the camera
    cap = cv2.VideoCapture(0)

    # Check if the camera is opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera")
        return

    # Increase camera exposure (optional)
    cap.set(cv2.CAP_PROP_EXPOSURE, 0.1)  # You can adjust the exposure value (0.1 - 1.0) based on your environment

    # Capture an image
    ret, frame = cap.read()

    # Check if the image is captured successfully
    if not ret:
        print("Error: Failed to capture image")
        return

    # Generate a unique filename based on the current timestamp
    filename = f"captured_image_{int(time.time())}.jpg"

    # Construct the full path to save the image
    filepath = os.path.join(output_dir, filename)

    # Save the captured image
    cv2.imwrite(filepath, frame)

    # Release the camera
    cap.release()

    print(f"Image captured and saved as {filepath}")

if __name__ == "__main__":
    # Define the output directory
    output_directory = "/Users/churnika/Desktop/Projects/fall_detection/fall_dataset/present"

    # Ensure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Capture and save an image every two minutes
    while True:
        capture_and_save_image(output_directory)
        time.sleep(120)  # Sleep for 2 minutes (120 seconds)
