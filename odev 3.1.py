import numpy as np
import matplotlib.pyplot as plt

def triangular_membership_function(u, a, b, c):
    if u < a or u > c:
        return 0
    elif a <= u <= b:
        return (u - a) / (b - a)
    elif b < u <= c:
        return (c - u) / (c - b)

def plot_triangular_membership(a, b, c, u):
    # Define u values for plotting the membership function
    u_values = np.linspace(a - 1, c + 1, 1000)
    membership_values = [triangular_membership_function(value, a, b, c) for value in u_values]

    # Plot the triangular membership function
    plt.plot(u_values, membership_values, label='Membership Function')
    plt.xlabel('u')
    plt.ylabel('$\mu_A(u)$')
    plt.title('Ucgen Uyelik Fonksiyonu (Triangular Membership Function)')

    # Plot the user-defined value and its membership value
    mu_u = triangular_membership_function(u, a, b, c)
    plt.scatter([u], [mu_u], color='red', zorder=5)
    plt.text(u, mu_u, f'({u}, {mu_u:.2f})', fontsize=10, verticalalignment='bottom')

    plt.legend()
    plt.grid(True)
    plt.show()

a, b, c = 1, 50, 100
u = float(input('Enter value for u (between 1 and 100): '))

plot_triangular_membership(a, b, c, u)
