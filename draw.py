import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import pandas as pd
import matplotlib.pyplot as plt

pod_data = pd.read_csv('train/metric-pod-front-end-d75fdb4bc-8vl6n.csv', parse_dates=['timestamp'], date_parser=lambda x: pd.to_datetime(x, format="%d/%m/%Y %H:%M:%S"))

plt.subplot(3, 1, 1)

plt.plot(pod_data['timestamp'], pod_data['container_memory_usage_bytes'])
plt.title('Memory Usage Bytes')

plt.subplot(3, 1, 2)
plt.plot(pod_data['timestamp'], pod_data['container_network_transmit_bytes_total'])
plt.title('Network Transmit Bytes')

plt.subplot(3, 1, 3)
plt.plot(pod_data["timestamp"], pod_data['container_cpu_usage_seconds_total'])
plt.title('CPU Usage Seconds')
plt.tight_layout()
plt.show()
