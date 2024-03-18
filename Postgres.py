import psycopg2 as db
class Data_Basa():
    @staticmethod
    def data_basa(quer, type):
        database = db.connect(
            database = "n37",
            user = "postgres",
            host = "localhost",
            password = "rus19tam98"
        )
        cursor = database.cursor()
        cursor.execute(quer)
        if type == "insert":
            database.commit()
            return "qo'shildi"
        else:
            return cursor.fetchall()