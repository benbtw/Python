from sql_stuff import SQL_CLASS
import time, os
sql = SQL_CLASS
connection = sql.create_db_connection("localhost", "root", "passwordToDatabase", "accounts")

def main_menu():
    os.system("cls")
    print("Welcome to a simple SQL Login and Register Program.")
    print("1. Login")
    print("2. Register")
    print("3. Change password")
    print("4. Delete Account")
    print("5. Exit")
    user_input = input("")
    match user_input:
        case "1":
            login()
        case "2":
            register()
        case "3":
            change_pass()
        case "4":
            delete_acc()
        case "5":
            print("Goodbye.")
        case _:
            print("Error, enter 1-5.")

def login():
    while True:
        user_name = input("Enter your Username: ")
        check_user = sql.check_data(connection, f"select user_name from account_info where user_name = '{user_name}';")
        if check_user is not None:
            pass_word = input("Enter your Password: ")
            check_pass = sql.check_data(connection, f"select pass_word from account_info where pass_word = '{pass_word}';")
            if check_pass is not None:
                print("Login Success!")
                break

def register():
    user_name = input("Enter a User name: ")
    pass_word = input("Enter a Password: ")
    pop_acc = f"INSERT INTO account_info VALUES ('{user_name}', '{pass_word}');"
    sql.execute_query(connection, pop_acc)
    print("Account registered.")
    time.sleep(1)
    main_menu()

def change_pass():
    ok = False
    while True:
        user_name = input("Enter your User name: ")
        check_user = sql.check_data(connection, f"select user_name from account_info where user_name = '{user_name}';")
        while check_user is not None:
            pass_word = input("Enter your old Password: ")
            check_pass = sql.check_data(connection, f"select pass_word from account_info where pass_word = '{pass_word}';")
            if check_pass is not None:
                ok = True
                break
        if ok:
            break
    pass_word = input("Enter your new Password: ")
    change_info = f"UPDATE account_info SET pass_word = '{pass_word}' WHERE user_name = '{user_name}';"
    sql.execute_query(connection, change_info)
    print("Password Changed.")
    time.sleep(1)
    main_menu()

def delete_acc():
    ok = False
    while True:
        user_name = input("Enter your User name: ")
        check_user = sql.check_data(connection, f"select user_name from account_info where user_name = '{user_name}';")
        while check_user is not None:
            pass_word = input("Enter your Password: ")
            check_pass = sql.check_data(connection, f"select pass_word from account_info where pass_word = '{pass_word}';")
            if check_pass is not None:
                ok = True
                break
        if ok:
            delete_info = f"delete from account_info where user_name = '{user_name}';"
            sql.execute_query(connection, delete_info)
            print("Deleted Account!")
            break
    time.sleep(1)
    main_menu()

main_menu()