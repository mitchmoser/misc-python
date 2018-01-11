#!/usr/bin/env python3
from Cocoa import NSSpeechSynthesizer
import time
import sys
sayIt = sys.argv[1]

sp = NSSpeechSynthesizer.alloc().initWithVoice_(None)
sp.startSpeakingString_(sayIt)

#needed so script doesn't end w/o talking
while sp.isSpeaking():
    time.sleep(0.1)
