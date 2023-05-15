from machine import Pin
from time import sleep
import neopixel
import random

#Set up LED colours and pin
led = neopixel.NeoPixel(machine.Pin(28), 1)
clear = (0,0,0)
green = (0, 255, 0)
red = (255, 0, 0)

# Assign buttons and buzzer
buzzer = Pin(18,Pin.OUT)
button_pins = [20, 21, 22]  # Pins for buttons 1, 2, and 3 respectively

# Set up buttons as inputs with pull-down resistors
for pin in button_pins:
    machine.Pin(pin, machine.Pin.IN, machine.Pin.PULL_DOWN)

#Generates a random sequence
def generateSequence(x):
    #Write code to generate a random sequence of [0,1] of length x

#Displays the colour on the LED
def display(i):
    if i == 0:
        led[0] = red
        led.write()
    elif i == 1:
        led[0] = green
        led.write()
    else:
        led[0] = clear
        led.write()

#Blinks a colour for a second
def blink():
    #Write code to make LED blink green once

#Buzzes once
def buzz():
    #Write code to make buzzer buzz once
    
while True:
    print("Welcome to the Multitask Memory Game!")
    print("======== Instructions ========")
    print("The goal of the game is to remember how many times lights and clicks appear.")
    print("Every round, a random number of clicks and lights will appear")
    print("Count the number of lights with the left button and number of buzzes with the right button")
    print("=============================")
    print("")
    print("Tap any button to start")
    start = 0
    #Write code that starts when the user presses any button
    print("GAME START")
    sleep(2)
    alive = True
    round = 1
    game = []
    
    #Runs while game is live
    while alive:
        print("Round " + str(round))
        display(-1)
        #Write code that generates a sequence of buzzes and blinks and plays them sequentially

        #Write code to let user input their options

        print("Checking...")
        sleep(2)
        #Checks if user count is correct and displays result
        if lightNo == seq.count(0) and buzzNo == seq.count(1):
            print("Correct!")
            display(1)
            sleep(0.3)
            display(-1)
            sleep(0.3)
            display(1)
            sleep(0.-1)
            display(-1)
            display(1)
            sleep(0.3)
            display(-1)
            sleep(3)
            round += 1
        else:
            print("Incorrect!")
            display(0)
            sleep(0.3)
            display(-1)
            sleep(0.3)
            display(0)
            sleep(0.3)
            display(-1)
            display(0)
            sleep(0.3)
            display(-1)
            print("======= GAME OVER =======")
            print("You have survived "+str(round)+ " round(s)!")
            alive = False
            break
        
    break

