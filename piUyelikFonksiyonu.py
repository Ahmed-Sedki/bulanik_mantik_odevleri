import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 100, 1)
b_genislik = 40
c_orta_nokta = 50

def omuz_ciz_sol(a, b, c):
    z = []
    for u in x:
        if u <= c:
            if u < a:
                z.append(0)
            elif a <= u <= b:
                z.append(2 * (pow(((u - a) / (c - a)), 2)))
            elif b < u <= c:
                z.append(1 - 2 * (pow(((u - c) / (c - a)), 2)))
            else:
                z.append(1)
        else:
            z.append(1)
    return z

def omuz_ciz_sag(a, b, c):
    z = []
    for u in x:
        if u >= a:
            if u < a:
                z.append(1)
            elif a <= u <= b:
                z.append(1 - (2 * (pow(((u - a) / (c - a)), 2))))
            elif b < u <= c:
                z.append(1 - (1 - 2 * (pow(((u - c) / (c - a)), 2))))
            else:
                z.append(0)
        else:
            z.append(0)
    return z

a = c_orta_nokta - b_genislik
b = c_orta_nokta - b_genislik / 2
c = c_orta_nokta
z_sol = omuz_ciz_sol(a, b, c)
plt.plot(x, z_sol, label='Left Shoulder')

a = c_orta_nokta
b = c_orta_nokta + b_genislik / 2
c = c_orta_nokta + b_genislik
z_sag = omuz_ciz_sag(a, b, c)
plt.plot(x, z_sag, label='Right Shoulder')

plt.xlabel('x')
plt.ylabel('Membership value')
plt.title('Fuzzy Membership Function')
plt.legend()
plt.grid(True)
plt.show()
