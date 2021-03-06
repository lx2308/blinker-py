#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Blinker.Blinker import Blinker, BlinkerButton, BlinkerNumber, BlinkerMiot
from Blinker.BlinkerConfig import *
from Blinker.BlinkerDebug import *

auth = 'Your Device Secret Key'

BLINKER_DEBUG.debugAll()

Blinker.mode('BLINKER_WIFI')
Blinker.miType('BLINKER_MIOT_OUTLET')
Blinker.begin(auth)

button1 = BlinkerButton('btn-abc')
number1 = BlinkerNumber('num-abc')

counter = 0
oState = 'on'

def miotPowerState(state):
    ''' '''

    global oState

    BLINKER_LOG('need set power state: ', state)

    oState = state

    BlinkerMiot.powerState(state)
    BlinkerMiot.print()

def miotQuery(queryCode):
    ''' '''

    global oState

    BLINKER_LOG('Miot Query codes: ', queryCode)

    if queryCode == BLINKER_CMD_QUERY_ALL_NUMBER :
        BLINKER_LOG('Miot Query All')
        BlinkerMiot.powerState(oState)
        BlinkerMiot.print()
    elif queryCode == BLINKER_CMD_QUERY_POWERSTATE_NUMBER :
        BLINKER_LOG('Miot Query Power State')
        BlinkerMiot.powerState(oState)
        BlinkerMiot.print()
    else :
        BlinkerMiot.powerState(oState)
        BlinkerMiot.print()

def button1_callback(state):
    ''' '''

    BLINKER_LOG('get button state: ', state)

    button1.icon('icon_1')
    button1.color('#FFFFFF')
    button1.text('Your button name or describe')
    button1.print(state)

def data_callback(data):
    global counter
    
    BLINKER_LOG('Blinker readString: ', data)
    counter += 1
    number1.print(counter)

button1.attach(button1_callback)
Blinker.attachData(data_callback)

BlinkerMiot.attachPowerState(miotPowerState)
BlinkerMiot.attachQuery(miotQuery)

if __name__ == '__main__':

    while True:
        Blinker.run()
