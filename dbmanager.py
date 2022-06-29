import mysql.connector
from connection import connection
from orders import order


class dbmanager():
    def __init__(self):
        self.connection = connection
        self.cursor =self.connection.cursor()
    

    #orderları id ye göre listeleme
    def getOrderbyId(self, id):
        sql = "Select * from orders Where id= %s"
        values = (id,)
        self.cursor.execute(sql,values)

        try:
            obj = self.cursor.fetchone()
            return order.getOrder(obj)
        except mysql.connector.Error as error:
            print("error: ",error)


    #orderları isme göre listeleme
    def getOrderbyName(self, name):
        sql = "Select * from orders Where name= %s"
        values = name
        self.cursor.execute(sql,values)

        try:
            obj = self.cursor.fetchone()
            return order.getOrder(obj)
        except mysql.connector.Error as error:
            print("error: ",error)
    

    #order ekleme
    def addOrder(self, order: order):
        sql = "INSERT INTO student(id,name,numofproduct,orderdate,startingdate,note,customerid) VALUES(%s,%s,%s,%s,%s,%s,%s)"
        value = (order.id, order.name, order.numofproduct, order.orderdate, order.startingdate, order.note, order.customerid)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
        except mysql.connector.Error as error:
            print("error: ",error)
    

    #order düzenleme
    def editOrder(self, order: order):
        sql = "Update order Set name= %s, numofproduct= %s, orderdate= %s, startingdate= %s, note= %s, customerid= %s Where id= %s"
        value = (order.name, order.numofproduct, order.orderdate, order.startingdate, order.note, order.customerid, order.id)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            #aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
            print(f"{self.cursor.rowcount} tane öge güncellendi")
        except mysql.connector.Error as error:
            print("error: ",error)


    #order silme
    def deleteOrder(self, id):
        sql = "Delete from Order Where id= %s"
        value = (id,)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            #aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
            print(f"{self.cursor.rowcount} tane öge silindi")
        except mysql.connector.Error as error:
            print("error: ",error)
        

    #sql bağlatısı silme
    def __del__(self):
        self.connection.close()
