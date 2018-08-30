import math
import os
import random
import re
import sys
import datetime

# Complete the solve function below.
def solve(reservations):
	list_reser=[]
	list_date=[]
	for pair in reservations:
		startDate=pair[0]
		endDate=pair[1]
		startDateObject=datetime.datetime.strptime(startDate,'%Y-%m-%d')
		endDateObject=datetime.datetime.strptime(endDate,'%Y-%m-%d')
		if list_date.count(startDate):
			index=list_date.index(startDate)
			list_reser[index] = list_reser[index] + 1
		else:
			list_date.append(startDate)
			index=list_date.index(startDate)
			list_reser.insert(index, 1)
		
		if list_date.count(endDate):
			index=list_date.index(endDate)
			list_reser[index] = list_reser[index] + 1
		else:
			list_date.append(endDate)
			index=list_date.index(endDate)
			list_reser.insert(index, 1)
	
		delta= (endDateObject - startDateObject).days
		for i in range (delta):
			dateObject=startDateObject+ datetime.timedelta(1)
			dateStr=dateObject.strftime('%Y-%m-%d')
			if list_date.count(dateStr):
				index=list_date.index(dateStr)
				list_reser[index] = list_reser[index] + 1
			else:
				list_date.append(dateStr)
				index=list_date.index(dateStr)
				list_reser.insert(index, 1)
	
	
	for i in range(len(list_date)):
		for j in range((len(list_date)) - i -1):
			if list_reser[j] > list_reser[j+1]:
				t=list_reser[j]
				d=list_date[j]
				list_reser[j]=list_reser[j+1]
				list_date[j]=list_date[j+1]
				
				list_date[j+1]=d
				list_reser[j+1]=t
				
	if list_reser.count(list_reser[len(list_reser)-1]) > 1:
		index=list_reser.index(list_reser[len(list_reser)-1])
		return list_date[index]
	else:
		return(list_date[-1])
				
if __name__ == '__main__':
	t = int(raw_input().strip())
	
	for t_itr in xrange(t):
		n = int(raw_input().strip())
		reservations = []

        for _ in xrange(n):
			reservations.append(raw_input().rstrip().split())
		

	result = solve(reservations)
	print result 
	print "log add"
