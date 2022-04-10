import pandas as pd, numpy as np, json, os, time, pyqtgraph as pg
from pyqtgraph import QtCore, QtGui

class StandardPlotItem(pg.GraphicsObject):
    def __init__(self, time_array, value_array, config):
        pg.GraphicsObject.__init__(self)
        self.time_array = time_array
        self.value_array = value_array
        
        # config
        self.color = config['color']
        self.width = config['width']
        self.style = self.style_str_to_qt(config['style'])
        print('config chosen to plot the standard item is :',config)
        
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
            print('error unknown color type for ',elt)
            
    def Qtcolor_to_list_rgb(self, color):
        rgb = color.getRgb()
        return [i for i in rgb]
    
    def generatePicture(self):
        ## pre-computing a QPicture object allows paint() to run much more quickly, 
        ## rather than re-drawing the shapes every time.
        self.picture = QtGui.QPicture()
        p = QtGui.QPainter(self.picture)
        p.setPen(pg.mkPen(s=self.style, color=self.color_to_QtColor(self.color), width=self.width))
        for index in range(len(self.time_array)-1):
            # draw line
            p.drawLine(QtCore.QPointF(self.time_array[index], self.value_array[index]), QtCore.QPointF(self.time_array[index+1], self.value_array[index+1]))
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
    now = time.time()
    time_array = np.array([now+60*60*i for i in range(6)])
    value_array = np.array([10, 13, 17, 14, 15, 9])
    config = {'color':pg.mkColor('k'), 'style':'solid', 'width':2}
    item = StandardPlotItem(time_array, value_array, config)
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