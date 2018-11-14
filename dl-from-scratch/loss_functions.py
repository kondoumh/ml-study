import numpy as np

def mean_squared_error(y, t):
    return 0.5 * np.sum((y-t)**2)

def cross_entropy_error(y, t):
    delta = 1e-7
    return -np.sum(t * np.log(y + delta))

t = [0, 0, 1, 0, 0, 0, 0, 0, 0 ,0]
y1 = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
y2 = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]

# test mean_squared_error

result = mean_squared_error(np.array(y1), np.array(t))
print(result)

result = mean_squared_error(np.array(y2), np.array(t))
print(result)

# test cross_entropy_error
result = cross_entropy_error(np.array(y1), np.array(t))
print(result)

result = cross_entropy_error(np.array(y2), np.array(t))
print(result)