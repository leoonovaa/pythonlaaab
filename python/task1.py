class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

    def __repr__(self):
        return f"User(username={self.username}, role={self.role})"


def requires_role(required_role):
    def decorator(func):
        def wrapper(user, *args, **kwargs):
            if user.role == required_role:
                return func(user, *args, **kwargs)
            else:
                return f"Відмовлено в доступі для {user.username}. Необхідна роль: {required_role}"
        return wrapper
    return decorator


def user_filter(users, role):
    for user in users:
        if user.role == role:
            yield user


users = [
    User("Elis", "admin"),
    User("Mike", "editor"),
    User("Charlie", "viewer")
]


@requires_role("admin")
def admin_function(user):
    return f"Вітаємо, {user.username}, ви маєте доступ до адмін-функцій."


@requires_role("editor")
def editor_function(user):
    return f"Вітаємо, {user.username}, ви можете редагувати контент."


print(admin_function(users[0]))  
print(editor_function(users[1]))  
print(editor_function(users[2]))  

print("Користувачі з роллю 'editor':")
for user in user_filter(users, "editor"):
    print(user)

