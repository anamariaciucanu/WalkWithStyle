import maya.cmds as cmds
import math

#Global variables
pi = math.pi
animationStart = 0
animationEnd = 100
frameInterval = 20 #similar to speed
footAmplitude = 10
ankleAmplitude = 5
footSpeed = 1.0

#Ellipse axes
asq = 3.0
bsq = 1


''' Resets feet translations to 0 and deletes keyframes on the foot controllers.'''
def resetFootTranslation(i_endFrame):    
    if (i_endFrame<=0):
        i_endFrame = animationEnd
        
    #Reset transformations
    for side in 'LR':
        for axis in 'XYZ':
            cmds.setAttr('%s_Foot_CTRL.translate%s' % (side, axis), 0)
            cmds.cutKey( '%s_Foot_CTRL'%side, time=(0,i_endFrame), attribute='translate%s'%axis, option='keys' )

    cmds.setAttr('L_Foot_CTRL.Ankle', 0)
    cmds.cutKey( 'L_Foot_CTRL', time=(0,i_endFrame), attribute='Ankle', option='keys' )
    
  
''' Creates the foot translation and rotation motion for the walk cycle'''    
def createFootMotion(i_startFrame, i_endFrame, i_footAmplitude, i_footSpeed, i_ankleAmplitude, i_fps):
    #TO DO: Add parameters n an objct
    #TO DO: Is fps really that?
    if (i_startFrame <=0):
        i_startFrame = animationStart    
    if (i_endFrame <=0):
        i_endFrame = animationEnd    
    if (i_footAmplitude <= 0):
        i_footAmplitude = footAmplitude
    if (i_footSpeed <= 0):
        i_footSpeed = footSpeed
    if (i_ankleAmplitude <= 0):
        i_ankleAmplitude = ankleAmplitude
    if (i_fps <= 0):
        i_fps = frameInterval        
        
    for i in range(i_startFrame, i_endFrame, i_fps):
        for j in range (0, i_fps, 1):
            if (i + j < i_endFrame):
                teta = j*2*pi/i_fps
                newX = 0                      
                newY = i_footAmplitude * math.sin(i_footSpeed * teta) / asq
                newZ = i_footAmplitude * math.cos(i_footSpeed * teta) / bsq
                newAnkle = i_ankleAmplitude * math.sin(0.9*(i_footSpeed * teta + math.pi)) #The + maph.pi is ispired by Zajac (2003)                           
                                      
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
            