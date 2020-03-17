import maya.cmds as cmds
import math

#Global variables
pi = math.pi
animationStart = 0
animationEnd = 100
frameInterval = 20 #similar to speed
footAmplitude = 10
ankleAmplitude = 5
footSpeed = 10.0

#Ellipse axes
asq = 3.0
bsq = 1.0

def resetFootTranslation(maxFrame):
    #Reset transformations
    cmds.setAttr('L_Foot_CTRL.translateX', 0)
    cmds.setAttr('L_Foot_CTRL.translateY', 0)
    cmds.setAttr('L_Foot_CTRL.translateZ', 0)
    cmds.setAttr('L_Foot_CTRL.Ankle', 0)
    
   #Delete key frames
    cmds.cutKey( 'L_Foot_CTRL', time=(0,maxFrame), attribute='translateX', option='keys' )
    cmds.cutKey( 'L_Foot_CTRL', time=(0,maxFrame), attribute='translateY', option='keys' )
    cmds.cutKey( 'L_Foot_CTRL', time=(0,maxFrame), attribute='translateZ', option='keys' )
    cmds.cutKey( 'L_Foot_CTRL', time=(0,maxFrame), attribute='Ankle', option='keys' )
    
def createFootMotion():
    for i in range(animationStart, animationEnd, frameInterval):
        for j in range (0, frameInterval, 1):
            if (i + j < animationEnd):
                teta = j*2*pi/frameInterval
                newX = 0  
                newY = footAmplitude * math.sin(teta) / asq
                newZ = footAmplitude * math.cos(teta) / bsq
                newAnkle = ankleAmplitude * (-math.sin(teta) + math.sin(2*teta)/2.0)
                
                                 
                print(" newAnkle ")
                print(newAnkle)
                                      
                oldX = cmds.getAttr('L_Foot_CTRL.translateX') 
                oldY = cmds.getAttr('L_Foot_CTRL.translateY') 
                oldZ = cmds.getAttr('L_Foot_CTRL.translateZ') 
                oldAnkle = cmds.getAttr('L_Foot_CTRL.Ankle') 
                    
                currentX = oldX 
                currentY = oldY + newY
                currentZ = oldZ - newZ           
                currentAnkle = newAnkle
    
                cmds.setAttr('L_Foot_CTRL.translateX', currentX)
                cmds.setKeyframe( 'L_Foot_CTRL', attribute='translateX', t=i+j )
                cmds.setAttr('L_Foot_CTRL.translateY', currentY)
                cmds.setKeyframe( 'L_Foot_CTRL', attribute='translateY', t=i+j )
                cmds.setAttr('L_Foot_CTRL.translateZ', currentZ)
                cmds.setKeyframe( 'L_Foot_CTRL', attribute='translateZ', t=i+j )   
                cmds.setAttr('L_Foot_CTRL.Ankle', currentAnkle)
                cmds.setKeyframe( 'L_Foot_CTRL', attribute='Ankle', t=i+j ) 
            else:
                break
                
resetFootTranslation(animationEnd)
createFootMotion()