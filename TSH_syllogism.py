"""
Created on Fri Jun 25 16:49:55 2021
@file:TSH-syllogism2.py
@author: Steve Highstead

Learning exercise using Imaginal Buffers and Declaraitive Memory

This model presents reasoning on the soundness of a syllogism, which is:
    Socrates is a man
    Man is mortal
    Therefore, Socrates is mortal
"""

#Set path to CCMSuite3 (on my computer. Different for other users)
import sys
sys.path.append('C:\CCMSuite3')

#Import CCM Architecture
import ccm                  # Import the ccm modelling modules
from ccm.lib.actr import *  # Import the ACT-R modelling modules


class Model(ACTR):
    
    # Set class attributes
    focus=Buffer()                     #focus or goal buffer
    IM1buffer = Buffer()               #Imaginal buffer temporary storage
    IM2buffer = Buffer()               #Imaginal buffer temporary storage
    DMbuffer=Buffer()                  #Declarative Memory buffer
    DM=Memory(DMbuffer,threshold=-0)   #Declarative memory 
 
    """ Production Rules """
    
    def init():
        """ 
        Intialize the model's production module
        Add the major and minor premises to declarative memory
        Set the focus buffer to 'start'
        """
        DM.add('premise:major subject:Socrates predicate:man')
        DM.add('premise:minor subject:man     predicate:mortal')
        print('Start run')
        focus.set('start')
    
    def recall_major_premise(focus='start'):
        DM.request('premise:major subject:?subject predicate:?predicate')
        focus.set('state_major_premise')
        
    def state_major_premise(focus='state_major_premise',
                            DMbuffer= 'premise:major subject:?subject predicate:?predicate'):   
        print(f'The major premise is: {subject} is a {predicate}')
        #Temproarily hold the subject, and predicate of the major premise in imaginal buffer
        IM1buffer.set('premise:major subject:?subject predicate:?predicate')

        focus.set('get_minor_premise')
         
    def recall_minor_premise(focus='get_minor_premise'):
        DM.request('premise:minor subject:?subject predicate:?predicate')
        focus.set('state_minor_premise')

    def state_minor_premise(focus='state_minor_premise',
                            DMbuffer= 'premise:minor subject:?subject predicate:?predicate'):   
        print(f'The minor premise is: {subject} is {predicate}')
        #Temporarily hold the subject and predicate of the minor premise in imaginal buffer
        IM2buffer.set('premise:minor subject:?subject predicate:?predicate')
        focus.set('deduce')
        
    def deduce(focus='deduce',
                IM1buffer ='predicate:man',
                IM2buffer ='subject:man'):
        """
        The predicate of the major premise, and
        the subject of the minor premise must be the same
        for the Barbara form of syllogism to be logical.
        Here we denote the values explicitly as [man].
        These values would change depending the syllogism's premises.
        """
        print(IM1buffer.chunk['subject'], 'is', IM2buffer.chunk['predicate'])
        focus.set('rpt')
        
    def report(focus = 'rpt'):
        #Print out the contents of the declarative memory
        print('DM report, just for fun')
        for chunk in DM.dm:
            print( chunk, 'Activation:', DM.get_activation(chunk))
        focus.set('stop')

    def stop_run(focus='stop'):
        # End of production run
        print('Stop run')
        self.stop()
        
"""    Production run """
      
sophy = Model()               # Model ()
ccm.log_everything(sophy)       # print out what happens to the agent
sophy.run()                     # run  the model             
ccm.finished()    