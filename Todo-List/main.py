class Todo_list:
    def __init__(self):
        self.task_lists = []
    
    def main_menu(self):
        while True:
            usr_chs = int(input("1.Add Task\n2.Delete Task\n3.View Task\n4.Exit\nEnter your choice: "))

            if usr_chs == 1:
                self.add_task()
            elif usr_chs == 2:
                self.delete_task()
            elif usr_chs == 3:
                self.view_taks()
            elif usr_chs == 4:
                print("GoodBye :)")
                break
            else:
                print("Something went wrong")
            
    def add_task(self):
        self.tsk_name = input("Enter your task name: ")
        self.tsk_des = input("Enter your task Description: ")
        self.tsk_info = self.tsk_name, self.tsk_des
        self.task_lists.append(self.tsk_info)

    
    def delete_task(self):
        self.tsk_del_name = input("Enter the task name you want to delete: ")
        found = False
        for task in self.task_lists:
            if task[0] == self.tsk_del_name:
                self.task_lists.remove(task)
                found = True
                break
            else:
                print("Task not found")
        if not found:
            print("Something went wrong")



    def view_taks(self):
        print(f"Tasks: {self.task_lists}")

if __name__ == "__main__":
    root = Todo_list()
    root.main_menu()