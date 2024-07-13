import sqlite3
connection = sqlite3.connect('database.db')
cursor = connection.cursor()
class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def aromat(self, aromat):
        with self.connection:
            return self.connection.execute("INSERT INTO 'americano' ('aromat') VALUES (?)", (aromat,))

    def krepost(self, krepost):
        with self.connection:
            return self.connection.execute("INSERT INTO 'americano' ('krepost') VALUES (?)", (krepost,))

    def gorkost(self, gorkost):
        with self.connection:
            return self.connection.execute("INSERT INTO 'americano' ('gorkost') VALUES (?)", (gorkost,))

    def aromatdouble(self, aromatdouble):
        with self.connection:
            return self.connection.execute("INSERT INTO 'double' ('aromatdouble') VALUES (?)", (aromatdouble,))

    def krepostdouble(self, krepostdouble):
        with self.connection:
            return self.connection.execute("INSERT INTO 'double' ('krepostdouble') VALUES (?)", (krepostdouble,))

    def gorkostdouble(self, gorkostdouble):
        with self.connection:
            return self.connection.execute("INSERT INTO 'double' ('gorkostdouble') VALUES (?)", (gorkostdouble,))

    def aromatkapuch(self, aromatkapuch):
        with self.connection:
            return self.connection.execute("INSERT INTO 'kapuch' ('aromatkapuch') VALUES (?)", (aromatkapuch,))

    def krepostkapuch(self, krepostkapuch):
        with self.connection:
            return self.connection.execute("INSERT INTO 'kapuch' ('krepostkapuch') VALUES (?)", (krepostkapuch,))

    def gorkostkapuch(self, gorkostkapuch):
        with self.connection:
            return self.connection.execute("INSERT INTO 'kapuch' ('gorkostkapuch') VALUES (?)", (gorkostkapuch,))

    def nasishkapuch(self, nasishkapuch):
        with self.connection:
            return self.connection.execute("INSERT INTO 'kapuch' ('nasishkapuch') VALUES (?)", (nasishkapuch,))

    def aromatlatte(self, aromatlatte):
        with self.connection:
            return self.connection.execute("INSERT INTO 'latte' ('aromatlatte') VALUES (?)", (aromatlatte,))

    def krepostlatte(self, krepostlatte):
        with self.connection:
            return self.connection.execute("INSERT INTO 'latte' ('krepostlatte') VALUES (?)", (krepostlatte,))

    def gorkostlatte(self, gorkostlatte):
        with self.connection:
            return self.connection.execute("INSERT INTO 'latte' ('gorkostlatte') VALUES (?)", (gorkostlatte,))

    def nasishlatte(self, nasishlatte):
        with self.connection:
            return self.connection.execute("INSERT INTO 'latte' ('nasishlatte') VALUES (?)", (nasishlatte,))

    def aromathot(self, aromathot):
        with self.connection:
            return self.connection.execute("INSERT INTO 'hot' ('aromathot') VALUES (?)", (aromathot,))

    def kreposthot(self, kreposthot):
        with self.connection:
            return self.connection.execute("INSERT INTO 'hot' ('kreposthot') VALUES (?)", (kreposthot,))

    def gorkosthot(self, gorkosthot):
        with self.connection:
            return self.connection.execute("INSERT INTO 'hot' ('gorkosthot') VALUES (?)", (gorkosthot,))

    def nasishhot(self, nasishhot):
        with self.connection:
            return self.connection.execute("INSERT INTO 'hot' ('nasishhot') VALUES (?)", (nasishhot,))

    def aromatbanana(self, aromatbanana):
        with self.connection:
            return self.connection.execute("INSERT INTO 'banana' ('aromatbanana') VALUES (?)", (aromatbanana,))

    def krepostbanana(self, krepostbanana):
        with self.connection:
            return self.connection.execute("INSERT INTO 'banana' ('krepostbanana') VALUES (?)", (krepostbanana,))

    def gorkostbanana(self, gorkostbanana):
        with self.connection:
            return self.connection.execute("INSERT INTO 'banana' ('gorkostbanana') VALUES (?)", (gorkostbanana,))

    def nasishbanana(self, nasishbanana):
        with self.connection:
            return self.connection.execute("INSERT INTO 'banana' ('nasishbanana') VALUES (?)", (nasishbanana,))

    def aromatmaka(self, aromatmaka):
        with self.connection:
            return self.connection.execute("INSERT INTO 'maka' ('aromatmaka') VALUES (?)", (aromatmaka,))

    def krepostmaka(self, krepostmaka):
        with self.connection:
            return self.connection.execute("INSERT INTO 'maka' ('krepostmaka') VALUES (?)", (krepostmaka,))

    def gorkostmaka(self, gorkostmaka):
        with self.connection:
            return self.connection.execute("INSERT INTO 'maka' ('gorkostmaka') VALUES (?)", (gorkostmaka,))

    def nasishmaka(self, nasishmaka):
        with self.connection:
            return self.connection.execute("INSERT INTO 'maka' ('nasishmaka') VALUES (?)", (nasishmaka,))

    def aromatx(aromat):
        cursor.execute('SELECT AVG(aromat) FROM americano')
        xx = cursor.fetchone()[0]
        return xx
    def krepostx(aromat):
        cursor.execute('SELECT AVG(krepost) FROM americano')
        xc = cursor.fetchone()[0]
        return xc
    def gorkostx(aromat):
        cursor.execute('SELECT AVG(gorkost) FROM americano')
        xv = cursor.fetchone()[0]
        return xv

    def aromatxdouble(aromat):
        cursor.execute('SELECT AVG(aromatdouble) FROM double')
        xx = cursor.fetchone()[0]
        return xx
    def krepostxdouble(aromat):
        cursor.execute('SELECT AVG(krepostdouble) FROM double')
        xc = cursor.fetchone()[0]
        return xc
    def gorkostxdouble(aromat):
        cursor.execute('SELECT AVG(gorkostdouble) FROM double')
        xv = cursor.fetchone()[0]
        return xv

    def aromatxkapuch(aromat):
        cursor.execute('SELECT AVG(aromatkapuch) FROM kapuch')
        xx = cursor.fetchone()[0]
        return xx
    def krepostxkapuch(aromat):
        cursor.execute('SELECT AVG(krepostkapuch) FROM kapuch')
        xc = cursor.fetchone()[0]
        return xc
    def gorkostxkapuch(aromat):
        cursor.execute('SELECT AVG(gorkostkapuch) FROM kapuch')
        xv = cursor.fetchone()[0]
        return xv
    def nasishxkapuch(aromat):
        cursor.execute('SELECT AVG(nasishkapuch) FROM kapuch')
        xv = cursor.fetchone()[0]
        return xv

    def aromatxlatte(aromat):
        cursor.execute('SELECT AVG(aromatlatte) FROM latte')
        xx = cursor.fetchone()[0]
        return xx
    def krepostxlatte(aromat):
        cursor.execute('SELECT AVG(krepostlatte) FROM latte')
        xc = cursor.fetchone()[0]
        return xc
    def gorkostxlatte(aromat):
        cursor.execute('SELECT AVG(gorkostlatte) FROM latte')
        xv = cursor.fetchone()[0]
        return xv
    def nasishxlatte(aromat):
        cursor.execute('SELECT AVG(nasishlatte) FROM latte')
        xv = cursor.fetchone()[0]
        return xv

    def aromatxhot(aromat):
        cursor.execute('SELECT AVG(aromathot) FROM hot')
        xx = cursor.fetchone()[0]
        return xx
    def krepostxhot(aromat):
        cursor.execute('SELECT AVG(kreposthot) FROM hot')
        xc = cursor.fetchone()[0]
        return xc
    def gorkostxhot(aromat):
        cursor.execute('SELECT AVG(gorkosthot) FROM hot')
        xv = cursor.fetchone()[0]
        return xv
    def nasishxhot(aromat):
        cursor.execute('SELECT AVG(nasishhot) FROM hot')
        xv = cursor.fetchone()[0]
        return xv

    def aromatxbanana(aromat):
        cursor.execute('SELECT AVG(aromatbanana) FROM banana')
        xx = cursor.fetchone()[0]
        return xx
    def krepostxbanana(aromat):
        cursor.execute('SELECT AVG(krepostbanana) FROM banana')
        xc = cursor.fetchone()[0]
        return xc
    def gorkostxbanana(aromat):
        cursor.execute('SELECT AVG(gorkostbanana) FROM banana')
        xv = cursor.fetchone()[0]
        return xv
    def nasishxbanana(aromat):
        cursor.execute('SELECT AVG(nasishbanana) FROM banana')
        xv = cursor.fetchone()[0]
        return xv

    def aromatxmaka(aromat):
        cursor.execute('SELECT AVG(aromatmaka) FROM maka')
        xx = cursor.fetchone()[0]
        return xx
    def krepostxmaka(aromat):
        cursor.execute('SELECT AVG(krepostmaka) FROM maka')
        xc = cursor.fetchone()[0]
        return xc
    def gorkostxmaka(aromat):
        cursor.execute('SELECT AVG(gorkostmaka) FROM maka')
        xv = cursor.fetchone()[0]
        return xv
    def nasishxmaka(aromat):
        cursor.execute('SELECT AVG(nasishmaka) FROM maka')
        xv = cursor.fetchone()[0]
        return xv

    def delamericano(aromat):
        cursor.execute('DELETE FROM americano')
        connection.commit()
        xv="ok"
        return xv

    def delbanana(aromat):
        cursor.execute('DELETE FROM banana')
        connection.commit()
        xv="ok"
        return xv

    def deldouble(aromat):
        cursor.execute('DELETE FROM double')
        connection.commit()
        xv="ok"
        return xv

    def delhot(aromat):
        cursor.execute('DELETE FROM hot')
        connection.commit()
        xv="ok"
        return xv

    def delkapuch(aromat):
        cursor.execute('DELETE FROM kapuch')
        connection.commit()
        xv="ok"
        return xv

    def dellatte(aromat):
        cursor.execute('DELETE FROM latte')
        connection.commit()
        xv="ok"
        return xv

    def delmaka(aromat):
        cursor.execute('DELETE FROM maka')
        connection.commit()
        xv="ok"
        return xv

    def amusers(self, amusers):
        with self.connection:
            return self.connection.execute("INSERT INTO 'americano' ('users') VALUES (?)", (amusers,))

    def bausers(self, amusers):
        with self.connection:
            return self.connection.execute("INSERT INTO 'banana' ('users') VALUES (?)", (amusers,))

    def dousers(self, amusers):
        with self.connection:
            return self.connection.execute("INSERT INTO 'double' ('users') VALUES (?)", (amusers,))

    def hotusers(self, amusers):
        with self.connection:
            return self.connection.execute("INSERT INTO 'hot' ('users') VALUES (?)", (amusers,))

    def kausers(self, amusers):
        with self.connection:
            return self.connection.execute("INSERT INTO 'kapuch' ('users') VALUES (?)", (amusers,))

    def lausers(self, amusers):
        with self.connection:
            return self.connection.execute("INSERT INTO 'latte' ('users') VALUES (?)", (amusers,))

    def mausers(self, amusers):
        with self.connection:
            return self.connection.execute("INSERT INTO 'maka' ('users') VALUES (?)", (amusers,))

    def usam(aromat):
        cursor.execute("SELECT SUM(users) FROM americano")
        result = cursor.fetchone()[0]
        return result

    def usba(aromat):
        cursor.execute("SELECT SUM(users) FROM banana")
        result = cursor.fetchone()[0]
        return result

    def usdo(aromat):
        cursor.execute("SELECT SUM(users) FROM double")
        result = cursor.fetchone()[0]
        return result

    def ushot(aromat):
        cursor.execute("SELECT SUM(users) FROM hot")
        result = cursor.fetchone()[0]
        return result

    def uska(aromat):
        cursor.execute("SELECT SUM(users) FROM kapuch")
        result = cursor.fetchone()[0]
        return result

    def usla(aromat):
        cursor.execute("SELECT SUM(users) FROM latte")
        result = cursor.fetchone()[0]
        return result

    def usma(aromat):
        cursor.execute("SELECT SUM(users) FROM maka")
        result = cursor.fetchone()[0]
        return result
