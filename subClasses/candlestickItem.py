import pandas as pd, numpy as np, json, os, time, pyqtgraph as pg
from pyqtgraph import QtCore, QtGui

class CandlestickItem(pg.GraphicsObject):
    def __init__(self, time_array, open_array, high_array, low_array, close_array, config):
        pg.GraphicsObject.__init__(self)
        self.time_array = time_array
        self.open_array = open_array
        self.high_array = high_array
        self.low_array = low_array
        self.close_array = close_array
        
        # config wick design
        self.color_wick = config['color_wick']
        self.width_wick = config['width_wick']
        self.style_wick = self.style_str_to_qt(config['style_wick'])
        # config body design
        self.color_body = config['color_body']
        self.width_body = config['width_body']
        self.style_body = self.style_str_to_qt(config['style_body'])
        # config color candles
        self.color_gCandle = config['color_gCandle']
        self.color_rCandle = config['color_rCandle']
        # config spread candle
        self.percentWidthCandle = config['percentWidthCandle'] # if 1 then all candle will stick on the x axis because the candle will be as big as possible. if 0 then there will the body will have no appearing body
        
        self.delta_x = self.time_array[1]-self.time_array[0]
        self.half_body_dx = self.delta_x*0.5*self.percentWidthCandle # initialy the candle goes from x-dx/2 to x+dx/2. The dx/2 param is adjusted with percentWidthCandle and can go from 0 to dx/2
        
        self.generatePicture()
        
    def style_str_to_qt(self, style_str):
        '''transform the style as a string (input) to a Qt model of style object'''
        if style_str == 'solid':
            return QtCore.Qt.SolidLine
        elif style_str == 'dash':
            return QtCore.Qt.DashLine
        elif style_str == 'dot':
            return QtCore.Qt.DotLine
        elif style_str == 'dash-dot':
            return QtCore.Qt.DashDotLine
        else:
            print('unknown style: ',style_str)
            return 1 
        
    def color_to_QtColor(self, elt):
        if type(elt) is str and len(elt) == 1:
            return pg.mkColor(elt)
        elif type(elt) is list and len(elt)==4:
            return pg.mkColor(tuple(elt))
        else:
            return elt
            print('error unknown color type for ',elt)
            
    def Qtcolor_to_list_rgb(self, color):
        rgb = color.getRgb()
        return [i for i in rgb]
    
    def generatePicture(self):
        ## pre-computing a QPicture object allows paint() to run much more quickly, 
        ## rather than re-drawing the shapes every time.
        self.picture = QtGui.QPicture()
        p = QtGui.QPainter(self.picture)
        p.setPen(pg.mkPen(s=self.style_wick, color=self.color_to_QtColor(self.color_to_QtColor(self.color_wick)), width=self.width_wick))
        for index in range(len(self.time_array)):
            t, o, h, l, c = self.time_array[index], self.open_array[index], self.high_array[index], self.low_array[index], self.close_array[index]
            # draw wick
            p.drawLine(QtCore.QPointF(t, l), QtCore.QPointF(t, h))
        p.setPen(pg.mkPen(s=self.style_body, color=self.color_to_QtColor(self.color_to_QtColor(self.color_body)), width=self.width_body))
        for index in range(len(self.time_array)):
            t, o, h, l, c = self.time_array[index], self.open_array[index], self.high_array[index], self.low_array[index], self.close_array[index]
            # paint candle
            if o > c:
                p.setBrush(self.color_to_QtColor(self.color_rCandle))
            else:
                p.setBrush(self.color_to_QtColor(self.color_gCandle))
            # draw body
            p.drawRect(QtCore.QRectF(t-self.half_body_dx, o, self.half_body_dx*2, c-o))
        p.end()
    
    def paint(self, p, *args):
        p.drawPicture(0, 0, self.picture)
    
    def boundingRect(self):
        ## boundingRect _must_ indicate the entire area that will be drawn on
        ## or else we will get artifacts and possibly crashing.
        ## (in this case, QPicture does all the work of computing the bouning rect for us)
        return QtCore.QRectF(self.picture.boundingRect())
    
## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    now = time.time()-56*60
    time_array = np.array([now+60*60*i for i in range(6)])
    open_array = np.array([10, 13, 17, 14, 15, 9])
    close_array = np.array([13, 17, 14, 15, 9, 15])
    low_array = np.array([5, 9, 11, 5, 8, 8])
    high_array = np.array([15, 20, 23, 19, 22, 16])
    config = {'color_gCandle':pg.mkColor('g'), 'color_rCandle':pg.mkColor('r'), 'color_wick':pg.mkColor('k'), 'style_wick':'solid', 'width_wick':2, 'color_body':pg.mkColor('k'), 'style_body':'solid', 'width_body':2, 'percentWidthCandle':0.9}
    item = CandlestickItem(time_array, open_array, high_array, low_array, close_array, config)
    plt = pg.plot()
    plt.setAxisItems({'bottom': pg.DateAxisItem()}) #(title="Dock 4 plot")
    plt.setBackground('w')
    plt.showGrid(x=True, y=True)
    plt.setXRange(time_array[0],time_array[-1])
    plt.addItem(item)
    plt.setWindowTitle('pyqtgraph example: customGraphicsItem')
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()