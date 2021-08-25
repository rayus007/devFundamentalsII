def loops():
    print('Insert a number to calculate squares: ')
    try:
        number = int(input())
        for i in range(number):
            print(f'{i ** 2}')
    except ValueError:
        print('Please enter a valid integer number')


def listComprehension():
    try:
        print('Insert a number for the X Axis: ')
        axisX = int(input())
        print('Insert a number for the Y Axis: ')
        axisY = int(input())
        print('Insert a number for the Z Axis: ')
        axisZ = int(input())
        print('Insert a number to avoid in the Axes sum')
        sumFilter = int(input())
        ListOfNumbers = [[x, y, z] for x in range(axisX+1) for y in range(axisY+1) for z in range(axisZ+1) if
                         sumFilter != (x + y + z)]
        print(ListOfNumbers)
    except ValueError:
        print('Please insert valid integer values.')


def runnerAppScore():
    print('Type a qty of scores to insert [Between 2-10]')
    try:
        myflag = False
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
                            myflag = True
                        else:
                            myflag = False
                            break
                if myflag is True:
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


if __name__ == '__main__':
    print('######################## TASK 1 ######################')
    loops()
    print('######################## TASK 2 ######################')
    listComprehension()
    print('######################## TASK 3 ######################')
    runnerAppScore()
