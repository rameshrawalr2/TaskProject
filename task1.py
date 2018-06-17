#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 12:31:18 2018

@author: ramesh
"""
import pandas as pd


#main function definition
def main():
    #Creating two DataFrame dframe,df 
    dframe=pd.DataFrame()
    df=pd.DataFrame()
    
    #Reading csv file and inserting in dataframe dframe
    dframe=pd.read_csv("insurance.csv")
    
    #deleting column named traded_date
    dframe.drop('traded_date', axis=1,inplace=True)
    
    #Multiplication of two columns 
    newcol=dframe['closing_price']*dframe['volume']

    #inserting SProduct value  in a data frame
    dframe.insert(5,"product",newcol)
    
    #for loop to get the required value from dataframe
    for index, row in dframe.iterrows():
        if(int(row['closing_price'])>7000 and int(row['volume'])>20000):
            df=df.append(row)   #adding row in another dataframe
            
    #saving the dataframe in new csv file   
    df.to_csv("finaldata.csv",index=False)

main()  #function call
        