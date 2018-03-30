#Michael Hany
#Aprior algorithm 
#Data Mining 4th year computer engineering

import itertools

def main():	
	database = [[1,3,4],[2,3,5],[1,2,3,5],[2,5]]
	minSupport = 2
	lItems = []
	lSupport = []
	cItems = []
	cSupport = []

	#extract unique items
	for i in database:
		for j in i:
			if([j] not in cItems):
				cItems.append([j])

	i = 1
	while True:
		cSupport = gnerateSupport(cItems,database)
		lItems,lSupport = generateL(cItems, cSupport, minSupport)
		if(lItems == []):break
		cItems = generateC(lItems)

		#printing
		print 'L'+ str(i) + ":"
		i +=1
		for n in range(len(lItems)):
			print str(lItems[n]) + str(lSupport[n])
		print

#generate ck+1 list from a given lk list	
def generateC(lItems):
	retItems = []
	common = (len(lItems[0]) - 1)
	for i in lItems:
		for j in lItems:
			#in case of C2 we don't need to find common items between sets
			if common < 1:
				if(i != j):
					if((j+i) not in retItems):
						retItems.append(i+j)
			#for other cases after c2
			else:
				temp = []
				for k in (list(i)+list(j)):
					if(k not in temp):
						 temp.append(k)
				temp = set(temp)
				if(len(temp) == (common + 2)):
					if(temp not in retItems):
						if(everySubsetExsists(temp,lItems)):
							retItems.append(temp)
	#turn output into list type instead of set
	for n in range(len(retItems)): 
		retItems[n] = list(retItems[n])

	return retItems

#this fuction generates the support of a set in a given database
def gnerateSupport(Items, database):
	Support = []
	for i in Items:
		Support.append(0)
	n = 0
	for i in Items:
		for j in database:
			if (set(i).issubset(set(j))):
				Support[n] += 1
		n += 1
	return Support

#this function gerated lk+1 by taking ck and minimum Support
def generateL(cItems, cSupport, minSupport):
	lItems = []
	lSupport = []
	size = len(cItems)

	for n in range(size):
		if(cSupport[n] >= minSupport):
			lItems.append(cItems[n])
			lSupport.append(cSupport[n])
	return (lItems,lSupport)

#retruns true if every subset of lenth n-1 where n is the length of candidate exists in superset
def everySubsetExsists(candidate, superSet):
	#generate subsets
	l = set(itertools.combinations(candidate, len(candidate) - 1))
	#if all subsets exist in superset return true else false
	for i in l:
		flag = False
		for j in superSet:
			if(set(i) == set(j)):
				flag = True
				break
		if(flag == False):return False
	return True

if __name__== "__main__":
	main()