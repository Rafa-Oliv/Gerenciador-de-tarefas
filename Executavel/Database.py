import sqlite3

class Database:
    def __init__(self, db_name='task_record.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            completed TEXT NOT NULL
            )
        ''')
        self.connection.commit()
        
    def create_task(self, task):
        self.cursor.execute('INSERT INTO tasks (task, completed) VALUES (?, ?)', (task, 'Não'))
        self.connection.commit()
        
    def read_tasks(self):
        self.cursor.execute('SELECT * FROM tasks')
        return self.cursor.fetchall()
    
    def update_task(self, task_id):
        self.cursor.execute('UPDATE tasks SET completed = ? WHERE id = ?', ('Sim', task_id))
        self.connection.commit()
        
    def delete_task(self, task_id):
        self.cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        self.connection.commit()
        
    def close_connection(self):
        self.connection.close()

           
               
    
                
                
                    
                
            
        
        
    
    



            
                        
                        
        
    
    
