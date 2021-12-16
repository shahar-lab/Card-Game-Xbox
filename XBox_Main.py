from random import sample
from psychopy import core, visual, gui, data
# List of different block code files to run
blocks = ["rumblePress", "rumbleReward", "noRumble"]
import psychopy, pygame
import rumblePress, rumbleReward, noRumble

# 0 -> rumblePress
# 1 -> rumbleReward
# 2 -> noRumble


# Make a text file to save data
expInfo = {"subject": "00"}
dlg = gui.DlgFromDict(expInfo, title="Two-armed bandit task XBOX")
fileName = "XBox_rumblePress_" + expInfo["subject"] + "_" + data.getDateStr()
dataFile = open(
    fileName + ".csv", "w"
)  # a simple text file with 'comma-separated-values'
dataFile.write("Trial, Stimulus card 1, Stimulus card 2, Card 1 prob, Card 2 prob, Pressed button, Button ID, Chosen card\n")

# create a window
win = visual.Window(
       [800, 600], fullscr = True, monitor="testMonitor", units="deg", color=(255, 255, 255)
    )
mytimer = core.Clock()
slide1 = visual.ImageStim(win, image="Slide1.jpg",  units='norm', size=[2,2])
slide2 = visual.ImageStim(win, image="Slide2.jpg",  units='norm', size=[2,2])
slide3 = visual.ImageStim(win, image="Slide3.jpg",  units='norm', size=[2,2])

def main():
    instructions_phase = True
    currSlide = 1
    slidename = "slide" + currSlide
    slidename.draw()
    while instructions_phase:
            events = pygame.event.poll()
            slidename = "slide" + currSlide
            if (events.type == pygame.JOYBUTTONDOWN):
                #Event 0 -> Pressed A Button
                if events.button == 0:
                    currSlide += 1
                    win.update()


    
    indexList = sample(range(0, 3), 3)
    print(indexList)
    for x in indexList:
        if (x == 0):
            phase = "Starting New Block: Rumble When Pressing Button Block"
            dataFile.write("%s\n" % phase)
            #instructions/ma3var
            rumblePress.mainRumblePress(dataFile)
        elif (x == 1):
            phase = "Starting New Block: Rumble When Showing Reward Block"
            dataFile.write("%s\n" % phase)            
            rumbleReward.mainRumbleReward(dataFile)
        elif (x == 2):
            phase = "Starting New Block: No Rumble Block"
            dataFile.write("%s\n" % phase)
            noRumble.mainNoRumble(dataFile)

main()
