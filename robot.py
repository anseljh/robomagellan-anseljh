import time

from fsm import State, StateMachine


class GoalSet:
    pass


class LatLong:
    """
    Latitude and longitude pair
    """

    def __init__(self, latitude: float, longitude: float):
        self.latitude = latitude
        self.longitude = longitude


class InitializingState(State):
    name = "initializing"
    MAX_INIT_COUNTER = 100

    def __init__(self):
        super().__init__()
        self.init_counter = 0

    def update(self, machine: StateMachine):
        State.update(self, machine)
        self.init_counter += 1
        if self.init_counter >= InitializingState.MAX_INIT_COUNTER:
            print(f"Reached target: {self.init_counter}")
            machine.transition("idle")
        else:
            time.sleep(0.01)


class IdleState(State):
    name = "idle"

    def update(self, machine: StateMachine):
        State.update(self, machine)
        print("Idling 1s")
        time.sleep(1)


class ManualState(State):
    name = "manual"


class ShuttingDownState(State):
    name = "shuttingdown"


ALL_STATES = [InitializingState, IdleState, ManualState, ShuttingDownState]


class RoboMagellanBot:

    def __init__(self):
        self.machine = StateMachine(ALL_STATES, InitializingState)

    def run(self):
        """
        Main event loop
        """
        while True:
            self.machine.state.update(self.machine)


if __name__ == "__main__":
    bot = RoboMagellanBot()
    print(bot)
    bot.run()
    print("The end!")
