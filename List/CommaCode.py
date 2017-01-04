def commaFunc(list):
    for i in range(len(list)):
        if i == len(list) - 1:
            print('and {0}'.format(list[i]))
        else:
            print('{0},'.format(list[i]), end=' ')

list = ['apples', 'bananas', 'tofu', 'cats', 1, 1.09, True]
commaFunc(list)