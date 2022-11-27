# #Problem:
# There are 4 customers who want to buy houses. There names are:
# 1. Om 
# 2. Jai
# 3. Jagdish
# 4. Krishna

# There are 4 agents who want to rent bungalows. The number of bunglows are
# 1. Bungalow1
# 2. Bungalow2
# 3. Bungalow3
# 4. Bungalow4

# Customers provide preferences of bunglows based of design, location and other factors.
# The agents of house analyse credibility of customers and lists there preference accordingly. 

#Python functions of index, dealing with lists, key has been inspired from my internship
#of webscrapping as it is massivley used there. 


customerpref = {'Om' : ['Bungalow1', 'Bungalow2', 'Bungalow3', 'Bungalow4'],
				'Jai' : ['Bungalow2', 'Bungalow1', 'Bungalow4', 'Bungalow3'],
				'Jagdish' : ['Bungalow2', 'Bungalow4', 'Bungalow3', 'Bungalow1'],
				'Krishna' : ['Bungalow1', 'Bungalow2', 'Bungalow3', 'Daniella']}


agentpref = {'Bungalow1' : ['Om', 'Jagdish', 'Jai', 'Krishna'],
			'Bungalow2' : ['Om', 'Jagdish', 'Krishna', 'Jai'],
			'Bungalow3' : ['Krishna', 'Jai', 'Om', 'Jagdish'],
			'Bungalow4' : ['Om', 'Jai', 'Krishna', 'Jagdish']}


# Here, we consider customers to be the priority. Our algorith terminates unless all customers 
# are assigned. 

#since we have words, we consider our input as a dictionary. Using imperative programming, 
# our operator must be a variable whose state is being updated. Hence, we use .keys to return 
# a view object and reflect changes to dictionary

#assertions describe state of computation at a particular time

x = customerpref.keys()

# Assert X: customerpref.keys()

#presently, we have no matching. Hence, present state for custormers is that they are unassigned

unassignedcustomer = [customer for customer in list(x)] 

#Assert B: unassignedcustomer: [Om, Jai, Jagdish, Krishna]

def stablematch():
	while len(unassignedcustomer) > 0:
		#invariant: 0 < len(unassignedcustomer) <= number of customers
		#assert B and (len(unassignedcustomer)>0)
		for customer in unassignedcustomer:
			assign(customer)
#we say that repeat the process till len(unassignedcustomer) > 0 is true, else terminate
# we do matching till all customers are assigned. 


#Now, we will start matching. At everystep we will match customers and property, but the agent 
#might also dump if has better preference. Hence, we store all temporary match in a list

temporarymatching = [] 
#assert C: temporarymatching = empty list []


#Invariant of main function: 
#counter: customer 1 <= customer <= total customers/size of row in matrix
# Invariant: customeri <-> bungalowj, 0 < i < len(customer) and 0 < j < len(bungalow)
# This is the general assignment you will observe throughout. Speciifc invariants have been specified in the code. 


def assign(customer):

	#assigning customer
	for Bungalow in customerpref[customer]:
		#Invariant: Counter: Bungalow takes the value of preferences of customers
		#in the particular list of the customer
		# Assert D: Bunglow belongs to customerpref[customer] 
		temporarymatch = [available for available in temporarymatching if Bungalow in available]
		#Assert E: D and check if Bunglow is avialable and go through them in the temporary list
		#Invariant: bungalow <-> previous customers, make its list
		# following is a special case of invariant wherein bungalow !<-> previous customers

		if not temporarymatch:
			# Assert F: D and not E: if there are no bungalows taken
			temporarymatching.append([customer, Bungalow])
			# Assert G: temporarymatching = [C1, B] (first customer and approproate match)
			unassignedcustomer.remove(customer)
			#Assert H: unassignedcustomer = [Jai, Jagdish, Krishna]
			break

		else:
			# Assert: Not F 
			# invariant overall: temporarymatch[0][0] = customer <-> (records, bungalows assigned to customers)
			# store: currentbunglow and potentialbungalow variables
			currentBungalow = agentpref[Bungalow].index(temporarymatch[0][0])
			#Assert I : stores the rank of current assignment of agent(bungalow).
			potentialBungalow = agentpref[Bungalow].index(customer)
			#Assert J: stores the rank of new_potential assignment of agent(bungalow). 
			if potentialBungalow < currentBungalow:
				#Assert K: rank of potential assignment is less than current assignment

				unassignedcustomer.remove(customer)
				#assert L: K and remove customer(more preferred) from unassigned
				unassignedcustomer.append(temporarymatch[0][0])
				#Assert M: L and add back the less prefereed
				temporarymatch[0][0] = customer 
				#Asset N: Now you check for the customer who just became unassigned
				break



stablematch()
print("Final Property allocations : ")
print(temporarymatching) # print out the final list of matchings
