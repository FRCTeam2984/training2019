from magicbot import AutonomousStateMachine, state


class Autonomous(AutonomousStateMachine):

    MODE_NAME = "Autonomous"
    DEFAULT = True

    def __init__(self):
        pass

    @state(first=True)
    def startingState(self, initial_call):
        pass
