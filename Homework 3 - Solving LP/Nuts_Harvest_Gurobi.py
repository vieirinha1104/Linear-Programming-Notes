import gurobipy as gp
from gurobipy import Model, GRB

# Dictionary
market_price = {"Peanuts": 1, "Cashews": 7, "Almonds": 3.5}
regular_tin = {"Cashews": 0.15, "Almonds": 0.20}
premium_tin = {"Cashews": 0.25, "Almonds": 0.30}
harvest = {"Peanuts": 900, "Cashews": 150, "Almonds": 200}

# Extract keys from the dictionary
products = market_price.keys()
tin = regular_tin.keys()

# Model
m = Model("Nuts_Harvest")

# Decision Variables
x = m.addVars(products, vtype = GRB.INTEGER, name = "x")
y = m.addVars(products, vtype = GRB.INTEGER, name = "y")
z = m.addVars(products, vtype = GRB.INTEGER, name = "z")

# Objective Function
m.setObjective(gp.quicksum(x[product]*market_price[product] for product in products) + 5*gp.quicksum(y[product] for product in products) + 6*gp.quicksum(z[product] for product in products), GRB.MAXIMIZE)

# Constraints
m.addConstrs(y[p] >= regular_tin[p]*gp.quicksum(y[product] for product in products) for p in tin)
m.addConstrs(z[p] >= premium_tin[p]*gp.quicksum(z[product] for product in products) for p in tin)
m.addConstrs(x[p]+y[p]+z[p] <= harvest[p] for p in products)
m.addConstrs(x[p] >= 0 for p in products)
m.addConstrs(y[p] >= 0 for p in products)
m.addConstrs(z[p] >= 0 for p in products)

# Print the Solution
def printSolution():
    if m.status == GRB.OPTIMAL:
        print("Optimal Distance: ", m.ObjVal, "\n")
        for p in products:
            print("x_", p, " = ", x[p].X)
        for p in products:
            print("y_", p, " = ", y[p].X)
        for p in products:
            print("z_", p, " = ", z[p].X)

    else:
        print("No solution")

m.optimize()
printSolution()