""" SAMPLE
In this file you can find sample data which could be used
into the TrafficFlowMod class in model.py file
"""

# import variables
from params import *
from model import TrafficFlowModel

# Graph represented by directed dictionary
# In order: first ("5", "7"), second ("5", "9"), third ("6", "7")...
graph = [
    ("0", ["1"]),
    ("1", ["2", "9"]),
    ("2", ["7", "8"]),
	("7", ["10"]),
    ("8", ["9"]),
    ("9", ["10"])
]

# Capacity of each link (Conjugated to Graph with order)
# Here all the 19 links have the same capacity
capacity = [C1,
            C2, C3,
            C4, C5,
            C6,
            C7,
			C8]

# Free travel time of each link (Conjugated to Graph with order)
free_time = [
    70.8658,
    97.2931, 328.0776,
    256.3823, 306.5713,
	209.1972,
	189.4586,
	42.088
]

# Origin-destination pairs
origins = ["0"]
destinations = ["10"]
# Generated ordered OD pairs: 
# first ("5", "15"), second ("5", "17"), third ("6", "15")...


# Demand between each OD pair (Conjugated to the Cartesian 
# product of Origins and destinations with order)
demand = [D]

# Initialize the model by data
mod = TrafficFlowModel(graph, origins, destinations, 
demand, free_time, capacity)

# Change the accuracy of solution if necessary
mod._conv_accuracy = 1e-6

# Display all the numerical details of
# each variable during the iteritions
# mod.disp_detail()

# Set the precision of display, which influences
# only the digit of numerical component in arrays
mod.set_disp_precision(4)

# Solve the model by Frank-Wolfe Algorithm
mod.solve()

# Generate report to console
# mod.report()

# Return the solution if necessary
# mod._formatted_solution()

if __name__ == "__main__":
	with open('results.out', 'w') as f:
		result = mod._formatted_solution()
		f.write('{} {} {}'.format(result[0],result[1],result[2]))

