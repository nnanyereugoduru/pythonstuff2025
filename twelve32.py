import numpy as np

scores = np.array([85, 92, 78.9, 99, 88, 80.6, 91, 83])

print(f"Mean:    {np.mean(scores):.2f}")
print(f"Median:  {np.median(scores):.2f}")
print(f"Std Dev: {np.std(scores):.2f}")
print(f"Max:     {np.max(scores):.2f}")
print(f"Min:     {np.min(scores):.2f}")
print(f"Above 85: {scores[scores > 85]}")