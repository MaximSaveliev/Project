from video_detector import *
import os

def main():
    rootDirectory = os.path.dirname(__file__)
    
    videoPath = os.path.join(rootDirectory, "videos", "C:\\Users\\Max\\Downloads\\videos\\Running - 294.mp4")
    configPath = os.path.join(rootDirectory, "data", "ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt")
    modelPath = os.path.join(rootDirectory, "data", "frozen_inference_graph.pb")
    classesPath = os.path.join(rootDirectory, "data", "coco.names")

    detector = Detector(videoPath, configPath, modelPath, classesPath)
    detector.onVideo()

if __name__== '__main__':
    main()