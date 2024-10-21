import numpy as np
import matplotlib.pyplot as plt

def pi_membership_function(u, a, b, c, d):
    if u < a or u > d:
        return 0
    elif a <= u < b:
        return 2 * ((u - a) / (d - a)) ** 2
    elif b <= u <= c:
        return 1 - 2 * ((u - c) / (d - a)) ** 2
    elif c < u <= d:
        return 2 * ((d - u) / (d - a)) ** 2

def plot_pi_membership(a, b, c, d, u):
    # Define u values for plotting the membership function
    u_values = np.linspace(a - 1, d + 1, 1000)
    membership_values = [pi_membership_function(value, a, b, c, d) for value in u_values]

    # Plot the pi membership function
    plt.plot(u_values, membership_values, label='Membership Function')
    plt.xlabel('u')
    plt.ylabel('$\mu_A(u)$')
    plt.title('Pi Uyelik Fonksiyonu (Pi Membership Function)')

    # Plot the user-defined value and its membership value
    mu_u = pi_membership_function(u, a, b, c, d)
    plt.scatter([u], [mu_u], color='red', zorder=5)
    plt.text(u, mu_u, f'({u}, {mu_u:.2f})', fontsize=10, verticalalignment='bottom')

    plt.legend()
    plt.grid(True)
    plt.show()

a, b, c, d = 1, 30, 70, 100
u = float(input('Enter value for u (between 1 and 100): '))

plot_pi_membership(a, b, c, d, u)
