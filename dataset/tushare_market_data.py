#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 11:30:16 2019

@author: dongdong
"""

import tushare as ts
ts.set_token('f867cf1c65e806c64096d26d7f7ea70db0c38bddb027c034f20c64de')
pro = ts.pro_api()
def LoadHistoryData(date):
    return date
def LoadTradeCalendar(start,end):
    dates =  pro.query('trade_cal', start_date=start, end_date=end)
    trade_days = []
    for date in dates.index:
        if dates.iloc[date].is_open:
            trade_days.append(dates.iloc[date].cal_date)
    return trade_days