from heapq import heappush, heappop
def solution(jobs):
    jobs.sort()
    current_time = total_time = complete_job = index = 0
    job_len, heap = len(jobs), []

    while complete_job < job_len:
        while index < job_len and jobs[index][0] <= current_time:
            start, duration = jobs[index]
            heappush(heap, (duration, start))
            index += 1

        if heap:
            duration, start = heappop(heap)
            current_time += duration
            total_time += current_time - start
            complete_job += 1
        else:
            if jobs:
                current_time = jobs[index][0]
    return total_time // job_len