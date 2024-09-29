class TaskChecker:
    @staticmethod
    def check_task_completion(fancode_users, todos):
        for user in fancode_users:
            user_todos = [todo for todo in todos if todo['userId'] == user['id']]
            completed_count = sum(todo['completed'] for todo in user_todos)

            if user_todos and (completed_count / len(user_todos)) <= 0.5:
                return False
        return True
