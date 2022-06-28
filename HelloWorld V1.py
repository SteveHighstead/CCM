########################## HELLO WORLD ##########################

"""
@Author: Steve Highstead
@Title: Hello World_v1.py
@ 28 June 2022
@ Version: V2
"""

# import  actr from ccm.lib.actr import*
import python_actr
from python_actr.actr import *

###################### The Environment ############################

class Desk_Environment(python_actr.Model):
    
    """
    This model reads a message from a piece of paper
    then inputs the message via a keyboard
    to be displayed on a computer monitor
    The agent then reads the computer screen, and remembers the message.
    The message is recalled and displayed

    Note, the message can be changed by changing the note's message.

    kbd == keyboard
    vdu == video display unit (computer monitor)
    note == a piece of paper with something written on it.
    """

    kbd = python_actr.Model(isa='KBD', location='desk', message=None)
    vdu = python_actr.Model(isa='VDU', location='desk', screen=None, salience=0.9)
    note= python_actr.Model(isa='note', location='desk', message='Hello World', salience =0.9)
                              #note: salience= 0.5 the lowest for SOSVision to pick up 

######################### Motor Module ######################

class MotorModule(python_actr.Model):
    
    """
    The motor module modifes an envieonment 'chunk'
    do_kbd changes the message chunk to be 'msg'
    do_screen changes the screen display to display 'msg'
    """
    
    def do_KBD(self, msg):
        """ 
        Type message into the keyboard
        and if the keyboard contains information
        display it on the computer screen
        """
        yield 0 
        print("do_KBD") #For testing
        self.parent.parent.kbd.message= msg
        """ If the kbd has information then display it on the screen """
        self.parent.parent.vdu.screen= msg if msg != None else None

################ Agent Production Module ########################

class TheAgent(python_actr.ACTR):
    """
    This is a cognitive agent, TheAgent, also known as the production module.
    The agent reads a message from a piece of paper (the note) and commits it to
    memory. The agent recalls the message from memory and enters it into a keyboard.
    This inturn displays the message on the computer screen.
    The agent then reads the message off the computer screen, committing the information
    to memory. The message is then recalled from memory.
    """
  
# Focus Buffer    
    agentFocus = Buffer()

# Motor Module assignment   
    motorBuffer = Buffer()
    motor = MotorModule(motorBuffer)
    
# Memory Module assignment
    DMbuffer = Buffer()
    DM = Memory(DMbuffer,
                latency = 0,
                threshold = 0)
    
# Vision Module assignment
    vision_buffer = Buffer()
    vision = SOSVision(vision_buffer,
                       delay = 0.0,
                       delay_sd=None)


    def __init__(self):
        """ Intialize the production module """
        print("initialize")
        vision_buffer.clear()
        DMbuffer.clear()
        agentFocus.set('start')
        
    def read_note(agentFocus='start'):
        """ The Agent reads the note """  
        vision.request('isa:note message:?msg')
        print("Reading the note")
        agentFocus.set('memorize')
     
    def memorize(agentFocus = 'memorize',
                 vision_buffer= 'isa:note message:?msg'):
        """ The Agent commits the message on the note to memory """
        print(f"Committing {msg} to memory")
        self.DM.add('isa:message content:?msg')
        vision_buffer.clear()
        agentFocus.set('recall_message')

    def retrieve_message(agentFocus='recall_message'):
        """ Agent retrieves the message from memory """
        print("Recalling message")
        self.DM.request('isa:message content:?msg')
        agentFocus.set('Print_msg')

    def remember(agentFocus='Print_msg',
                 DMbuffer= 'isa:message content:?msg'):
        """ Agent recalls the message """
        print(f"I remember the message as {msg}" )
        agentFocus.set('KBD Input')
   
    def enter_msg(agentFocus= 'KBD Input',
                  DMbuffer= 'isa:message content:?msg'):
        """ The Agent enters message into the keyboard  """
        print(f"Entering {msg} into the keyboard")
        motor.do_KBD(msg)
        agentFocus.set('display')  
   
    def read_screen(agentFocus='display'):
        """ The Agent reads computer screenn  """
        vision.request('isa:VDU screen:?msg')
        print("Reading the computer screen")
        agentFocus.set('memorize_scr')
    
    def memorize_screen(agentFocus = 'memorize_scr',
                 vision_buffer='isa:VDU screen:?msg'):
        """ The Agent commits message to memeory   """
        #print("The Screen reads, ", msg)
        print(f"Committing {msg} to memory")
        self.DM.add('isa:scr_message content:?msg')
        vision_buffer.clear()
        agentFocus.set('recall_Scr_message')
 
    def retrieve_Scr_message(self, agentFocus='recall_Scr_message'):
        """ The Agent recalls the message from memory  """
        print("Recalling screen message")
        self.DM.request('isa:scr_message content:?msg')
        agentFocus.set('Scr_msg')

    def remember_scr(agentFocus='Scr_msg',
                 DMbuffer= 'isa:scr_message content:?msg'):
        """ The Agent remembers the screen message """
        print( msg )
        agentFocus.set('stop')
      
    def end_run(self, agentFocus= 'stop'):
        """ This ends the Agent production """
        self.stop()
        

##################### Production ###################################

"""
The production section instantiates the class and executes the model
It also logs the execution of the model for dipslay
"""
    
deskTop = Desk_Environment()      # name the environment

sophy = TheAgent()                # name the agent

deskTop.agent = sophy             # put the agent into the environment

python_actr.log_everything(deskTop)       # print out what happens in the environment

deskTop.run()                     # run the environment

#python_actr.finished()                    # stop the environment

##################### Finished  #########################################

