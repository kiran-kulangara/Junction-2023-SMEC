import matplotlib.pyplot as plt
import json

# data = CONFIDENTIAL_SAMPLE_DATA
# file_path = 'Data/walking/AFE_000_CONFIDENTIAL.json'

# Extracting and plotting data
left_eye = [sample['afe'][0]['m'][0] for sample in data if sample['afe'][0]]
right_eye = [sample['afe'][1]['m'][0] for sample in data if sample['afe'][1]]

# Plotting
fig, axes = plt.subplots(2, 1, figsize=(12, 8))
fig.suptitle('Eye Sensor Data')

# Left Eye Data
for i in range(6):  # Plotting first six sensors
    axes[0].plot([sample[i] for sample in left_eye], label=f'Sensor {i+1}')
axes[0].set_title('Left Eye')
axes[0].set_xlabel('Sample Index')
axes[0].set_ylabel('Sensor Value')
axes[0].legend()
axes[0].grid(True)

# Right Eye Data
for i in range(6):  # Plotting first six sensors
    axes[1].plot([sample[i] for sample in right_eye], label=f'Sensor {i+1}', color='green')
axes[1].set_title('Right Eye')
axes[1].set_xlabel('Sample Index')
axes[1].set_ylabel('Sensor Value')
axes[1].legend()
axes[1].grid(True)

plt.tight_layout()
plt.show()


