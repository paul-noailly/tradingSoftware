import numpy as np, pandas as pd, json, os, datetime, time, pyqtgraph as pg

class DictWork():
    def __init__(self, new_work_dic_name):
        self.new_work_dic_name = new_work_dic_name.replace(' ','_')
        self.new_work_path = 'work/'
        self.path_folder_work_files = self.new_work_path+self.new_work_dic_name+'/'
        self.path_json_new_dic_to_save = self.new_work_path+self.new_work_dic_name+'.json'
        
    def get_work_dic(self):
        with open(self.path_json_new_dic_to_save, 'r') as f:
            dic_work = json.load(f)
            f.close()
        return dic_work
    
    def add_new_var(self, dic_work, name, type_data, timeframe, path_value_np, path_time_np, plot, dock, array_value, array_timestamp):
        with open(self.path_json_new_dic_to_save, 'r') as f:
            dic_work = json.load(f)
            f.close()
        dic_work = self.add_variable_new_dic_work(dic_work, name, type_data, timeframe, path_value_np, path_time_np, plot, dock)
        self.save_as_numpy(path_value_np, array_value)
        self.save_as_numpy(path_time_np, array_timestamp)
        with open(self.path_json_new_dic_to_save, 'w') as f:
            json.dump(dic_work, f)
            f.close()
            
    def edit_var(self, name_var, param_var, new_value):
        with open(self.path_json_new_dic_to_save, 'r') as f:
            dic_work = json.load(f)
            f.close()
        dic_var = dic_work['variables'][name_var]
        dic_var[param_var] = new_value
        dic_work['variables'][name_var] = dic_var
        with open(self.path_json_new_dic_to_save, 'w') as f:
            json.dump(dic_work, f)
            f.close()
    
    def init_create_dic_work(self, df, name_date_column, name_timestamp_column, format_date, data_type, init_date, end_date, path_original_data):

        self.init_date, self.end_date = datetime.datetime.strptime(init_date, '%Y-%m-%d %H:%M').strftime(format=format_date), datetime.datetime.strptime(end_date, '%Y-%m-%d %H:%M').strftime(format=format_date)
        self.df = df.loc[(df[name_date_column]>=self.init_date)&(df[name_date_column]<=self.end_date)]
        self.name_date_column = name_date_column
        self.name_timestamp_column = name_timestamp_column
        self.format_date = format_date
        if name_timestamp_column not in df.columns:
            print('we add timestamp')
            self.df = self.add_timestamp(self.df, name_timestamp_column=self.name_timestamp_column, name_date_column=self.name_date_column, format_date=self.format_date)
        self.tf_str, self.tf_sec, self.tf_nbs, self.tf_metric= self.get_timeframe(self.df, name_date_column=self.name_date_column, format_date=self.format_date)
        self.data_type = data_type
        #initiate new_work_dic
        self.new_work_dic = {}
        self.new_work_dic['path_folder_work_files'] = self.path_folder_work_files
        self.new_work_dic['path_original_data'] = [path_original_data]
        self.new_work_dic['list_docks'] = {'1':{'name':'main', 'position':'is','withRespectTo':'main'}, '2':{'name':'osci', 'position':'is','withRespectTo':'osci'}} #This is the default docks
        self.new_work_dic['variables'] = {}
        
        
    def add_timestamp(self, df, name_timestamp_column='timestamp', name_date_column='time', format_date='%Y-%m-%d %H:%M:%S'):
        '''Add a timestamp column to the df, usefull for plotting with x time axis on pyqtgraph'''
        array_date = df[name_date_column].to_numpy()
        timestamp_list = [datetime.datetime.strptime(date, format_date).timestamp() for date in array_date]
        df[name_timestamp_column] = pd.Series(timestamp_list)
        return df
    
    def get_timeframe(self, df, name_date_column='time', format_date='%Y-%m-%d %H:%M:%S'):
        '''Use the df to detect the timeframe of it'''
        seconds_timeframe = (datetime.datetime.strptime(df[name_date_column].iloc[1], format_date)-datetime.datetime.strptime(df[name_date_column].iloc[0], format_date)).total_seconds()
        if seconds_timeframe % 2592000 == 0 or seconds_timeframe % 2678400 == 0:
            tf_str  = '1_mth'
            tf_sec = seconds_timeframe
            tf_nbs, tf_metric = 1, 'month'
        elif seconds_timeframe % 86400 == 0:
            tf_str  = '{}_day'.format(int(seconds_timeframe//86400))
            tf_sec = seconds_timeframe
            tf_nbs, tf_metric = int(seconds_timeframe//86400), 'day'
        elif seconds_timeframe % 3600 == 0:
            tf_str  = '{}_hrs'.format(int(seconds_timeframe//3600))
            tf_sec = seconds_timeframe
            tf_nbs, tf_metric = int(seconds_timeframe//3600), 'hour'
        elif seconds_timeframe % 60 == 0:
            tf_str  = '{}_min'.format(int(seconds_timeframe//60))
            tf_sec = seconds_timeframe
            tf_nbs, tf_metric = int(seconds_timeframe//60), 'min'
        elif seconds_timeframe % 1 == 0:
            tf_str  = '{}_sec'.format(int(seconds_timeframe//1))
            tf_sec = seconds_timeframe
            tf_nbs, tf_metric = int(seconds_timeframe//1), 'sec'
        else:
            tf_str  = 'tick'
            tf_sec = seconds_timeframe
            tf_nbs, tf_metric = 0, 'tick'
        return tf_str, tf_sec, tf_nbs, tf_metric
    
    def add_variable_new_dic_work(self, dic, name, type_data, timeframe, path_value_dic, path_time_np, plot, config, config_builder, default_config, informations, plot_builder):
        '''Add a new variable providing the name, the type (ohlc, date, timestamp, or indicator), timeframe, path to numpy array save (value and time), plot: if it is plotted by default, dock: the id of the dock to plot it on'''
        dic['variables'][name] = {'type':type_data, 'timeframe':timeframe, 'path_value_dic':path_value_dic, 'path_time_np':path_time_np, 'plot':plot, 
                                    'config':config, 'config_builder':config_builder, 'default_config':default_config, 'informations':informations, 'plot_builder':plot_builder}
        return dic
    
    def create_folder_work(self):
        '''Create the folder in which to save the numpy array to'''
        path_new_folder = self.new_work_path+self.new_work_dic_name
        try:
            os.mkdir(path_new_folder)
        except:
            print('unnable to create new dic, maybe it already exists')
    
    def save_as_numpy(self, name_file, array):
        '''Save the array in the file folder'''
        path = self.path_folder_work_files+name_file
        if name_file not in os.listdir(self.path_folder_work_files):
            np.save(path, array)
    
    def build_dic(self):
        print('building variables json with column name time is ',self.name_timestamp_column)
        i = 0
        for col in self.df.columns:
            print('columns {}: (type: {})'.format(col, type(self.df[col].iloc[0])))
            i += 1
            if i > 10:
                break
        '''Add variable to the dic'''
        list_var_already_put = []
        for var in self.df.columns:
            if var not in list_var_already_put:
                if var == self.name_date_column:
                    type_data = 'date'
                    timeframe = self.tf_str
                    path_value_np =  'date' + '_' + timeframe + '.npy'
                    path_time_np =  'timestamp' + '_' + timeframe + '.npy'
                    plot = False
                    dock = 'main'
                    list_var_already_put.append(var)
                    self.save_as_numpy(path_value_np, self.df[var].to_numpy())
                    #self.save_as_numpy(path_time_np, self.df[self.name_timestamp_column].to_numpy())
                elif var == self.name_timestamp_column:
                    type_data = 'timestamp'
                    timeframe = self.tf_str
                    path_value_np =  'timestamp' + '_' + timeframe + '.npy'
                    path_time_np =  'timestamp' + '_' + timeframe + '.npy'
                    plot = False
                    dock = 'main'
                    list_var_already_put.append(var)
                    self.save_as_numpy(path_value_np, self.df[var].to_numpy())
                    #self.save_as_numpy(path_time_np, self.df[self.name_timestamp_column].to_numpy())
                else:
                    if var != 'Timestamp' or var != 'timestamp':
                        type_data = 'source_data'
                        timeframe = self.tf_str
                        path_value_dic =  {var : var + '_' + timeframe + '.npy'}
                        path_time_np =  'timestamp' + '_' + timeframe + '.npy'
                        plot = True
                        list_var_already_put.append(var)
                        config = {'display_name':var, 'color':'k', 'style':'solid', 'width':1, 'dock':'main'}
                        informations = {'type_config':'standard', 'tf_nbs':self.tf_nbs, 'tf_metric':self.tf_metric}
                        default_config = config
                        config_builder = self.get_configBuilder_standard()
                        plot_builder = {'type_plot': 'standard'}
                        self.save_as_numpy(var + '_' + timeframe + '.npy', self.df[var].to_numpy())
                        #self.save_as_numpy(path_time_np, self.df[self.name_timestamp_column].to_numpy())
                        self.new_work_dic = self.add_variable_new_dic_work(self.new_work_dic, var, type_data, timeframe, path_value_dic, path_time_np, plot, config, config_builder, 
                                                                        default_config, informations, plot_builder)
        print('new work dic: ', self.new_work_dic)




        
    def save_new_work_dic(self):
        '''Save the created dic as a json file in the new_work_path'''
        with open(self.path_json_new_dic_to_save,'w') as f:
            json.dump(self.new_work_dic, f)
            f.close()

    def get_configBuilder_standard(self):
        return {'color':'color', 'style':'style', 'width':'spinInt', 'dock':'dock'}
    
    def create_work(self, df, name_date_column, name_timestamp_column, format_date, data_type, init_date, end_date, path_original_data):
        if type(df[name_date_column].iloc[0]) == int or type(df[name_date_column].iloc[0]) ==  np.int64:
            date = [str(d) for d in df[name_date_column]]
            df[name_date_column] = pd.Series(np.array(date))
        self.init_create_dic_work(df, name_date_column, name_timestamp_column, format_date, data_type, init_date, end_date, path_original_data)
        self.create_folder_work()
        self.build_dic()
        self.save_new_work_dic()
        
    
    
    