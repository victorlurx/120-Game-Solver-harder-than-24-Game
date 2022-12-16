# make sure that using pypy to run this file! otherwise it will take forever to complete
from preparation import Solve5
import time
import itertools

if __name__ == '__main__':
    # 判断5个数是否一定能凑出120的倍数！
    filt = lambda x: x%5!=0
    m = 120
    start = time.time()    
    # 不写多重循环，经测试直接省了2.5倍时间

    num_list = [i for i in range(1, m) if filt(i)]
    for num in itertools.combinations(num_list, 5):
        Solve5(list(num), 120, True)                # you can change obj number and decide whether to print the answer

    end = time.time()
    print('it costs ' + str(end-start) + ' seconds to finish' + '. Current problem dimension: ' + str(m))