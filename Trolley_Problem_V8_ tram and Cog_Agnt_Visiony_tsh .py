## Trolley Problem Project
# @Professor: Robert Wset
#@Course CGSC5901
#@Author Steve Hightead
#@version V8.0, April 10, 2017

#import sys
#sys.path.append('E:\Desktop\CCMSuite3-master')

#Import modules from ccmsuite3
import ccm
from ccm.lib.actr import*

#log=ccm.log()

class TramWayEnvironment (ccm.Model):
    #Build the environment for Sophy and the Tram to live in
    tram=ccm.Model(isa='tram1', position='unknown')
    switchLever=ccm.Model(isa='leverl', position='mainLine')
    trackSwitch=ccm.Model(isa='switch', position='mainLine')
    people=ccm.Model(isa='five_people', condition='alive',position='mainLine4')

class MotorModule(ccm.Model):

# The Motor Module provides the movement for the Tram agent.
# The locations the Tram can move to are locations one, two three, trackswitch four and the spurline.
# In this version, the Cognitive agent can switch the tram for the mainline to a spurline.    
# If the Tram is not switched to the spurline, the tram kills fve pople on the mainline.

# Tran Motor 1
    def moveTramToOne(self):
        yield 2.5
        print ("Motor 1. Move the tram to Main Line Position One")
        self.parent.parent.tram.position='mainLine1'

#Tram Motor 2a
    def moveTramToTwo(self):
        yield 2
        print ("Motor 2a. Move the tram to Main Line Position Two")
        self.parent.parent.tram.position='mainLine2'

#Tram Motor 2b
    def moveTramToThree(self):
        yield 2
        print ("Motor 2b. Move the tram to Main Line Position Three")
        self.parent.parent.tram.position='mainLine3'

#Tram Motor 3
    def moveTramIntoSwitch(self):
        yield 2
        print ("Motor 3. Move the tram into the Switch")
        self.parent.parent.tram.position='intoSwitch'

# Tram Motor 4
    def tramInSwitch(self):
        yield 2
        print ("Motor 4. The Tram is passing through the Switch")
        self.parent.parent.tram.position='inSwitch'
        #self.parent.parent.trackSwitch.position='Mainline'

# Tram Motor 5
    def moveTramPastSwitch(self):
        yield 2
        print ("Motor 5. Move the tram past Switch")
        self.parent.parent.tram.position='pastSwitch'

# Tram Motor 6        
    def moveTramToFour(self):
        yield 2
        print ("Motor 6. Move the tram to Main Line Position four")
        self.parent.parent.tram.position='mainLine4'

# Tram Motor 7
    def moveTramToSpurLine(self):
        yield 2
        print ("Motor 7. Move the tram down the Spur Line")
        self.parent.parent.tram.position='spurLine'

# Tram Motor 8
    def tramStopMain(self):
        yield 2
        print ("Motor 8. Stop the tram on Main Line")
        self.parent.parent.tram.position='mainLineStopped'

# Tram Motor 9
    def tramStopSpur(self):
        yield 2
        print ("Motor 9. Stop the tram on the spur line")
        self.parent.parent.tram.position='spurLineStopped'

# Tram Motor 10
    def do_switch(self):
        yield 6  # ************Any delay greater that 7 kills people *******
        print ("Motor 10. Switch points activated to Spur Line")
        self.parent.parent.trackSwitch.position='spurLine'

# Tram Motor 11
    def killPeople(self):
        yield 2
        print ("Motor 11. Tram kills five people")
        self.parent.parent.people.condition='dead'

# Tram Motor 12
    def do_lever(self):
        print ("Motor 12. Lever is pulled from mainLine to spurLine")
        self.parent.parent.switchLever.position='spurLine'

# Tram Motor 13
    def peopleDanger(self):
        print ("Motor 13. Change the state of the people from safe to being in danger")
        self.parent.parent.people.condition='inDanger'
        
 
class TramAgent(ACTR):

    tramFocus=Buffer()
    motor=MotorModule()

# Tram starts it run 
# Tram moves to maiLine11   
    def init():
        tramFocus.set ('tram:moveTo1')
        motor.moveTramToOne() #Motor 1. tram.position:mainLine1
        print("Tram at mainLine1")

# Tram moves to mainLine2
    def tramOne(tramFocus='tram:moveTo1',
                tram='position:mainLine1'):
        print(" ")
        print("Tram 1.  Tram moves to Main Line position One")
        print("****Tram Position is ",tram.position," ****")
        motor.moveTramToTwo() #Motor 2. tram.position:mainLine2
        tramFocus.set('tram:moveTo2')

# Tram Moves to mainLine 3
    def tramTwo(tramFocus='tram:moveTo2',
                tram='position:mainLine2'):
        print(" ")
        print("Tram 2. The tram moves to Main Line position Two")
        print("***Tram Position is ",tram.position," ****")
        # print("***Track Switch is ",trackSwitch.position," ****")
        motor.moveTramToThree() #Motor 2b. tram.position:mainLine3
        tramFocus.set('tram:moveTo3')

    def tramTwoB(tramFocus='tram:moveTo3',
                tram='position:mainLine3'):
        print(" ")
        print("Tram 2b. The tram moves to Main Line position Three")
        print("***Tram Position is ",tram.position," ****")
        print("***Track Switch is ",trackSwitch.position," ****")
        motor.moveTramIntoSwitch() #Motor 3. tram.position:intoSwitch
        tramFocus.set('tram:moveIntoSwitch')

    def tramThree(tramFocus='tram:moveIntoSwitch',
                  tram='position:intoSwitch'):
        print(" ")
        print("Tram 3. Tram moves into the Switch")
        print("***Tram Position is ",tram.position," ****")
        print("***Track Switch Position is ",trackSwitch.position," ****")
        motor.tramInSwitch() #Motor 4. tram.position:inSwitch
        tramFocus.set('tram:move3')
        
    

    def tramSwitchA(tramFocus='tram:move3',
                    tram='position:inSwitch',
                    trackSwitch='position:mainLine'):
        print(" ")
        print("Tram 4. Tram moves through the switch")
        print("***Tram Position is ", tram.position," ****")
        print( "***Tram Switch Position is  ", trackSwitch.position," ****")
        motor.moveTramToFour() #Motor 6. tram.position:mainLine4
        tramFocus.set('tram:move5')


    def tramSwitchB(tramFocus='tram:move3',
                    tram='position:inSwitch',
                    trackSwitch='position:spurLine'):
        print(" ")
        print("Tram 5. Tram moves through the switch")
        print( "Switch lever has been pulled")
        print( "***Tram Position is ", tram.position," ****")
        print( "***Tram Switch Position is  ", trackSwitch.position," ****")
        motor.do_switch() #Motor 11. trackSwitch.position:spurLine
        tramFocus.set('tram:move6')

    def tramFour(tramFocus='tram:move5',
                 tram='position:mainLine4'):
        print(" ")
        print( "Tram 6. Tram moves to Main Line position Four ")
        print( "***Tram Position is ",tram.position," ****")
        print( "***Track Switch Position is ",trackSwitch.position," ****")
        motor.killPeople() #Motor 12. people.condition:dead
        tramFocus.set('tram:stopMain')

    def tramFive(tramFocus='tram:move6',
                 trackSwitch='position:spurLine'):
        print(" ")
        print( "Tram 7. Tram moves onto the Spur Line"," ****")
        motor.moveTramToSpurLine() #Motor 7.tram.position:spurLine5
        tramFocus.set('tram:stopSpur')

    def tramStopMain(tramFocus='tram:stopMain',
                   people='condition:dead'):
        print(" ")
        print( "Tram 8. Tram stops at Main Line position Four")
        print("After killing five people")
        print( "***Tram Position is ",tram.position," ****")
        print( "***Five people are ",people.condition," ****")
        motor.tramStopMain() #Motor 9. tram.position:mainLineStopped
        tramFocus.set('stop')
        
    def tramStopSpur(tramFocus='tram:stopSpur',
                   tram='position:spurLine'):
        print(" ")
        print( "Tram 9. Tram stops on the Spur Line")
        motor.tramStopSpur() #tram:spurLine5Stopped
        tramFocus.set('stop')

    def tramStop(tramFocus='stop',
                 tram='position:spurLineStopped'):
        print(" ")
        print( "Tram 10. production stop")
        print( "***Tram Position is ",tram.position," ****")

        
class SophyFeelings(ccm.ProductionSystem):
    productionTime=0.0

    def fear_for_people_safety(sophyFocus='sophy:seePeople'):
        print(" ")
        print( "Emotion 1. There are People on the Main Track")
        motor.peopleDanger() #Motor 13. people.condition:inDanger
        sophyFocus.set('people:danger')

    def must_save_people(sophyFocus='people:danger',
                         people='condition:inDanger'):
       print(" ")
       print( "Emotion 2a. Five People are in ", people.condition)
       print( "Emotion 2b. Must pull the track switch lever to save them!!!!!")
       motor.do_lever() #Motor 12. switchLever.position:spurLine
       sophyFocus.set('sophy:leverPull')
       
    def setTrackSwitch(sophyFocus='sophy:leverPull'):
        print(" ")
        print("Sophy pulls  track switch lever")
        print("This changes the track switch from mainline to spurLine")
        motor.do_switch() # ste trackSwitch to spurLine
        sophyFocus.set('sophy:waits')

    def people_are_safe(tram='position:spurLineStopped'):
        print(" ")
        print( "Track Switch Position is ",trackSwitch.position)
        print( "Emotion 3. People are safe!!!")
    
class MyAgent(ACTR):

    sophyFocus=Buffer()
    motor=MotorModule()
    emotion=SophyFeelings()
      
    def init():
        print(" ")
        print( "Sophy 0. Sophy arrives at the TramWay")
        sophyFocus.set('sophy:start')

    def arriveTramWay(sophyFocus='sophy:start',
                      tram='position:mainLine1'):
        print(" ")
        print( "Sophy 1. Sophy looks around")
        sophyFocus.set('sophy:lookForTram')  
       
    def lookForTram(sophyFocus='sophy:lookForTram'):
        print(" ")
        print( "Sophy 2. Looking for the tram")
        sophyFocus.set('sophy:see_a_tram')
        
    def foundTram(sophyFocus='sophy:see_a_tram'):
        print(" ")
        print( "Sophy 3. Sophy has found the tram")
        sophyFocus.set('sophy:lookForPeople')
        
    def lookForPeople(sophyFocus='sophy:lookForPeople'):
        print(" ")
        print("Sophy 4. Looking for people")
        sophyFocus.set('sophy:seePeople')

    def foundPeople(sophyFocus='sophy:seePeople'):
        print(" ")
        print( "Sophy 5. Found five people on the mainLine")
        sophyFocus.set('sophy:next1')

    def waitAnxiously(sophyFocus='sophy:waits'):
        print(" ")
        print( "Sophy 6.  Waits to see what happens")
        sophyFocus.set('sophy:stop')
                      
    def sophyStop(sophyFocus='sophy:stop',
                  tram='position:spurLineStopped'):
        print(" ")
        print( "Sophy 7. Sighs relief")
        self.stop()
        
    
print( "Production Start")
print( " ")

tramWay=TramWayEnvironment()

sophy=MyAgent()
tram=TramAgent()

tramWay.agent=sophy
tramWay.agent=tram


ccm.log_everything(tramWay)

tramWay.run()
ccm.finished()

print( " ")
print( "Production Stop")
