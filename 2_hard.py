def password(number):
    pas = ''
    for i in range(1, number):
        for j in range(i + 1, number):
            if number % (i+j) == 0:
                pas += str(i) + str(j)
    return pas

print('Введите число: ')
print(password(int(input())))

