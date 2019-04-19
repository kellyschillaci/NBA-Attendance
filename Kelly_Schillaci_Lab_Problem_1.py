# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 12:16:13 2019

@author: kdoyl
"""

NBAfile= open('NBA-attendance-1989.txt','r')
NBAList = []
for line in NBAfile:
     textline=line.strip()
     items = textline.split()
     NBAList.append(items)

attendances = []
for line in NBAList:
     attendances.append(int(line[1]))
team, att, price = NBAList[0]
prices = []
for (team, att, price) in NBAList:
     prices.append(float(price))     
teams = []
for (team, att, price) in NBAList:
     teams.append(team)

team, att, price = NBAList[0]
for (team, att, price) in NBAList:
    print('The attendance at',team, 'was',att, 'and the ticket price was',price)
