#coding:utf-8
'''
Created on 2018-4-2

@author: 
'''

import time
from settings import POSITION_MAX,PERIOD_MAX_LEN

class PK10OnePosition:
    def __init__(self):
        self.period_max_len = PERIOD_MAX_LEN

    def update_num_set(self,period_num,postion_value,datetime):
        self.period_num = period_num
        self.postion_value = int(postion_value)
        self.period_date = datetime
        self.type = []
        for i in range(self.period_max_len):
            self.type.append('')

class PK10PostionSet:
    def __init__(self):
        self.range_num = POSITION_MAX
        self.postion_list = []
        for i in range(self.range_num):
            self.postion_list.append( [] )

        #print self.postion_list

    def get_positin_list(self,num):
        if len(self.postion_list) <= num:
            return []
        return self.postion_list[num]
    
    def get_range_num(self):
        return self.range_num
    
    def read_positon(self,linestr):
        if linestr == '':
            return
        lineslicelist = linestr.split()
        data_parse = PK10DataParse()
        period_num = data_parse.read_period_num(lineslicelist[0])
        one_num_set = data_parse.read_num_set(lineslicelist[1])
        period_date = data_parse.read_period_datetime(lineslicelist[2]
                                                           +' '+lineslicelist[3])
        for i in range(self.range_num):
            one_postion = PK10OnePosition()
            one_postion.update_num_set(period_num, one_num_set.get_one_num(i), period_date)
            self.postion_list[i].append(one_postion)
        pass
            

class PK10NumSet:
    def __init__(self):
        pass
    
    def read_one_num_set(self,linestr):
        #self.position_list = linestr.split(',')
        #print linestr
        self.position_list = [int(x) for x in linestr.split(',')]
        
    def get_one_num(self,postion):
        return self.position_list[postion]

    
class PK10DataParse:
    def __init__(self):
        pass
  
    def read_period_num(self,linestr):
        return int(linestr.strip())
    
    def read_period_datetime(self,linestr):
        timeArray = time.strptime(linestr.strip(), "%Y-%m-%d %H:%M")
        return int(time.mktime(timeArray))

    def read_num_set(self,linestr):
        if linestr == '':
            return
        one_num_set = PK10NumSet()
        one_num_set.read_one_num_set(linestr)
        return one_num_set

    
class PK10OnePeriod:
    def __init__(self):
        pass
    
    def read_one_period(self,linestr):
        if linestr == '':
            return
        lineslicelist = linestr.split()
        data_parse = PK10DataParse()
        self.period_num = data_parse.read_period_num(lineslicelist[0])
        self.one_num_set = data_parse.read_num_set(lineslicelist[1])
        self.period_date = data_parse.read_period_datetime(lineslicelist[2]
                                                           +' '+lineslicelist[3])

            
class PK10PeriodSet:
    def __init__(self):
        self.data_list = []
    
    def read_num_set(self,linestr):
        pk10_one_period = PK10OnePeriod()
        pk10_one_period.read_one_period(linestr)
        self.data_list.append(pk10_one_period)

    
class PK10RawData:
    def __init__(self):
        self.data_period = PK10PeriodSet()
        self.data_postion = PK10PostionSet()
        
    def read_Pk10_rawdata(self,filepath):
        with open(filepath, 'r') as file_to_read:
            while True:
                _line = file_to_read.readline()
                if not _line:
                    break
                #self.data_period.read_num_set(_line)
                self.data_postion.read_positon(_line)    
        pass
        
if __name__ == '__main__':
    raw_data = PK10RawData()
    raw_data.read_Pk10_rawdata('../xxx.txt')
    pass
