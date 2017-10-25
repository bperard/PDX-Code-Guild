'''
lab 32 - rain data
'''

import datetime
import matplotlib.pyplot as plt


def mean_rain(list):    # receive list of lists of daily data, return mean rain per day
    total = 0
    days = 0
    for day in list:    # itereate through daily data lists
        if day[1] != None:    # if data present, add data to total and increment days by 1
            total += day[1]
            days += 1
    return total / days    # return total sum divided by days total (mean rain per day)


def variance_rain(average, list):    # receive mean rain per day and list of daily data lists, return variance
    variance = 0
    for day in list:    # iterate through daily data lists
        if day[1] is not None:    # if data present, add square of difference between the daily total & the daily mean
            variance += (day[1] - average)**2
    return variance    # return variance value


def max_rain(list):    # receive list of daily data lists, print max rainfall with date(s)
    max = float('-inf')    # set absolute low
    days = []
    for day in list:    # iterate through daily data lists
        if day[1] != None:    # disregard None
            if day[1] > max:    # record new max with date
                max = day[1]
                days = [day[0]]
            elif day[1] == max:    # record date for shared max
                days.append(day[0])
    print('Max rainfall in a day was ' + str(max) + ' gage tips, on date(s):')    # print max rainfall gage tips
    for line in days:
        print(line)    # print date(s) of max rainfall


def yearly_max(list):    # receive list of daily data lists, print year with highest daily average
    max_year = {}
    for day in list:    # iterate through daily data lists
        if day[0].year in max_year:    # check if key present in max_year dict
            if day[1] is not None:    # proceed if data present
                max_year[day[0].year][0] += day[1]    # add daily total to sum at index 0
                max_year[day[0].year][1] += 1    # increment days total by 1 at index 1
        else:
            max_year[day[0].year] = [day[1], 1]    # create list with year as key, add daily sum [0], increment total days [1]
    top = [0, 0]    # track max and year
    for year in max_year:    # iterate between max_year dict keys
        temp = max_year[year][0] / max_year[year][1]    # sum of daily totals divided by total days
        if temp > top[0]:    # record new max daily average and year
            top[0] = temp
            top[1] = year
    print(str(top[1]) + ' had the highest daily average at ' + str(top[0]) + ' tips.')    # print year with max rainfall


dates = []    # variable used for main list

with open('sylvan.csv', 'r') as file:    # open file for readiing, split into strings at '\n'
    lines = file.read().split('\n')

for day in lines:    # iterate through each string in list, split strings into individual elements at blank space
    dates.append(day.split())

for data in dates:    # iterate through elements in each list
    if data == []:
        dates.remove(data)    # remove blank set
    else:
        data[0] = datetime.datetime.strptime(data[0], '%d-%b-%Y')    # index 0 to datetime class
        for i in range(1, len(data)):
            if data[i] == '-':    # convert - to None
                data[i] = None
            else:
                data[i] = int(data[i])    # convert index 1+ to int type

# create data lists for x and y values of plot
yval = []
xval = []
i = 0
for day in dates:
    if day[0].year == 2017:    # increment days on x axis, y axis daily totals
        i += 1
        xval.append(i)
        yval.append(day[1])

plt.plot(xval, yval)    # plot values from lists
plt.show()    # show plot
