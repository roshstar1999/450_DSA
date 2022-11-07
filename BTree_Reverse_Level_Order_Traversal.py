def reverseLevelOrder(root):
    # code here
    
    if root==None:
        return None
    l=[]
    Q=queue.Queue()
    
    Q.put(root)
    
    
    while  not  Q.empty():
        
        temp=Q.get()
        l.append(temp.data)
        
        if temp.right is  not None:
            Q.put(temp.right)
        
        if temp.left is  not None:
            Q.put(temp.left)
            
    n=len(l)
    for i in range(n//2):
        l[i],l[n-1-i]=l[n-1-i],l[i]
    return l
