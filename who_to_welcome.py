def check_user(user):
    new = True
    try:
        f = open("users.txt", "r")
        try:
            file_contents = f.readlines()
        finally:
            f.close()
    except IOError:
        return False
    
    for x in range(0, len(file_contents)):
        if user == file_contents[x]:
            new = False
    
    if new is True:
        try:
            logfile = open("users.txt", "a")
            try:
                logfile.write(user)
            finally:
                logfile.close()
        except IOError:
            new = False
    return new
