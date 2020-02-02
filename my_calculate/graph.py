from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams['font.family'] = 'IPAexGothic'
plt.rcParams['font.size'] = 30

class graph:
    
    def __init__(self, name):
        self.name = name
        self.meanx = 0.0
        self.meany = 0.0
        self.s1 = 0.0
        self.s2 = 0.0
        self.s3 = 0.0
        self.a = 0.0
        self.b = 0.0
        self.r = 0.0
        self.df = {}
        print('コンストラクタが呼ばれました。')
    
    def reader(self):
        self.df = pd.read_csv(self.name + '.csv', names=['num1', 'num2'])
        print(self.name +'を読み込みました。')
    
    def calculate(self):
        for i in range(len(self.df)):
            self.meanx += self.df['num1'][i]
            self.meany += self.df['num2'][i]
        self.meanx = self.meanx/len(self.df)
        self.meany = self.meany/len(self.df)

        for i in range(len(self.df)):
            self.s1 += (self.df['num1'][i]-self.meanx)*(self.df['num2'][i]-self.meany)
            self.s2 += (self.df['num1'][i]-self.meanx)*(self.df['num1'][i]-self.meanx)
            self.s3 += (self.df['num2'][i]-self.meany)*(self.df['num2'][i]-self.meany)
        self.b = self.s1 / self.s2
        self.a = self.meany - self.b *self.meanx
        self.r = self.s1/(np.sqrt(self.s2)*np.sqrt(self.s3))
        print('計算が完了しました。')
    
    def create(self):
        self.fig = plt.figure(figsize = (20, 10))
        self.fig.patch.set_edgecolor('k')
        self.fig.subplots_adjust(hspace = 0.5)
        self.fig.subplots_adjust(bottom=0.2)
        
        self.ax1 = self.fig.add_subplot(111)
        self.ax1.patch.set_facecolor('lightgray')
        self.ax1.patch.set_alpha(1)
        self.ax1.grid(color = 'black', linestyle = '--')
        self.ax1.set_axisbelow(True)
        print('グラフを作成しました。')
        
        
    def plots(self, title, xlabel, ylabel):
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.ax1.set_title(label = self.title, fontsize = 40, pad = 20, )
        self.ax1.set_xlabel(xlabel = self.xlabel, fontsize = 40)
        self.ax1.set_ylabel(ylabel = self.ylabel, fontsize = 40)
        self.ax1.plot(self.df['num1'], self.df['num2'] ,color = 'red', marker = '.', markersize = '20', linewidth = 0)
        print('グラフにプロットしました。')
        
    def line(self):
        dt = 0.01
        t = np.arange(self.df['num1'][0],self.df['num1'][len(self.df)-1],dt)
        self.ax1.plot(t, t*self.b + self.a, color = 'blue', marker = '.', markersize = '0', linewidth = 2)
        print('最小二乗法で求めた直線をプロットしました。')
        
    def save(self, NAME):
        self.NAME = NAME
        self.fig.savefig(self.NAME + '.png', format = 'png', dpi = 300, transparent=True, bbox_inches='tight')
    
    def display(self):
        print('回帰直線:y = '+ '{:.3f}'.format(self.b)+ 'x + '+ '{:.3f}'.format(self.a))
        print('相関係数:r = '+ '{:.3f}'.format(self.r))
        print('決定係数:r^2 = '+ '{:.3f}'.format(self.r*self.r))
        plt.show()


      