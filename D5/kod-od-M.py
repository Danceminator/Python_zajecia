import pymysql

class MySQLConnector:
    def __init__(self, passwd):
    self.passwd = passwd
    self.conn = pymysql.connect("localhost", "root", self.passwd, "skoczkowie1")
    self.c = self.conn.cursor()
    print("Po³¹czenie ustanowione")
    nav = ''
    while(nav != "Q"):
        nav = input("Co chcesz zrobiæ? (S)-select, (I)-insert, (U)-update, (Q)- wyjœcie")
        if(nav == "S"):
        self.select()
        elif(nav == "I"):
        self.insert()
        elif(nav == "U"):
        self.update()           	 
    print("Po³¹czenie zakoñczone")
    self.conn.close()    
    def select(self):
    self.c.execute("SELECT id_skoczka, imie, nazwisko, kraj FROM zawodnicy1 order by id_skoczka;")
    res = self.c.fetchall()   	 
    for v in res:
        id_s = v[0]
        imie = v[1]
        nazwisko = v[2]
        kraj = v[3]
        print("%-3s %-15s %-30s %-3s" % (id_s, imie, nazwisko, kraj))
    def insert(self):
    self.c.execute("INSERT INTO zawodnicy1 VALUES (25, 'xxx', 'xxx', 'GER', '1981-02-24', 187, 68);")
    self.conn.commit()
    print("dane wprowadzono")
    def update(self):
    self.c.execute("UPDATE zawodnicy1 SET imie='yyy' where id_skoczka = 25;")
    self.conn.commit()
    print("dane zaktualizowane")   	 
c1 = MySQLConnector("miki123")




