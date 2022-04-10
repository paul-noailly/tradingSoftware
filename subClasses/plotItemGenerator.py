import pandas as pd, numpy as np, json, os, time, pyqtgraph as pg
from pyqtgraph import QtCore, QtGui

class PlotItemGenerator():
    '''Object that alows to generate plot items depending on the config and the plot builder'''
    def __init__(self, config={}, plot_builder={}, dic_values={}, arr_time=[]):
        self.config = config
        self.plot_builder = plot_builder
        self.type_plot = self.plot_builder['type_plot']
        self.dic_values = dic_values
        self.arr_time = arr_time

    def get_plotItem(self):
        if self.type_plot == 'standard':
            return self.get_standard_plotItem()
        elif self.type_plot == 'ohlc':
            return self.get_ohlc_plotItem()
        elif self.type_plot == 'rsi':
            return self.get_rsi_plotItem()
        else:
            print('ERROR: unknown type_plot ({})'.format(self.type_plot))

    def get_example_plotItem(self, config):
        if self.type_plot == 'standard':
            now = time.time()
            arr_value = np.array([10, 13, 17, 14, 15, 9])
            arr_time = np.array([now+60*60*i for i in range(6)])
            return StandardItem(config, arr_value, arr_time)
        elif self.type_plot == 'ohlc':
            now = time.time()-56*60
            arr_time = np.array([now+60*60*i for i in range(6)])
            open_array = np.array([10, 13, 17, 14, 15, 9])
            close_array = np.array([13, 17, 14, 15, 9, 15])
            low_array = np.array([5, 9, 11, 5, 8, 8])
            high_array = np.array([15, 20, 23, 19, 22, 16])
            dic_values = {'open':open_array, 'high':high_array, 'low':low_array, 'close':close_array}
            return CandlestickItem(config, dic_values, arr_time)
        elif self.type_plot == 'rsi':
            return 0
        else:
            print('ERROR: unknown type_plot ({})'.format(self.type_plot))

    def get_standard_plotItem(self):
        list_values_keys = [key for key in self.dic_values.keys()]
        arr_value = self.dic_values[list_values_keys[0]]
        item_to_plot = StandardItem(self.config, arr_value, self.arr_time)
        return item_to_plot

    def get_ohlc_plotItem(self):
        item_to_plot = CandlestickItem(self.config, self.dic_values, self.arr_time)
        return item_to_plot

    def get_rsi_plotItem(self):
        item_to_plot = 0
        return item_to_plot

'''---------------Standard Item------------------'''

class StandardItem(pg.GraphicsObject):
    def __init__(self, config, arr_value, arr_time):
        pg.GraphicsObject.__init__(self)
        self.arr_time = arr_time
        self.arr_value =arr_value
        
        # config plot design
        self.color = config['color']
        self.style = self.style_str_to_qt(config['style'])
        self.width = config['width']
        
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
        self.picture = QtGui.QPicture()
        p = QtGui.QPainter(self.picture)
        p.setPen(pg.mkPen(s=self.style, color=self.color_to_QtColor(self.color), width=self.width))
        for index in range(len(self.arr_time)-1):
            # draw line
            p.drawLine(QtCore.QPointF(self.arr_time[index], self.arr_value[index]), QtCore.QPointF(self.arr_time[index+1], self.arr_value[index+1]))
        p.end()
    
    def paint(self, p, *args):
        p.drawPicture(0, 0, self.picture)
    
    def boundingRect(self):
        return QtCore.QRectF(self.picture.boundingRect())

'''---------------OHLC Item------------------'''

class CandlestickItem(pg.GraphicsObject):
    def __init__(self, config, dic_values, arr_time):
        pg.GraphicsObject.__init__(self)
        self.time_array = arr_time
        self.open_array = dic_values['open']
        self.high_array = dic_values['high']
        self.low_array = dic_values['low']
        self.close_array = dic_values['close']
        
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
        return QtCore.QRectF(self.picture.boundingRect())

'''---------------RSI Item------------------'''