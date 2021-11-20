def do_stuff(num):
    try:
        return int(num)+5
    except ValueError as err:
        return err

if __name__ == '__main__':
    do_stuff(10)

