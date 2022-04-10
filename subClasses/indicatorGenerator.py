import numpy as np, pandas as pd, json, os, datetime, time, pyqtgraph as pg, tulipy as ti

class IndicatorGenerator():
	def __init__(self, indicator_name):
		self.indicator_name = indicator_name
		self.path_indicator_sumup_json = 'indicator/indicator.json'
		with open(self.path_indicator_sumup_json,'r') as f:
			self.dic_indicator_sumup = json.load(f)
			f.close()
		self.dic_indicator_template = {'main group':'', 'sub group':'', 'inputs':{}, 'params':{}, 'outputs':{}, 'default_config':{}, 'type_config':''}

	def get_outputs_array(self, name_indicator, inputs, inputs_name, params, dic_current_work):
		'''Use name_indicator to know what fonction to use, then return ouputs dict of arrays and time array
		sava all array and work_files folder of .npy then add indicator to the work_sumup
		inputs_name = {"x":"close"}, inputs:{"x":[85,87,76,...]},params:{"p":9}'''
		if name_indicator == 'ema':
			outputs = self.ema(inputs, params)
			return outputs
		elif name_indicator == 'diff_from_1st':
			outputs = self.diff_from_1st(inputs, params)
			return outputs
		elif name_indicator == 'diff_from_pre':
			outputs = self.diff_from_pre(inputs, params)
			return outputs
		elif name_indicator == 'diff_from_avg':
			outputs = self.diff_from_avg(inputs, params)
			return outputs
		elif name_indicator == 'rsi':
			outputs = self.rsi(inputs, params)
			return outputs
		elif name_indicator == 'ohlc':
			outputs = self.ohlc(inputs, params)
			return outputs

	def get_dic_variable_sumup(self, name_indicator, inputs, inputs_name, params, dic_current_work):
		'''Return a dic of the variable containing the paths, the config ect... so that we can plot the indicator'''
		path_folder_work_files = dic_current_work['path_folder_work_files']
		return dic_variable_sumup, name_indicator

	def build_indicator(self, new_variable_name, name_indicator, inputs_name, params, dic_current_work):
		'''1: create the inputs dic by importing the npy
		2: generate the outputs with get_outputs_array function and save them in the work files
		3: update the variable_sumup of current_work to add new variable and new paths (don't update immediatly because we cant acces the current dic work)
		new_variable_name is the name we give to the newly adde indicator. It is the named registered on the work sumup
		and also the name displayed in the form layout checkboxes. Each must be different so that we can have for ex 2 ema on the smae var but of different length'''
		# 1
		path_folder_work_files = dic_current_work['path_folder_work_files']
		inputs = {}
		inputs_path = {}
		for name_input in inputs_name.keys():

			timeframe = dic_current_work['variables'][inputs_name[name_input]]['timeframe']
			tf_nbs = dic_current_work['variables'][inputs_name[name_input]]['informations']['tf_nbs']
			tf_metric = dic_current_work['variables'][inputs_name[name_input]]['informations']['tf_metric']
			path_time_np = dic_current_work['variables'][inputs_name[name_input]]['path_time_np']
			path_value_dic = dic_current_work['variables'][inputs_name[name_input]]['path_value_dic']
			list_key_path_value_dic = [key for key in path_value_dic]
			inputs_path[name_input] = path_folder_work_files+path_value_dic[list_key_path_value_dic[0]]
			inputs[name_input] = np.load(inputs_path[name_input])
		# 2
		outputs = self.get_outputs_array(name_indicator, inputs, inputs_name, params, dic_current_work)
		outputs_path = {}
		outputs_name_np_file = {}
		inputs_name_str = str(inputs_name).replace(' ','').replace('{','').replace('}','').replace(':','=').replace("'","").replace('"','')
		params_str = str(params).replace(' ','').replace('{','').replace('}','').replace(':','=').replace("'","").replace('"','')
		id_output = '{}_{}_{}'.format(name_indicator,inputs_name_str,params_str)
		for name_output in outputs.keys():
			outputs_path[name_output] = path_folder_work_files + name_output + '_' + timeframe +'_'+ id_output + '.npy'
			outputs_name_np_file[name_output] = name_output + '_' + timeframe +'_'+ id_output + '.npy'
		# 3
		type_data = 'indicator'
		name_indicator:name_indicator = name_indicator
		timeframe = timeframe
		path_value_np = outputs_path
		plot = True
		config = self.get_default_config(name_indicator)
		config_builder = self.get_config_builder(name_indicator)
		default_config = config
		informations = {'type_config':'standard', 'tf_nbs':tf_nbs, 'tf_metric':tf_metric}
		plot_builder = self.get_plot_builder(name_indicator)
		indicator_builder = {'inputs_name':inputs_name, 'params':params, 'name_indicator':name_indicator}
		config['display_name'] = name_indicator
		for name_output in outputs_path.keys():
			np.save(outputs_path[name_output], outputs[name_output])
		dic_new_variable = {'type_data':type_data, 'name_indicator':name_output, 'timeframe':timeframe, 'path_value_dic':outputs_name_np_file, 
								'path_time_np':path_time_np, 'plot':plot, 'config':config, 'config_builder':config_builder, 'default_config':default_config, 
								'informations':informations, 'plot_builder':plot_builder, 'indicator_builder':indicator_builder}
		dic_current_work['variables'][new_variable_name] = dic_new_variable
		return dic_current_work

	def get_default_config(self, name_indicator):
		'''Return a dict called default config consisting on the default config value for ech name_indicator'''
		return self.dic_indicator_sumup[name_indicator]['default_config']

	def get_config_builder(self, name_indicator):
		'''Return a dic with same keys as default config that specifies how to build the config dialog later'''
		return self.dic_indicator_sumup[name_indicator]['config_builder']

	def get_plot_builder(self, name_indicator):
		return self.dic_indicator_sumup[name_indicator]['plot_builder']

	def get_plot_item_nonStandard(self, name_indicator, inputs, params, config, type_config):
		'''Depending on the name_indicator, return the corresponding item'''

	def get_config_dialog_nonStandard(self, name_indicator):
		'''return a config dialog object to be instanciated in the main.py refresh layout function'''

	#The following functions are made for calculating arrays of indecator

	def ema(self, inputs, params):
		x, p = np.array(inputs['x']), params['p']
		res = ti.ema(x, p)
		outputs = {'ema':res}
		return outputs

	def diff_from_1st(self, inputs, params):
		x = np.array(inputs['x'])
		res = (x-x[0])/x[0]
		outputs = {'name_diff1st':res}
		return outputs

	def diff_from_pre(self, inputs, params):
		x = np.array(inputs['x'])
		res = [0]
		for i in range(1,len(x)):
			res.append((x[i]-x[i-1])/x[i-1])
		res = np.array(res)
		outputs = {'name_diffPre':res}
		return outputs

	def diff_from_avg(self, inputs, params):
		x, p = np.array(inputs['x']), params['p']
		avg = ti.ema(x,p)
		res = [0]*p
		for i in range(p,len(x)):
			res.append((x[i]-avg[i-1])/avg[i-1])
		res = np.array(res)
		outputs = {'name_diffAvg':res}
		return outputs
	
	def rsi(self, inputs, params):
		x, p = np.array(inputs['x']), params['p']
		res = ti.rsi(x, p)
		outputs = {'rsi':res}
		return outputs

	def ohlc(self, inputs, params):
		o, h, l, c = np.array(inputs['open']), np.array(inputs['high']), np.array(inputs['low']), np.array(inputs['close'])
		outputs = {'open':o, 'high':h, 'low':l, 'close':c}
		return outputs