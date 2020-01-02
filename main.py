from tkinter import *
import math
import os

coordList = {}
actionList = {}
botAngle = 0
botX = 0
botY = 0
stringToAngle = ""
nameProgram = ""
groupProgram = ""
firstPoint = True
filePath = ""
locatePath = ""

d = open("fileLocationSaver.txt","r")
locatePath = d.readline()

test = Tk()
test.title("Choose starting condition")
def blueDepot(event):
    global botX,botY, botAngle
    botX = 307
    botY = 307
    botAngle = 135
    return
def blueCrater(event):
    global botX, botY, botAngle
    botX = 227
    botY = 307
    botAngle = 45
    return
def redDepot(event):
    global botX, botY, botAngle
    botX = 225
    botY = 225
    botAngle = 315
    return
def redCrater(event):
    global botX, botY, botAngle
    botX = 307
    botY = 225
    botAngle = 225
    return
def quit(self):
    self.test.destroy()
    return
framebox = Frame(test, width = 100, height = 100)
framebox.pack()
blueDepotButt = Button(framebox, text = "Blue Depot", command = test.destroy)
blueDepotButt.bind("<Button-1>",blueDepot)
blueDepotButt.pack(side = TOP)
blueCraterButt = Button(framebox, text = "Blue Crater", command = test.destroy)
blueCraterButt.bind("<Button-1>",blueCrater)
blueCraterButt.pack(side = TOP)
redDepotButt = Button(framebox, text = "Red Depot", command = test.destroy)
redDepotButt.bind("<Button-1>",redDepot)
redDepotButt.pack(side = TOP)
redCraterButt = Button(framebox, text = "Red Crater", command = test.destroy)
redCraterButt.bind("<Button-1>",redCrater)
redCraterButt.pack(side = TOP)

test.mainloop()

root = Tk()
root.title("Plus or Minos program generator")




# def clicking(event):
#     global botAngle, botX, botY
#     coordList[len(coordList)] = str(event.x)+", "+str(event.y)+" Angle: "+str(botAngle)
#     if int(math.degrees(math.atan2(event.x - botX, event.y - botY))) - botAngle < 0:
#         actionList[len(actionList)] = "             robot.encoderDrive(" + str((int(math.degrees(math.atan2((540-event.y) - (540-botY), event.x - botX))) + botAngle)) + "," + str(10 * int(math.sqrt(((botX - event.x) ** 2) + ((botY - event.y) ** 2)))) + ");"
#     else:
#         actionList[len(actionList)] = "             robot.encoderDrive(" + str(int(math.degrees(math.atan2((540-event.y) - (540-botY), event.x - botX))) - botAngle) + "," + str(10 * int(math.sqrt(((botX - event.x) ** 2) + ((botY - event.y) ** 2)))) + ");"
#
#     # if int(math.degrees(math.atan2(event.y - botY, event.x - botX))) > 0:
#     #     actionList[len(actionList)] = "             robot.encoderDrive(" + str(botAngle+(360-int(math.degrees(math.atan2(event.y - botY, event.x - botX))))) + "," + str(10 * int(math.sqrt(((botX - event.x) ** 2) + ((botY - event.y) ** 2)))) + ");" + str(int(math.degrees(math.atan2(event.y - botY, event.x - botX))))
#     # else:
#     #     actionList[len(actionList)] = "             robot.encoderDrive(" + str(botAngle+abs(int(math.degrees(math.atan2(event.y - botY, event.x - botX))))) + "," + str(10 * int(math.sqrt(((botX - event.x) ** 2) + ((botY - event.y) ** 2)))) + ");" + str(int(math.degrees(math.atan2(event.y - botY, event.x - botX))))
#     botX = event.x
#     botY = event.y
#     python_color = "#af271d"
#     x1, y1 = (event.x - 4), (event.y - 4)
#     x2, y2 = (event.x + 4), (event.y + 4)
#     topFrame.create_oval(x1, y1, x2, y2, fill=python_color)
def clicking(event):
    global botAngle, botX, botY
    angle = int(math.degrees(math.atan2(event.y - botY, event.x - botX)))
    if angle >= 0 and angle < 90:
        angle = 360 - angle
    elif angle >= 90 and angle <= 180:
        angle = angle + 90
    elif angle <= -90 and angle >= -180:
        angle = abs(angle)
    elif angle <= 0 and angle > -90:
        angle = abs(angle)

    angle = angle - botAngle
    if angle < 0:
        angle = angle + 360
    angle += 90
    actionList[len(actionList)] = "             robot.encoderDrive(" + str(angle) + "," + str(int(5.28122807018*math.sqrt(((botX - event.x) ** 2) + ((botY - event.y) ** 2)))) + ");"
    botX = event.x
    botY = event.y
    python_color = "#af271d"
    x1, y1 = (event.x - 4), (event.y - 4)
    x2, y2 = (event.x + 4), (event.y + 4)
    topFrame.create_oval(x1, y1, x2, y2, fill=python_color)
    return

def addAngle(event):
    global botAngle, botX,botY
    angleString = angle.get()
    botAngle = botAngle + int(angleString)
    actionList[len(actionList)] = "             robot.encoderSpin("+angleString+");"
    coordList[len(coordList)] = str(botX)+", "+str(botY)+" Angle: "+angleString
    return
def addName(event):
    global nameProgram
    nameProgram = name.get()
    return
def addGroup(event):
    global groupProgram
    groupProgram = group.get()
    return
def locateSet(event):
    global locatePathPath
    locatePath = location.get()
    return
def dorpTheBox(event):
    actionList[len(actionList)] = "             robot.flagDrop.setPosition(1);"
    actionList[len(actionList)] = "             runtime.reset();"
    actionList[len(actionList)] = "             while(opModeIsActive() && runtime.seconds()<=.75){"
    actionList[len(actionList)] = "             "
    actionList[len(actionList)] = "             }"
    actionList[len(actionList)] = "             robot.flagDrop.setPosition(0);"
    return
def printCode(event):
    global locatePath, nameProgram
    filePath = os.path.join(locatePath, nameProgram+".java")
    f = open(filePath,"w+")
    f.write("""/* Copyright (c) 2017 FIRST. All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without modification,
 * are permitted (subject to the limitations in the disclaimer below) provided that
 * the following conditions are met:
 *
 * Redistributions of source code must retain the above copyright notice, this list
 * of conditions and the following disclaimer.
 *
 * Redistributions in binary form must reproduce the above copyright notice, this
 * list of conditions and the following disclaimer in the documentation and/or
 * other materials provided with the distribution.
 *
 * Neither the name of FIRST nor the names of its contributors may be used to endorse or
 * promote products derived from this software without specific prior written permission.
 *
 * NO EXPRESS OR IMPLIED LICENSES TO ANY PARTY'S PATENT RIGHTS ARE GRANTED BY THIS
 * LICENSE. THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 * "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
 * THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE
 * FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
 * DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
 * SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
 * CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
 * OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
 * OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */\n""")
    f.write("""package org.firstinspires.ftc.teamcode;

import com.qualcomm.robotcore.eventloop.opmode.Autonomous;
import com.qualcomm.robotcore.eventloop.opmode.Disabled;
import com.qualcomm.robotcore.eventloop.opmode.LinearOpMode;
import com.qualcomm.robotcore.hardware.DcMotor;
import com.qualcomm.robotcore.util.ElapsedTime;

import org.firstinspires.ftc.robotcontroller.external.samples.HardwarePushbot;\n""")
    f.write("//Built using Team 11654 (Plus or Minos)'s quick autonomous creator\n")
    f.write('@Autonomous(name="' + nameProgram + '", group="' + groupProgram + '")\n')
    f.write("//@Disabled\n")
    f.write("public class " + nameProgram + " extends LinearOpMode {\n")
    f.write("""
        /* Declare OpMode members. */
        HardwareDrive robot = new HardwareDrive();
        Varibles var = new Varibles();
        private ElapsedTime     runtime = new ElapsedTime();
        @Override
        public void runOpMode() {

            /*
             * Initialize the drive system variables.
             * The init() method of the hardware class does all the work here
             */
            robot.init(hardwareMap);

            // Send telemetry message to signify robot waiting;
            telemetry.addData("Status", "Ready to run");    
            telemetry.update();

            // Wait for the game to start (driver presses PLAY)
            waitForStart();
            robot.platIn();
            runtime.reset();
            while (opModeIsActive() && runtime.seconds() <= 2.4){

            }
            robot.platStop();

            robot.encoderStrut(-1940, false, 0);
            robot.hook.setPosition(1);
            runtime.reset();
            while (opModeIsActive() && runtime.seconds() <= 4){

            }
            robot.encoderStrut(2040, true, 4);
            robot.hook.setPosition(0);
            robot.platOut();
            runtime.reset();
            while (opModeIsActive() && runtime.seconds() <= 2.4){

            }
            robot.platStop();
            //begin generated code
                               
\n""")
    for i in range(0, len(actionList)):
        f.write(actionList[i]+"\n")
    f.write("""   
        }
    }\n""")
    for i in range(0, len(coordList)):
        f.write("//" + str(coordList[i])+"\n")
    return
namePanel = Frame(root, width = 540, height = 10)
namePanel.pack(side = TOP)
nameLabel = Label(namePanel, text = "Name: ")
nameLabel.pack(side = LEFT)
name = Entry(namePanel)
name.pack(side = LEFT)
nameButton = Button(namePanel, text = "Set name of program")
nameButton.bind("<Button-1>",addName)
nameButton.pack(side = LEFT)
groupLabel = Label(namePanel, text = "Group Name")
groupLabel.pack(side = LEFT)
group = Entry(namePanel)
group.pack(side = LEFT)
groupButton = Button(namePanel, text = "Set Group")
groupButton.bind("<Button-1>",addGroup)
groupButton.pack(side = LEFT)

sidePanel = Frame(root, width = 100, height = 540)
sidePanel.pack(side = LEFT)

locatePanel = Frame(root, width = 540, height = 10)
locatePanel.pack(side = BOTTOM)

buttonAngle = Button(sidePanel,text = "Rotate")
buttonAngle.bind("<Button-1>",addAngle)
buttonAngle.pack(side = TOP)
angle = Entry(sidePanel)
angle.pack(side = TOP)
printButton = Button(sidePanel,text = "Print Code to File")
printButton.bind("<Button-1>",printCode)
printButton.pack(side = TOP)
dropBox = Button(sidePanel, text = "Place Down Marker")
dropBox.bind("<Button-1>", dorpTheBox)
dropBox.pack(side = TOP)

locateButton = Button(locatePanel, text = "Set file location")
locateButton.bind("<Button-1>",locateSet)
locateButton.pack(side = LEFT)
location = Entry(locatePanel)
location.pack(side = LEFT)


angleString = angle.get()

topFrame = Canvas(root, width = 540, height = 540)
topFrame.bind("<Button-1>",clicking)
topFrame.pack(side = RIGHT)

photo = PhotoImage(file = "Capture.png")

topFrame.create_image(0,0, image = photo, anchor = NW)
#ethan has hair
if firstPoint == True:
    python_color = "#3514ba"
    x1, y1 = (botX - 4), (botY - 4)
    x2, y2 = (botX + 4), (botY + 4)
    topFrame.create_oval(x1, y1, x2, y2, fill=python_color)
    firstPoint = False
root.mainloop()
