# python3

def parallel_processing(n, m, data):
    output = []
    th=[0]*n
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    for i in range(m):
        minth=min(th)
        print(th.index(minth))
        print(th[th.index(minth)])
        th[th.index(minth)]= th[th.index(minth)]+data[i]

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
    for i,k in result:
        print(i, k)
if __name__ == "__main__":
    main()
