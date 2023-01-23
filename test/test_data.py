import sys
sys.path.append("./src")
from data import DATA

path = r"auto93.csv"
d = DATA(path)
stats = d.stats("mid", d.cols.y, 2)
print("Size of csv = {} * {}".format(len(d.rows), len(d.cols.names)))
print("Column headers : ",d.cols.names)
print("Independent columns : ", d.cols.x)
print("Dependent columns : ", d.cols.y)
