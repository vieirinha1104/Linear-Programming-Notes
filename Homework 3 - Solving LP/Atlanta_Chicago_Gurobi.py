import gurobipy as gp
from gurobipy import Model, GRB

# Model
m = Model("Atlanta_Chicago")

# Dictionaries
a = {"Boston": 1076, "Dallas": 781, "St. Louis": 555, "Tampa": 456} # Miles from Atlanta to each city
b = {"Boston": 984, "Dallas": 968, "St. Louis": 297, "Tampa": 1174} # Miles from Chicago to each city
c = {"Boston": 70000, "Dallas": 100000, "St. Louis": 80000, "Tampa": 60000} # Widget demand to each city

# Extract the keys from the dictionary
cities = a.keys()

# Decision Variables
x = m.addVars(cities, vtype = GRB.INTEGER, name = "x")
y = m.addVars(cities, vtype = GRB.INTEGER, name = "y")

# Objective Function
m.setObjective(gp.quicksum(x[city]*a[city] for city in cities) + gp.quicksum(y[city]*b[city] for city in cities), GRB.MINIMIZE)

# Constraints
m.addConstrs(x[city] + y[city] == c[city] for city in cities)
m.addConstr(gp.quicksum(x[city] for city in cities) - 180000 <= 0)
m.addConstr(gp.quicksum(y[city] for city in cities) - 220000 <= 0)

# Non-negativity Constraints
m.addConstrs(x[city] >= 0 for city in cities) 
m.addConstrs(y[city] >= 0 for city in cities)

# Print the Solution
def printSolution():
    if m.status == GRB.OPTIMAL:
        print("Optimal Distance: ", m.ObjVal, "\n")
        for city in cities:
            print("x_", city, " = ", x[city].X)
        for city in cities:
            print("y_", city, " = ", y[city].X)
    else:
        print("No solution")

m.optimize()
printSolution()
