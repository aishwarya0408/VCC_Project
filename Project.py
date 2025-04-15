import time
import numpy as np

def simulate_computation():
    data = np.random.rand(5000, 5000)
    result = np.dot(data, data.T)
    return result

if __name__ == "__main__":
    for _ in range(3):
        print("Running HPC workload...")
        simulate_computation()
        time.sleep(2)
