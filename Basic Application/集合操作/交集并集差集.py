# 求两个列表的交集、并集和差集，不考虑两个列表中元素值的重复
 
def diff(listA,listB):
    #求交集的两种方式
    retA = [i for i in listA if i in listB]
    retB = list(set(listA).intersection(set(listB)))
    ret_B = list(set(listA) & set(listB))
    print(retA)
    print(retB)
    print(ret_B)
    
    #求并集
    retC = list(set(listA).union(set(listB)))
    ret_C = list(set(listA) | set(listB))
    print(retC)
    print(ret_C)
    
    #求差集，在B中但不在A中
    retD = list(set(listB).difference(set(listA)))
    ret_D = list(set(listB) - set(listA))
    print(retD)
    print(ret_D)
    
    retE = [i for i in listB if i not in listA]
    print(retE)
    
def main():
    listA = [1,2,3,4,5]
    listB = [3,4,5,6,7]
    diff(listA,listB)
    
if __name__ == '__main__':
    main()
