import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Define the universe of discourse
U = np.arange(-500, 500.1, 0.1)  # Include 500

# Define membership functions
def cok_yakin(mesafe):
    if mesafe < 0:
        return 0
    elif 0 <= mesafe <= 100:
        return 1 - (mesafe / 100)
    else:
        return 0

def yakin(mesafe):
    if mesafe < 0:
        return 0
    elif 50 <= mesafe <= 150:
        return (mesafe - 50) / 100
    elif 150 < mesafe <= 250:
        return 1 - (mesafe - 150) / 100
    else:
        return 0

def ortada(mesafe):
    if mesafe < 0:
        return 0
    elif 200 <= mesafe <= 300:
        return (mesafe - 200) / 100
    elif 300 < mesafe <= 400:
        return 1 - (mesafe - 300) / 100
    else:
        return 0

def uzak(mesafe):
    if mesafe < 0:
        return 0
    elif 350 <= mesafe <= 450:
        return (mesafe - 350) / 100
    elif 450 < mesafe <= 500:
        return 1 - (mesafe - 450) / 50
    else:
        return 0

def cok_uzak(mesafe):
    if mesafe < 500:
        return 0
    else:
        return 1

# Vectorize the membership functions for plotting
cok_yakin_values = np.array([cok_yakin(x) for x in U])
yakin_values = np.array([yakin(x) for x in U])
ortada_values = np.array([ortada(x) for x in U])
uzak_values = np.array([uzak(x) for x in U])
cok_uzak_values = np.array([cok_uzak(x) for x in U])

# Set up the Tkinter window
root = tk.Tk()
root.title("Fuzzy Set YAKIN Membership Function")

# Create a matplotlib figure
fig, ax = plt.subplots(figsize=(10,6))

# Plot the membership functions
ax.axhline(y=0, color='black', linestyle='--')  # x-axis
ax.axvline(x=0, color='black', linestyle='--')  # y-axis
line1, = ax.plot(U, cok_yakin_values, label='Çok Yakın', color='blue')
line2, = ax.plot(U, yakin_values, label='Yakın', color='green')
line3, = ax.plot(U, ortada_values, label='Ortada', color='orange')
line4, = ax.plot(U, uzak_values, label='Uzak', color='red')
line5, = ax.plot(U, cok_uzak_values, label='Çok Uzak', color='purple')

# Set labels and limits
ax.set_xlabel('Mesafe')
ax.set_ylabel('YAKIN')
ax.set_xlim(-500, 500)
ax.set_ylim(-0.1, 1.1)
ax.set_xticks(np.arange(-500, 501, 100))
ax.set_title('Fuzzy Set YAKIN Membership Function')
ax.grid(True)
ax.legend()

# Embed the plot in Tkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Create a frame for input and button
input_frame = tk.Frame(root)
input_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

# Label and Entry for 'mesafe'
label = tk.Label(input_frame, text="Mesafe Değeri:")
label.pack(side=tk.LEFT, padx=5)

mesafe_var = tk.StringVar()
entry = tk.Entry(input_frame, textvariable=mesafe_var)
entry.pack(side=tk.LEFT, padx=5)

# Lists to keep track of plotted points and texts
plotted_points = []
plotted_texts = []

# Function to plot the point based on user input
def plot_point():
    # Clear previous annotations or points
    for point in plotted_points:
        point.remove()
    plotted_points.clear()
    for text in plotted_texts:
        text.remove()
    plotted_texts.clear()

    try:
        mesafe = float(mesafe_var.get())
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli bir sayısal değer girin.")
        return

    # Compute membership values
    memberships = {
        'Çok Yakın': cok_yakin(mesafe),
        'Yakın': yakin(mesafe),
        'Ortada': ortada(mesafe),
        'Uzak': uzak(mesafe),
        'Çok Uzak': cok_uzak(mesafe)
    }

    # Colors corresponding to each set
    colors = {
        'Çok Yakın': 'blue',
        'Yakın': 'green',
        'Ortada': 'orange',
        'Uzak': 'red',
        'Çok Uzak': 'purple'
    }

    any_membership_positive = False

    # Plot points for each membership >= 0
    for key, value in memberships.items():
        if value > 0:
            any_membership_positive = True
            point, = ax.plot(mesafe, value, marker='o', color=colors[key], markersize=8)
            plotted_points.append(point)
            # Add text annotation slightly above the point
            text = ax.text(mesafe, value + 0.05, f"{key}: {value:.2f}", color=colors[key],
                           ha='center', va='bottom', fontsize=9, fontweight='bold')
            plotted_texts.append(text)

    if not any_membership_positive:
        # mesafe has 0 membership in all sets
        # Plot a point at y=0 and show annotation
        point, = ax.plot(mesafe, 0, marker='o', color='black', markersize=8)
        plotted_points.append(point)
        text = ax.text(mesafe, 0.05, f"Üyelik Değeri: 0", color='black',
                       ha='center', va='bottom', fontsize=9, fontweight='bold')
        plotted_texts.append(text)

    # Refresh the canvas
    canvas.draw()

# Button to trigger plotting
button = tk.Button(input_frame, text="Çiz", command=plot_point)
button.pack(side=tk.LEFT, padx=5)

# Start the Tkinter event loop
root.mainloop()
