from time import monotonic, sleep


class State:
    def __init__(self, name: str):
        self.name = name
        self.transitions = {}


class StateMachine:

    def __init__(self, initial_state: State = None):
        self.state = initial_state
        self.states = {}
        self.transition_table = {}

    def add_state(self, state: State):
        self.states[state.name] = state
    
    def add_transition(self, from_state: State, to_state: State, evaluator_fn):
        from_state.transitions[to_state.name] = evaluator_fn
        
        # self.transition_table[(from_state.name, evaluator_fn)] = to_state
        if from_state.name not in self.transition_table:
            self.transition_table[from_state.name] = {}
        self.transition_table[from_state.name][to_state.name] = evaluator_fn
    
    def enter(self, state: State):
        print(f"Entering state '{state.name}'")
        self.last_transition_time = monotonic()
        self.state = state
        # self.state.run(self)
    
    def exit(self, state: State):
        print(f"Exiting state '{state.name}'")


class InitializingState(State):
    def run(self, machine: StateMachine):
        print(f"Initializing...")
        print("beep")
        print("boop")

        if monotonic() - machine.start_time > 5:
            machine.init_done = True
            print("Done initializing")
        

class AwaitingMapState(State):
    def run(self, machine: StateMachine):
        print(f"Awaiting map...")
        print("beep")
        print("boop")
        if monotonic() - machine.last_transition_time > 5:
            machine.map_data = (
                (1,2),
                (3,4),
                (5,6),
            )
            print(f"Got a map! {machine.map_data}")


class MissionAccomplishedState(State):
    def run(self, machine: StateMachine):
        machine.stop_condition = True
        print(f"Mission accomplished!!!")


class RobotStateMachine(StateMachine):

    def __init__(self):
        super().__init__()
        self.start_time = monotonic()
        self.last_transition_time = None
        
        self.init_done = False
        self.map_data = None
        self.stop_condition = False

        initializing_state = InitializingState("initializing")
        print(initializing_state)
        awaiting_map_state = AwaitingMapState("awaiting_map")
        mission_accomplished_state = MissionAccomplishedState("mission_accomplished")

        self.add_state(initializing_state) #, self.initialize)
        self.add_state(awaiting_map_state)
        self.add_state(mission_accomplished_state)
        self.add_transition(initializing_state, awaiting_map_state, self.is_init_done)
        self.add_transition(awaiting_map_state, mission_accomplished_state, self.is_map_loaded)

        self.enter(initializing_state)


    def loop(self):
        while not self.stop_condition:
            print(monotonic() - self.start_time)
            next_state = None
            self.state.run(self)

            from_state = self.state.name
            if from_state in self.transition_table:
                for to_state in self.transition_table[from_state]:
                    evaluator_fn = self.transition_table[from_state][to_state]
                    if evaluator_fn():
                        next_state = self.states[to_state]
                        break

            if next_state:
                self.exit(self.state)
                self.enter(next_state)
                self.state.run(self)
            sleep(1)
        print("loop() done!")

    def is_init_done(self):
        print("is_init_done()")
        if self.init_done:
            print("yes")
            return True
        else:
            print("no")
            return False

    def is_map_loaded(self):
        print("is_map_loaded()")
        if self.map_data is not None:
            print("yes")
            return True
        else:
            print("no")
            return False
