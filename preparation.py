import math
import sys
def Com(A, n=2):# 所有可能下标组合
    temp = []
    for i in range(0, len(A)):
        for j in range(i+1, len(A)):
            temp.append(i)
            temp.append(j)
    return temp

def DualPos(A, c): # 用字典写case，反而会更慢。还不如这种笨方法
    x = A[0]
    y = A[1]
    if c==1:
        return x+y
    elif c==2:
        return x*y
    elif c==3:
        return x/y
    elif c==4:
        return y/x
    elif c==5:
        return x-y
    elif c==6:
        return y-x
    
def divisionbyzero(A, c):
    x = A[0]
    y = A[1]
    if c==3 and near(y,0):
        return 1
    elif c==4 and near(x,0):
        return 1
    else:
        return 0
def showanswer(L1,a1,L2,a2,L3,a3):    
    f1 = showoperator(a1)
    f2 = showoperator(a2)
    f3 = showoperator(a3)
    print(str(L1)+f1+" "+str(L2)+f2+" "+str(L3)+f3)
    
def showanswer5(L1,a1,L2,a2,L3,a3,L4,a4):    
    f1 = showoperator(a1)
    f2 = showoperator(a2)
    f3 = showoperator(a3)
    f4 = showoperator(a4)
    print(str(L1[0])+f1+str(L1[1])+" "+str(L2[0])+f2+str(L2[1])+" "+str(L3[0])+f3+str(L3[1])+" "+str(L4[0])+f4+str(L4[1]))
    
def showoperator(c):
    if c==1:
        return str("+")
    elif c==2:
        return str("*")
    elif c==3:
        return str("/")
    elif c==4:
        return str("/")
    elif c==5:
        return str("-")
    elif c==6:
        return str("-")
    
def near(x, y):
    return approx_eq(x,y)

def approx_eq(x, y, tolerance=1e-8):
    return abs(x - y) < tolerance

Com1 = Com([1,1,1,1,1]) # 下标组合提前算出来，能省10%左右时间
Com2 = Com([1,1,1,1])
Com3 = Com([1,1,1])
Com4 = Com([1,1])

def Solve5(A, obj = 120, print_answer=False): # 这函数虽然丑陋，但是性能不算慢
    flag = 1
    #Com1 = Com(A)
    n = len(A)
    
    for i in range(0, math.comb(n,2)):
        NumCom1 = [A[Com1[2*i]], A[Com1[2*i+1]]]
        B1 = A[:]
        del B1[Com1[2*i]]
        del B1[Com1[2*i+1]-1]  # B1为A中剩下的元素      
        for c1 in range(1,7):
            if divisionbyzero(NumCom1, c1):
                continue
            else:
                if c1!=1:
                    del B1[-1]
                B1.append(DualPos(NumCom1, c1))
                #Com2 = Com(B1)

                for j in range(0, math.comb(n-1,2)):
                    NumCom2 = [B1[Com2[2*j]], B1[Com2[2*j+1]]]
                    B2 = B1[:]
                    del B2[Com2[2*j]]
                    del B2[Com2[2*j+1]-1] # B2为B1中剩下的元素  
                    for c2 in range(1,7):
                        if divisionbyzero(NumCom2, c2):
                            continue
                        else:
                            if c2!=1:
                                del B2[-1]
                            B2.append(DualPos(NumCom2, c2))
                            #Com3 = Com(B2)

                            for k1 in range(0, math.comb(n-2,2)):
                                NumCom3 = [B2[Com3[2*k1]], B2[Com3[2*k1+1]]]
                                B3 = B2[:]
                                del B3[Com3[2*k1]]
                                del B3[Com3[2*k1+1]-1] # B2为B1中剩下的元素  
                                for c3 in range(1,7):
                                    if divisionbyzero(NumCom3, c3):
                                        continue
                                    else:
                                        if c3!=1:
                                            del B3[-1]
                                        B3.append(DualPos(NumCom3, c3))
                                        #Com4 = Com(B3)
                                            
                                        for k2 in range(0, math.comb(n-3,2)):
                                            NumCom4 = [B3[Com4[2*k2]], B3[Com4[2*k2+1]]]  
                                            for c4 in range(1,7):
                                                if divisionbyzero(NumCom4, c4):
                                                    continue
                                                else:
                                                    if near(DualPos(NumCom4, c4) % obj, 0):
                                                        if print_answer:
                                                            print("number combination: "+str(A)+"\ncalculation step: ")
                                                            showanswer5(NumCom1,c1,NumCom2,c2,NumCom3,c3,NumCom4,c4)
                                                            print("successful answer: ", DualPos(NumCom4, c4), "\n")
                                                        
                                                        return 1

    print(":)") # 此时失败，说明找到了不能凑出120的一组数
    print(A) # 将它们打印出来
    sys.exit()