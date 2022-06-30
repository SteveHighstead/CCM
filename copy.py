from python_actr import *

class MyEnvironment(Model):
    pass

class MyAgent(ACTR):
    focus=Buffer()
    Imagebuffer=Buffer
    Visionbuffer=Buffer()
    DMbuffer=Buffer()
    DM=Memory(DMbuffer)

    
    def init():
        DM.add('isa:objectcontainer objectx:apple container:bowl')
        DM.add('isa:objectcontainer objectx:apple container:bucket')
        DM.add('isa:objectcontainer objectx:apple container:bin')
        
        DM.add('isa:containerlocation container:bowl location:house')
        DM.add('isa:containerlocation container:bucket location:store')
        DM.add('isa:containerlocation container:bin location:park')
        
        focus.set('status:start')
        Visionbuffer.set('isa:objectlocation objectx:apple location:house')


    #start trial
    def start(focus='status:start', Visionbuffer='isa:objectlocation objectx:?objectx'):
        print ("recalling based on objects")
        DM.request('isa:objectcontainer objectx:?objectx container:?')
        focus.set('status:get_container') 


    #recall a container for the target object
    def container(focus='status:get_container', 
                  DMbuffer='isa:objectcontainer objectx:?objectx container:?container'):  
        print (objectx)
        print ("is in .......")         
        print (container)
        DM.request('isa:containerlocation container:?container location:?')
        focus.set('status:get_location')
        

    #recall a location for the container the object is in
    def location(focus='status:get_location', 
                 DMbuffer='isa:containerlocation container:?container location:?location'):  
        print (container)
        print ("is in .......")         
        print (location)
        focus.set('status:check_location')


    #success
    def yes_location(focus='status:check_location', 
                     DMbuffer='container:?container location:?location', Visionbuffer='location:?location'):  
        print ('YES')
        focus.set('status:stop')


    #failure
    def no_location(focus='status:check_location', 
                    DMbuffer='container:?container location:?location', Visionbuffer='location:!?location'):  
        print ('NO')
        focus.set('status:stop')



tim=MyAgent()                              # name the agent
DM="test"
subway=MyEnvironment()                     # name the environment
subway.agent=tim                           # put the agent in the environment
log_everything(subway)                 # print out what happens in the environment

subway.run()                               # run the environment
#ccm.finished()