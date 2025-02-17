"""
zadanie 3
"""

import re


filesystem = {}
current_folder = []

def main():
    """main input loop"""
    running = True

    while running:
        inp = input('# ')
        running = parser(inp)


def parser(text):
    """parser pre input"""
    cmd = text.split()

    current_folder_dict = filesystem
    current_folder_perms = 'rwx'

    for name in current_folder:
        current_folder_perms = current_folder_dict[name][1]
        current_folder_dict = current_folder_dict[name][2]

    if cmd[0] == 'ls':
        if len(cmd) < 1 or len(cmd) >= 3:
            print('chyba')
            return True

        if len(current_folder_dict) == 0:
            print('ziaden subor')
            return True

        if len(cmd) == 2:
            if cmd[1] in current_folder_dict:
                if len(current_folder_dict[cmd[1]]) == 3:
                    print('{} {} {}'.format(cmd[1], current_folder_dict[cmd[1]][0],
                                    current_folder_dict[cmd[1]][1]))
                    return True
                else:
                    print('chyba')
                    return True
            else:
                print('chyba')
                return True                    

        for item in current_folder_dict:
            print('{} {} {}'.format(item, current_folder_dict[item][0],
                                    current_folder_dict[item][1]))

        return True

    elif cmd[0] == 'touch':
        if len(cmd) <= 1 or len(cmd) > 2:
            print('chyba')
            return True

        if cmd[1] in current_folder_dict:
            print('chyba')

        else:
            if current_folder_perms[1] == 'w':
                current_folder_dict[cmd[1]] = ['root', current_folder_perms]
            else:
                print('chyba prav')

        return True

    elif cmd[0] == 'mkdir':
        if len(cmd) <= 1 or len(cmd) > 2:
            print('chyba')
            return True

        if cmd[1] in current_folder_dict:
            print('chyba')

        else:
            if current_folder_perms[1] == 'w':
                current_folder_dict[cmd[1]] = ['root', current_folder_perms,{}]
            else:
                print('chyba prav')

        return True

    elif cmd[0] == 'rm':
        if len(cmd) <= 1 or len(cmd) > 2:
            print('chyba')
            return True

        if cmd[1] in current_folder_dict:
            if current_folder_dict[cmd[1]][1][1] == 'w':
                current_folder_dict.pop(cmd[1])
            else:
                print('chyba prav')
        else:
            print("chyba")

        return True

    elif cmd[0] == 'vypis':
        if len(cmd) <= 1 or len(cmd) > 2:
            print('chyba')
            return True

        if cmd[1] in current_folder_dict:
            if len(current_folder_dict[cmd[1]]) == 3:
                print('chyba')

            if current_folder_dict[cmd[1]][1][0] == 'r':
                print('ok')
            else:
                print('chyba prav')
        else:
            print('chyba')

        return True

    elif cmd[0] == 'spusti':

        if len(cmd) <= 1 or len(cmd) > 2:
            print('chyba')
            return True

        if cmd[1] in current_folder_dict:
            if len(current_folder_dict[cmd[1]]) == 3:
                print('chyba')
                return True

            if current_folder_dict[cmd[1]][1][2] == 'x':
                print('ok')
            else:
                print('chyba prav')
        else:
            print('chyba')

        return True

    elif cmd[0] == 'cd':
        if len(cmd) <= 1 or len(cmd) > 2:
            print('chyba')
            return True
        if cmd[1] == '..':
            if len(current_folder) != 0 :
                current_folder.pop(len(current_folder)-1)
            else:
                print('chyba')
        else:
            if cmd[1] in current_folder_dict and len(current_folder_dict[cmd[1]]) == 3:
                if current_folder_dict[cmd[1]][1][0] == 'r':
                    current_folder.append(cmd[1])
                else:
                    print('chyba prav')
            else:
                print('chyba')

        return True

    elif cmd[0] == 'zapis':
        if len(cmd) <= 1 or len(cmd) > 2:
            print('chyba')
            return True

        if cmd[1] in current_folder_dict:
            if len(current_folder_dict[cmd[1]]) == 3:
                print('chyba')

            if current_folder_dict[cmd[1]][1][1] == 'w':
                print('ok')
            else:
                print('chyba prav')
        else:
            print('chyba')

        return True

    elif cmd[0] == 'chmod':
        if len(cmd) <= 2 or len(cmd) > 3:
            print('chyba')
            return True

        if cmd[2] in current_folder_dict:
            perms = '{0:b}'.format(int(cmd[1]))
            temp = ''
            temp += 'r' if (perms[0] == '1') else '-'
            temp += 'w' if (perms[1] == '1') else '-'
            temp += 'x' if (perms[2] == '1') else '-'
            current_folder_dict[cmd[2]][1] = temp
        else:
            print('chyba')

        return True

    elif cmd[0] == 'chown':
        if len(cmd) <= 2 or len(cmd) > 3:
            print('chyba')
            return True

        if cmd[2] in current_folder_dict:
            current_folder_dict[cmd[2]][0] = cmd[1]
        else:
            print('chyba')

        return True

    elif cmd[0] == 'quit':
        return False

    else:
        print('chyba')
        return True


if __name__ == '__main__':
    main()
