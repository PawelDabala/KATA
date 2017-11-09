class Cube:
    # This cube needs help
    # Define a constructor which takes one integer, or handles no args
    def __init__(self,value = 0):
        if isinstance(value, int):
            self._side = abs(value)

    def get_side(self):
        """Return the side of the Cube"""
        return self._side

    def set_side(self, new_side):
        """Set the value of the Cube's side."""
        self._side = abs(new_side)