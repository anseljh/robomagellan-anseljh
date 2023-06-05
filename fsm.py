"""
Finite state machine classes

Inspired by CircuitPython 101: State Machines, Two Ways, By Dave Astels 
https://learn.adafruit.com/circuitpython-101-state-machines
"""


class State:
    name = "State"

    def __init__(self):
        print(f"State.__init__() called. name: {self.name}")

    def enter(self, machine):
        print(f"Entering State: {self.name}")
        machine.state = self

    def exit(self, machine):
        print(f"Exiting State: {self.name}")
        machine.previous_states.append(self)
        machine.state = None

    def update(self, machine):
        print(f"State.update() called for state {self.name}")


class StateMachine:

    # TODO: Do something with null_state

    def __init__(self, states: list, initial_state: State, null_state: State = None):
        self.state: State = None
        self.states = {str: State}
        self.previous_states = []
        self.null_state = null_state

        print("Initializing StateMachine...")

        for state in states:
            state_instance = state()
            self.states[state_instance.name] = state_instance

        print("StateMachine initialized.")

        print("Entering initial state...")
        self.states[initial_state.name].enter(self)

    def transition(self, state_name: str):
        print(f"Transitioning to {state_name}...")
        if self.state:
            self.state.exit(self)
        self.states[state_name].enter(self)

    def __repr__(self) -> str:
        return f"<StateMachine {hex(id(self))} state: {self.state.name if self.state else 'None'}>"


if __name__ == "__main__":
    s1 = State("s1")
    s2 = State("s2")

    fsm = StateMachine([s1, s2], s1)
    print(fsm)

    fsm.transition("s2")
    print(fsm)
