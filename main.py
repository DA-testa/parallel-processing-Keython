# python3

def parallel_processing(n, m, data):
    output = []
    th=[0]*n
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    for i in range(m):
        minth=min(th)
        ieksa=th.index(minth)
        output.append((minth,ieksa))
        th[ieksa]=th[ieksa]+data[i]
    return output
def main():
    n,m =map(int,input().split())
    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    #data = []
    data = list(map(int, input().split()))
    # TODO: create the function
    result = parallel_processing(n,m,data)
    # TODO: print out the results, each pair in it's own line

    for j,k in result:
        print(j, k)

if __name__ == "__main__":
    main()
