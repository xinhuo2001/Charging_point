from user import User

if __name__ == "__main__":
    u1 = User(1, "张三", "123", 20)
    u2 = User(2, "李四", "456", 25)

    u1.showInfo()
    u2.showInfo()
    User.showUserCount()