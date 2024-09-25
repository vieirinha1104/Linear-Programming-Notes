import gurobipy as gp
from gurobipy import GRB, Model

# Dictionary for the Material Cost:
c_dict = {"Car": 2, "Soldier": 2, "Train": 3}
# Dictionary for the Material Selling Price:
s_dict = {"Car": 9, "Soldier": 11, "Train": 13}
# Dictionary for the Woodwork Time:
w_dict = {"Car": 5, "Soldier": 5, "Train": 5}
# Dictionary for the Painting Time:
p_dict = {"Car": 4, "Soldier": 8, "Train": 6}

# Create the model
m = Model("Joy_Kim")

# Extract chores from the dictionary
toys = list(c_dict.keys())

# Define decision variables
x = m.addVars(toys, vtype = GRB.INTEGER, name = "x")
y = m.addVars(toys, vtype = GRB.INTEGER, name = "y")

# Define objective function
m.setObjective(gp.quicksum(s_dict[toy]*y[toy] for toy in toys) - gp.quicksum(c_dict[toy]*x[toy] for toy in toys), GRB.MAXIMIZE) # Syntax: setObjective (objective function, GRB.MINIMIZE or GRB.MAXIMIZE)

# Add Constraints
m.addConstr(gp.quicksum(x[toy]*w_dict[toy] for toy in toys) <= 240) # Single Constraint, Joy's maximum work hours
m.addConstr(gp.quicksum(y[toy]*p_dict[toy] for toy in toys) <= 360) # Single Constraint, Kim's maximum work hours
m.addConstrs((y[toy] - x[toy]) <= 0 for toy in toys) # Multiple Constraints, Kim can only paint if Joy had produced, y_i <= x_i for all i in {0, 1, 2}

# Add non-negativity constraint
m.addConstrs(x[toy] >= 0 for toy in toys)
m.addConstrs(y[toy] >= 0 for toy in toys)

# Print the Solution
def printSolution():
    if m.status == GRB.OPTIMAL:
        print("Profit: ", m.ObjVal, "\n")
        for toy in toys:
            if x[toy].X > 0.0001:
                print("x_", toy," : ", x[toy].X, " ")
            if y[toy].X > 0.0001:
                print("y_", toy," : ", y[toy].X, "\n")
    else:
        print("No solution")

m.optimize()
printSolution()

