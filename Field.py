class Field():
    """
    Represents field (n*n), filled 0 and 1
    """
    def __init__(self, n: int, values: list) -> None:
        """Create Field object

        Args:
            n (int): amount of rows (or columns) in Field 
            values (list): two-dimensional array of values 0 or 1
        """
        self._n = n
        self._values = values


    @property
    def size(self) -> int:
        """Return amount rows (or columns)

        Returns:
            int: amount rows (or columns)
        """
        return self._n


    def get_point(self, x: int, y: int) -> int:
        """Return value of point with coords (x, y)

        Args:
            x (int): x-coordinate
            y (int): y-coordinate

        Returns:
            int: value of point
        """
        return self._values[y, x]


    def set_point(self, value: int, x: int, y: int) -> None:
        """Set new value for point with coords (x, y)

        Args:
            value (int): new value
            x (int): x-coordinate
            y (int): y-coordinate
        """
        if value not in (0, 1):
            raise ValueError('New value must be 0 or 1')

        self._values[y][x] = value
        