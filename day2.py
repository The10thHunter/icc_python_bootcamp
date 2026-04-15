import random
rng_list = random.sample(range(10000), 10)
print(rng_list)
org_list = [2,1,1,1,2]
print(org_list)

def highLow(exlist):
    low = 10001
    high = -1 
    for n in range(len(exlist)): #We're gonna get each thing in the list
        if exlist[n] > high: #Which item was bigger than the last
            high = exlist[n]
            print("New high: ", high)
        if exlist[n] < low: 
            low = exlist[n]
            print("Low:", low)


    print("Highest Number: ", high)
    print("Lowest Number: ", low)

#print("Smallest number:", x)

highLow(rng_list)
highLow(org_list)

