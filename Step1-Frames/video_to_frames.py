import cv2
import csv
import os
import sys
import shutil
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

try:
    videoName = sys.argv[1]
    outputPath = sys.argv[2]
    if (not videoName) or (not outputPath):
        raise ValueError("Missing command-line arguments")
except Exception as e:
    logging.error(f"Error: {e}")
    logging.info('Usage: python3 Frame_Generator.py <videoPath> <outputFolder>')
    exit(1)

# Check and create output folder
if outputPath[-1] != '/':
    outputPath += '/'

try:
    if os.path.exists(outputPath):
        shutil.rmtree(outputPath)
    os.makedirs(outputPath)
    logging.info(f"Created output folder: {outputPath}")
except Exception as e:
    logging.error(f"Error creating output folder: {e}")
    exit(1)

# Segment the video into frames
cap = cv2.VideoCapture(videoName)
success, count = True, 0
try:
    success, image = cap.read()
    while success:
        cv2.imwrite(outputPath + '%d.png' % (count), image)
        count += 1
        success, image = cap.read()
    logging.info(f"Segmented video into {count} frames")
except Exception as e:
    logging.error(f"Error segmenting video: {e}")
