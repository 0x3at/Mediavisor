import random


def simulate_server_latency():
    server_load = random.randint(0, 100)
    server_bandwidth = random.randint(500, 2000)

    congestion_factor = random.uniform(0.8, 1.2)
    load_factor = 1 + (server_load / 100)
    bandwidth_factor = 1 - (server_bandwidth / 10000)

    latency = congestion_factor * load_factor * bandwidth_factor
    latency += random.uniform(-5, 5)

    return latency
