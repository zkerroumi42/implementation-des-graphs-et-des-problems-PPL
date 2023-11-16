import cvxpy as cp
import numpy as np

# Définition du problème primal
c = np.array([-1, -1])  # Coefficients de la fonction objectif
A = np.array([[-1, -3], [-2, -1]])  # Coefficients des contraintes/
b = np.array([-3, -2])  # Termes constants des contraintes

n = c.shape[0]
x = cp.Variable(n)
objective = cp.Minimize(c @ x)
constraints = [A @ x >= b, x >= 0]
problem = cp.Problem(objective, constraints)
problem.solve()

# Solution du problème primal
print("Primal Solution:")
print("Optimal value:", problem.value)
print("Optimal variables:", x.value)

# Définition du problème dual
m = b.shape[0]
y = cp.Variable(m)
dual_objective = cp.Maximize(b @ y)
dual_constraints = [A.T @ y <= c, y >= 0]
dual_problem = cp.Problem(dual_objective, dual_constraints)
dual_problem.solve()

# Solution du problème dual
print("Dual Solution:")
print("Optimal value:", dual_problem.value)
print("Optimal variables:", y.value)