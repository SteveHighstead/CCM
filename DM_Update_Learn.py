# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 14:05:23 2021

@author: Steve

This is an exercise to change a value of a chunk slot in declarative memory.

"""

#Set path to CCMSuite3 (on my computer. Different for other users)
import sys
sys.path.append('C:\CCMSuite3')

import ccm  #Import the ccm modelling modules
from ccm.lib.actr import *  # Import the ACT-R modelling modules


class DM_Update(ACTR):
    
    """ Set Buffers and Modules """
    focus = Buffer()          # Assign focus buffer
    DMbuffer = Buffer()       # Assign Memory buffer
    DM = Memory(DMbuffer)     # Invoke Memory module

    """ Initialize the model """
    def init():
        DM.add('isa:John status:unmarried')
        print('start')
        focus.set('request_person')

    """Get the memory status of the person"""    
    def get_person(focus = 'request_person'): # IF the focus condition is matched
        DM.request('isa:John status:?status') # THEN do this
        focus.set('check_status')

    """If the status matches then update the memory"""
    def status_check(focus = 'check_status',
                  	 DMbuffer = 'isa:John status:unmarried'): # IF these conditions are met
        print('John is unmarried is a match')                 # THEN execute these instructions
        print('Update John to be a bachelor')
        DM.add('isa:John status:bachelor')
        DMbuffer.clear()
        focus.set('request_status')

    """Request current memory status"""
    def request_status(focus = 'request_status'):

        DM.request('isa:John status:?status')
        print('Get updated status')
        focus.set('report_status')
        

    """Report on the current memory status"""
    def report(focus = 'report_status',
               DMbuffer = 'isa:?isa status:?status'):
        print(f'The status of {isa} is {status}')
        self.stop()
   
""" Instantiate model and run """
model = DM_Update()
ccm.log_everything(model)
model.run()
ccm.finished()
        
  
        