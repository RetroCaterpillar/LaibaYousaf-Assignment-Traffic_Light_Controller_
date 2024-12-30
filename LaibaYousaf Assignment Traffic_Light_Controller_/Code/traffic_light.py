class TrafficLight:
    def __init__(self):
        self.state = "Red"

    def transition(self):
        if self.state == "Red":
            self.state = "Green"
        elif self.state == "Green":
            self.state = "Yellow"
        elif self.state == "Yellow":
            self.state = "Red"

    def current_state(self):
        return self.state
