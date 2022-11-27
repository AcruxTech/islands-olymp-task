import typing


class Field():
    '''
    Represents field (n*n), filled 0 and 1
    '''
    def __init__(self, n: int, values: list) -> None:
        '''Create Field object

        Args:
            n (int): amount of rows (or columns) in Field 
            values (list): two-dimensional array of values 0 or 1 (or 2 for temp purposes)
        '''
        self._n = n
        self._values = values
        # insert '0' values along edges of Field
        self._values.insert(0, [0]*n)
        self._values.append([0]*n)
        for row in self._values:
            row.insert(0, 0)
            row.append(0)


    @property
    def size(self) -> int:
        '''Return amount rows (or columns)

        Returns:
            int: amount rows (or columns)
        '''
        return len(self._values)


    def get_point(self, x: int, y: int) -> int:
        '''Return value of point with coords (x, y)

        Args:
            x (int): x-coordinate
            y (int): y-coordinate

        Returns:
            int: value of point
        '''
        return self._values[y][x]


    def set_point(self, value: int, x: int, y: int) -> None:
        '''Set new value for point with coords (x, y)

        Args:
            value (int): new value
            x (int): x-coordinate
            y (int): y-coordinate
        '''
        # '2' value - for temp purposes
        if value not in (0, 1, 2):
            raise ValueError('New value must be 0 or 1')

        self._values[y][x] = value


    def get_coords_next_one(self, x: int, y: int) -> typing.Optional[tuple]:
        '''Return coordinates of nearest '1' or None (if '1' not found). 

        Args:
            x (int): x-coordinate
            y (int): y-coordinate

        Returns:
            tuple | None: pair of coords (x, y) or None
        '''
        near_points = {
            (x,   y-1): self.get_point(x,   y-1),
            (x+1, y):   self.get_point(x+1, y),
            (x,   y+1): self.get_point(x,   y+1),
            (x-1, y):   self.get_point(x-1, y),
        }

        for key in near_points:
            if near_points[key] == 1:
                return key
        return None


    def delete_all_two(self) -> None:
        '''Delete all '2' values in Field'''

        for y in range(self.size):
            for x in range(self.size):
                if self.get_point(x, y) == 2:
                    self.set_point(0, x, y)
        
        
    def get_values(self):
        return self._values