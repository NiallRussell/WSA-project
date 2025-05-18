import mysql.connector
import dbconfig as cfg


class QueenDAO:
    def __init__(self):
        self.host=       cfg.mysql['host']
        self.user=       cfg.mysql['user']
        self.password=   cfg.mysql['password']
        self.database=   cfg.mysql['database']

    def getcursor(self): 
        self.connection = mysql.connector.connect(
            host=       self.host,
            user=       self.user,
            password=   self.password,
            database=   self.database,
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def closeAll(self):
        self.connection.close()
        self.cursor.close()
         
    def getAll(self):
        cursor = self.getcursor()
        sql="select id, name, age_on_show, season, place, city from queen"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results)
        for result in results:
            #print(result)
            returnArray.append(self.convertToDictionary(result))
        
        self.closeAll()
        return returnArray

    def findByID(self, id):
        cursor = self.getcursor()
        sql="select id, name, age_on_show, season, place, city from queen where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue

    def create(self, queen):
        cursor = self.getcursor()
        sql="insert into queen (name, age_on_show, season, place, city) values (%s,%s,%s,%s,%s)"
        values = (queen.get("name"), queen.get("age_on_show"), queen.get("season"), queen.get("place"), queen.get("city"))
        cursor.execute(sql, values)

        self.connection.commit()
        newid = cursor.lastrowid
        queen["id"] = newid
        self.closeAll()
        return queen


    def update(self, id, queen):
        cursor = self.getcursor()
        sql="update queen set name= %s,age_on_show=%s, season=%s, place=%s, city=%s  where id = %s"
        print(f"update queen {queen}")
        values = (queen.get("title"), queen.get("author"), queen.get("price"), queen.get("place"), queen.get("city"), id)
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        
    def delete(self, id):
        cursor = self.getcursor()
        sql="delete from queen where id = %s"
        values = (id,)

        cursor.execute(sql, values)

        self.connection.commit()
        self.closeAll()
        
        print("queen deleted")

    def convertToDictionary(self, resultLine):
        attkeys=['id','name','age_on_show', "season", "place", "city"]
        queen = {}
        currentkey = 0
        for attrib in resultLine:
            queen[attkeys[currentkey]] = attrib
            currentkey = currentkey + 1 
        return queen

        
queenDAO = QueenDAO()