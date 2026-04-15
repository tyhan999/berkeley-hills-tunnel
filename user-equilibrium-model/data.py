""" SAMPLE
In this file you can find sample data which could be used
into the TrafficFlowMod class in model.py file
"""

# Graph represented by directed dictionary
# In order: first ("5", "7"), second ("5", "9"), third ("6", "7")...
graph = [
    ("0", ["2"]),
    ("2", ["4", "7"]),
    ("3", ["6"]),
    ("4", ["3", "5"]),
    ("5", ["8", "9"]),
    ("6", ["9"]),
    ("7", ["6", "10"]),
    ("9", ["8"]),
    ("8", []),
    ("10", [])
]

# Capacity of each link (Conjugated to Graph with order)
capacity = [7200,
            900, 7200,
            1800,
            600, 900,
            900, 900,
            7200,
            7200, 7200,
            900]

# Free travel time of each link (Conjugated to Graph with order)
free_time = [
    70.8654,
    97.292, 199.8751,
    189.459,
    306.571, 478.0569,
    170.2786, 423.013,
    42.088,
    68.2025, 56.035,
    213.279
    ]

# Origin-destination pairs
origins = ["0"]
destinations = ["8", "9", "10"]
# Generated ordered OD pairs: 
# first ("5", "15"), second ("5", "17"), third ("6", "15")...


# Demand between each OD pair (Conjugated to the Cartesian 
# product of Origins and destinations with order)
demand = [3000, 8000, 4000]

