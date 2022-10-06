import copy


def update_queue(queue, n, max_processindex):
    beg_process = n-1
    for i in range(n):
        # print("update")
        if queue[i] == 0:
            beg_process = i
            break

    queue[beg_process] = max_processindex + 1


def organize_queue(queue, n):
    i = 0

    while i < n-1 and queue[i+1] != 0:
        # print("organize")
        temp = queue[i]
        queue[i] = queue[i+1]
        queue[i+1] = temp

        i += 1


def process_arrival_check(queue, curr_time, arrival_time, n, max_processindex):
    if curr_time <= arrival_time[n-1]:
        isArrived = False

        for j in range((max_processindex+1), n):
            # print("check")
            if arrival_time[j] <= curr_time:
                if max_processindex < j:
                    max_processindex = j
                    isArrived = True

        if isArrived:
            update_queue(queue, n, max_processindex)


def display(n, arrival_time, burst_time, waiting_time, turn_around_time, exit_time):
    avg_wait_time = 0
    avg_turn_around_time = 0
    print()
    print("Process ID \t Arrival Time \t Burst Time \t Waiting Time \t Turn-Around Time")
    for i in range(n):
        print(
            f"\tP{i+1}\t\t{arrival_time[i]}\t\t{burst_time[i]}\t\t{waiting_time[i]}\t\t{turn_around_time[i]}")

        avg_wait_time += waiting_time[i]
        avg_turn_around_time += turn_around_time[i]

    print()
    print("Average Waiting Time :: ", avg_wait_time/n)
    print("Average Turn-Around Time :: ", avg_turn_around_time/n)


def main():
    curr_time = 0
    max_processindex = 0

    quantum = int(input("Enter the Quantum value :: "))
    n = int(input("Enter the number of processes :: "))

    waiting_time = [0 for _ in range(n)]
    turn_around_time = [0 for _ in range(n)]
    burst_time = []
    arrival_time = []
    isComplete = [False for _ in range(n)]

    for i in range(n):
        arrival_time.append(
            int(input(f"Enter the arrival time for process P{i+1} :: ")))
        burst_time.append(
            int(input(f"Enter the burst time for process P{i+1} :: ")))

    temp_burst_time = copy.deepcopy(burst_time)

    queue = [0 for _ in range(n)]

    while curr_time < arrival_time[0]:
        curr_time += 1
    
    if arrival_time[-1]==0:
        for i in range (n):
            queue[i]=i+1
    else:
        queue[0] = 1

    while True:
        flag = True

        for i in range(n):
            if temp_burst_time[i] != 0:
                flag = False
                break

        if flag:
            break

        i = 0
        while i < n and queue[i] != 0:
            ctr = 0

            while ctr < quantum and temp_burst_time[queue[0]-1] > 0:
                # print("hello")
                temp_burst_time[queue[0]-1] -= 1
                curr_time += 1
                ctr += 1

                process_arrival_check(
                    queue, curr_time, arrival_time, n, max_processindex)

            if temp_burst_time[queue[0]-1] == 0 and isComplete[queue[0]-1] == False:
                turn_around_time[queue[0]-1] = curr_time
                isComplete[queue[0]-1] = True

            idle = True
            if queue[n-1] == 0:
                j = 0
                while j < n and queue[j] != 0:
                    if isComplete[queue[j]-1] == False:
                        idle = False
                    j += 1
            else:
                idle = False

            if idle:
                curr_time += 1
                process_arrival_check(
                    queue, curr_time, arrival_time, n, max_processindex)

            organize_queue(queue, n)

            i += 1

    exit_time = copy.deepcopy(turn_around_time)
    for i in range(n):
        turn_around_time[i] = turn_around_time[i] - arrival_time[i]
        waiting_time[i] = turn_around_time[i] - burst_time[i]

    display(n, arrival_time, burst_time,
            waiting_time, turn_around_time, exit_time)


if __name__ == "__main__":
    main()
