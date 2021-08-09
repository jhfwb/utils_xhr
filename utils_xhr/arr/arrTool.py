def getArrNoneNum(arr):
    """
    获得一个数组中None的个数
    """
    index=0
    for a in arr:
        if a==None:
            index=index+1
    return index
def removeRepeat(arr, keyFunction=""):
    """
    去除掉[]中相同的元素，根据方法keyFunction。
    e.g.:a=[{'name':1},{'name':3},{'name':2},{'name':1},{'name':1}]
    假设要去除name为1的元素
    c=removeRepeat(a,keyFunction=lambda x:x['name'])
    print(c) =>[{'name': 1}, {'name': 2}, {'name': 3}]

    @param:arr |[] 需要去重的数组
    @param:keyFunction |function 存放需要进行去重的函数
    """
    try:
        arr.sort(key=keyFunction)
    except:
        raise ValueError("keyFunction无法正常调用,请确保数组arr中的每个元素都能够执行keyFunction方法,并且不会报错。arr:"+str(arr))
    mid = None
    for i in range(len(arr)):
        if mid != arr[i]:
            mid = arr[i]
        else:
            arr[i] = None
    return list(filter(lambda x: x != None, arr))