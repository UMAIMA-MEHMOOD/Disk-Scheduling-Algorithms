def sstf_scheduling(requests, head_start):
    requests = sorted(requests)
    head = head_start
    seek_sequence = []
    total_seek_time = 0
    while requests:
        closest_request = min(requests, key=lambda x: abs(x - head))
        seek_sequence.append((head, closest_request))
        total_seek_time += abs(head - closest_request)
        head = closest_request
        requests.remove(closest_request)
    return seek_sequence, total_seek_time

