from rows import ROWS
from cols import COLS
import copy
import utils
class DATA:
    def __init__(self, src) -> None:
        self.rows = []
        self.cols = None

        self.total_values = 0


        if type(src) == str:
            self.from_csv(src)
        else:
            self.from_list(src)
    
    def add(self, t) -> None:
        if self.cols :
            # if t.cells != None :
            t = ROWS(t)
            self.rows.append(t)
            self.cols.add(t)
        else:
            self.cols = COLS(t)
    
    def clone(self, init):
        return copy.deepcopy(self)

    def stats(self, what, cols, nPlaces):
        ret = dict()
        if cols == None:
            cols = self.cols.y

        if what == "mid":
            for col in cols :
                ret[col.txt] = col.rnd(col.mid(), nPlaces)
            return ret
        else:
            for col in cols :
                ret[col.txt] = col.rnd(col.div(), nPlaces)
            return ret

    def from_csv(self, src):
        path = src
        with open(path, "r") as csv:
            lines = csv.readlines()
            for line in lines:
                split_line = line.split(",")
                split_line = [utils.coerce(i) for i in split_line]
                self.add(split_line)
                self.total_values += len(split_line)


    
    def from_list(self, lines):
        if self.src == None:
            src = []
        
        for line in lines:
            self.add(line)

