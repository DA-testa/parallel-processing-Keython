# python3

def parallel_processing(n, m, data):
    output = []
    th=[0]*n
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    for i in range(0,m):
        minth=min(th)
        ieksa=th[(th.index(min(th)))]
        output.append((ieksa,minth))
    return output
def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n = 0
    m = 0
    n,m =map(int,input().split())
    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = []
    # TODO: create the function
    result = parallel_processing(n,m,data)
    # TODO: print out the results, each pair in it's own line

    for j,k in result:
        print(j, k)

if __name__ == "__main__":
    main()
