#!/usr/bin/env python3
from Cocoa import NSSpeechSynthesizer
import time
import re

sp = NSSpeechSynthesizer.alloc().init()

for voice in NSSpeechSynthesizer.availableVoices():
    v = str(voice)
    name = str(re.split("\.", v).pop())
    sp.setVoice_(voice)
    phrase = "My name is %s" % (name)
    print(phrase)
    sp.startSpeakingString_(phrase)
    #needed so script doesn't end w/o talking
    while not sp.isSpeaking():
        time.sleep(0.1)
    while sp.isSpeaking():
        time.sleep(0.1)
