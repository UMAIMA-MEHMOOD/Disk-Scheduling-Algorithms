def look_scheduling(requests, head_start, direction):
    # Sort the requests
    requests = sorted(requests)
    seek_sequence = []
    total_seek_time = 0
    head = head_start

    if direction == "left":
        # Split requests into 'left' and 'right' based on the initial head position
        left = [r for r in requests if r <= head]  # Requests to the left of the head
        right = [r for r in requests if r > head]  # Requests to the right of the head

        # Process 'left' requests in reverse order
        prev = head
        for r in reversed(left):
            seek_sequence.append((prev, r))
            total_seek_time += abs(prev - r)
            prev = r

        # Process 'right' requests
        if right:
            for r in right:
                seek_sequence.append((prev, r))
                total_seek_time += abs(prev - r)
                prev = r

    else:  # direction == "right"
        # Split requests into 'left' and 'right' based on the initial head position
        left = [r for r in requests if r < head]  # Requests to the left of the head
        right = [r for r in requests if r >= head]  # Requests to the right of the head

        # Process 'right' requests
        prev = head
        for r in right:
            seek_sequence.append((prev, r))
            total_seek_time += abs(prev - r)
            prev = r

        # Process 'left' requests in reverse order
        if left:
            for r in reversed(left):
                seek_sequence.append((prev, r))
                total_seek_time += abs(prev - r)
                prev = r

    # Return the seek sequence and total seek time
    return seek_sequence, total_seek_time