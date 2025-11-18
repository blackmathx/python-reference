import pandas as pd
import numpy as np
import matplotlib

matplotlib.use("Agg") # Headless backend and save to files

import matplotlib.pyplot as plt


print("\nRandom  Numbers\n")
a = np.random.random()
b = np.random.random(2) # random array  of len 2
c = np.random.randint(0, 11, 3) # 3 random numbers in [1, 10]
d = np.random.seed(99) # setting a seed will produce the same output

print(a, b, c)



# Read the CSV file
df = pd.read_csv('data.csv')

# Print info
print(f"Rows: {len(df)}")
print(f"Columns: {list(df.columns)}")
print("\nFirst 5 rows:")
print(df.head())




# f(x) = x²
x = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
y = [16, 9, 4, 1, 0, 1, 4, 9, 16]


plt.figure(figsize=(6, 4))
plt.plot(x, y, linewidth=2)
plt.title("f(x) = x²")
plt.xlabel("x")
plt.ylabel("x²")

# Save as out.png
plt.savefig("out.png")
