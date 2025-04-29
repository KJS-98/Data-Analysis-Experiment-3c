#toDO
#change lists to dictionaries to make code more readable (289-388)
#add steps per stair to correct number (more that 40?) 
#add steps per stair to correct number (more that 40?) 
import psychopy
from psychopy import visual, core, gui, data, monitors
from psychopy.hardware import keyboard
import numpy
from time import perf_counter
import random

def waitFunc(ms):
    '''function that accurately allows a wait for a specified number of ms'''
    tNow = 0 
    startTime = perf_counter()
    while tNow-startTime <= ms/1000: 
        tNow = perf_counter()
               
def drawMask(patchNo, ms): 

    '''function to creates a mask after the object is presented 
    creates random noise patches and draws them to the screen repeatedly
    use ms to decide how fast it changes between patches, use patchNo to decide how many patches''' 
    x = 0
    while x < patchNo:
        noiseTexture = numpy.random.rand(70, 70) * 2.0 - 1
        patch = visual.GratingStim(win, tex=noiseTexture, size=(1800, 1800), units='pix', interpolate=False, autoLog=False)
        waitFunc(ms)
        patch.draw()
        win.flip()
        x += 1

'''
These are the changable variables that should be 
selected before begining.
'''
scaleFactor = 12.27 # scale factor will change based on projector and projector distance
jitRange = (0, 5)#20 #what range do you want the jitter to be (cm)
horJitRange = (0, 10)
startGuidePos = (-190/scaleFactor, 0) # where do you want the guide to be? (jitter will be added to determine the starting position for participant on each trial)
smallStoneStepSizeRange = (10, 35)
stoneSize = 20/scaleFactor
smallStart = 50/scaleFactor
largeStart = 110/scaleFactor
stepsPerStair = 40
stepSize = 10/scaleFactor
smallestSize = 10/scaleFactor
foilScale = 1.17
rivWid = 50/scaleFactor #how much larger than the large foil should the width of the river be? /2
'''
set up GUI to take some information about the participant and 
testing session. 
'''

expName = 'Stepping with Projector' # Experiment name
expInfo = {'participant': '', 'session': ''} # What we want the participant (ppt) to record in the dialogue box
expInfo['date'] = data.getDateStr() # Gets the date
expInfo['expName'] = expName 

dlg = gui.DlgFromDict(expInfo, title=expName, fixed=['date']) # Dialogue box to record participant information
if dlg.OK:
    fileName = expInfo['participant'] + "_determineFoilSize_combinedStaircase_" + expInfo['date'] # Names the experiment file based on ppt info 
    fileName2 = expInfo['participant'] + "_determineFoilSize_combinedStaircase_StaircaseOnly" 
else:
    core.quit()  # The user hit cancel so exit
'''
Set up the  monitor, windown and keyboard for psychopy to use. 
note - the units are set to cm (on monitor). Monitor details will 
need to be updated if another monitor is used.
'''
monitor = monitors.Monitor(name='myMonitor')
monitor2 = monitors.Monitor(name='secondaryMonitor')
monitor.setWidth(31)
monitor2.setWidth(47.5)
monitor.setSizePix((1920,1080))
monitor2.setSizePix((1920,1080))
win = visual.Window(size=(1600, 900), monitor=monitor, color='black', units='cm', fullscr=True)  # Adjust window size as needed
kb = keyboard.Keyboard()


oneUp15= largeStart
threeUp15 = smallStart

bigSteps15ms1up = True
bigSteps15ms3up = True
bigSteps150ms1up = True
bigSteps150ms3up = True
bigSteps2000ms1up = True
bigSteps2000ms3up = True
bigStepsCtrl15ms1Up = True
bigStepsCtrl15ms3Up = True
bigStepsCtrl150ms1Up = True
bigStepsCtrl150ms3Up = True
bigStepsCtrl2000ms1Up = True
bigStepsCtrl2000ms3Up = True

tar15ms1up = largeStart
tar15ms3up = smallStart
tar150ms1up = largeStart
tar150ms3up = smallStart
tar2000ms1up = largeStart
tar2000ms3up = smallStart

ctrl15ms1up = largeStart
ctrl15ms3up = smallStart
ctrl150ms1up = largeStart
ctrl150ms3up = smallStart
ctrl2000ms1up = largeStart
ctrl2000ms3up = smallStart


list1 = [1]*stepsPerStair #15ms 1up SS
list2 = [2]*stepsPerStair #15ms 3up SS
list3 = [3]*stepsPerStair #15ms 1up BB
list4 = [4]*stepsPerStair #15ms 3up BB
list5 = [5]*stepsPerStair #150ms 1up SS
list6 = [6]*stepsPerStair #150ms 3up SS

list7 = [7]*stepsPerStair #150ms 1up BB
list8 = [8]*stepsPerStair #150ms 3up BB
list9 = [9]*stepsPerStair #2000ms 1up SS
list10 = [10]*stepsPerStair #2000ma 3up SS
list11 = [11]*stepsPerStair #2000ms 1up BB
list12 = [12]*stepsPerStair #2000ms 3up BB

list13 = [13]*stepsPerStair # control 15ms 1UP
list14 = [14]*stepsPerStair # control 15ms 3UP
list15 = [15]*stepsPerStair # control 150ms 1UP
list16 = [16]*stepsPerStair # control 150ms 3UP
list17 = [17]*stepsPerStair # control 2000ms 1UP
list18 = [18]*stepsPerStair # control 2000ms 3UP


stairList = list1+list2+list3+list4+list5+list6+list7+list8+list9+list10+list11+list12+list13+list14+list15+list16+list17+list18
random.shuffle(stairList)
totalTrials = stepsPerStair*18

#create a blank list to store responses
#and to store the size of steps
responseList = []
responseList2 = []
sizeList1 = [] #15ms 1up SS
sizeList2 = [] #15ms 3up SS
sizeList3 = [] #15ms 1up BB
sizeList4 = [] #15ms 3up BB
sizeList5 = [] #150ms 1up SS
sizeList6 = [] #150ms 3up SS
sizeList7 = [] #150ms 1up BB
sizeList8 = [] #150ms 3ip BB
sizeList9 = []  #2000ms 1up SS
sizeList10 = [] #2000ma 3up SS
sizeList11 = [] #2000ms 1up BB
sizeList12 = [] #2000ms 3up BB
sizeList13 = [] # Control 15ms 1up
sizeList14 = [] # Control 15ms 3up
sizeList15 = [] # Control 150ms 1up
sizeList16 = [] # Control 150ms 3up
sizeList17 = [] # Control 2000ms 1up
sizeList18 = [] # Control 2000ms 3up
trialNum = 0 

#This will repeat until the number of trials equals the total trials we want 
while int(len(responseList)) < int(totalTrials):
    #determine which stair we are on from list 
    thisStair = stairList[trialNum]
    
    if len(responseList) % (totalTrials//2) == 0 and len(responseList) != 0:
        message = visual.TextStim(win, text='Please take a break - switch on the lights')
        message.draw()
        win.flip()
        
        psychopy.event.waitKeys(500000, keyList=None, modifiers=False, timeStamped=False, clearEvents=True)
    
    #decide what size river obstacle based on stair:
    #and then print the object to the screen
         
   
    if thisStair == 1 or thisStair == 3:  #15ms 11p (ss and bb)
        ctr = False
        targetLength = tar15ms1up
        if thisStair == 1:
            ss = True
        elif thisStair == 3: 
            ss = False
    elif thisStair == 2 or thisStair == 4:
        ctr = False
        targetLength = tar15ms3up
        if thisStair == 2: 
            ss = True
        elif thisStair == 4: 
            ss = False
    elif thisStair == 5 or thisStair == 7:
        ctr = False
        targetLength = tar150ms1up
        if thisStair == 5: 
            ss = True
        elif thisStair == 7: 
            ss = False
    elif thisStair == 6 or thisStair == 8: 
        ctr = False
        targetLength = tar150ms3up
        if thisStair == 6: 
            ss = True
        elif thisStair == 8: 
            ss = False
    elif thisStair == 9 or thisStair == 11: 
        ctr = False
        targetLength = tar2000ms1up
        if thisStair == 9: 
            ss = True
        elif thisStair == 11: 
            ss = False
    elif thisStair == 10 or thisStair == 12: 
        ctr = False
        targetLength = tar2000ms3up
        if thisStair == 10: 
            ss = True
        elif thisStair == 12: 
            ss = False
    elif thisStair == 13: 
        targetLength = ctrl15ms1up
        ss = False
        ctr = True
    elif thisStair == 14: 
        targetLength = ctrl15ms3up
        ss = False
        ctr = True
    elif thisStair == 15: 
        targetLength = ctrl150ms1up
        ss = False
        ctr = True
    elif thisStair == 16: 
        targetLength = ctrl150ms3up
        ss = False
        ctr = True
    elif thisStair == 17: 
        targetLength = ctrl2000ms1up
        ss = False
        ctr = True
    elif thisStair == 18:
        targetLength = ctrl2000ms3up
        ss = False
        ctr = True
        

    foilLength = targetLength*foilScale   

    leftRight = random.randint(1,2)
    smallStoneStepSize = random.randint(smallStoneStepSizeRange[0]*10, smallStoneStepSizeRange[1]*10)
    smallStoneStepSize = smallStoneStepSize/10/scaleFactor
    jit = 1.35+(random.randint(jitRange[0]*10, jitRange[1]*10)/10)/scaleFactor
    horJit = 1.5#1+(random.randint(horJitRange[0]*10, horJitRange[1]*10)/10/0)/scaleFactor
    disJit = random.randint(1,2)
    
    if ss == True: 
        targetLength = float(targetLength) + float(smallStoneStepSize) + float(stoneSize)
        foilLength = float(foilLength)
    elif ss == False:
        foilLength = float(foilLength) + float(smallStoneStepSize) + float(stoneSize)
    

    rivWid = foilLength*1.1
   
    guidePos = -15+jit, 0+horJit   
    guideX, guideY = guidePos
    
    if leftRight == 1: #target is on the left (foil on right)
       
        if disJit == 1: #steps start at same place, stepping stone first, relevent step second
            firstStep = 1 # stepping stone first, relevent step second
            if ctr == True: 
                vertices = [(guideX+3.5+jit, 7+horJit), (guideX+3.5+rivWid+jit, 7+horJit), (guideX+5+targetLength+jit, 4+horJit), (guideX+5+targetLength+jit, 1+horJit), (guideX+3.5+rivWid+jit, -1+horJit), (guideX+3.5+rivWid+jit, -4+horJit), 
                            (guideX+3.5+rivWid+jit, -7+horJit), (guideX+3.5+jit, -7+horJit), (guideX+3.5+jit, -4+horJit), (guideX+3.5+jit, -1+horJit), (guideX+5+jit, 1+horJit), (guideX+5+jit, 4+horJit) ]
            elif ctr == False: 
                vertices = [(guideX+3.5+jit, 7+horJit), (guideX+3.5+rivWid+jit, 7+horJit), (guideX+5+targetLength+jit, 4+horJit), (guideX+5+targetLength+jit, 1+horJit), (guideX+5+foilLength+jit, -1+horJit), (guideX+5+foilLength+jit, -4+horJit), 
                        (guideX+3.5+rivWid+jit, -7+horJit), (guideX+3.5+jit, -7+horJit), (guideX+5+jit, -4+horJit), (guideX+5+jit, -1+horJit), (guideX+5+jit, 1+horJit), (guideX+5+jit, 4+horJit) ]    
            
            
            if ss == True: #Target is stepping stone (left)
                stoneVertices = (guideX+5+smallStoneStepSize+jit, 1.5+horJit), (guideX+5+smallStoneStepSize+jit, 3.5+horJit), (guideX+5+smallStoneStepSize+stoneSize+jit, 3.5+horJit), (guideX+5+smallStoneStepSize+stoneSize+jit, 1.5+horJit)
            elif ss == False: #Foil is steppingstone (right)
                stoneVertices = (guideX+5+smallStoneStepSize+jit, -1.5+horJit), (guideX+5+smallStoneStepSize+jit, -3.5+horJit), (guideX+5+smallStoneStepSize+stoneSize+jit, -3.5+horJit), (guideX+5+smallStoneStepSize+stoneSize+jit, -1.5+horJit)
           
            targetX, targetY = vertices[11]  
            foilX, foilY = vertices[9]
        
        if disJit == 2: 
            firstStep = 2
            if ctr == True:
                vertices = [(guideX+5+foilLength+smallStoneStepSize+stoneSize+1.5-rivWid+jit, 7+horJit), (guideX+5+foilLength+smallStoneStepSize+stoneSize+1.5+jit, 7+horJit), (guideX+5+foilLength+smallStoneStepSize+stoneSize+jit, 4+horJit), (guideX+5+foilLength+smallStoneStepSize+stoneSize+jit, 1+horJit), (guideX+5+foilLength+smallStoneStepSize+stoneSize+1.5+jit, -1+horJit), (guideX+5+foilLength+smallStoneStepSize+stoneSize+1.5+jit, -4+horJit), 
                        (guideX+5+foilLength+smallStoneStepSize+stoneSize+1.5+jit, -7+horJit), (guideX+5+foilLength+smallStoneStepSize+stoneSize+1.5-rivWid+jit, -7+horJit), (guideX+5+foilLength+smallStoneStepSize+stoneSize+1.5-rivWid+jit, -4+horJit), (guideX+5+foilLength+smallStoneStepSize+stoneSize+1.5-rivWid+jit, -1+horJit), (guideX+5+foilLength+smallStoneStepSize+stoneSize-targetLength+jit, 1+horJit), (guideX+5+foilLength+smallStoneStepSize+stoneSize-targetLength+jit, 4+horJit)] 
            elif ctr == False:  
                vertices = [(guideX+5+foilLength+smallStoneStepSize+stoneSize+1.5-rivWid+jit, 7+horJit), (guideX+5+foilLength+smallStoneStepSize+stoneSize+1.5+jit, 7+horJit), (guideX+5+foilLength+smallStoneStepSize+stoneSize+jit, 4+horJit), (guideX+5+foilLength+smallStoneStepSize+stoneSize+jit, 1+horJit), (guideX+5+foilLength+smallStoneStepSize+stoneSize+jit, -1+horJit), (guideX+5+foilLength+smallStoneStepSize+stoneSize+jit, -4+horJit), 
                        (guideX+5+foilLength+smallStoneStepSize+stoneSize+1.5+jit, -7+horJit), (guideX+5+foilLength+smallStoneStepSize+stoneSize+1.5-rivWid+jit, -7+horJit), (guideX+5+foilLength+smallStoneStepSize+stoneSize-foilLength+jit, -4+horJit), (guideX+5+foilLength+smallStoneStepSize+stoneSize-foilLength+jit, -1+horJit), (guideX+5+foilLength+smallStoneStepSize+stoneSize-targetLength+jit, 1+horJit), (guideX+5+foilLength+smallStoneStepSize+stoneSize-targetLength+jit, 4+horJit)]
             
            if ss == True: #target is stepping stone  (left)
                stoneVertices = (guideX+5+foilLength+stoneSize+jit, 1.5+horJit), (guideX+5+foilLength+stoneSize+jit, 3.5+horJit), (guideX+5+foilLength+jit, 3.5+horJit), (guideX+5+foilLength+jit, 1.5+horJit)
            elif ss == False: #Foil is stepping stone (right)  
                stoneVertices = (guideX+5+foilLength+stoneSize+jit, -1.5+horJit), (guideX+5+foilLength+stoneSize+jit, -3.5+horJit), (guideX+5+foilLength+jit, -3.5+horJit), (guideX+5+foilLength+jit, -1.5+horJit)
                
            targetX, targetY = vertices[11]  
            foilX, foilY = vertices[9]
        
        
    elif leftRight == 2:#target is on the right (foil on left)
        
        if disJit == 1: # start in same place, stepping stone first, relevent step second
            firstStep = 1
            if ctr == True: 
                vertices = [(guideX+3.5+jit, 7+horJit), (guideX+3.5+rivWid+jit, 7+horJit), (guideX+3.5+rivWid+jit, 4+horJit), (guideX+3.5+rivWid+jit, 1+horJit), (guideX+5+targetLength+jit, -1+horJit), (guideX+5+targetLength+jit, -4+horJit), 
                        (guideX+3.5+rivWid+jit, -7+horJit), (guideX+3.5+jit, -7+horJit), (guideX+5+jit, -4+horJit), (guideX+5+jit, -1+horJit), (guideX+3.5+jit, 1+horJit), (guideX+3.5+jit, 4+horJit) ]
            elif ctr == False: 
                vertices = [(guideX+3.5+jit, 7+horJit), (guideX+3.5+rivWid+jit, 7+horJit), (guideX+5+foilLength+jit, 4+horJit), (guideX+5+foilLength+jit, 1+horJit), (guideX+5+targetLength+jit, -1+horJit), (guideX+5+targetLength+jit, -4+horJit), 
                        (guideX+3.5+rivWid+jit, -7+horJit), (guideX+3.5+jit, -7+horJit), (guideX+5+jit, -4+horJit), (guideX+5+jit, -1+horJit), (guideX+5+jit, 1+horJit), (guideX+5+jit, 4+horJit) ]
           
    
            if ss == True: #target = steppingStone (right)
                stoneVertices = (guideX+5+smallStoneStepSize+jit, -1.5+horJit), (guideX+5+smallStoneStepSize+jit, -3.5+horJit), (guideX+5+smallStoneStepSize+stoneSize+jit, -3.5+horJit), (guideX+5+smallStoneStepSize+stoneSize+jit, -1.5+horJit)
            elif ss == False: #Foil = steppingStone (left)
                stoneVertices = (guideX+5+smallStoneStepSize+jit, 1.5+horJit), (guideX+5+smallStoneStepSize+jit, 3.5+horJit), (guideX+5+smallStoneStepSize+stoneSize+jit, 3.5+horJit), (guideX+5+smallStoneStepSize+stoneSize+jit, 1.5+horJit)
            
            targetX, targetY = vertices[9]  
            foilX, foilY = vertices[11]
            
        elif disJit == 2: #end in same place, stepping stone second, relevent step first 
            firstStep = 2
            if ctr == True: 
                vertices = [(guideX+5+foilLength+smallStoneStepSize+stoneSize+1.5-rivWid+jit, 7+horJit), (guideX+5+foilLength+smallStoneStepSize+stoneSize+1.5+jit, 7+horJit), (guideX+5+foilLength+smallStoneStepSize+stoneSize+1.5+jit, 4+horJit), (guideX+5+foilLength+smallStoneStepSize+stoneSize+1.5+jit, 1+horJit), (guideX+5+foilLength+smallStoneStepSize+stoneSize+jit, -1+horJit), (guideX+5+foilLength+smallStoneStepSize+stoneSize+jit, -4+horJit), 
                        (guideX+5+foilLength+smallStoneStepSize+stoneSize+1.5, -7+horJit), (guideX+5+foilLength+smallStoneStepSize+stoneSize+1.5-rivWid+jit, -7+horJit), (guideX+5+foilLength+smallStoneStepSize+stoneSize-targetLength+jit, -4+horJit), (guideX+5+foilLength+smallStoneStepSize+stoneSize-targetLength+jit, -1+horJit), (guideX+5+foilLength+smallStoneStepSize+stoneSize+1.5-rivWid+jit, 1+horJit), (guideX+5+foilLength+smallStoneStepSize+stoneSize+1.5-rivWid+jit, 4+horJit)] 
            elif ctr == False: 
                vertices = [(guideX+5+foilLength+smallStoneStepSize+stoneSize+1.5-rivWid+jit, 7+horJit), (guideX+5+foilLength+smallStoneStepSize+stoneSize+1.5+jit, 7+horJit), (guideX+5+foilLength+smallStoneStepSize+stoneSize+jit, 4+horJit), (guideX+5+foilLength+smallStoneStepSize+stoneSize+jit, 1+horJit), (guideX+5+foilLength+smallStoneStepSize+stoneSize+jit, -1+horJit), (guideX+5+foilLength+smallStoneStepSize+stoneSize+jit, -4+horJit), 
                        (guideX+5+foilLength+smallStoneStepSize+stoneSize+1.5, -7+horJit), (guideX+5+foilLength+smallStoneStepSize+stoneSize+1.5-rivWid+jit, -7+horJit), (guideX+5+foilLength+smallStoneStepSize+stoneSize-targetLength+jit, -4+horJit), (guideX+5+foilLength+smallStoneStepSize+stoneSize-targetLength+jit, -1+horJit), (guideX+5+foilLength+smallStoneStepSize+stoneSize-foilLength+jit, 1+horJit), (guideX+5+foilLength+smallStoneStepSize+stoneSize-foilLength+jit, 4+horJit)]
            
            if ss == True: #target is stepping stone  (right)
                stoneVertices = (guideX+5+foilLength+stoneSize+jit, -1.5+horJit), (guideX+5+foilLength+stoneSize+jit, -3.5+horJit), (guideX+5+foilLength+jit, -3.5+horJit), (guideX+5+foilLength+jit, -1.5+horJit)
            elif ss == False: #Foil is stepping stone (Left)  
                stoneVertices = (guideX+5+foilLength+stoneSize+jit, 1.5+horJit), (guideX+5+foilLength+stoneSize+jit, 3.5+horJit), (guideX+5+foilLength+jit, 3.5+horJit), (guideX+5+foilLength+jit, 1.5+horJit)
  
            targetX, targetY = vertices[9]  
            foilX, foilY = vertices[11]
         
    #turn target length back to relevnt length for storage and next stage (remove extras of stepping stone)
    if ss == True: 
        targetLength = targetLength - smallStoneStepSize - stoneSize

    if ss == True: 
        stoneOrBank = 1
    elif ss == False: 
        stoneOrBank = 2

    
    guideToTar = guideX - targetX + jit
    '''    
    print(f'Trial number: {trialNum}')
    if stoneOrBank == 1: 
        print('Target == SS')
    elif stoneOrBank == 2:
        print('Target == BB')
    
    if leftRight == 1: 
        print('Target on left')
    elif leftRight == 2: 
        print('Target on Right')
        
    if disJit == 1: 
        print('START at same place')
        print('Stepping stone FIRST')
    elif disJit ==2: 
        print('END at same place')
        print('stepping stone SECOND')
    
    print(f'Staircase = {thisStair}')
    print('\n')
    print('\n')
    '''
    print(f' Trial Number: {trialNum}')  
    print(f' Stone or Bank: {stoneOrBank}')
    print(f' Staircase: {thisStair}')
    print(f' Target Length: {round(targetLength, 1)}')
    print(f' Position (left/right): {leftRight}')
    print(f' First Step (1=ss 1st, 2=ss 2nd): {firstStep}')
    print(f' Small Stepping Step Size: {round(smallStoneStepSize, 1)}')
    print(f' Disrupt Jitter: {disJit}')
    print(f' Jitter: {round(jit, 1)}')
    print(f' Stone Size: {round(stoneSize)}')
    print(f' Foil Length: {round(targetLength*foilScale)}')
    print(f' guide to Target: {round(guideToTar,1)}')
    print('\n')
    print('\n')
  
    
    #drawGuide and wait for participant to state tehy are ready (any key push)
    guide = visual.Rect(win=win, height=4, width=(0.1), pos = (guideX+jit, guideY), fillColor='yellow', units='cm')
    guide.draw()
    win.flip()
    
    psychopy.event.waitKeys(500000, keyList=None, modifiers=False, timeStamped=False, clearEvents=True)


    river = visual.ShapeStim(win, vertices=vertices, fillColor='blue', lineColor=None)
    guide.draw()
    river.draw()
    
    stone = visual.ShapeStim(win, vertices=stoneVertices, fillColor = 'yellow', lineColor = None)
    
    if ctr == False: 
        stone.draw()
    
    
    win.flip()
    #waitFunc(2000)
    #psychopy.event.waitKeys(500000, keyList=None, modifiers=False, timeStamped=False, clearEvents=True)
    
    if thisStair == 1 or thisStair == 2 or thisStair == 3 or thisStair == 4 or thisStair == 13 or thisStair == 14: 
        waitFunc(15) #15
    elif thisStair == 5 or thisStair == 6 or thisStair == 7 or thisStair == 8 or thisStair == 15 or thisStair == 16: 
        waitFunc(150) #150
    elif thisStair == 9 or thisStair == 10 or thisStair == 11 or thisStair == 12 or thisStair == 17 or thisStair == 18: 
        waitFunc(2000) #2000
    
    
        
    drawMask(15, 50)
    
    KeyPress = psychopy.event.waitKeys(500000, keyList=None, modifiers=False, timeStamped=False, clearEvents=True)
    
    #allows the user to terminate the experiemnet by pressing f instead of responding
    for key in KeyPress: 
        if key == 'f': 
            win.close()
            core.quit()
        else:
            response = key

        '''This allows a repeat of a trial by pressing 9. If no repeat needed, response is added to list'''
        
    
    if response == 9: 
        responseList.pop()# removed the last item in the list
        print(f" Trial:{trialNum}, staircase  {stairList[trialNum-1]}. re-do trial") 
        prevStair = stairList[trialNum-1]  # go back to previous stair
        if prevStair == 1:
            # get last item from sizelist1.  Pop() removed the item from the
            # list and keeps it as a new variable.  -1 is last value in list.
            currentSize1 = sizeList1.pop(-1)
        elif prevStair ==2:
            # get last item from sizelist2
            # now switch current size to previous size
            currentSize2 = sizeList2.pop(-1)
        elif prevStair == 3: 
            currentSize3 = sizeList3.pop(-1)
        elif prevStair == 4:
            currentSize4 = sizeList4.pop(-1)
        
   
    else:
            
        if thisStair == 1: 
            dataToSave = f"{stoneOrBank},{thisStair},{round(tar15ms1up*scaleFactor, 1)},{response},{leftRight},{firstStep},{round(guideToTar*scaleFactor)},{round(smallStoneStepSize*scaleFactor)},{round(disJit*scaleFactor)},{round(jit*scaleFactor)},{stoneSize*scaleFactor}\n"
        elif thisStair == 2: 
            dataToSave = f"{stoneOrBank},{thisStair},{round(tar15ms3up*scaleFactor,1)},{response},{leftRight},{firstStep},{round(guideToTar*scaleFactor)},{round(smallStoneStepSize*scaleFactor)},{round(disJit*scaleFactor)},{round(jit*scaleFactor)},{stoneSize*scaleFactor}\n"
        elif thisStair == 3: 
            dataToSave = f"{stoneOrBank},{thisStair},{round(tar15ms1up*scaleFactor,1)},{response},{leftRight},{firstStep},{round(guideToTar*scaleFactor)},{round(smallStoneStepSize*scaleFactor)},{round(disJit*scaleFactor)},{round(jit*scaleFactor)},{stoneSize*scaleFactor}\n"
        elif thisStair == 4: 
            dataToSave = f"{stoneOrBank},{thisStair},{round(tar15ms3up*scaleFactor,1)},{response},{leftRight},{firstStep},{round(guideToTar*scaleFactor)},{round(smallStoneStepSize*scaleFactor)},{round(disJit*scaleFactor)},{round(jit*scaleFactor)},{stoneSize*scaleFactor}\n"
        elif thisStair == 5: 
            dataToSave = f"{stoneOrBank},{thisStair},{round(tar150ms1up*scaleFactor, 1)},{response},{leftRight},{firstStep},{round(guideToTar*scaleFactor)},{round(smallStoneStepSize*scaleFactor)},{round(disJit*scaleFactor)},{round(jit*scaleFactor)},{stoneSize*scaleFactor}\n"
        elif thisStair == 6: 
            dataToSave = f"{stoneOrBank},{thisStair},{round(tar150ms3up*scaleFactor,1)},{response},{leftRight},{firstStep},{round(guideToTar*scaleFactor)},{round(smallStoneStepSize*scaleFactor)},{round(disJit*scaleFactor)},{round(jit*scaleFactor)},{stoneSize*scaleFactor}\n"
        elif thisStair == 7: 
            dataToSave = f"{stoneOrBank},{thisStair},{round(tar150ms1up*scaleFactor,1)},{response},{leftRight},{firstStep},{round(guideToTar*scaleFactor)},{round(smallStoneStepSize*scaleFactor)},{round(disJit*scaleFactor)},{round(jit*scaleFactor)},{stoneSize*scaleFactor}\n"
        elif thisStair == 8: 
            dataToSave = f"{stoneOrBank},{thisStair},{round(tar150ms3up*scaleFactor,1)},{response},{leftRight},{firstStep},{round(guideToTar*scaleFactor)},{round(smallStoneStepSize*scaleFactor)},{round(disJit*scaleFactor)},{round(jit*scaleFactor)},{stoneSize*scaleFactor}\n"    
        elif thisStair == 9: 
            dataToSave = f"{stoneOrBank},{thisStair},{round(tar2000ms1up*scaleFactor, 1)},{response},{leftRight},{firstStep},{round(guideToTar*scaleFactor)},{round(smallStoneStepSize*scaleFactor)},{round(disJit*scaleFactor)},{round(jit*scaleFactor)},{stoneSize*scaleFactor}\n"
        elif thisStair == 10: 
            dataToSave = f"{stoneOrBank},{thisStair},{round(tar2000ms3up*scaleFactor,1)},{response},{leftRight},{firstStep},{round(guideToTar*scaleFactor)},{round(smallStoneStepSize*scaleFactor)},{round(disJit*scaleFactor)},{round(jit*scaleFactor)},{stoneSize*scaleFactor}\n"
        elif thisStair == 11: 
            dataToSave = f"{stoneOrBank},{thisStair},{round(tar2000ms1up*scaleFactor,1)},{response},{leftRight},{firstStep},{round(guideToTar*scaleFactor)},{round(smallStoneStepSize*scaleFactor)},{round(disJit*scaleFactor)},{round(jit*scaleFactor)},{stoneSize*scaleFactor}\n"
        elif thisStair == 12: 
            dataToSave = f"{stoneOrBank},{thisStair},{round(tar2000ms3up*scaleFactor,1)},{response},{leftRight},{firstStep},{round(guideToTar*scaleFactor)},{round(smallStoneStepSize*scaleFactor)},{round(disJit*scaleFactor)},{round(jit*scaleFactor)},{stoneSize*scaleFactor}\n" 
        elif thisStair == 13: 
            dataToSave = f"{stoneOrBank},{thisStair},{round(ctrl15ms1up*scaleFactor,1)},{response},{leftRight},{firstStep},{round(guideToTar*scaleFactor)},{round(smallStoneStepSize*scaleFactor)},{round(disJit*scaleFactor)},{round(jit*scaleFactor)},{stoneSize*scaleFactor}\n"
        elif thisStair == 14: 
            dataToSave = f"{stoneOrBank},{thisStair},{round(ctrl15ms3up*scaleFactor,1)},{response},{leftRight},{firstStep},{round(guideToTar*scaleFactor)},{round(smallStoneStepSize*scaleFactor)},{round(disJit*scaleFactor)},{round(jit*scaleFactor)},{stoneSize*scaleFactor}\n"    
        elif thisStair == 15: 
            dataToSave = f"{stoneOrBank},{thisStair},{round(ctrl150ms1up*scaleFactor, 1)},{response},{leftRight},{firstStep},{round(guideToTar*scaleFactor)},{round(smallStoneStepSize*scaleFactor)},{round(disJit*scaleFactor)},{round(jit*scaleFactor)},{stoneSize*scaleFactor}\n"
        elif thisStair == 16: 
            dataToSave = f"{stoneOrBank},{thisStair},{round(ctrl150ms3up*scaleFactor,1)},{response},{leftRight},{firstStep},{round(guideToTar*scaleFactor)},{round(smallStoneStepSize*scaleFactor)},{round(disJit*scaleFactor)},{round(jit*scaleFactor)},{stoneSize*scaleFactor}\n"
        elif thisStair == 17: 
            dataToSave = f"{stoneOrBank},{thisStair},{round(ctrl2000ms1up*scaleFactor,1)},{response},{leftRight},{firstStep},{round(guideToTar*scaleFactor)},{round(smallStoneStepSize*scaleFactor)},{round(disJit*scaleFactor)},{round(jit*scaleFactor)},{stoneSize*scaleFactor}\n"
        elif thisStair == 18: 
            dataToSave = f"{stoneOrBank},{thisStair},{round(ctrl2000ms3up*scaleFactor,1)},{response},{leftRight},{firstStep},{round(guideToTar*scaleFactor)},{round(smallStoneStepSize*scaleFactor)},{round(disJit*scaleFactor)},{round(jit*scaleFactor)},{stoneSize*scaleFactor}\n"  
        responseList.append(dataToSave)
        
       
        components = dataToSave.split(',')
        selectedData = ",".join(components[1:4]) + '\n'
        responseList2.append(selectedData)
        
        if trialNum < len(stairList):
            trialNum += 1
    '''     
    Adaptive Staircase: 
    This part is an adaptive staircase that changes the stimuli that will be presneted based on
    the participant's response. Each condition has two stairs, (a three-up, one down and 
    a one-down, three-up.)' This experiment starts with large step-sizes that change as participants 
    judge a 1-up, 3-down staircase as not-graspable and vice-versa.
    '''
#changes the sizes for the relevent staircase based on participant's response     
    if thisStair == 1 or thisStair == 3:
        if thisStair == 1: 
            sizeList1.append(tar15ms1up)
        else: 
            sizeList2.append(tar15ms1up)
        if response == "1" : 
            tar15ms1up = (tar15ms1up + (stepSize*0.5))
            bigSteps15ms1up = False
        elif response == "2": 
            if bigSteps15ms1up == True: 
                tar15ms1up = (tar15ms1up - (stepSize*3))
            else: 
                tar15ms1up = (tar15ms1up - (stepSize*3*0.5))          
             
    elif thisStair == 2 or thisStair == 4: 
        if thisStair == 2: 
            sizeList2.append(tar15ms3up)
        else: 
            sizeList4.append(tar15ms3up)
        if response == "1": 
            if bigSteps15ms3up == True: 
                tar15ms3up = (tar15ms3up + (3*stepSize))
            elif bigSteps15ms3up == False: 
                tar15ms3up = ((tar15ms3up +3*0.5*stepSize))
        elif response == "2": 
            bigSteps15ms3up = False 
            tar15ms3up = (tar15ms3up - (stepSize*0.5))

    elif thisStair == 5 or thisStair == 7:
        if thisStair == 5: 
            sizeList5.append(tar150ms1up)
        else: 
            sizeList7.append(tar150ms1up)
        if response == "1" : 
            tar150ms1up = (tar150ms1up + (stepSize*0.5))
            bigSteps150ms1up = False
        elif response == "2": 
            if bigSteps150ms1up == True: 
                tar150ms1up = (tar150ms1up - (stepSize*3))
            else: 
                tar150ms1up = (tar150ms1up - (stepSize*3*0.5))
             
    elif thisStair == 6 or thisStair == 8: 
        if thisStair == 6: 
            sizeList6.append(tar150ms3up)
        else: 
            sizeList8.append(tar150ms3up)
        if response == "1": 
            if bigSteps150ms3up == True: 
                tar150ms3up = (tar150ms3up + (3*stepSize))
            elif bigSteps150ms3up == False: 
                tar150ms3up = ((tar150ms3up +3*0.5*stepSize))
        elif response == "2": 
            bigSteps150ms3up = False 
            tar150ms3up = (tar150ms3up - (stepSize*0.5))   
            
    elif thisStair == 9 or thisStair == 11:
        if thisStair == 9: 
            sizeList9.append(tar2000ms1up)
        else: 
            sizeList11.append(tar2000ms1up)
        if response == "1" : 
            tar2000ms1up = (tar2000ms1up + (stepSize*0.5))
            bigSteps2000ms1up = False
        elif response == "2": 
            if bigSteps2000ms1up == True: 
                tar2000ms1up = (tar2000ms1up - (stepSize*3))
            else: 
                tar2000ms1up = (tar2000ms1up - (stepSize*3*0.5))
                
             
    elif thisStair == 10 or thisStair == 12: 
        if thisStair == 10: 
            sizeList10.append(tar2000ms3up)
        else: 
            sizeList12.append(tar2000ms3up)
        if response == "1": 
            if bigSteps2000ms3up == True: 
                tar2000ms3up = (tar2000ms3up + (3*stepSize))
            elif bigSteps2000ms3up == False: 
                tar2000ms3up = ((tar2000ms3up +3*0.5*stepSize))
        elif response == "2": 
            bigSteps2000ms3up = False 
            tar2000ms3up = (tar2000ms3up - (stepSize*0.5))
    

    elif thisStair == 13:
        sizeList13.append(ctrl15ms1up)
        if response == "1" : 
            ctrl15ms1up = (ctrl15ms1up + (stepSize*0.5))
            bigStepsCtrl15ms1Up = False
        elif response == "2": 
            if bigStepsCtrl15ms1Up == True: 
                ctrl15ms1up = (ctrl15ms1up - (stepSize*3))
            else: 
                ctrl15ms1up = (ctrl15ms1up - (stepSize*3*0.5))

    elif thisStair == 14:
        sizeList14.append(ctrl15ms3up)
        if response == "1": 
            if bigStepsCtrl15ms3Up == True: 
                ctrl15ms3up = (ctrl15ms3up + (3*stepSize))
            elif bigStepsCtrl15ms3Up == False: 
                ctrl15ms3up = ((ctrl15ms3up +3*0.5*stepSize))
        elif response == "2": 
            bigStepsCtrl15ms3Up = False 
            ctrl15ms3up = (ctrl15ms3up - (stepSize*0.5))
       
    elif thisStair == 15:
        sizeList15.append(ctrl150ms1up)
        if response == "1" : 
            ctrl150ms1up = (ctrl150ms1up + (stepSize*0.5))
            bigStepsCtrl150ms1Up = False
        elif response == "2": 
            if bigStepsCtrl150ms1Up == True: 
                ctrl150ms1up = (ctrl150ms1up - (stepSize*3))
            else: 
                ctrl150ms1up = (ctrl150ms1up - (stepSize*3*0.5))

    elif thisStair == 16:
        sizeList16.append(ctrl150ms3up)
        if response == "1": 
            if bigStepsCtrl150ms3Up == True: 
                ctrl150ms3up = (ctrl150ms3up + (3*stepSize))
            elif bigStepsCtrl150ms3Up == False: 
                ctrl150ms3up = ((ctrl150ms3up +3*0.5*stepSize))
        elif response == "2": 
            bigStepsCtrl150ms3Up = False 
            ctrl150ms3up = (ctrl150ms3up - (stepSize*0.5))
            
    elif thisStair == 17:
        sizeList17.append(ctrl2000ms1up)
        if response == "1" : 
            ctrl2000ms1up = (ctrl2000ms1up + (stepSize*0.5))
            bigStepsCtrl2000ms1Up = False
        elif response == "2": 
            if bigStepsCtrl2000ms1Up == True: 
                ctrl2000ms1up = (ctrl2000ms1up - (stepSize*3))
            else: 
                ctrl2000ms1up = (ctrl2000ms1up - (stepSize*3*0.5))

    elif thisStair == 18:
        sizeList18.append(ctrl2000ms3up)
        if response == "1": 
            if bigStepsCtrl2000ms3Up == True: 
                ctrl2000ms3up = (ctrl2000ms3up + (3*stepSize))
            elif bigStepsCtrl2000ms3Up == False: 
                ctrl2000ms3up = ((ctrl2000ms3up +3*0.5*stepSize))
        elif response == "2": 
            bigStepsCtrl2000ms3Up = False 
            ctrl2000ms3up = (ctrl2000ms3up - (stepSize*0.5))
       
       
    if tar15ms1up <= smallestSize:
        tar15ms1up = smallestSize
    if tar15ms3up <= smallestSize:
        tar15ms3up = smallestSize
    if tar150ms1up <= smallestSize: 
        tar150ms1up = smallestSize
    if tar150ms3up <= smallestSize: 
        tar150ms3up = smallestSize
    if tar2000ms1up <= smallestSize: 
        tar2000ms1up = smallestSize
    if tar2000ms3up <= smallestSize: 
        tar2000ms3up = smallestSize
    if ctrl15ms1up <= smallestSize: 
        ctrl15ms1up = smallestSize
    if ctrl15ms3up <= smallestSize: 
        ctrl15ms3up = smallestSize
    if ctrl150ms1up <= smallestSize: 
        ctrl150ms1up = smallestSize
    if ctrl150ms3up <= smallestSize: 
        ctrl150ms3up = smallestSize
    if ctrl2000ms1up <= smallestSize: 
        ctrl2000ms1up = smallestSize
    if ctrl2000ms3up <= smallestSize: 
        ctrl2000ms3up = smallestSize
    
    
'''records responses'''
writeResponse = open(fileName, "a+")
writeResponse2 = open(fileName2, "a+")
writeResponse.write("stepping stone or bank-to-bank, staircase, target length, response, Position, stepping stone order, Guide-to-target distance,Irrelevent (small) stone step size,  dirupt jitter, jitter, stone size\n")
writeResponse.write("1=stepping stone  2= bank-to-bank, , , ,Position = Position of target 1=Left  2=right, stepping stone order. 1= target length after stone  2=target length before stone, , ,disrupt jitter= jitter between guide(ps) and target start location, jitter=jitter of all stimuli 9 (and ps) (in relation to room), ,\n")
writeResponse.write(f'Irrelevent(small) step stone range = {smallStoneStepSize}\n')
for dataRow in responseList:
    writeResponse.write(dataRow)
#    writeResponse.write(input("Notes: How did you find the study? Did you use any methods/strategies? Anything else to note? "))
for dataRow in responseList2: 
    writeResponse2.write(dataRow)
writeResponse.close()
writeResponse2.close()

'''#closes window and quits programe - do both to work on Spyder and Psychopy'''
win.close()
core.quit()