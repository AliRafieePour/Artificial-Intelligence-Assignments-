#Ali Rafiee Pour 9425643
#jim
from scipy.optimize import linprog
c = [0,0,0,0,-1]
A = [[3, -3, -4, 0, 1],
     [-1, -2, 0, 4, 1],
     [-2, 0, 1, 2, 1],
     [-1, 2, -2, 1, 1],
     [2, -3, 3, -2, 1]]
Aeq=[[1,1,1,1,0]]
beq=[[1]]
b = [0, 0, 0, 0, 0]
res =linprog(c, A_eq=Aeq, b_eq=beq, A_ub=A, b_ub=b, bounds = ((0, 1), (0, 1), (0, 1), (0, 1), (None, None)))

print(res)


#Ali Rafiee Pour 9425643
#jim p2
from scipy.optimize import linprog
c = [0, 0, 0, 0, 0, 1]
A = [[1, -3, 2, -2, 1, -1],
     [2, 3, 0, 3, -2, -1],
     [0, 4, -1, -3, 2, -1],
     [-4, 0, -2, 2, -1, -1]]
Aeq=[[1,1,1,1,1, 0]]
beq=[[1]]
b = [0, 0, 0, 0]
res =linprog(c, A_eq=Aeq, b_eq=beq, A_ub=A, b_ub=b, bounds = ((0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (None, None)))

print(res)

#Ali Rafiee Pour 9425643
#dal p1
from scipy.optimize import linprog
c = [0, 0, 0, -1]
A = [[0, -2, 0, 1],
     [1, 0, -1, 1],
     [-1, 0, 0, 1],
     [-1, -1, 1, 1]]
Aeq=[[1,1,1,0]]
beq=[[1]]
b = [0, 0, 0, 0]
res =linprog(c, A_eq=Aeq, b_eq=beq, A_ub=A, b_ub=b, bounds = ((0, 1), (0, 1), (0, 1),(None, None)))
print(res)


#Ali Rafiee Pour 9425643
#dal p2
from scipy.optimize import linprog
c = [0, 0, 0, 0, 1]
A = [[0, -1, 1, 1, -1],
     [2, 0, 0, 1, -1],
     [0, 1, 0, -1, -1]]
Aeq=[[1, 1, 1, 1, 0]]
beq=[[1]]
b = [0, 0, 0]
res =linprog(c, A_eq=Aeq, b_eq=beq, A_ub=A, b_ub=b, bounds = ((0, 1), (0, 1), (0, 1), (0, 1), (None, None)))
print(res)

