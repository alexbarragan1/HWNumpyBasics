import time
import numpy as np

start_time = time.time()
python_list = [i for i in range(1, 1000001)]
squared_list = [x ** 2 for x in python_list]
end_time = time.time()
print("Time taken with Python lists:", end_time - start_time, "seconds")

start_time = time.time()
numpy_array = np.arange(1, 1000001)
squared_array = numpy_array ** 2
end_time = time.time()
print("Time taken with NumPy arrays:", end_time - start_time, "seconds")