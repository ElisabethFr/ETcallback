'''
this is a script that does a simple callback to tobii eyetracker for use in psychopy
streams the data directly to hdf5 file, while keeping the last value in memory

Version: 10/23/2023
author: Elisabeth Freund
Human Brain Mapping Lab at Feinstein Institutes for Medical Research
'''

'''
SETUP INFO:
    this script requires additional packages: tobii_research and h5py
    If you are using psychopy standalone, I recommend the following:
    Install miniconda3 and create an environment with the same Python version as your standalone.
    In that environment, run pip install tobii_research and pip install h5py
    in the environment folder under Lib>site-packages you will find the folders with the source code for the packages
    copy these folders to the Psychopy site-packages folder
'''

TESTNO = 1 # change this to a new number whenever you want to start a new test

from psychopy import core
import numpy as np
import tobii_research as tobii
import os
import h5py

def gaze_callback(gazedata):
#    cdata = np.empty((1,32))
    global cdata
    cdata[0,0] = gazedata._GazeData__device_time_stamp / 1000000
    cdata[0,1] = gazedata._GazeData__system_time_stamp / 1000000
    cdata[0,2] = gazedata._GazeData__left._EyeData__gaze_origin._GazeOrigin__position_in_track_box_coordinates[0]
    cdata[0,3] = gazedata._GazeData__left._EyeData__gaze_origin._GazeOrigin__position_in_track_box_coordinates[1]
    cdata[0,4] = gazedata._GazeData__left._EyeData__gaze_origin._GazeOrigin__position_in_track_box_coordinates[2]
    cdata[0,5] = gazedata._GazeData__left._EyeData__gaze_origin._GazeOrigin__position_in_user_coordinates[0]
    cdata[0,6] = gazedata._GazeData__left._EyeData__gaze_origin._GazeOrigin__position_in_user_coordinates[1]
    cdata[0,7] = gazedata._GazeData__left._EyeData__gaze_origin._GazeOrigin__position_in_user_coordinates[2]
    cdata[0,8] = gazedata._GazeData__left._EyeData__gaze_origin._GazeOrigin__validity
    cdata[0,9] = gazedata._GazeData__left._EyeData__gaze_point._GazePoint__position_in_user_coordinates[0]
    cdata[0,10] = gazedata._GazeData__left._EyeData__gaze_point._GazePoint__position_in_user_coordinates[1]
    cdata[0,11] = gazedata._GazeData__left._EyeData__gaze_point._GazePoint__position_in_user_coordinates[2]
    cdata[0,12] = gazedata._GazeData__left._EyeData__gaze_point._GazePoint__position_on_display_area[0]
    cdata[0,13] = gazedata._GazeData__left._EyeData__gaze_point._GazePoint__position_on_display_area[1]
    cdata[0,14] = gazedata._GazeData__left._EyeData__gaze_point._GazePoint__validity
    cdata[0,15] = gazedata._GazeData__left._EyeData__pupil_data._PupilData__diameter
    cdata[0,16] = gazedata._GazeData__left._EyeData__pupil_data._PupilData__validity
    cdata[0,17] = gazedata._GazeData__right._EyeData__gaze_origin._GazeOrigin__position_in_track_box_coordinates[0]
    cdata[0,18] = gazedata._GazeData__right._EyeData__gaze_origin._GazeOrigin__position_in_track_box_coordinates[1]
    cdata[0,19] = gazedata._GazeData__right._EyeData__gaze_origin._GazeOrigin__position_in_track_box_coordinates[2]
    cdata[0,20] = gazedata._GazeData__right._EyeData__gaze_origin._GazeOrigin__position_in_user_coordinates[0]
    cdata[0,21] = gazedata._GazeData__right._EyeData__gaze_origin._GazeOrigin__position_in_user_coordinates[1]
    cdata[0,22] = gazedata._GazeData__right._EyeData__gaze_origin._GazeOrigin__position_in_user_coordinates[2]
    cdata[0,23] = gazedata._GazeData__right._EyeData__gaze_origin._GazeOrigin__validity
    cdata[0,24] = gazedata._GazeData__right._EyeData__gaze_point._GazePoint__position_in_user_coordinates[0]
    cdata[0,25] = gazedata._GazeData__right._EyeData__gaze_point._GazePoint__position_in_user_coordinates[1]
    cdata[0,26] = gazedata._GazeData__right._EyeData__gaze_point._GazePoint__position_in_user_coordinates[2]
    cdata[0,27] = gazedata._GazeData__right._EyeData__gaze_point._GazePoint__position_on_display_area[0]
    cdata[0,28] = gazedata._GazeData__right._EyeData__gaze_point._GazePoint__position_on_display_area[1]
    cdata[0,29] = gazedata._GazeData__right._EyeData__gaze_point._GazePoint__validity
    cdata[0,30] = gazedata._GazeData__right._EyeData__pupil_data._PupilData__diameter
    cdata[0,31] = gazedata._GazeData__right._EyeData__pupil_data._PupilData__validity
    global ETdata
    ETdata.resize(ETdata.shape[0]+1,axis=0)
    ETdata[-1:,:] = cdata

eyetracker = tobii.find_all_eyetrackers()[0]

ETdataFilePath = 'C:\\Users\\lisaf\\Documents\\git\\ETcallback\\test\\test' + str(TESTNO) + '_eyetrackerData.h5'
# initiate data frame for eyetracker data

ETcolumns = [
    'deviceTimeStampInSec',
    'systemTimeStampInSec',
    'xLeftGazeOriginInTrackboxCoords',
    'yLeftGazeOriginInTrackboxCoords',
    'zLeftGazeOriginInTrackboxCoords',
    'xLeftGazeOriginInUserCoords',
    'yLeftGazeOriginInUserCoords',
    'zLeftGazeOriginInUserCoords',
    'leftGazeOriginValidity',
    'xLeftGazePositionInUserCoords',
    'yLeftGazePositionInUserCoords',
    'zLeftGazePositionInUserCoords',
    'xLeftGazePositionOnDisplay',
    'yLeftGazePositionOnDisplay',
    'leftGazePointValidity',
    'leftPupilDiameter',
    'leftPupilValidity',
    'xRightGazeOriginInTrackboxCoords',
    'yRightGazeOriginInTrackboxCoords',
    'zRightGazeOriginInTrackboxCoords',
    'xRightGazeOriginInUserCoords',
    'yRightGazeOriginInUserCoords',
    'zRightGazeOriginInUserCoords',
    'rightGazeOriginValidity',
    'xRightGazePositionInUserCoords',
    'yRightGazePositionInUserCoords',
    'zRightGazePositionInUserCoords',
    'xRightGazePositionOnDisplay',
    'yRightGazePositionOnDisplay',
    'rightGazePointValidity',
    'rightPupilDiameter',
    'rightPupilValidity'
    ]
#ETcolumns = 'deviceTimeStampInSec,systemTimeStampInSec,xLeftGazeOriginInTrackboxCoords,yLeftGazeOriginInTrackboxCoords,zLeftGazeOriginInTrackboxCoords,xLeftGazeOriginInUserCoords,yLeftGazeOriginInUserCoords,zLeftGazeOriginInUserCoords,leftGazeOriginValidity,xLeftGazePositionInUserCoords,yLeftGazePositionInUserCoords,zLeftGazePositionInUserCoords,xLeftGazePositionOnDisplay,yLeftGazePositionOnDisplay,leftGazePointValidity,leftPupilDiameter,leftPupilValidity,xRightGazeOriginInTrackboxCoords,yRightGazeOriginInTrackboxCoords,zRightGazeOriginInTrackboxCoords,xRightGazeOriginInUserCoords,yRightGazeOriginInUserCoords,zRightGazeOriginInUserCoords,rightGazeOriginValidity,xRightGazePositionInUserCoords,yRightGazePositionInUserCoords,zRightGazePositionInUserCoords,xRightGazePositionOnDisplay,yRightGazePositionOnDisplay,rightGazePointValidity,rightPupilDiameter,rightPupilValidity'
if os.path.isfile(ETdataFilePath):
    raise ValueError('eyetracker data file already exists! check what happened here!')
#ETdata = np.empty((0,32))

cdata = np.empty((1,32))
ETio = h5py.File(ETdataFilePath,'a')
ETdata = ETio.create_dataset(
    name='ETdata',
    shape=(0,32),
    maxshape=(None,32),
    dtype='float64'
    )
ETdata.attrs["headers"] = ETcolumns

eyetracker.subscribe_to(tobii.EYETRACKER_GAZE_DATA, gaze_callback)
core.wait(300)
eyetracker.unsubscribe_from(tobii.EYETRACKER_GAZE_DATA)
