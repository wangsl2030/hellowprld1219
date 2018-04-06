#coding: utf-8
'''
Created on 2018-4-2

@author:
'''
from train.traindata import PK10TrainData as PK10TrainData
#import train.traindata.TrainData as TrainData
from settings import POSITION_MAX,PERIOD_MAX_LEN,PERIOD_MIN_LEN,PERIOD_STEP

class PatternPositionPeriod:
    def __init__(self):
        self.pattern_count = 0
        self.pattern_apperance = []
        self.pattern_last_apperance = 0
        self.pattern_period_average = 0
        self.pattern_period_max = 0
        self.pattern_period_min = 0
        self.pattern_period = []

class PatternPositionDict:
    def __init__(self):
        self.pattern_data = {}

    def init_pattern(self,pattern_len,train_data):
        for item in train_data:
            _pattern = None
            type_name = item.type[pattern_len-1]
            if type_name == '':
                continue
            if self.pattern_data.has_key(type_name):
                _pattern = self.pattern_data[type_name]
            else:
                _pattern = PatternPositionPeriod()
                
            _pattern.pattern_count += 1
            _pattern.pattern_apperance.append(item)
            
            if item.period_date > _pattern.pattern_last_apperance:
                _pattern.pattern_last_apperance = item.period_date
                   
            self.pattern_data[type_name] = _pattern
            pass
        
        for type_name,_pattern in self.pattern_data.iteritems():
            _cur_apperance = 0
            _period_total = 0
            for item in _pattern.pattern_apperance:
                if 0 == _cur_apperance:
                    _cur_apperance = item.period_date
                    continue
                _period = _cur_apperance - item.period_date
                _pattern.pattern_period.append(_period)
                _period_total += _period
                if _period > _pattern.pattern_period_max:
                    _pattern.pattern_period_max = _period
                if 0 == _pattern.pattern_period_min:
                    _pattern.pattern_period_min = _period 
                if _period < _pattern.pattern_period_min:
                    _pattern.pattern_period_min = _period
                _cur_apperance = item.period_date
            if _pattern.pattern_count > 0:
                _pattern.pattern_period_average = float(_period_total) / float(_pattern.pattern_count)
        pass
    
class PatternPosition:
    def __init__(self):
        self.pattern_data = {}
        self.period_max_len = PERIOD_MAX_LEN
        self.period_min_len = PERIOD_MIN_LEN
        self.period_step_len = PERIOD_STEP
        
    def init_pattern(self,train_data):
        for i in range(self.period_min_len,self.period_max_len,self.period_step_len):
            _pattern_pp = PatternPositionDict()
            _pattern_pp.init_pattern(i,train_data)
            self.pattern_data[i] = _pattern_pp

class PatternPeriod:
    def __init__(self):
        self.range_num = POSITION_MAX
        self.pattern = []
        for i in range(self.range_num):
            self.pattern.append(PatternPosition())
    
    def init_pattern_position_period(self,positon_num,train_data):
        self.pattern[positon_num].init_pattern(train_data)
        pass

    def init_pattern_period(self,train_data):
        for i in range(self.range_num):
            self.init_pattern_position_period(i,train_data[i])
        pass
   
class Pattern:
    def __init__(self):
        _pk10_train_data = PK10TrainData()
        _pk10_train_data.update_train_data()
        self.train_data = _pk10_train_data.train_data
       
    def init_pattern(self):
        self.pattern_period = PatternPeriod()
        self.pattern_period.init_pattern_period(self.train_data)
        pass

if __name__ == '__main__':
    _pattern = Pattern()
    _pattern.init_pattern()
    pass

