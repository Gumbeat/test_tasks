def biggest_substr(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    i = 0
    max_substr = ''
    while i < len(s1):
        i2 = 0
        while i2 < len(s2):
            if s1[i] == s2[i2]:
                j = i
                substr = ''
                while j < len(s1) and i2 < len(s2) and s1[j] == s2[i2]:
                    substr += s1[j]
                    j += 1
                    i2 += 1
                if len(substr) > len(max_substr):
                    max_substr = substr
            else:
                i2 += 1
        i += 1
    return max_substr


s1 = input('Введите первую строку: ')
s2 = input('Введите вторую строку: ')
s3 = biggest_substr(s1, s2)
print(f'Наибольшая подстрока: {s3}')

# abcd abd abcdef
# abcdefabcx xd cgxddd