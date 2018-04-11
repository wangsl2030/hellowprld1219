#coding:utf-8
'''
Created on 2018-4-10

@author: 
'''

class FileFilter():
    def __init__(self):
        pass
    
    def get_next_time(self,_time):
        h_s = _time.split(':')
        if int(h_s[1]) >= 5:
            return h_s[0] +':'+'%02d'%(int(h_s[1]) - 5)
        else:
            return '%02d'%(int(h_s[0])-1) +':'+'%02d'%(int(h_s[1]) + 55)
    
    def get_next_date(self,_date):
        y_m_d = _date.split('-')
        if int(y_m_d[2]) > 1:
            return y_m_d[0] + '-' + y_m_d[1] + '-' + '%02d'%(int(y_m_d[2]) - 1)
        else:
            #print _date
            if y_m_d[1] == '12':
                return y_m_d[0]+'-11-30'
            elif y_m_d[1] == '11':
                return y_m_d[0]+'-10-31'
            elif y_m_d[1] == '10':
                return y_m_d[0]+'-09-30'
            elif y_m_d[1] == '09':
                return y_m_d[0]+'-08-31'
            elif y_m_d[1] == '08':
                return y_m_d[0]+'-07-31'
            elif y_m_d[1] == '07':
                return y_m_d[0]+'-06-30'
            elif y_m_d[1] == '06':
                return y_m_d[0]+'-05-31'
            elif y_m_d[1] == '05':
                return y_m_d[0]+'-04-30'
            elif y_m_d[1] == '04':
                return y_m_d[0]+'-03-31'
            elif y_m_d[1] == '03':
                if int(y_m_d[0])%4 == 0:
                    return y_m_d[0]+'-02-29'
                else:
                    return y_m_d[0]+'-02-28'
            elif y_m_d[1] == '02':
                return y_m_d[0]+'-01-31'
            elif y_m_d[1] == '01':
                return '%04d'%(int(y_m_d[0])-1)+'-12-31'
            return _date

    def filter(self,file_path):
        file_out = 'out.txt'
        _cur_date = ''
        _cur_time = ''
        b_first_line = True
        file_to_write = open(file_out,'w+')
        with open(file_path,'r') as file_to_read:
            while True:
                _line = file_to_read.readline()
                if not _line:
                    break
                _line_list = _line.split()
                
                if b_first_line == True:
                    _cur_time = _line_list[3]
                    b_first_line = False
                    _cur_date = _line_list[2]
                    
                else:
                    _cur_time = self.get_next_time(_cur_time)
                
                file_to_write.write(_line_list[0]+'\t'+_line_list[1]+'\t'+
                                    _cur_date+' '+_cur_time+'\n')
                    
                if _cur_time == '09:07':
                    _cur_time = '24:02'
                    _cur_date = self.get_next_date(_cur_date) 
                    pass
                
        file_to_write.close()
if __name__ == '__main__':
    _filter = FileFilter()
    _filter.filter('../xxx.txt')
    pass