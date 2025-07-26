import matplotlib.pyplot as plt

# Data from the 4 frames
packet_sizes = [1480, 2960, 4440, 5008]  # Accumulated payload sizes
fragment_counts = [1, 2, 3, 4]  # Corresponding fragment counts

# Plotting the graph
plt.figure(figsize=(8, 6))
plt.step(packet_sizes, fragment_counts, where='post', color='blue', linewidth=2)
plt.title("Количество фрагментов в зависимости от размера пакета", fontsize=14)
plt.xlabel("Размер пакета (байты)", fontsize=12)
plt.ylabel("Количество фрагментов", fontsize=12)
plt.grid(True)
plt.tight_layout()

# Save the plot to a file
plt.savefig("fragment_count_vs_packet_size_new.png")
plt.show()
