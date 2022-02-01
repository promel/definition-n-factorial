# Definition: n factorial (n!) e.g 6! = 6 ⋅ 5 ⋅ 4 ⋅ 3 ⋅ 2 ⋅ 1 = 720.
from this import d


n = int(input('Enter n factorial: '))
factors = list(range(n , 1, -1))
answer = 1
for factor in factors:
    answer *= factor

definition = " * ".join(map(str, factors))
result = f'{n}! {definition} = {answer}'
print(result)
