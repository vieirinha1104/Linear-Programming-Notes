import gurobipy as gp
from gurobipy import GRB, Model
# Input
W, s=input().split()
W = int(W)
s = int(s)
w = [0]*2000
v = [0]*2000
for i in range(0,s):
    a, b=input().split()
    w[i] = int(a)
    v[i] = int(b)
# Model
m = Model("Knapsack")
# Decision Var
x = m.addVars(s, vtype = GRB.BINARY, name = "x")
# Objective Function
m.setObjective(gp.quicksum(x[i]*v[i] for i in range(0,s)), GRB.MAXIMIZE)
# Constraints
m.addConstr(gp.quicksum(x[i]*w[i] for i in range(0,s)) <= W)
m.optimize()
print(m.ObjVal) 