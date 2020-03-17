import maya.cmds as cmds
import math

#Global variables
pi = math.pi
animationStart = 0
animationEnd = 100
frameInterval = 20 #similar to speed
footAmplitude = 20

#Ellipse axes
asq = 2.0
bsq = 1.0

def resetFootTranslation(maxFrame):
    #Reset transformations
    cmds.setAttr('L_Foot_CTRL.translateX', 0)
    cmds.setAttr('L_Foot_CTRL.translateY', 0)
    cmds.setAttr('L_Foot_CTRL.translateZ', 0)
    
   #Delete key frames
    cmds.cutKey( 'L_Foot_CTRL', time=(0,maxFrame), attribute='translateX', option='keys' )
    cmds.cutKey( 'L_Foot_CTRL', time=(0,maxFrame), attribute='translateY', option='keys' )
    cmds.cutKey( 'L_Foot_CTRL', time=(0,maxFrame), attribute='translateZ', option='keys' )
    
def createFootMotion():
    for i in range(animationStart, animationEnd, frameInterval):
        for j in range (0, frameInterval, 1):
            if (i + j < animationEnd):
                teta = j*2*pi/frameInterval
                newX = 0  
                newY = footAmplitude * math.sin(teta) / asq
                newZ = footAmplitude * math.cos(teta) / bsq
                
                print(" sin(theta) ")
                print(newY)
                                      
                oldX = cmds.getAttr('L_Foot_CTRL.translateX') 
                oldY = cmds.getAttr('L_Foot_CTRL.translateY') 
                oldZ = cmds.getAttr('L_Foot_CTRL.translateZ') 
                    
                currentX = oldX 
                currentY = oldY - newY
                currentZ = oldZ - newZ           
    
                cmds.setAttr('L_Foot_CTRL.translateX', currentX)
                cmds.setKeyframe( 'L_Foot_CTRL', attribute='translateX', t=i+j )
                cmds.setAttr('L_Foot_CTRL.translateY', currentY)
                cmds.setKeyframe( 'L_Foot_CTRL', attribute='translateY', t=i+j )
                cmds.setAttr('L_Foot_CTRL.translateZ', currentZ)
                cmds.setKeyframe( 'L_Foot_CTRL', attribute='translateZ', t=i+j )   
            else:
                break
                
resetFootTranslation(animationEnd)
createFootMotion()