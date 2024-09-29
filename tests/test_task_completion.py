from src.api_client import APIClient
from src.user_filter import UserFilter
from src.task_checker import TaskChecker

def test_fancode_task_completion():

    users = APIClient.get_users()
    todos = APIClient.get_todos()


    fan_code_users = UserFilter.get_fancode_users(users)


    print("\nFiltered FanCode Users:")
    for user in fan_code_users:
        print(user)

    result = TaskChecker.check_task_completion(fan_code_users, todos)

    if result:
        print("\nAll FanCode users have more than 50% of their tasks completed.")
    else:
        print("\nSome FanCode users do not have more than 50% of their tasks completed.")

