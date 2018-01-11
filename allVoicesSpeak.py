#!/usr/bin/env python3
from Cocoa import NSSpeechSynthesizer
import time
import sys
sayIt = sys.argv[1]

sp = NSSpeechSynthesizer.alloc().init()

for voice in NSSpeechSynthesizer.availableVoices():
    sp.setVoice_(voice)
    sp.startSpeakingString_(sayIt)
    #needed so script doesn't end w/o talking
    while not sp.isSpeaking():
        time.sleep(0.1)
    while sp.isSpeaking():
        time.sleep(0.1)
