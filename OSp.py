gant_time=0
quantum=0
pid=[]
arrival_time=[]
burst_time=[]
queue=[]
gant=[]
exit_times=[]
def input_data(n):
    i=0
    for i in range(n):
        a=int(input(f"Enter Arrival time of P{i+1}: "))
        b=int(input(f"Enter Burst time of P{i+1}: "))
        arrival_time.append(a)
        burst_time.append(b)

def make_gant():
    temp_min_index=min(arrival_time.index)
    if not gant:
        gant[0]=pid[temp_min_index]


# def display(n):
#     for i in range(n):
#         print(*data[i])


def main():
    global quantum
    quantum=int(input("Enter time quantum: "))
    input_data(2)
    display(2)

if __name__=="__main__":
    main()

