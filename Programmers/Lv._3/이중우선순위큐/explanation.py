def solution(operations):
    queue_list = []

    for task in operations:
        if task == "D -1":
            if queue_list:
                queue_list.remove(min(queue_list))
        elif task == "D 1":
            if queue_list:
                queue_list.remove(max(queue_list))
        else:
            queue_list.append(int(task.split()[-1]))

    return [max(queue_list), min(queue_list)] if queue_list else [0, 0]