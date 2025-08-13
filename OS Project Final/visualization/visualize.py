import matplotlib.pyplot as plt

# Function to visualize Gantt chart
def visualize_gantt_chart(processes, ax, algo_name, color):
    start_times = [p['arrival_time'] for p in processes]
    end_times = [p['completion_time'] for p in processes]
    process_ids = [f"P{p['process_id']}" for p in processes]

    # Plot the Gantt chart with specified color
    ax.barh(
        process_ids, 
        [end - start for start, end in zip(start_times, end_times)],  #bar length
        left=start_times, #starting position of bar
        color=color
    )
    ax.set_xlabel("Time", fontsize=12)
    ax.set_ylabel("Processes", fontsize=12)
    ax.set_title(algo_name, fontsize=14, fontweight="bold")

    # Annotate the start and end times 
    # adding labels on plot
    for i, p in enumerate(processes):
        ax.text(
            p['arrival_time'], i, f"{p['arrival_time']}", 
            va='center', ha='right', fontsize=10, color="black", 
            bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3')
        )
        ax.text(
            p['completion_time'], i, f"{p['completion_time']}", 
            va='center', ha='left', fontsize=10, color="black", 
            bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3')
        )

# Function to visualize seek sequences
def visualize_seek_sequence(seek_sequence, algo_name, ax, color):
    # Prepare x-axis (track requests)
    x_vals = [x[1] for x in seek_sequence] # keeping only to-tracks
    y_vals = list(range(1, len(seek_sequence) + 1))  # Order of requests or nubering the tasks requested
    
    # Plot the updated graph
    ax.plot(x_vals, y_vals, marker="o", color=color, linestyle="-")
    ax.set_title(algo_name, fontsize=14, fontweight="bold")
    ax.set_xlabel("Track Requests (0-199)", fontsize=12)
    ax.set_ylabel("Order of Requests", fontsize=12)
    ax.set_xlim(0, 199)  # Ensures the x-axis is limited to the valid range
    
    # Annotate seek movements
    for idx, (curr, next_) in enumerate(seek_sequence):
        ax.annotate( # helps to put little text labels on graph
            f"{curr}-{next_}", #(37-24) created    
            (next_, idx + 1),  # Annotating on next request's position
            textcoords="offset points", 
            xytext=(10, 10), 
            ha="center", 
            fontsize=10,
            bbox=dict(facecolor="white", edgecolor="black", boxstyle="round,pad=0.3")
        )
