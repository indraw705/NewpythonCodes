from multiprocessing import Pool
import os
def get_sqaure(num):
    print("Worker process id for {0}: {1}".format(num, os.getpid()))
    return (num*num)

if __name__=='__main__':
    arr= [1,2,3,4,5]
    # res = []

    p = Pool()

    result = p.map(get_sqaure, arr)
    print("sqare of each element")
    print(result)
