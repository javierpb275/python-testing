def do_stuff(num=0):
    try:
        if num:
            return num + 5
        else:
            return 'please enter number'
    except ValueError as err:
        return err

if __name__ == '__main__':
    do_stuff(10)

