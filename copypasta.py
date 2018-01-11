#!/usr/bin/env python3
from Cocoa import NSSpeechSynthesizer
import time
import sys
sayIt = "What the fuck did you just fucking say about me you little bitch? I'll have you know I graduated top of my class in Computer Science, and I've been involved in numerous deployments on A W S, and I have over 300 confirmed commits. I am trained in VB .NET and I'm the top haxor in my entire development team. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again fucker. As we speak I am contacting my secret network of Google interns across the USA and your IP is being traced right now so you better prepare for ehe storm, maggot. The storm that wipes out the pathetic little thing you call your life. You're fucking dead kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that's just with HTML. Not only am I extensively trained in web development, but I have access to the entire standard library of Python and I will use it to its full extent to wipe your miserable ass off the face of the continent you little shit. If only you could have known what unholy retribution your little nerd comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn't, you didn't, and now you're paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You're fucking dead kiddo."

sp = NSSpeechSynthesizer.alloc().initWithVoice_(None)
sp.startSpeakingString_(sayIt)

#needed so script doesn't end w/o talking
while sp.isSpeaking():
    time.sleep(0.1)
