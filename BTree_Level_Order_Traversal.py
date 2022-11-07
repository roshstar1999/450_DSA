  def levelOrder(self,root ):
        l=[]
        
        customQ=queue.Queue()
        customQ.put(root)
        
        while not customQ.empty():
            temp=customQ.get()
            l.append(temp.data)
            
            
            if temp.left is not None:
                customQ.put(temp.left)
            if temp.right is not None:
                customQ.put(temp.right)
        return l
