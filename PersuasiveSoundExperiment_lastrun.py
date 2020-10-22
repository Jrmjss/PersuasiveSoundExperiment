#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.4),
    on October 21, 2020, at 13:17
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
prefs.hardware['audioLib'] = 'pyo'
prefs.hardware['audioLatencyMode'] = '1'
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.4'
expName = 'PersuasiveSoundExperiment'  # from the Builder filename that created this script
expInfo = {'level of study': '', 'participant': '', 'age': '', 'first language': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sort_keys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Jeremie\\OneDrive\\Documents\\Toulouse Uni\\Mémoire M2\\Survey Experiment\\PersuasiveSoundExperiment_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1366, 768], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
mouse_2 = event.Mouse(win=win)
x, y = [None, None]
mouse_2.mouseClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='Hello !\n\nThanks for participating in this study !\n\nAt each stage of this experiment, you will hear two people speaking one after the other. You will not understand what they are saying. However, after carefully listening to each of them, you will indicate which one sounds the most persuasive to you by completing the sentence below.\n\nYou can listen to each speaker again by right-clicking on the sound icons.\n\n\n',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_6 = visual.TextStim(win=win, name='text_6',
    text='[Click anywhere to continue]',
    font='Arial',
    pos=(0.0, -0.4), height=0.025, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Ready"
ReadyClock = core.Clock()
mouse_4 = event.Mouse(win=win)
x, y = [None, None]
mouse_4.mouseClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='Ready ?\n\n\n',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_8 = visual.TextStim(win=win, name='text_8',
    text='[Click anywhere to continue]',
    font='Arial',
    pos=(0.0, -0.4), height=0.025, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Entrance"
EntranceClock = core.Clock()
Icon1 = visual.ImageStim(
    win=win,
    name='Icon1', 
    image='OrangeSoundIcon.png', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
Icon2 = visual.ImageStim(
    win=win,
    name='Icon2', 
    image='OrangeSoundIcon.png', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
text_2 = visual.TextStim(win=win, name='text_2',
    text='___________    is more persuasive than    ___________',
    font='Arial',
    pos=(0, -0.25), height=0.038, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
CircleM = visual.ImageStim(
    win=win,
    name='CircleM', 
    image='IconCircle.png', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
CircleL = visual.ImageStim(
    win=win,
    name='CircleL', 
    image='IconCircle.png', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)

# Initialize components for Routine "Listen1"
Listen1Clock = core.Clock()
SoundIcon1 = visual.ImageStim(
    win=win,
    name='SoundIcon1', 
    image='OrangeSoundIcon.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
SoundIcon2 = visual.ImageStim(
    win=win,
    name='SoundIcon2', 
    image='OrangeSoundIcon.png', mask=None,
    ori=0, pos=(0.0, 0.0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
Question = visual.TextStim(win=win, name='Question',
    text='___________    is more persuasive than    ___________',
    font='Arial',
    pos=(0, -0.25), height=0.038, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
Sound_1 = sound.Sound('A', secs=-1, stereo=True, hamming=False,
    name='Sound_1')
Sound_1.setVolume(1)
Playing1 = visual.ImageStim(
    win=win,
    name='Playing1', 
    image='GreenSoundIcon.png', mask=None,
    ori=0, pos=(0.0, 0.0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
IconCircle1 = visual.ImageStim(
    win=win,
    name='IconCircle1', 
    image='IconCircle.png', mask=None,
    ori=0, pos=(-0.355, -0.16), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
IconCircle2 = visual.ImageStim(
    win=win,
    name='IconCircle2', 
    image='IconCircle.png', mask=None,
    ori=0, pos=(0.355, -0.16), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
RightClicked = None

# Initialize components for Routine "Pause2"
Pause2Clock = core.Clock()
SoundIcon1_3 = visual.ImageStim(
    win=win,
    name='SoundIcon1_3', 
    image='OrangeSoundIcon.png', mask=None,
    ori=0, pos=(0, 0.25), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
SoundIcon2_3 = visual.ImageStim(
    win=win,
    name='SoundIcon2_3', 
    image='OrangeSoundIcon.png', mask=None,
    ori=0, pos=(0, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
Question_3 = visual.TextStim(win=win, name='Question_3',
    text='___________    is more persuasive than    ___________',
    font='Arial',
    pos=(0, -0.25), height=0.038, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
IconCircle1_3 = visual.ImageStim(
    win=win,
    name='IconCircle1_3', 
    image='IconCircle.png', mask=None,
    ori=0, pos=(-0.355, -0.16), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
IconCircle2_3 = visual.ImageStim(
    win=win,
    name='IconCircle2_3', 
    image='IconCircle.png', mask=None,
    ori=0, pos=(0.355, -0.16), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)

# Initialize components for Routine "Listen2"
Listen2Clock = core.Clock()
SoundIcon1_2 = visual.ImageStim(
    win=win,
    name='SoundIcon1_2', 
    image='OrangeSoundIcon.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
SoundIcon2_2 = visual.ImageStim(
    win=win,
    name='SoundIcon2_2', 
    image='OrangeSoundIcon.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
Question_2 = visual.TextStim(win=win, name='Question_2',
    text='___________    is more persuasive than    ___________',
    font='Arial',
    pos=(0, -0.25), height=0.038, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
Sound_2 = sound.Sound('A', secs=-1, stereo=True, hamming=False,
    name='Sound_2')
Sound_2.setVolume(1)
Playing2 = visual.ImageStim(
    win=win,
    name='Playing2', 
    image='GreenSoundIcon.png', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
IconCircle1_2 = visual.ImageStim(
    win=win,
    name='IconCircle1_2', 
    image='IconCircle.png', mask=None,
    ori=0, pos=(-0.355, -0.16), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
IconCircle2_2 = visual.ImageStim(
    win=win,
    name='IconCircle2_2', 
    image='IconCircle.png', mask=None,
    ori=0, pos=(0.355, -0.16), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)

# Initialize components for Routine "Choice"
ChoiceClock = core.Clock()
IconChoice1 = visual.ImageStim(
    win=win,
    name='IconChoice1', 
    image='OrangeSoundIcon.png', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
IconChoice2 = visual.ImageStim(
    win=win,
    name='IconChoice2', 
    image='OrangeSoundIcon.png', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='___________    is more persuasive than    ___________',
    font='Arial',
    pos=(0, -0.25), height=0.038, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
BlueMore = visual.ImageStim(
    win=win,
    name='BlueMore', 
    image='BlueSoundIcon.png', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=0.2,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
BlueLess = visual.ImageStim(
    win=win,
    name='BlueLess', 
    image='BlueSoundIcon.png', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=0.2,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
MoreP = visual.ImageStim(
    win=win,
    name='MoreP', 
    image='IconCircle.png', mask=None,
    ori=0, pos=(-0.355, -0.16), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
LessP = visual.ImageStim(
    win=win,
    name='LessP', 
    image='IconCircle.png', mask=None,
    ori=0, pos=(0.355, -0.16), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
NextIcon = visual.ImageStim(
    win=win,
    name='NextIcon', 
    image='NextIcon.png', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
def movePicked(picked, mouse, grabbed):
    # Move piece if we already moving that piece
    if grabbed is not None and mouse.isPressedIn(grabbed):
        grabbed.pos = mouse.getPos()
        return grabbed
    else:
        # Move newly clicked piece
        for piece in picked:
            if mouse.isPressedIn(piece) and grabbed is None:
                return piece
                
RightClicked = None
NotRightClicked = None
#thisExp = psychoJS.experiment;
Instruct = visual.TextStim(win=win, name='Instruct',
    text='Right-click to listen again.\n\nDrag and drop to complete the sentence.',
    font='Arial',
    pos=(-0.54, 0.40), height=0.03, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);

# Initialize components for Routine "Byyee"
ByyeeClock = core.Clock()
mouse_3 = event.Mouse(win=win)
x, y = [None, None]
mouse_3.mouseClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text="And you're done !\nThanks again, you've been great ! :)",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_5 = visual.TextStim(win=win, name='text_5',
    text='[Click anywhere to exit]',
    font='Arial',
    pos=(0.0, -0.4), height=0.025, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instructions"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_2
gotValidClick = False  # until a click is received
# keep track of which components have finished
InstructionsComponents = [mouse_2, text_3, text_6]
for thisComponent in InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instructions"-------
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *mouse_2* updates
    if mouse_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_2.frameNStart = frameN  # exact frame index
        mouse_2.tStart = t  # local t and not account for scr refresh
        mouse_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_2, 'tStartRefresh')  # time at next scr refresh
        mouse_2.status = STARTED
        mouse_2.mouseClock.reset()
        prevButtonState = mouse_2.getPressed()  # if button is down already this ISN'T a new click
    if mouse_2.status == STARTED:  # only update if started and not finished!
        buttons = mouse_2.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # abort routine on response
                continueRoutine = False
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    
    # *text_6* updates
    if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_6.frameNStart = frameN  # exact frame index
        text_6.tStart = t  # local t and not account for scr refresh
        text_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
        text_6.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
x, y = mouse_2.getPos()
buttons = mouse_2.getPressed()
thisExp.addData('mouse_2.x', x)
thisExp.addData('mouse_2.y', y)
thisExp.addData('mouse_2.leftButton', buttons[0])
thisExp.addData('mouse_2.midButton', buttons[1])
thisExp.addData('mouse_2.rightButton', buttons[2])
thisExp.nextEntry()
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Ready"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_4
gotValidClick = False  # until a click is received
# keep track of which components have finished
ReadyComponents = [mouse_4, text_7, text_8]
for thisComponent in ReadyComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ReadyClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Ready"-------
while continueRoutine:
    # get current time
    t = ReadyClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ReadyClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *mouse_4* updates
    if mouse_4.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_4.frameNStart = frameN  # exact frame index
        mouse_4.tStart = t  # local t and not account for scr refresh
        mouse_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_4, 'tStartRefresh')  # time at next scr refresh
        mouse_4.status = STARTED
        mouse_4.mouseClock.reset()
        prevButtonState = mouse_4.getPressed()  # if button is down already this ISN'T a new click
    if mouse_4.status == STARTED:  # only update if started and not finished!
        buttons = mouse_4.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # abort routine on response
                continueRoutine = False
    
    # *text_7* updates
    if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_7.frameNStart = frameN  # exact frame index
        text_7.tStart = t  # local t and not account for scr refresh
        text_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
        text_7.setAutoDraw(True)
    
    # *text_8* updates
    if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_8.frameNStart = frameN  # exact frame index
        text_8.tStart = t  # local t and not account for scr refresh
        text_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
        text_8.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ReadyComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Ready"-------
for thisComponent in ReadyComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
x, y = mouse_4.getPos()
buttons = mouse_4.getPressed()
thisExp.addData('mouse_4.x', x)
thisExp.addData('mouse_4.y', y)
thisExp.addData('mouse_4.leftButton', buttons[0])
thisExp.addData('mouse_4.midButton', buttons[1])
thisExp.addData('mouse_4.rightButton', buttons[2])
thisExp.nextEntry()
# the Routine "Ready" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
ChoiceLoop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('LocutionPairsData.xls'),
    seed=None, name='ChoiceLoop')
thisExp.addLoop(ChoiceLoop)  # add the loop to the experiment
thisChoiceLoop = ChoiceLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisChoiceLoop.rgb)
if thisChoiceLoop != None:
    for paramName in thisChoiceLoop:
        exec('{} = thisChoiceLoop[paramName]'.format(paramName))

for thisChoiceLoop in ChoiceLoop:
    currentLoop = ChoiceLoop
    # abbreviate parameter names if possible (e.g. rgb = thisChoiceLoop.rgb)
    if thisChoiceLoop != None:
        for paramName in thisChoiceLoop:
            exec('{} = thisChoiceLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Entrance"-------
    continueRoutine = True
    # update component parameters for each repeat
    Icon1.setPos((0.5, 0.25))
    Icon1.setSize((0.2, 0.2))
    Icon2.setPos((0.5, 0))
    Icon2.setSize((0.2, 0.2))
    CircleM.setPos((-0.355, -0.16))
    CircleM.setSize((0.04, 0.04))
    CircleL.setPos((0.355, -0.16))
    CircleL.setSize((0.04, 0.04))
    IconIndex = 1
    CircleIndex = 1
    InstTextIndex = 1
    # keep track of which components have finished
    EntranceComponents = [Icon1, Icon2, text_2, CircleM, CircleL]
    for thisComponent in EntranceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    EntranceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Entrance"-------
    while continueRoutine:
        # get current time
        t = EntranceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=EntranceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Icon1* updates
        if Icon1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Icon1.frameNStart = frameN  # exact frame index
            Icon1.tStart = t  # local t and not account for scr refresh
            Icon1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Icon1, 'tStartRefresh')  # time at next scr refresh
            Icon1.setAutoDraw(True)
        
        # *Icon2* updates
        if Icon2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Icon2.frameNStart = frameN  # exact frame index
            Icon2.tStart = t  # local t and not account for scr refresh
            Icon2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Icon2, 'tStartRefresh')  # time at next scr refresh
            Icon2.setAutoDraw(True)
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            text_2.setAutoDraw(True)
        
        # *CircleM* updates
        if CircleM.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            CircleM.frameNStart = frameN  # exact frame index
            CircleM.tStart = t  # local t and not account for scr refresh
            CircleM.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CircleM, 'tStartRefresh')  # time at next scr refresh
            CircleM.setAutoDraw(True)
        
        # *CircleL* updates
        if CircleL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            CircleL.frameNStart = frameN  # exact frame index
            CircleL.tStart = t  # local t and not account for scr refresh
            CircleL.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CircleL, 'tStartRefresh')  # time at next scr refresh
            CircleL.setAutoDraw(True)
        if IconIndex is not 11:
            Icon1.pos -= (0.05, 0.0)
            Icon2.pos -= (0.05, 0.0)
            IconIndex += 1
            
        if CircleIndex is not 8:
            CircleM.size += 0.02
            CircleL.size += 0.02
            CircleIndex += 1
            
        if CircleIndex is 8 and IconIndex is 11:
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in EntranceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Entrance"-------
    for thisComponent in EntranceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Entrance" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    ListenLoop = data.TrialHandler(nReps=20, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('LocutionRandPos.xls'),
        seed=None, name='ListenLoop')
    thisExp.addLoop(ListenLoop)  # add the loop to the experiment
    thisListenLoop = ListenLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisListenLoop.rgb)
    if thisListenLoop != None:
        for paramName in thisListenLoop:
            exec('{} = thisListenLoop[paramName]'.format(paramName))
    
    for thisListenLoop in ListenLoop:
        currentLoop = ListenLoop
        # abbreviate parameter names if possible (e.g. rgb = thisListenLoop.rgb)
        if thisListenLoop != None:
            for paramName in thisListenLoop:
                exec('{} = thisListenLoop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Listen1"-------
        continueRoutine = True
        # update component parameters for each repeat
        SoundIcon1.setPos((0.0, 0.0))
        Sound_1.setSound(Locution_1, secs=Locution_1_Dur, hamming=False)
        Sound_1.setVolume(1, log=False)
        if RightClicked is IconChoice1:
            SoundIcon2.setPos(IconChoice2.pos)
            SoundIcon1.setPos(IconChoice1.pos)
            Playing1.setPos(IconChoice1.pos)
        
        if RightClicked is None:
            if Locution_1_Down is "N":
                Playing1.pos = (0.0, 0.25)
                SoundIcon1.pos = (0.0, 0.25)
                SoundIcon2.pos = (0.0, 0.0)
            if Locution_1_Down is "Y":
                Playing1.pos = (0.0, 0.0)
                SoundIcon1.pos = (0.0, 0.0)
                SoundIcon2.pos = (0.0, 0.25)
        # keep track of which components have finished
        Listen1Components = [SoundIcon1, SoundIcon2, Question, Sound_1, Playing1, IconCircle1, IconCircle2]
        for thisComponent in Listen1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Listen1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Listen1"-------
        while continueRoutine:
            # get current time
            t = Listen1Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Listen1Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *SoundIcon1* updates
            if SoundIcon1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                SoundIcon1.frameNStart = frameN  # exact frame index
                SoundIcon1.tStart = t  # local t and not account for scr refresh
                SoundIcon1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(SoundIcon1, 'tStartRefresh')  # time at next scr refresh
                SoundIcon1.setAutoDraw(True)
            if SoundIcon1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > SoundIcon1.tStartRefresh + Locution_1_Dur-frameTolerance:
                    # keep track of stop time/frame for later
                    SoundIcon1.tStop = t  # not accounting for scr refresh
                    SoundIcon1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(SoundIcon1, 'tStopRefresh')  # time at next scr refresh
                    SoundIcon1.setAutoDraw(False)
            
            # *SoundIcon2* updates
            if SoundIcon2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                SoundIcon2.frameNStart = frameN  # exact frame index
                SoundIcon2.tStart = t  # local t and not account for scr refresh
                SoundIcon2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(SoundIcon2, 'tStartRefresh')  # time at next scr refresh
                SoundIcon2.setAutoDraw(True)
            if SoundIcon2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > SoundIcon2.tStartRefresh + Locution_1_Dur-frameTolerance:
                    # keep track of stop time/frame for later
                    SoundIcon2.tStop = t  # not accounting for scr refresh
                    SoundIcon2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(SoundIcon2, 'tStopRefresh')  # time at next scr refresh
                    SoundIcon2.setAutoDraw(False)
            
            # *Question* updates
            if Question.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Question.frameNStart = frameN  # exact frame index
                Question.tStart = t  # local t and not account for scr refresh
                Question.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Question, 'tStartRefresh')  # time at next scr refresh
                Question.setAutoDraw(True)
            if Question.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Question.tStartRefresh + Locution_1_Dur-frameTolerance:
                    # keep track of stop time/frame for later
                    Question.tStop = t  # not accounting for scr refresh
                    Question.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Question, 'tStopRefresh')  # time at next scr refresh
                    Question.setAutoDraw(False)
            # start/stop Sound_1
            if Sound_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Sound_1.frameNStart = frameN  # exact frame index
                Sound_1.tStart = t  # local t and not account for scr refresh
                Sound_1.tStartRefresh = tThisFlipGlobal  # on global time
                Sound_1.play(when=win)  # sync with win flip
            if Sound_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Sound_1.tStartRefresh + Locution_1_Dur-frameTolerance:
                    # keep track of stop time/frame for later
                    Sound_1.tStop = t  # not accounting for scr refresh
                    Sound_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Sound_1, 'tStopRefresh')  # time at next scr refresh
                    Sound_1.stop()
            
            # *Playing1* updates
            if Playing1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Playing1.frameNStart = frameN  # exact frame index
                Playing1.tStart = t  # local t and not account for scr refresh
                Playing1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Playing1, 'tStartRefresh')  # time at next scr refresh
                Playing1.setAutoDraw(True)
            if Playing1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Playing1.tStartRefresh + Locution_1_Dur-frameTolerance:
                    # keep track of stop time/frame for later
                    Playing1.tStop = t  # not accounting for scr refresh
                    Playing1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Playing1, 'tStopRefresh')  # time at next scr refresh
                    Playing1.setAutoDraw(False)
            
            # *IconCircle1* updates
            if IconCircle1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                IconCircle1.frameNStart = frameN  # exact frame index
                IconCircle1.tStart = t  # local t and not account for scr refresh
                IconCircle1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(IconCircle1, 'tStartRefresh')  # time at next scr refresh
                IconCircle1.setAutoDraw(True)
            if IconCircle1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > IconCircle1.tStartRefresh + Locution_1_Dur-frameTolerance:
                    # keep track of stop time/frame for later
                    IconCircle1.tStop = t  # not accounting for scr refresh
                    IconCircle1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(IconCircle1, 'tStopRefresh')  # time at next scr refresh
                    IconCircle1.setAutoDraw(False)
            
            # *IconCircle2* updates
            if IconCircle2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                IconCircle2.frameNStart = frameN  # exact frame index
                IconCircle2.tStart = t  # local t and not account for scr refresh
                IconCircle2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(IconCircle2, 'tStartRefresh')  # time at next scr refresh
                IconCircle2.setAutoDraw(True)
            if IconCircle2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > IconCircle2.tStartRefresh + Locution_1_Dur-frameTolerance:
                    # keep track of stop time/frame for later
                    IconCircle2.tStop = t  # not accounting for scr refresh
                    IconCircle2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(IconCircle2, 'tStopRefresh')  # time at next scr refresh
                    IconCircle2.setAutoDraw(False)
            if RightClicked is IconChoice2:
                continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Listen1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Listen1"-------
        for thisComponent in Listen1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        Sound_1.stop()  # ensure sound has stopped at end of routine
        # the Routine "Listen1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Pause2"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        Pause2Components = [SoundIcon1_3, SoundIcon2_3, Question_3, IconCircle1_3, IconCircle2_3]
        for thisComponent in Pause2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Pause2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Pause2"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Pause2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Pause2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *SoundIcon1_3* updates
            if SoundIcon1_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                SoundIcon1_3.frameNStart = frameN  # exact frame index
                SoundIcon1_3.tStart = t  # local t and not account for scr refresh
                SoundIcon1_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(SoundIcon1_3, 'tStartRefresh')  # time at next scr refresh
                SoundIcon1_3.setAutoDraw(True)
            if SoundIcon1_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > SoundIcon1_3.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    SoundIcon1_3.tStop = t  # not accounting for scr refresh
                    SoundIcon1_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(SoundIcon1_3, 'tStopRefresh')  # time at next scr refresh
                    SoundIcon1_3.setAutoDraw(False)
            
            # *SoundIcon2_3* updates
            if SoundIcon2_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                SoundIcon2_3.frameNStart = frameN  # exact frame index
                SoundIcon2_3.tStart = t  # local t and not account for scr refresh
                SoundIcon2_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(SoundIcon2_3, 'tStartRefresh')  # time at next scr refresh
                SoundIcon2_3.setAutoDraw(True)
            if SoundIcon2_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > SoundIcon2_3.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    SoundIcon2_3.tStop = t  # not accounting for scr refresh
                    SoundIcon2_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(SoundIcon2_3, 'tStopRefresh')  # time at next scr refresh
                    SoundIcon2_3.setAutoDraw(False)
            
            # *Question_3* updates
            if Question_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Question_3.frameNStart = frameN  # exact frame index
                Question_3.tStart = t  # local t and not account for scr refresh
                Question_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Question_3, 'tStartRefresh')  # time at next scr refresh
                Question_3.setAutoDraw(True)
            if Question_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Question_3.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    Question_3.tStop = t  # not accounting for scr refresh
                    Question_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Question_3, 'tStopRefresh')  # time at next scr refresh
                    Question_3.setAutoDraw(False)
            
            # *IconCircle1_3* updates
            if IconCircle1_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                IconCircle1_3.frameNStart = frameN  # exact frame index
                IconCircle1_3.tStart = t  # local t and not account for scr refresh
                IconCircle1_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(IconCircle1_3, 'tStartRefresh')  # time at next scr refresh
                IconCircle1_3.setAutoDraw(True)
            if IconCircle1_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > IconCircle1_3.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    IconCircle1_3.tStop = t  # not accounting for scr refresh
                    IconCircle1_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(IconCircle1_3, 'tStopRefresh')  # time at next scr refresh
                    IconCircle1_3.setAutoDraw(False)
            
            # *IconCircle2_3* updates
            if IconCircle2_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                IconCircle2_3.frameNStart = frameN  # exact frame index
                IconCircle2_3.tStart = t  # local t and not account for scr refresh
                IconCircle2_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(IconCircle2_3, 'tStartRefresh')  # time at next scr refresh
                IconCircle2_3.setAutoDraw(True)
            if IconCircle2_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > IconCircle2_3.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    IconCircle2_3.tStop = t  # not accounting for scr refresh
                    IconCircle2_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(IconCircle2_3, 'tStopRefresh')  # time at next scr refresh
                    IconCircle2_3.setAutoDraw(False)
            if RightClicked is not None:
                continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Pause2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Pause2"-------
        for thisComponent in Pause2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # ------Prepare to start Routine "Listen2"-------
        continueRoutine = True
        # update component parameters for each repeat
        SoundIcon1_2.setPos((0.0, 0.0))
        SoundIcon2_2.setPos((0.0, 0.0))
        Sound_2.setSound(Locution_2, secs=Locution_2_Dur, hamming=False)
        Sound_2.setVolume(1, log=False)
        Playing2.setPos((0.0, 0.0))
        if RightClicked is IconChoice2:
            SoundIcon1_2.setPos(IconChoice1.pos)
            SoundIcon2_2.setPos(IconChoice2.pos)
            Playing2.setPos(IconChoice2.pos)
            
        if RightClicked is None:
            if Locution_1_Down is "N":
                Playing2.pos = (0.0, 0.0)
                SoundIcon1_2.pos = (0.0, 0.25)
                SoundIcon2_2.pos = (0.0, 0.0)
            if Locution_1_Down is "Y":
                Playing2.pos = (0.0, 0.25)
                SoundIcon1_2.pos = (0.0, 0.0)
                SoundIcon2_2.pos = (0.0, 0.25)
        # keep track of which components have finished
        Listen2Components = [SoundIcon1_2, SoundIcon2_2, Question_2, Sound_2, Playing2, IconCircle1_2, IconCircle2_2]
        for thisComponent in Listen2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Listen2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Listen2"-------
        while continueRoutine:
            # get current time
            t = Listen2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Listen2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *SoundIcon1_2* updates
            if SoundIcon1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                SoundIcon1_2.frameNStart = frameN  # exact frame index
                SoundIcon1_2.tStart = t  # local t and not account for scr refresh
                SoundIcon1_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(SoundIcon1_2, 'tStartRefresh')  # time at next scr refresh
                SoundIcon1_2.setAutoDraw(True)
            if SoundIcon1_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > SoundIcon1_2.tStartRefresh + Locution_2_Dur-frameTolerance:
                    # keep track of stop time/frame for later
                    SoundIcon1_2.tStop = t  # not accounting for scr refresh
                    SoundIcon1_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(SoundIcon1_2, 'tStopRefresh')  # time at next scr refresh
                    SoundIcon1_2.setAutoDraw(False)
            
            # *SoundIcon2_2* updates
            if SoundIcon2_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                SoundIcon2_2.frameNStart = frameN  # exact frame index
                SoundIcon2_2.tStart = t  # local t and not account for scr refresh
                SoundIcon2_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(SoundIcon2_2, 'tStartRefresh')  # time at next scr refresh
                SoundIcon2_2.setAutoDraw(True)
            if SoundIcon2_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > SoundIcon2_2.tStartRefresh + Locution_2_Dur-frameTolerance:
                    # keep track of stop time/frame for later
                    SoundIcon2_2.tStop = t  # not accounting for scr refresh
                    SoundIcon2_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(SoundIcon2_2, 'tStopRefresh')  # time at next scr refresh
                    SoundIcon2_2.setAutoDraw(False)
            
            # *Question_2* updates
            if Question_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Question_2.frameNStart = frameN  # exact frame index
                Question_2.tStart = t  # local t and not account for scr refresh
                Question_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Question_2, 'tStartRefresh')  # time at next scr refresh
                Question_2.setAutoDraw(True)
            if Question_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Question_2.tStartRefresh + Locution_2_Dur-frameTolerance:
                    # keep track of stop time/frame for later
                    Question_2.tStop = t  # not accounting for scr refresh
                    Question_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Question_2, 'tStopRefresh')  # time at next scr refresh
                    Question_2.setAutoDraw(False)
            # start/stop Sound_2
            if Sound_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                Sound_2.frameNStart = frameN  # exact frame index
                Sound_2.tStart = t  # local t and not account for scr refresh
                Sound_2.tStartRefresh = tThisFlipGlobal  # on global time
                Sound_2.play(when=win)  # sync with win flip
            if Sound_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Sound_2.tStartRefresh + Locution_2_Dur-frameTolerance:
                    # keep track of stop time/frame for later
                    Sound_2.tStop = t  # not accounting for scr refresh
                    Sound_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Sound_2, 'tStopRefresh')  # time at next scr refresh
                    Sound_2.stop()
            
            # *Playing2* updates
            if Playing2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                Playing2.frameNStart = frameN  # exact frame index
                Playing2.tStart = t  # local t and not account for scr refresh
                Playing2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Playing2, 'tStartRefresh')  # time at next scr refresh
                Playing2.setAutoDraw(True)
            if Playing2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Playing2.tStartRefresh + Locution_2_Dur-frameTolerance:
                    # keep track of stop time/frame for later
                    Playing2.tStop = t  # not accounting for scr refresh
                    Playing2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Playing2, 'tStopRefresh')  # time at next scr refresh
                    Playing2.setAutoDraw(False)
            
            # *IconCircle1_2* updates
            if IconCircle1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                IconCircle1_2.frameNStart = frameN  # exact frame index
                IconCircle1_2.tStart = t  # local t and not account for scr refresh
                IconCircle1_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(IconCircle1_2, 'tStartRefresh')  # time at next scr refresh
                IconCircle1_2.setAutoDraw(True)
            if IconCircle1_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > IconCircle1_2.tStartRefresh + Locution_2_Dur-frameTolerance:
                    # keep track of stop time/frame for later
                    IconCircle1_2.tStop = t  # not accounting for scr refresh
                    IconCircle1_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(IconCircle1_2, 'tStopRefresh')  # time at next scr refresh
                    IconCircle1_2.setAutoDraw(False)
            
            # *IconCircle2_2* updates
            if IconCircle2_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                IconCircle2_2.frameNStart = frameN  # exact frame index
                IconCircle2_2.tStart = t  # local t and not account for scr refresh
                IconCircle2_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(IconCircle2_2, 'tStartRefresh')  # time at next scr refresh
                IconCircle2_2.setAutoDraw(True)
            if IconCircle2_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > IconCircle2_2.tStartRefresh + Locution_2_Dur-frameTolerance:
                    # keep track of stop time/frame for later
                    IconCircle2_2.tStop = t  # not accounting for scr refresh
                    IconCircle2_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(IconCircle2_2, 'tStopRefresh')  # time at next scr refresh
                    IconCircle2_2.setAutoDraw(False)
            if RightClicked is IconChoice1:
                continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Listen2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Listen2"-------
        for thisComponent in Listen2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        Sound_2.stop()  # ensure sound has stopped at end of routine
        # the Routine "Listen2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Choice"-------
        continueRoutine = True
        # update component parameters for each repeat
        IconChoice1.setPos((0.0, 0.0))
        IconChoice1.setSize((0.2, 0.2))
        IconChoice2.setPos((0.0, 0.0))
        IconChoice2.setSize((0.2, 0.2))
        # setup some python lists for storing info about the mouse
        mouse.x = []
        mouse.y = []
        mouse.leftButton = []
        mouse.midButton = []
        mouse.rightButton = []
        mouse.time = []
        mouse.clicked_name = []
        gotValidClick = False  # until a click is received
        BlueMore.setPos((-0.355, -0.16))
        BlueMore.setSize((0.2, 0.2))
        BlueLess.setPos((0.355, -0.16))
        BlueLess.setSize((0.2, 0.2))
        NextIcon.setPos((0.7, -0.35))
        NextIcon.setSize((0.0, 0.0))
        pieces = [IconChoice1, IconChoice2]
        picked = []
        movingPiece = None
        MorePersuasive = None
        LessPersuasive = None
        NextGrow = 1
        
        if RightClicked is IconChoice1:
            IconChoice2.setPos(SoundIcon2.pos)
            IconChoice1.setPos(SoundIcon1.pos)
        
        if RightClicked is IconChoice2:
            IconChoice1.setPos(SoundIcon1_2.pos)
            IconChoice2.setPos(SoundIcon2_2.pos)
        
        if RightClicked is None:
            if Locution_1_Down is "N":
                IconChoice1.pos = (0.0, 0.25)
                IconChoice2.pos = (0.0, 0.0)
            if Locution_1_Down is "Y":
                IconChoice1.pos = (0.0, 0.0)
                IconChoice2.pos = (0.0, 0.25)
            
        RightClicked = None
        NotRightClicked = None
        
        LessPersuasive = None
        MorePersuasive = None
        # keep track of which components have finished
        ChoiceComponents = [IconChoice1, IconChoice2, mouse, text, BlueMore, BlueLess, MoreP, LessP, NextIcon, Instruct]
        for thisComponent in ChoiceComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        ChoiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Choice"-------
        while continueRoutine:
            # get current time
            t = ChoiceClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=ChoiceClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *IconChoice1* updates
            if IconChoice1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                IconChoice1.frameNStart = frameN  # exact frame index
                IconChoice1.tStart = t  # local t and not account for scr refresh
                IconChoice1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(IconChoice1, 'tStartRefresh')  # time at next scr refresh
                IconChoice1.setAutoDraw(True)
            
            # *IconChoice2* updates
            if IconChoice2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                IconChoice2.frameNStart = frameN  # exact frame index
                IconChoice2.tStart = t  # local t and not account for scr refresh
                IconChoice2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(IconChoice2, 'tStartRefresh')  # time at next scr refresh
                IconChoice2.setAutoDraw(True)
            # *mouse* updates
            if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse.frameNStart = frameN  # exact frame index
                mouse.tStart = t  # local t and not account for scr refresh
                mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
                mouse.status = STARTED
                mouse.mouseClock.reset()
                prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
            if mouse.status == STARTED:  # only update if started and not finished!
                buttons = mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        for obj in [IconChoice1, IconChoice2]:
                            if obj.contains(mouse):
                                gotValidClick = True
                                mouse.clicked_name.append(obj.name)
                        x, y = mouse.getPos()
                        mouse.x.append(x)
                        mouse.y.append(y)
                        buttons = mouse.getPressed()
                        mouse.leftButton.append(buttons[0])
                        mouse.midButton.append(buttons[1])
                        mouse.rightButton.append(buttons[2])
                        mouse.time.append(mouse.mouseClock.getTime())
            
            # *text* updates
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                text.setAutoDraw(True)
            
            # *BlueMore* updates
            if BlueMore.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                BlueMore.frameNStart = frameN  # exact frame index
                BlueMore.tStart = t  # local t and not account for scr refresh
                BlueMore.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(BlueMore, 'tStartRefresh')  # time at next scr refresh
                BlueMore.setAutoDraw(True)
            
            # *BlueLess* updates
            if BlueLess.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                BlueLess.frameNStart = frameN  # exact frame index
                BlueLess.tStart = t  # local t and not account for scr refresh
                BlueLess.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(BlueLess, 'tStartRefresh')  # time at next scr refresh
                BlueLess.setAutoDraw(True)
            
            # *MoreP* updates
            if MoreP.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                MoreP.frameNStart = frameN  # exact frame index
                MoreP.tStart = t  # local t and not account for scr refresh
                MoreP.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(MoreP, 'tStartRefresh')  # time at next scr refresh
                MoreP.setAutoDraw(True)
            
            # *LessP* updates
            if LessP.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                LessP.frameNStart = frameN  # exact frame index
                LessP.tStart = t  # local t and not account for scr refresh
                LessP.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(LessP, 'tStartRefresh')  # time at next scr refresh
                LessP.setAutoDraw(True)
            
            # *NextIcon* updates
            if NextIcon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                NextIcon.frameNStart = frameN  # exact frame index
                NextIcon.tStart = t  # local t and not account for scr refresh
                NextIcon.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(NextIcon, 'tStartRefresh')  # time at next scr refresh
                NextIcon.setAutoDraw(True)
            for piece in pieces:
                if mouse.isPressedIn(piece, buttons=[0]) and movingPiece is None:
                    picked.append(piece)
            
            movingPiece = movePicked(picked, mouse, movingPiece)
            
            #if IconChoice1.overlaps(MoreP) or IconChoice2.overlaps(MoreP):
            if MoreP.contains(IconChoice1.pos) or MoreP.contains(IconChoice2.pos):
                BlueMore.opacity = 1.0
            #    if IconChoice1.overlaps(MoreP):
                if MoreP.contains(IconChoice1.pos):
                    BlueMore.setPos(IconChoice1.pos)
                    MorePersuasive = "Locution_1"
                else:
                    BlueMore.setPos(IconChoice2.pos)
                    MorePersuasive = "Locution_2"
            else:
                BlueMore.opacity = 0.2
                BlueMore.setPos(MoreP.pos)
                MorePersuasive = None
                
            #if IconChoice1.overlaps(LessP) or IconChoice2.overlaps(LessP):
            if LessP.contains(IconChoice1.pos) or LessP.contains(IconChoice2.pos):
                BlueLess.opacity = 1.0
            #    if IconChoice1.overlaps(LessP):
                if LessP.contains(IconChoice1.pos):
                    BlueLess.setPos(IconChoice1.pos)
                    LessPersuasive = "Locution_1"
                else:
                    BlueLess.setPos(IconChoice2.pos)
                    LessPersuasive = "Locution_2"
            else:
                BlueLess.opacity = 0.2
                BlueLess.setPos(LessP.pos)
                LessPersuasive = None
                
            if LessPersuasive is not None and MorePersuasive is not None:
                if NextGrow is not 10:
                    NextIcon.size += 0.01
                    NextGrow += 1
                else:
                    if mouse.isPressedIn(NextIcon):
                        ListenLoop.finished = True
                        continueRoutine = False
                        
            if mouse.isPressedIn(IconChoice1, buttons=[2]):
                RightClicked = IconChoice1
                NotRightClicked = IconChoice2
                continueRoutine = False
                
            if mouse.isPressedIn(IconChoice2, buttons=[2]):
                RightClicked = IconChoice2
                NotRightClicked = IconChoice1
                continueRoutine = False
                
            
            # *Instruct* updates
            if Instruct.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Instruct.frameNStart = frameN  # exact frame index
                Instruct.tStart = t  # local t and not account for scr refresh
                Instruct.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Instruct, 'tStartRefresh')  # time at next scr refresh
                Instruct.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ChoiceComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Choice"-------
        for thisComponent in ChoiceComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store data for ListenLoop (TrialHandler)
        ListenLoop.addData('mouse.x', mouse.x)
        ListenLoop.addData('mouse.y', mouse.y)
        ListenLoop.addData('mouse.leftButton', mouse.leftButton)
        ListenLoop.addData('mouse.midButton', mouse.midButton)
        ListenLoop.addData('mouse.rightButton', mouse.rightButton)
        ListenLoop.addData('mouse.time', mouse.time)
        ListenLoop.addData('mouse.clicked_name', mouse.clicked_name)
        if RightClicked is None:
            thisExp.addData('MorePersuasive', MorePersuasive)
            thisExp.addData('LessPersuasive', LessPersuasive)
            
        if RightClicked is IconChoice1:
            thisExp.addData('Replayed', "Locution_1")
            
        if RightClicked is IconChoice2:
            thisExp.addData('Replayed', "Locution_2")
        # the Routine "Choice" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 20 repeats of 'ListenLoop'
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'ChoiceLoop'


# ------Prepare to start Routine "Byyee"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_3
gotValidClick = False  # until a click is received
# keep track of which components have finished
ByyeeComponents = [mouse_3, text_4, text_5]
for thisComponent in ByyeeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ByyeeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Byyee"-------
while continueRoutine:
    # get current time
    t = ByyeeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ByyeeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *mouse_3* updates
    if mouse_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_3.frameNStart = frameN  # exact frame index
        mouse_3.tStart = t  # local t and not account for scr refresh
        mouse_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_3, 'tStartRefresh')  # time at next scr refresh
        mouse_3.status = STARTED
        mouse_3.mouseClock.reset()
        prevButtonState = mouse_3.getPressed()  # if button is down already this ISN'T a new click
    if mouse_3.status == STARTED:  # only update if started and not finished!
        buttons = mouse_3.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # abort routine on response
                continueRoutine = False
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        text_4.setAutoDraw(True)
    
    # *text_5* updates
    if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_5.frameNStart = frameN  # exact frame index
        text_5.tStart = t  # local t and not account for scr refresh
        text_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
        text_5.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ByyeeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Byyee"-------
for thisComponent in ByyeeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
x, y = mouse_3.getPos()
buttons = mouse_3.getPressed()
thisExp.addData('mouse_3.x', x)
thisExp.addData('mouse_3.y', y)
thisExp.addData('mouse_3.leftButton', buttons[0])
thisExp.addData('mouse_3.midButton', buttons[1])
thisExp.addData('mouse_3.rightButton', buttons[2])
thisExp.nextEntry()
# the Routine "Byyee" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
