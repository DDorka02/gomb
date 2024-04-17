#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Image


class Feladatok():

    def __init__(self):
        # tégla
        self.ev3 = EV3Brick()
        # motorok
        self.jm = Motor(Port.B)
        self.bm = Motor(Port.C)
        self.km = Motor(Port.A)
        # szenzorok
        self.cs = ColorSensor(Port.S3)
        self.ts = TouchSensor(Port.S1)
        self.gs = GyroSensor(Port.S2)
        self.us = UltrasonicSensor(Port.S4)
        #kép a kijelzőn

        self.kep1= Image(ImageFile.BOTTOM_LEFT)
        self.kep2= Image(ImageFile.BOTTOM_RIGHT)


        # dupla motorkezelő
        self.robot = DriveBase(self.jm, self.bm, 55, 115)

        #stopppr ora
        self.ido=StopWatch()

    def gombOsszekotese(self):
        logikai = True
        while(logikai):
            if len(self.ev3.buttons.pressed())> 0:
                print(self.ev3.buttons.pressed())
                print(type(self.ev3.buttons.pressed()[0]))
                if self.ev3.buttons.pressed()==[Button.UP]:
                    self.robot.drive(100, 0)
                    wait(500)
                elif self.ev3.buttons.pressed()==[Button.DOWN]:
                    self.robot.drive(-100, 0)
                    wait(500)
                elif self.ev3.buttons.pressed()==[Button.RIGHT]:
                    self.km.run_angle(100,90,Stop.BRAKE,100)
                    wait(500)
                elif self.ev3.buttons.pressed()==[Button.LEFT]:
                    self.km.run_angle(-100,90,Stop.BRAKE,100)
                    wait(500)
                elif self.ev3.buttons.pressed()==[Button.CENTER]:
                    self.robot.stop(Stop.BRAKE)
                    logikai= False
                self.robot.stop(Stop.BRAKE)


