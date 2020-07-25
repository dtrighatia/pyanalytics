# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 18:52:28 2020

@author: PC
"""


import pandas as pd
#%%
#1. Customer Transaction Data 
denco=pd.read_csv("denco.csv")
denco.columns
customer_data=denco.groupby("custname").aggregate({'revenue':['sum','count']}).reset_index()           
customer_data.columns=['Custname','revenue_sum','transaction_count'] 

#Sorting by Count

customer_data=customer_data.sort_values('transaction_count',ascending=False)
top5_customer_count=customer_data.head()
top5_customer_count #Top 5 Customers by Transaction Count
bot5_customer_count=customer_data.tail()
bot5_customer_count #Bottom 5 Customers by Transaction Count
    #%%
#2. Customer Revenue Data

customer_data=customer_data.sort_values('revenue_sum',ascending=False)
top5_customer_rev=customer_data.head()
top5_customer_rev #Top 5 Customers by Total Revenue Amount
bot5_customer_rev=customer_data.tail()
bot5_customer_rev #Bottom 5 Customers by Total Revenue Amount

#%% 
#3. Part no data
part_data=denco.groupby("partnum").aggregate({'revenue':'sum','margin':'sum'}).reset_index()           
part_data.columns=['partnum','revenue_sum','margin_sum'] 

#Sorting by Revenue

part_data=part_data.sort_values('revenue_sum',ascending=False)
top5_part_rev=part_data.head()
top5_part_rev  #Top 5 Parts by Total Revenue Amount
Bot5_part_rev=part_data.tail()
Bot5_part_rev  #Bottom 5 Parts by Total Revenue Amount

#Sorting by Profit Margin
part_data=part_data.sort_values('margin_sum',ascending=False)
top5_part_margin=part_data.head()
top5_part_margin #Top 5 Parts by Total Profit Margin 
bot5_part_margin=part_data.tail()
bot5_part_margin #Bottom 5 Parts by Total Profit Margin