import heapq

def min_cost_to_connect_cables(lengths): #lenghts = lenghts of cables
    # Edge case: If there are no cables or only one cable, no cost is required.
    if len(lengths) <= 1:
        return 0

    # Create a min-heap from the list of cables
    heapq.heapify(lengths)

    total_cost = 0

    # Continue until we have only one cable left
    while len(lengths) > 1:
        # Extract the two shortest cables
        first = heapq.heappop(lengths)
        second = heapq.heappop(lengths)

        # Cost to connect these two cables
        cost = first + second

        # Accumulate the total cost
        total_cost += cost

        # Insert the resulting cable back into the heap
        heapq.heappush(lengths, cost)

    return total_cost

# Example usage
if __name__ == "__main__":
    lengths = [4, 3, 2, 5, 2]
    print(f"Min cost to connect all cables: {min_cost_to_connect_cables(lengths)}")


# Min cost = 36
# Conclusion
# Always connect the two shortest cables first, as this minimizes the incremental cost at each step.
