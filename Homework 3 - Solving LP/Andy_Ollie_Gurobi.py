import gurobipy as gp
from gurobipy import GRB, Model

# Create the model
m = Model("Andy_Ollie")

# Create the time table 
time = {"Mow_Lawn": 70, "Clean_Bath": 40, "Vacuum_House": 40, "Clean_Kitchen": 25, "Fold_Laundry": 20, "Wash_Dishes": 15}

# Extract chores from the dictionary
chores = list(time.keys())

# Define decision variables
x = m.addVars(chores, vtype = GRB.BINARY, name = "x")
y = m.addVars(chores, vtype = GRB.BINARY, name = "y")

# Print the Solution
def printSolution():
    assignment = {}
    for chore in chores:
        if(x[chore].X > 0.5):
            assignment[chore] = "Andy"
        elif(y[chore].X > 0.5):
             assignment[chore] = "Ollie"
    print("Assignment:", assignment)

# Define objective function
m.setObjective(gp.quicksum(time[chore]*x[chore] for chore in chores) - gp.quicksum(time[chore]*y[chore] for chore in chores), GRB.MINIMIZE) # Syntax: setObjective (objective function, GRB.MINIMIZE or GRB.MAXIMIZE)

# Add Constraints
m.addConstrs(x[chore] + y[chore] == 1 for chore in chores) # assignment constraints, you can't have x and y picking the same chore, x_c + y_c = 1, for all c in C -> m.addConstrs(x[chore] + y[chore] == 1 for chore in chores)
# Add non-negativity constraint
m.addConstr(gp.quicksum(time[chore]*x[chore] for chore in chores) - gp.quicksum(time[chore]*y[chore] for chore in chores) >= 0)

m.optimize()
printSolution()
