def fizzbuzz(max_num: int):
    m = 'buzz'
    res = []
    for n in range(1, max_num+1, 1):
        if n % 3 == 0 and m == 'fizz':
            res.append('buzz')
            m = 'buzz'
        elif n % 3 == 0 and m == 'buzz':
            res.append('fizz')
            m = 'fizz'
        else:
            res.append(n)

    print(res)

if __name__ == '__main__':
    print('Enter number you want for fizz-buzz: ')
    number = input()
    fizzbuzz(int(number))
