while True:
    try:
        print('Введите значения')
        s, l1, r1, l2, r2 = map(int,input().split())
        break
    except ValueError:
        print('Неверный ввод!')
        continue


if l1 + l2 <= s <= l1 + r2 :
    if s <= r2 :
        print(l1, s-l1)
    else :
        print(s - r2, r2)
elif r1 + l2 <= s <= r1 + r2 :
    if s <= r2 :
        print(r1, s - r1)
    else :
        print(s - r2, r2)
else :
    print(-1)
