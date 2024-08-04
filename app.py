from TaskManager import TaskManager
from time import sleep

task_manager = TaskManager()
    
while True:
    option = task_manager.menu()
        
    if option == "1":
        task = input('Digite a Tarefa: ')
        task_manager.add_task(task)
        sleep(2)  
    elif option == "2":
        task_manager.list_tasks()
        sleep(2)
    elif option == "3":
        task_manager.mark_task_completed()
        sleep(2)
    elif option == "4":
        task_manager.delete_task()
        sleep(2)
    elif option == "5":
        task_manager.close_task_manager()
        print('Gerenciador Finalizado!')
        sleep(2)
        break
    else:
        print('Opção inválida, tente novamente.')
        sleep(2)
    print(f'\n{37*"-"}\n')
