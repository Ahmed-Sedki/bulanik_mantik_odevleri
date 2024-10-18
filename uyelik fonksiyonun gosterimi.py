import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 10, 0.1)
y = np.array([])
z = []

for i, tutx in enumerate(x):
    # Use ** for exponentiation
    z.insert(i, (1 / (1 + (tutx - 30) ** 5)))
    y = np.append(y, (1 / (1 + (tutx - 30) ** 5)))

plt.plot(x, z)

cevap = 'e'
while cevap == 'e' or cevap == 'E':
    userx = float(input("1-10 arası değer girin: "))
    mx = (1 / (1 + (userx - 30) ** 5))
    print("Üyelik Derecesi:", mx)
    cevap = input("Devam edecek misiniz (E/e)? ")
