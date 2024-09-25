import gurobipy as gp
from gurobipy import Model, GRB
# Work Hours Table
c = [[3, 2, 5], [4, 1, 4], [5, 3, 7]]

# Model
m = Model("3_Workers_3_Tasks")

# Decision Var
x = m.addVars(3, 3, vtype = GRB.BINARY, name ="x") # For example, x = model.addVars(2, 3) would create six variables, accessed as x[0,0], x[0,1], x[0,2], x[1,0], x[1,1], and x[1,2].

# Objective Function
m.setObjective(gp.quicksum(x[i, j]*c[i][j] for i in range (0,3) for j in range (0,3)), GRB.MINIMIZE)

# Constraints
m.addConstrs(gp.quicksum(x[i, j] for i in range (0,3)) == 1 for j in range(0,3))
m.addConstrs(gp.quicksum(x[i, j] for j in range (0,3)) == 1 for i in range(0,3))

# Print Solution
def printSolution():
    if m.status == GRB.OPTIMAL:
        print("Total Work Hours: ", m.ObjVal)
        for i in range(0,3):
            for j in range (0,3):
                if(x[i, j].X > 0.5):
                    print("Worker: ", i+1, "Assigned to: ", j+1, " with ", c[i][j], " hours")
    else:
        print("No solution")

m.optimize()
printSolution()