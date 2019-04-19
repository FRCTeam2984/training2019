#!/usr/bin/env python
import magicbot
import wpilib


class Robot(magicbot.MagicRobot):
    def createObjects(self):
        """Create global objects here."""
        pass

    def teleopInit(self):
        """Called when teleop starts."""
        pass

    def teleopPeriodic(self):
        """Called on each iteration of the control loop."""
        try:
            pass
        except:
            self.onException()


if __name__ == "__main__":
    wpilib.run(Robot)
