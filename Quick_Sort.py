def QuickSort(li):
    QS_Re(li, 0, len(li))
    return li

def QS_Re(li, i, f):
    if i < f:
        m = QS_Partition(li, i, f)
        QS_Re(li, i, m)
        QS_Re(li, m + 1, f)
    return

def QS_Partition(li, i, f):
    m = (i + f)//2
    li[m], li[f - 1] = li[f - 1], li[m]
    '''take the middle point as the split point can avoid the sorted list hit the worst case of quick sort'''
    
    mid_num = li[f - 1]
    #li[i] is the next number larger than li[f - 1]
    for j in xrange(i, f - 1):
        if li[j] < mid_num:
            li[j], li[i] = li[i], li[j]
            i += 1
    li[i], li[f - 1] = li[f - 1], li[i]
    return i
