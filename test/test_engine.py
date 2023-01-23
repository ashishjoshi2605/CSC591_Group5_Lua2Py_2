import sys
sys.path.append("./src")

from num import NUM
from sym import SYM
from data import DATA
import utils
import main
from egs import Egs


stdoutOrigin = sys.stdout 
sys.stdout = open("./etc/out/test_engine.out", "w", encoding="utf-8")

help = '''
data.lua : an example csv reader script
USAGE:   data.lua  [OPTIONS] [-g ACTION]
OPTIONS:
  -d  --dump  on crash, dump stack = false
  -f  --file  name of file         = ./etc/data/auto93.csv
  -g  --go    start-up action      = data
  -h  --help  show help            = false
  -s  --seed  random number seed   = 937162211
ACTIONS:
'''

the = main.cli(main.settings(help))

tester = Egs(help)


def test1():
    utils.oo(the)
    print(the)


def test2():
    sym =SYM(None, None)
    l = ['a','a','a','a','b','b','c']
    for i in l:
        sym.add(i)
    return "a" == sym.mid() and 1.379 == utils.rnd(sym.div(), None)
    

def test3():
    num = NUM(None, None)
    l = [1,1,1,1,2,2,3]
    for n in l:
        num.add(n)
    return 11/7 == num.mid() and 0.787 == utils.rnd(num.div(), None)

def test4():
    global the
    file_path = the['file']
    d = DATA(file_path)
    n = d.total_values
    return n == 399*8 

def test5():
    global the
    file_path = the['file']
    data = DATA(file_path)
    # since python's indexing starts with 0 data.cols.x[0] will be 0 but in case of lua, it will be 1
    return  len(data.rows) == 398 and data.cols.y[0].w == -1 and data.cols.x[0].at == 0 and  len(data.cols.x) == 4

def test6():
    global the
    file_path = the['file']
    data = DATA(file_path)
    print("x: mid: ",data.stats("mid", data.cols.x, 2))
    print("   div: ",data.stats("div", data.cols.x, 2))
    print("y: mid: ",data.stats("mid", data.cols.y, 2))
    print("   div: ",data.stats("div", data.cols.y, 2))

tester.eg("the", "show settings", test1)
tester.eg("sym", "check syms", test2)
tester.eg("num", "check nums", test3)
tester.eg("csv","read from csv", test4)
tester.eg("data","read DATA csv", test5)
tester.eg("stats","stats from DATA", test6)


main.main(the, tester.help, tester.egs)

# sys.stdout.close()
# sys.stdout = stdoutOrigin






