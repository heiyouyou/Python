#!/usr/bin/env python
# coding=utf-8  
__author__ = 'wzy'  
import logging 
logging.basicConfig(
	level=logging.WARNING,  
	filename='./log/log.txt', #log.txt文件不存在，则进行自动创建，但是./log/路径必须存在
	filemode='w',
    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'
)  
# use logging  
logging.info('this is a loggging info message')  
logging.debug('this is a loggging debug message')  
logging.warning('this is loggging a warning message')  
logging.error('this is an loggging error message')  
logging.critical('this is a loggging critical message')  