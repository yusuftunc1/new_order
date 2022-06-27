
class order:
    
    def __init__(self,id,name,numofproduct,orderdate,startingdate,note,customerid):
        if id == None:
            self.id = 0
        else:
            self.id = id

        self.name = name
        self.numofproduct = numofproduct
        self.orderdate = orderdate
        self.startingdate = startingdate
        self.note = note
        self.customerid = customerid
    
    @staticmethod
    def getOrder(obj):
        list = []

        if isinstance(obj,tuple):
            list.append(order(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5],obj[6]))
        else:
            for i in obj:
                list.append(order(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
        
        return list

