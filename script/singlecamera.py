#!/usr/bin/env python
from uiautomatorplug.android import device as d
import time
import unittest
import commands
import util
import string
import random

a  = util.Adb()
sm = util.SetCaptureMode()
so = util.SetOption()
tb = util.TouchButton()

Exposure          = ['-6','-3','0','3','6'] #_0_0
ISO               = ['iso-auto','iso-100','iso-200','iso-400','iso-800'] #_0_0
White_Balance     = ['auto','incandescent','fluorescent','cloudy-daylight','daylight'] #_0_0
Switch_Camera     = ['1','0'] #_0
Face_Detection    = ['off','on'] #_0
Scenes            = ['auto','landscape','portrait','night','sports'] #_0_0 ,'night-portrait'
Self_Timer        = ['0','3','5','10'] #_0_0
Geo_Location      = ['off','on'] #_0
Picture_Size      = ['WideScreen','StandardScreen'] #_0_0
Hints             = ['off','on'] #_0_0
Video_Size        = [['false','4'],['false','5'],['true','5'],['false','6'],['true','6']] #_0_0
Settings_Layout   = ['Mini','Large'] #_0
Shortcut_Button_1 = ['exposure','iso','whitebalance','flashmode','id','fdfr','scenemode','delay','geo'] #_0
Shortcut_Button_2 = ['exposure','iso','whitebalance','flashmode','id','fdfr','scenemode','delay','geo'] #_0
Shortcut_Button_3 = ['exposure','iso','whitebalance','flashmode','id','fdfr','scenemode','delay','geo'] #_0

class CameraTest(unittest.TestCase):

    def setUp(self):
        super(CameraTest,self).setUp()
        # rm DCIM folder and refresh from adb shell
        #a.cmd('rm','/sdcard/DCIM/100ANDRO')
        #a.cmd('refresh','/sdcard/DCIM/100ANDRO')
        #Because default camera after launching is single mode, so we set this step in setUp().
        #Step 1. Launch single capture activity
        #a.cmd('launch','com.intel.camera22/.Camera')
        #time.sleep(2)
        #if d(text = 'Yes').wait.exists(timeout = 3000):
        #    d(text = 'Yes').click.wait()
        #if d(text = 'Skip').wait.exists(timeout = 3000):
        #    d(text = 'Skip').click.wait()
        #else:
        #    assert d(resourceId = 'com.intel.camera22:id/shutter_button'),'Launch camera failed!!'
        a.setUpDevice()
        sm.switchCaptureMode('Single')

    def tearDown(self):
        super(CameraTest,self).tearDown()
        #4.Exit  activity
        tb.switchBackOrFrontCamera('back')
        #self._pressBack(4)
        a.tearDownDevice()

    # Testcase 2
    def testCaptureSingleImageWithExposure(self):
        """
        Summary:Capture image with Exposure mode.
        Step:
        1.Launch single capture activity
        2.Set exposure mode
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        randomoption = random.choice(Exposure)
        so.setCameraOption('Exposure',randomoption)
        tb.captureAndCheckPicCount('single')

    # Testcase 3
    def testCaptureSingleImageWithScene(self):
        """
        Summary:Capture image with Scene mode.
        Step:
        1.Launch single capture activity
        2.Set scene mode
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        randomoption = random.choice(Scenes)
        so.setCameraOption('Scenes',randomoption)
        tb.captureAndCheckPicCount('single')
        so.setCameraOption('Scenes','auto') #Force set scenes to auto

    # Testcase 4
    def testCaptureSingleImageWithFDFR(self):
        """
        Summary:Capture image with FD/FR.
        Step:
        1.Launch single capture activity
        2.Set FD/FR ON
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        randomoption = random.choice(Face_Detection)
        so.setCameraOption('Face Detection',randomoption)
        tb.captureAndCheckPicCount('single')

    # Testcase 5
    def testCaptureSingleImageWithPictureSize(self):
        """
        Summary:Capture image with Photo size.
        Step:
        1.Launch single capture activity
        2.Set photo size
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        randomoption = random.choice(Picture_Size)
        so.setCameraOption('Picture Size',randomoption)
        tb.captureAndCheckPicCount('single')

    # Testcase 6
    def testCaptureSingleImageWithHits(self):
        """
        Summary:Capture image with Hints.
        Step:
        1.Launch single capture activity
        2.Set Hints
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        randomoption = random.choice(Hints)
        so.setCameraOption('Hints',randomoption)
        tb.captureAndCheckPicCount('single')

    # Testcase 7
    def testCaptureSingleImageWithSelfTimer(self):
        """
        Summary:Capture image with Self-timer.
        Step:
        1.Launch single capture activity
        2.Set Self-timer
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        randomoption = random.choice(Self_Timer)
        so.setCameraOption('Self Timer',randomoption)
        tb.captureAndCheckPicCount('single',int(randomoption))
        so.setCameraOption('Self Timer','0') #Force set timer to off

    # Testcase 8
    def testCaptureSingleImageWithISO(self):
        """
        Summary:Capture image with ISO Setting.
        Step:
        1.Launch single capture activity
        2.Set ISO Setting
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        randomoption = random.choice(ISO)
        so.setCameraOption('ISO',randomoption)
        tb.captureAndCheckPicCount('single')

    # Testcase 9
    def testCaptureSingleImageWithWB(self):
        """
        Summary:Capture image with White Balance.
        Step:
        1.Launch single capture activity
        2.Set White Balance
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        randomoption = random.choice(White_Balance)
        so.setCameraOption('White Balance',randomoption)
        tb.captureAndCheckPicCount('single')

    def testCapturepictureWithLocation(self):
        """
        Summary:Capture image with Location.
        Step:
        1.Launch single capture activity
        2.Set Geo location
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        randomoption = random.choice(Geo_Location)
        so.setCameraOption('Geo Location',randomoption)
        tb.captureAndCheckPicCount('single')

    def testFrontFaceCapturePictureWithFD(self):
        """
        Summary:Capture image with FD/FR on front camera.
        Step:
        1.Launch single capture activity
        2.Switch to front camera
        3.Set FD/FR
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        so.setCameraOption('Switch Camera','1')
        randomoption = random.choice(Face_Detection)
        so.setCameraOption('Face Detection',randomoption)
        tb.captureAndCheckPicCount('single')

    def testFrontFaceCapturepictureWithLocation(self):
        """
        Summary:Capture image with location front camera.
        Step:
        1.Launch single capture activity
        2.Switch to front camera
        3.Set Geo location
        3.Touch shutter button to capture picture
        4.Exit  activity
        """
        so.setCameraOption('Switch Camera','1')
        randomoption = random.choice(Geo_Location)
        so.setCameraOption('Geo Location',randomoption)
        tb.captureAndCheckPicCount('single')

    def _pressBack(self,touchtimes):
        for i in range(1,touchtimes+1):
            d.press('back')

    def _confirmSettingMode(self,sub_mode,option):
        if sub_mode == 'location':
            result = a.cmd('cat','/data/data/com.intel.camera22/shared_prefs/com.intel.camera22_preferences_0.xml | grep '+ sub_mode)
            if result.find(option) == -1:
                self.fail('set camera setting ' + sub_mode + ' to ' + option + ' failed')
        else:
            result = a.cmd('cat','/data/data/com.intel.camera22/shared_prefs/com.intel.camera22_preferences_0_0.xml | grep ' + sub_mode)
            if result.find(option) == -1:
                self.fail('set camera setting ' + sub_mode + ' to ' + option + ' failed')

    def _capturePictureAndConfirm(self,timer=0):
        beforeC = a.cmd('ls','/sdcard/DCIM/100ANDRO')
        tb.takePicture('single')
        time.sleep(timer)
        afterC  = a.cmd('ls','/sdcard/DCIM/100ANDRO')
        if afterC == beforeC:
            self.fail('take picture failed !!')
