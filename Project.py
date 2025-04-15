# cloud_hpc_optimization.py

"""
Optimizing Cloud Resource Allocation for High-Performance Computing (HPC) Workloads

This script simulates a cloud-based dynamic provisioning and monitoring system for HPC workloads.
It uses multithreading to mimic concurrent workloads, and logs system metrics for analysis.
"""

import time
import threading
import random
import numpy as np
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

# Simulate workload execution
def hpc_workload(task_id):
    logging.info(f"Task {task_id}: Starting workload computation...")
    data = np.random.rand(3000, 3000)
    result = np.dot(data, data.T)
    logging.info(f"Task {task_id}: Workload completed with result shape {result.shape}")
    return result

# Simulate auto-scaling decision-making
class AutoScaler:
    def __init__(self, min_nodes=1, max_nodes=5):
        self.current_nodes = min_nodes
        self.min_nodes = min_nodes
        self.max_nodes = max_nodes

    def evaluate_scale(self, current_load):
        if current_load > 70 and self.current_nodes < self.max_nodes:
            self.current_nodes += 1
            logging.info(f"[AutoScaler] Scaling up. New node count: {self.current_nodes}")
        elif current_load < 30 and self.current_nodes > self.min_nodes:
            self.current_nodes -= 1
            logging.info(f"[AutoScaler] Scaling down. New node count: {self.current_nodes}")
        else:
            logging.info(f"[AutoScaler] No scaling action taken. Node count: {self.current_nodes}")

# Simulate monitoring and triggering workloads
def workload_manager():
    scaler = AutoScaler()
    task_id = 1

    for cycle in range(5):
        logging.info(f"\n=== Cycle {cycle + 1} ===")
        load = random.randint(20, 100)  # simulate % utilization
        logging.info(f"Simulated load: {load}%")
        scaler.evaluate_scale(load)

        threads = []
        for i in range(scaler.current_nodes):
            t = threading.Thread(target=hpc_workload, args=(task_id,))
            threads.append(t)
            t.start()
            task_id += 1

        for t in threads:
            t.join()

        time.sleep(2)

# Entry point
if __name__ == "__main__":
    logging.info("Starting HPC Cloud Resource Optimization Simulation...")
    workload_manager()
    logging.info("Simulation completed.")
