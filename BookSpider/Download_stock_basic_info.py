# -*- coding: utf-8 -*-

import tushare as ts
import pandas as pd
def download_stock_basic_info():

    try:
        df = ts.get_stock_basics()
        #直接保存到csv
        print 'choose csv'
        df.to_csv('stock_basic_list.csv');
        print 'download csv finish'
    except:
        print ('download error')
    return

if __name__ == '__main__':
    download_stock_basic_info()



