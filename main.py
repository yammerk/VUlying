f1 = open('MokumAirwaysPassengers.txt')
f2 = open('MokumAirwaysDistances.txt')
f3 = open('MokumAirwaysCities.txt')

passengermatrix = open('MokumAirwaysPassengers.txt').read()
passengermatrix = [item.split(',') for item in passengermatrix.split('\n')[:-1]]



distancematrix = open('MokumAirwaysDistances.txt').read()
distancematrix = [item.split(',') for item in distancematrix.split('\n')[:-1]]

pkresult = [[0 for x in range(28)] for y in range(28)]

#iterate through rows of X
for i in range(len(passengermatrix)):
    ##iterate through columns of Y
   for j in range(len(distancematrix[0])):
          pkresult[i][j] += int(passengermatrix[i][j]) * int(distancematrix[i][j])

print pkresult

tresult = [[0 for x in range(28)] for y in range(28)]

for i in range(len(distancematrix)):
    for j in range(len(distancematrix)):
        tresult[i][j] = int(distancematrix[i][j])/800.0

print tresult

###result = [[sum(a*b for a,b in zip(passengermatrix_row, distancematrix_col)) for distancematrix_col in zip(*distancematrix)] for passengermatrix_row in passengermatrix]
###for r in result:
###   print(r)



#for r in result:
    #print(r)