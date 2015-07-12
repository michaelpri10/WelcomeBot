import shelve


def check_user(user_id, id_room, enter_or_leave):
    f = shelve.open("users.txt")

    if (id_room + enter_or_leave) in f:
        if user_id in f[id_room + enter_or_leave]:
            print f[id_room + enter_or_leave]
            print user_id
            print False
            return_value = False
        else:
            f[id_room + enter_or_leave] += [user_id]
            print f[id_room + enter_or_leave]
            print user_id
            print True
            return_value = True
    else:
        f[id_room + enter_or_leave] = []
        f[id_room + enter_or_leave] += [user_id]
        print f[id_room + enter_or_leave]
        print user_id
        print True
        return_value = True

    f.close()
    return return_value
