#coding:utf-8
'''
Created on 2018-4-3

@author: 
'''
from database.datasource import PK10RawData as PK10RawData
from settings import POSITION_MAX,PERIOD_MAX_LEN,PERIOD_MIN_LEN,PERIOD_STEP

class PK10TrainData:
    def __init__(self):
        self.period_max_len = PERIOD_MAX_LEN
        self.period_min_len = PERIOD_MIN_LEN
        self.period_step_len = PERIOD_STEP
        self.range_num = POSITION_MAX
        self.raw_data = PK10RawData()
        self.raw_data.read_Pk10_rawdata('../pk10_500000.txt')
        self.train_data = []
        for i in range(self.range_num):
            self.train_data.append([])
        pass

    def update_position_train_data(self,data_source,list_len,period_len):
        period_tmp = period_len-1
        for i in range(list_len-1,0,-1):
            data_source[i].type[period_tmp] = ''
            for j in range(i,i-period_len,-1):
                if data_source[j].postion_value <= 5:
                    data_source[i].type[period_tmp] += 'A'
                else:
                    data_source[i].type[period_tmp] += 'B'
        #self.train_data[position].append(data_source[i])
        pass

    def update_period_train_data(self,data_source):
        list_len = len(data_source)
        for _len in range(self.period_min_len,self.period_max_len+1,self.period_step_len):
            self.update_position_train_data(data_source,list_len,_len)
    
    def update_train_data(self):
        for i in range(self.range_num):
            _data_source = self.raw_data.data_postion.get_positin_list(i)
            self.update_period_train_data(_data_source)
            self.train_data[i] = _data_source

if __name__ == '__main__':
    pk10_train_data = PK10TrainData()
    pk10_train_data.update_train_data()
    pass
