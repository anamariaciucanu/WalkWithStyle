import maya.cmds as cmds
import walking as wk
reload(wk)

widgets = {}
internalTypes = ['archetype', 'memory', 'personality', 'emotion', 'intention']
externalTypes = ['action']


def createGUI():
    #Create window
    windowID = 'E-Motion' 
    if (cmds.window(windowID, exists=True)):
        cmds.deleteUI(windowID, window=True)    
   
    widgets['window'] = cmds.window(windowID, title = "E-Motion: Emergent Procedural Character Animation")
    
    #Create layout
    widgets['winLayout'] = cmds.columnLayout(adj=True, rowSpacing = 10)
    
    #Create general parameters
    widgets['startFrame'] = cmds.intFieldGrp( numberOfFields=1, label='Animation Start Frame ')
    widgets['endFrame'] = cmds.intFieldGrp( numberOfFields=1, label='Animation End Frame ')
    widgets['FPS'] = cmds.intFieldGrp( numberOfFields=1, label='Frames per Seconds ')
    
    #Create tabs
    widgets['tabLayout'] = cmds.tabLayout(imh = 10, imw = 10)
    
    #Internal tab ------------------------------------------------
    widgets['internalTabLayout'] = cmds.columnLayout('Internal Motion', parent = widgets['tabLayout'], adj=True)         

    #Create Internal Motion types
    for internalType in internalTypes:
        cmds.separator(height = 20)
        widgets[internalType + 'Box'] = cmds.frameLayout(internalType.capitalize(), collapsable=True, collapse=False)
        cmds.setParent('..')
    
    createEmotionBox()
   
    #External tab -------------------------------------------------
    widgets['externalTabLayout'] = cmds.columnLayout('External Motion', parent = widgets['tabLayout'], adj=True)         

    #Create external motion types
    for externalType in externalTypes:
        cmds.separator(height = 20)
        widgets[externalType + 'Box'] = cmds.frameLayout(externalType.capitalize(), collapsable=True, collapse=False)
        
    createActionBox()
    
    #Create reset and generate button
    widgets['mainButtonsLayout'] = cmds.rowLayout('Main Buttons', parent = widgets['winLayout'], numberOfColumns=2)  
    widgets['resetButton'] = cmds.button( label='Reset', c = 'resetParameters()', h = 50, w = 200, align = 'left')
    widgets['generateButton'] = cmds.button( label='Generate', c = 'generateBehaviour()', h = 50, w = 200, align = 'right')
       
    #Show GUI 
    cmds.showWindow(widgets['window'])


def createEmotionBox():
    cmds.setParent(widgets['emotionBox'])   
    cmds.columnLayout()
    widgets['emotionType'] = cmds.optionMenu( label='Type of Emotion' )
    cmds.menuItem( label='Joy' )
    cmds.menuItem( label='Sadness' )
    cmds.menuItem( label='Anger' )
    cmds.menuItem( label='Fear' )    

    #cmds.setParent(widgets['emotionBox'])   
    widgets['emotionIntensity'] = cmds.intFieldGrp( numberOfFields=1, label='Emotion Intensity')
    
def createActionBox():
    cmds.setParent(widgets['actionBox'])     
    cmds.columnLayout()
    widgets['cyclicActionType'] = cmds.optionMenu( label='Type of Cyclic Action' )
    cmds.menuItem( label='Idle' )
    cmds.menuItem( label='Walking' )
    cmds.menuItem( label='Running' )    
    cmds.setParent(widgets['actionBox'])
    widgets['walkAmplitude'] = cmds.intFieldGrp( numberOfFields=1, label='Amplitude ')
    widgets['walkSpeed'] = cmds.intFieldGrp( numberOfFields=1, label='Speed ')
    
def resetParameters():
    endFrame = cmds.intFieldGrp(widgets['endFrame'], q = True, v = True)
    wk.resetFootTranslation(endFrame[0])
        
def generateWalk():
    _startFrame = cmds.intFieldGrp(widgets['startFrame'], q = True, v = True)
    _endFrame = cmds.intFieldGrp(widgets['endFrame'], q = True, v = True)
    _footAmplitude = cmds.intFieldGrp(widgets['walkAmplitude'], q = True, v = True)
    _footSpeed = cmds.intFieldGrp(widgets['walkSpeed'], q = True, v = True)
    _fps = cmds.intFieldGrp(widgets['FPS'], q = True, v = True)
    wk.createFootMotion(_startFrame[0], _endFrame[0], _footAmplitude[0], _footSpeed[0], 5, _fps[0])

def generateBehaviour():
    generateWalk()
    
createGUI()