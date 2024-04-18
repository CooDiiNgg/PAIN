
import sqlite3

class DatabaseWork:
    def __init__(self, db):
        self.db = db

    def put_user(self, service, password, email, active):
        self.db.execute('INSERT INTO user (service, password, email, active) VALUES (?, ?, ?, ?)', (service, password, email, active))
        self.db.commit()

    def get_users(self):
        return self.db.execute('SELECT * FROM user').fetchall()
    
    def activate_user(self, id):
        self.db.execute('UPDATE user SET active = 1 WHERE id = ?', (id,))
        self.db.commit()
    
    def deactivate_user(self, id):
        self.db.execute('UPDATE user SET active = 0 WHERE id = ?', (id,))
        self.db.commit()
    
    def delete_user(self, id):
        self.db.execute('DELETE FROM user WHERE id = ?', (id,))
        self.db.commit()