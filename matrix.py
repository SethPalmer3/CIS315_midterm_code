class matrix:
    def __init__(self, rows: int, cols: int, default_val: any = 0) -> None:
        """Give size of the matrix"""
        self.rows = rows
        self.cols = cols
        self.vals = []
        for r in range(rows):
            temp = []
            for c in range(cols):
                temp.append(default_val)
            self.vals.append(temp)

    def __str__(self):

        ret_str =""
        for r in range(self.rows):
            for c in range(self.cols):
                ret_str +=(f"{str(self.getitem(r, c))} ")
            ret_str += "\n" if r < self.rows - 1 else ""
        return ret_str
    
    def getitem(self, x, y) -> any:
        return self.vals[x][y]

    def setitem(self, x, y, val) -> None:
        self.vals[x][y] = val

    def __mul__(self, other: "matrix") -> "matrix":
        """Does not modify self or other, makes a new matrix as the result"""
        try:
            assert other.cols == self.rows, "dimentions incorrect"
            result = matrix(self.rows, self.cols, 0)
            for i in range(self.rows):
                for j in range(other.cols):
                    for k in range(other.rows):
                        result.vals[i][j] += self.vals[i][k] * other.vals[k][j]
            return result
        except AttributeError:
            print("Incorrect type")
            return None

