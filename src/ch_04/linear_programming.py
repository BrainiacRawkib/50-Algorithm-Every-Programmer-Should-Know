import pulp


# instantiate our problem class

model = pulp.LpProblem('Profit_maximizing_problem', pulp.LpMaximize)

A = pulp.LpVariable('A', lowBound=0, cat='Integer')

B = pulp.LpVariable('B', lowBound=0, cat='Integer')

# objective function

model += 5000 * A + 2500 * B, "Profit"

# Constraints

model += 3 * A + 2 * B <= 20

model += 4 * A + 3 * B <= 30

model += 4 * A + 3 * B <= 44


if __name__ == '__main__':
    # solve our problem
    model.solve()
    pulp.LpStatus[model.status]

    # print the decision variable values
    print(A.varValue)
    print(B.varValue)

    # print our objective function value
    print(pulp.value(model.objective))
