#coding:utf-8
'''
Created on 2018-4-3

@author: 
'''

from pattern.pattern import Pattern as Pattern
#import database.datasource.PK10Period as PK10Period
from database.datasource import PK10DataParse

class VerifyData:
    def __init__(self):
        self.pattern = Pattern()
        self.pattern.init_pattern()
        pass
            
    def verify_data(self,user_position,user_pattern_str,user_period):
        with open('../xxx.txt', 'r') as file_to_read:
            i_loop = 0
            _loop = 0
            _pattern_len = len(user_pattern_str)
            _total_num = 0
            _total_list = []
            _f_num = 0
            _total_ok_num = 0
            while i_loop < user_period:
                _line = file_to_read.readline()
                if not _line:
                    break
                _value = self.get_one_period(user_position,_line)
                #print user_pattern_str[_loop:_loop+1],
                #print _value
                if _loop == 0:
                    _f_num = 0
                if user_pattern_str[_loop:_loop+1] != _value:
                    _f_num += 1
                    if _f_num == _pattern_len:
                        _total_num += 1
                    #_total_list.append(_line)
                else:
                    _total_ok_num += 1
                    _f_num = 0
                _loop = (_loop+1)%_pattern_len
                i_loop += 1
            #print user_position
            #print user_pattern_str
            print _total_num  
            print _total_ok_num

    def check_data_period(self,user_position,user_pattern_str,user_period=10):
        user_pattern_str = user_pattern_str.replace('A','X').replace('B','A').replace('X','B')
        print user_pattern_str
        _pattern_pp = self.pattern.get_pattern(user_pattern_str,user_position)
        _pattern_pp.show_pattern(user_period)

    def get_one_period(self,position,linestr):
        _parse = PK10DataParse()
        _lineslice = linestr.split()
        one_num_set = _parse.read_num_set(_lineslice[1])
        _value = int(one_num_set.get_one_num(position))
        if _value <= 5:
            return 'A'
        else:
            return 'B'
        pass

    def verify_data_hit(self,user_position,user_pattern_str,user_period):
        with open('../xxx.txt', 'r') as file_to_read:
            _pattern_len = len(user_pattern_str)
            i_loop = 0
            while i_loop < user_period:
                _line = file_to_read.readline()
                if not _line:
                    break
                _value = self.get_one_period(user_position,_line)
                
if __name__ == '__main__':
    verify_data = VerifyData()
    while True:
        _str = raw_input('position:')
        if _str.lower() == 'exit':
            break
        _position = int(_str)
        _str = raw_input('pattern:')
        if _str.lower() == 'exit':
            break
        _pattern = _str
        _str = raw_input('period:')
        if _str.lower() == 'exit':
            break
        _period = int(_str)
        
        #verify_data.verify_data(_position, _pattern, _period)
        verify_data.check_data_period(_position,_pattern,_period)
    #verify_data.verify_data(0, 'ABABB', 100)
    pass
