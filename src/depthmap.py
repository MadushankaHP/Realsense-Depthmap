#!/usr/bin/env python3

import pyrealsense2 as rs 
import numpy as np 
import cv2 
import math
import rospy

refPt = np.zeros(2)
click = False


def mouse_cb(event, x, y, flags, param):
    global refPt ,click
    if event == cv2.EVENT_LBUTTONDOWN:
        click = True
        refPt[0] = x
        refPt[1] = y
        
    elif event == cv2.EVENT_LBUTTONUP:
        click = False
        

def depth_cal(refPt):
    node = rospy.init_node("camera_node",anonymous=True);
    pipe = rs.pipeline()
    cfg = rs.config()

    cfg.enable_stream(rs.stream.color,640,480,rs.format.bgr8,30)
    cfg.enable_stream(rs.stream.depth,640,480,rs.format.z16,30)

    pipe.start(cfg)

    pc = rs.pointcloud()
    points = rs.points()
    decimate = rs.decimation_filter()
    colorizer = rs.colorizer()


    cv2.namedWindow('rgb')
    cv2.setMouseCallback('rgb', mouse_cb)


    while not rospy.is_shutdown():
        frame = pipe.wait_for_frames()
        depth_frame = frame.get_depth_frame()
        color_frame = frame.get_color_frame()
        

        depth_image = np.asanyarray(depth_frame.get_data())
        color_image = np.asanyarray(color_frame.get_data())
        #print(type(depth_image))
        
        depth_image2 = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)
        
        color_intrin = frame.profile.as_video_stream_profile().intrinsics 
        x_1 = int(refPt[0])
        y_1 = int(refPt[1])
        
        depth = depth_frame.get_distance(x_1, y_1)
        dx ,dy, dz = rs.rs2_deproject_pixel_to_point(color_intrin, [refPt[0],refPt[1]], depth)
        distance = math.sqrt(((dx)**2) + ((dy)**2) + ((dz)**2)) 
        pt_data = "x = " + str(round(dx, 2)) + "m " + "y = " + str(round(dx, 2)) + "m "+"z = " + str(round(dx, 2)) + "m " + "distance = " + str(round(distance, 2))+"m" 
        #print(pt_data)
        cv2.imwrite('./depth_5.png',depth_image)
        np.save('./depth_6.npy',depth_image)
        cv2.imshow('rgb', color_image)
        cv2.imshow('depth1',depth_image)
        cv2.imshow('depth2',depth_image2)

     <include file="$(find jetbot_slam)/launch/drive.launch" />y(1) == ord('q'):
     <include file="$(find jetbot_slam)/launch/drive.launch" />
     <include file="$(find jetbot_slam)/launch/drive.launch" />
     <include file="$(find jetbot_slam)/launch/drive.launch" />
    
if __name__ == "__main__":
    try:
        depth_cal(refPt)
        
    except:
        #rospy.logerr(e);
        print('Error')
        pass;
        