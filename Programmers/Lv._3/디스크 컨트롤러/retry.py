from heapq import heappop, heappush

def solution(jobs):
    jobs.sort()
    j_len = len(jobs)
    queue = []

    total_time = 0
    current_time = 0
    job_idx = 0
    complete_cnt = 0
    while complete_cnt < j_len:

        while job_idx < j_len and jobs[job_idx][0] <= current_time:
            heappush(queue, (jobs[job_idx][1], jobs[job_idx][0]))
            job_idx += 1

        if queue:
            times, start_time = heappop(queue)
            current_time += times
            total_time += current_time - start_time
            complete_cnt += 1
        else:
            current_time = jobs[job_idx][0]

    return total_time // j_len