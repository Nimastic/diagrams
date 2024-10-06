import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 8))

# Draw blocks for each layer
ax.text(0.5, 0.95, "User Programs", ha="center", va="center",
        bbox=dict(boxstyle="round,pad=1", facecolor="lightgreen"), fontsize=12)

ax.text(0.2, 0.75, "Device Driver", ha="center", va="center",
        bbox=dict(boxstyle="round,pad=1", facecolor="orange"), fontsize=10)
ax.text(0.5, 0.75, "Process Management", ha="center", va="center",
        bbox=dict(boxstyle="round,pad=1", facecolor="orange"), fontsize=10)
ax.text(0.8, 0.75, "Memory Management", ha="center", va="center",
        bbox=dict(boxstyle="round,pad=1", facecolor="orange"), fontsize=10)
ax.text(0.5, 0.6, "File System", ha="center", va="center",
        bbox=dict(boxstyle="round,pad=1", facecolor="orange"), fontsize=10)

ax.text(0.25, 0.45, "IPC", ha="center", va="center",
        bbox=dict(boxstyle="round,pad=1", facecolor="lightskyblue"), fontsize=10)
ax.text(0.5, 0.45, "Scheduling", ha="center", va="center",
        bbox=dict(boxstyle="round,pad=1", facecolor="lightskyblue"), fontsize=10)
ax.text(0.75, 0.45, "Interrupt Handler", ha="center", va="center",
        bbox=dict(boxstyle="round,pad=1", facecolor="lightskyblue"), fontsize=10)
ax.text(0.5, 0.35, "...", ha="center", va="center",
        bbox=dict(boxstyle="round,pad=1", facecolor="lightskyblue"), fontsize=10)

ax.text(0.5, 0.15, "Hardware", ha="center", va="center",
        bbox=dict(boxstyle="round,pad=1", facecolor="lightcoral"), fontsize=12)

# Draw arrows to represent interactions
arrowprops = dict(facecolor='black', arrowstyle='->', lw=1.5)

ax.annotate("", xy=(0.5, 0.9), xytext=(0.2, 0.8), arrowprops=arrowprops)
ax.annotate("", xy=(0.5, 0.9), xytext=(0.5, 0.8), arrowprops=arrowprops)
ax.annotate("", xy=(0.5, 0.9), xytext=(0.8, 0.8), arrowprops=arrowprops)
ax.annotate("", xy=(0.5, 0.7), xytext=(0.5, 0.6), arrowprops=arrowprops)

ax.annotate("", xy=(0.2, 0.7), xytext=(0.25, 0.5), arrowprops=arrowprops)
ax.annotate("", xy=(0.5, 0.7), xytext=(0.5, 0.5), arrowprops=arrowprops)
ax.annotate("", xy=(0.8, 0.7), xytext=(0.75, 0.5), arrowprops=arrowprops)
ax.annotate("", xy=(0.5, 0.55), xytext=(0.5, 0.4), arrowprops=arrowprops)

ax.annotate("", xy=(0.25, 0.4), xytext=(0.5, 0.2), arrowprops=arrowprops)
ax.annotate("", xy=(0.5, 0.4), xytext=(0.5, 0.2), arrowprops=arrowprops)
ax.annotate("", xy=(0.75, 0.4), xytext=(0.5, 0.2), arrowprops=arrowprops)
ax.annotate("", xy=(0.5, 0.3), xytext=(0.5, 0.2), arrowprops=arrowprops)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

plt.show()
