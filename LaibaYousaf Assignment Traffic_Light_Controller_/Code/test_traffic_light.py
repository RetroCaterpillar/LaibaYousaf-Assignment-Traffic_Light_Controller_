import unittest
from traffic_light import TrafficLight

class TestTrafficLight(unittest.TestCase):
    def test_transitions(self):
        light = TrafficLight()
        self.assertEqual(light.current_state(), "Red")  # Initial state
        light.transition()
        self.assertEqual(light.current_state(), "Green")  # Red → Green
        light.transition()
        self.assertEqual(light.current_state(), "Yellow")  # Green → Yellow
        light.transition()
        self.assertEqual(light.current_state(), "Red")  # Yellow → Red

if __name__ == "__main__":
    unittest.main()
