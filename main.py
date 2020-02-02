from my_calculate import graph as gh

if __name__ == '__main__':
    blood = gh.graph('gennsui1')
    blood.reader()
    blood.calculate()
    blood.create()
    blood.plots("年齢と血圧", "年齢", "血圧")
    blood.line()
    blood.display()