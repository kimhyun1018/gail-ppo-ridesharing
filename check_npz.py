import numpy as np

npz_file = '/home/hyun/AS_IL_GAIL_RL/data/expert_demonstration/session_9_30/merged_expert_data.npz'

# Load the .npz file
expert_data = np.load(npz_file)

# Print the keys in the file to verify
print("Keys in the .npz file:", expert_data.files)

# Optionally, print the shape of rewards to verify
if 'rewards' in expert_data.files:
    print("Rewards shape:", expert_data['rewards'].shape)
else:
    print("'rewards' key not found.")
