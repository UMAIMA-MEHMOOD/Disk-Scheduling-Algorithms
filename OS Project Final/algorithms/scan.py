def scan_scheduling(requests, head_start, disk_size, direction):
    requests = sorted(requests)
    seek_sequence = []
    total_seek_time = 0
    head = head_start

    if direction == "left":
        left = [r for r in requests if r <= head]  # Requests to the left of the head
        right = [r for r in requests if r > head]  # Requests to the right of the head

        # Process 'left' requests in reverse order
        prev = head
        for r in reversed(left):
            seek_sequence.append((prev, r))
            total_seek_time += abs(prev - r)
            prev = r

        # Move to the start of the disk if there are right requests
        if right:
            seek_sequence.append((prev, 0))  # Move to track 0
            total_seek_time += abs(prev - 0)
            prev = 0

        # Process 'right' requests
        for r in right:
            seek_sequence.append((prev, r))
            total_seek_time += abs(prev - r)
            prev = r

    else:  # direction == "right"
        # Step 2: Split requests into 'left' and 'right' based on the initial head position
        left = [r for r in requests if r < head]  # Requests to the left of the head
        right = [r for r in requests if r >= head]  # Requests to the right of the head

        #  Process 'right' requests
        prev = head
        for r in right:
            seek_sequence.append((prev, r))
            total_seek_time += abs(prev - r)
            prev = r

        # Move to the end of the disk if there are left requests
        if left:
            seek_sequence.append((prev, disk_size - 1))  # Move to the end of the disk
            total_seek_time += abs(prev - (disk_size - 1))
            prev = disk_size - 1

        #  Process 'left' requests in reverse order
        for r in reversed(left):
            seek_sequence.append((prev, r))
            total_seek_time += abs(prev - r)
            prev = r

    return seek_sequence, total_seek_time
