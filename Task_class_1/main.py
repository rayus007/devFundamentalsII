def loops():
    print('Insert a number to calculate squares: ')
    try:
        number = int(input())
        for i in range(number):
            print(f'{i ** 2}')
    except ValueError:
        print('Please enter a valid integer number')


def list_comprehension():
    try:
        print('Insert a number for the X Axis: ')
        axis_x = int(input())
        print('Insert a number for the Y Axis: ')
        axis_y = int(input())
        print('Insert a number for the Z Axis: ')
        axis_z = int(input())
        print('Insert a number to avoid in the Axes sum')
        sum_filter = int(input())
        list_of_numbers = [[x, y, z] for x in range(axis_x + 1) for y in range(axis_y + 1) for z in range(axis_z + 1) if
                           sum_filter != (x + y + z)]
        print(list_of_numbers)
    except ValueError:
        print('Please insert valid integer values.')


def runner_app_score():
    print('Type a qty of scores to insert [Between 2-10]')
    try:
        my_flag = False
        n = int(input())
        if 2 <= n <= 10:
            print(f'Insert {n} scores [limit: -100, 100] as integer values separated by Spaces: ')
            try:
                scores = list(map(int, input().split()))
                if len(scores) != n:
                    print(f'Please insert only {n} scores separated by Spaces in the next attempt.')
                else:
                    for i in scores:
                        if -100 <= i <= 100:
                            my_flag = True
                        else:
                            my_flag = False
                            break
                if my_flag is True:
                    aux = sorted(set(scores), reverse=True)
                    print(f'The Runner-up score is: {aux[1]}')
                else:
                    print('Scores out of range, insert values between -100 and 100.')
            except ValueError:
                print('Please insert Integer values in the next attempt.')
        else:
            print("Good luck in the next attempt")
    except ValueError:
        print('Please insert a valid integer value in the next attempt.')


def print_word():
    print('Type a qty of words to insert.')
    n = int(input())
    dictionary = dict()
    for i in range(n):
        word = input().strip()
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1

    result = [str(i) for i in dictionary.values()]
    print(f'{len(dictionary)}\n', result)


if __name__ == '__main__':
    print('######################## TASK 1 ######################')
    loops()
    print('######################## TASK 2 ######################')
    list_comprehension()
    print('######################## TASK 3 ######################')
    runner_app_score()
    print('######################## TASK 4 ######################')
    print_word()
