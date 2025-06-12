def add(a, b):
    return a + b

result = add(5, 3)  

'''

def greet(name):
    print("Hello, " + name + "!")
greet("Alice")  
'''


def calculate_weighted_average(values, weights):
    if len(values) != len(weights) or len(values) == 0:
        return 0  
    weighted_sum = sum(value * weight for value, weight in zip(values, weights))
    total_weight = sum(weights)
    weighted_average = weighted_sum / total_weight
    return weighted_average

# Example usage
values = [10, 20, 30]
weights = [1, 2, 3]
print("The weighted average is:", calculate_weighted_average(values, weights))

  
