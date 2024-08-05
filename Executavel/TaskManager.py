from Database import Database
from time import sleep

class TaskManager:
    
    def __init__(self) -> None:
        self.database = Database()
    
    def menu(self):
        print("\nGerenciador de Tarefas:\n")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Marcar tarefa como concluída")
        print("4. Remover tarefa")
        print("5. Sair\n")
        choice = input("Escolha uma opção: ")
        return choice
    
    def add_task(self, choice):
        self.database.create_task(choice)
        print('Tarefa adicionada com sucesso!')
      
    def list_tasks(self):
        tasks = self.database.read_tasks()
        if tasks != []:
            print('\n-------- Tarefas registradas --------\n')
            for pos, task in enumerate(tasks):
                if task[2] == 'Não':
                    print(f'{pos + 1} - {task[1]}')
                else:
                    print(f'{pos + 1} - {task[1]} ✅')
        else:
            print('Nenhuma tarefa adicionada!')
    
    def get_tasks(self):
        tasks = self.database.read_tasks()
        return tasks
    
    def get_user_choice(self):
        while True:
            try:
                choice = int(input('Digite o número da tarefa: '))
                return choice
            except:
                print('Digite apenas números')
                
    def mark_task_completed(self):
        self.list_tasks()
        tasks = self.get_tasks()
        print('Qual tarefa foi concluída?')
        choice = self.get_user_choice()
        
        if choice in range(len(tasks) + 1):
            self.database.update_task(tasks[choice - 1][0])
            print('Tarefa marcada como concluída!')
            sleep(1)
            self.list_tasks()
        else:
            print('Tarefa não encontrada!')
        
    def delete_task(self): 
        self.list_tasks()
        tasks = self.get_tasks()
        print('Qual tarefa será excluída?')
        choice = self.get_user_choice()
        if choice in range(len(tasks) + 1):
            self.database.delete_task(tasks[choice - 1][0])
            print('Tarefa excluída com sucesso!')
            sleep(1)
            self.list_tasks()
        else:
            print('Tarefa não encontrada!')
            
    def close_task_manager(self):
        self.database.close_connection()
        

