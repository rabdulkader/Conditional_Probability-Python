from numpy import random as rand

#random seed generetor
rand.seed(0)

#list of age
age_list=[20,30,40,50]

#dict of age for any customer and purchasing customer
cust= {age_list[0]:0, age_list[1]:0, age_list[2]:0, age_list[3]:0}
purch= {age_list[0]:0, age_list[1]:0, age_list[2]:0, age_list[3]:0}

total_purch=0

#number of potential customers
n=100000

#counter for for loop
counter = 0

#sample data generetor
for _ in range(n):
    
    #picks random age from list
    age=rand.choice(age_list)
    #adds one customer to the picked age group
    cust[age] += 1
    
    #custom sample of the relation between customer age and purchase probability 
    prob_purch= float(age) / 100.0
    if (rand.random() <+ prob_purch):
        purch[age] += 1
        total_purch += 1
        
#print result
print("Customers               : " + str(cust))
print("Customers that pucheased: " + str(purch))


#probability of someone purchasing
PE= float(total_purch) / n
print("\nProbability of purchase (PE) is " + str(PE), "\n")

#conditional probability calculator
for _ in range(4):
    
    #picks age from ahe list in order
    age=age_list[counter]
    counter += 1
    
    #probability of any an age from potentia customers 
    PF=float(cust[age]) / n
    print("\nPF for age " + str(age) + " is " + str(PF))
    
    #probability of being an specific age group and puchasing
    PFE= float(purch[age]) / float(cust[age])
    print("P(F|E) Probability of purchasing at age " + str(age) + " is " + str(PFE))
    
    #probability of a specific age group perchasing out of all potential customers
    PEF= PF * PFE
    print("P(E,F) at age: " + str(age), " is " + str(PEF))
