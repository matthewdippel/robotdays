__author__ = 'mdippel'

def greedy_task_insert(segmented_schedule, tasks):
    from collections import defaultdict
    has_been_inserted = defaultdict(lambda: False)
    for i in range(segmented_schedule.length):
        if segmented_schedule.task_at_ith_slot(i) is not None:
            continue
    for task in tasks:
        if has_been_inserted[task]:
            continue

    return
