#Кутузов Михаил Андреевич Группа-3140 ИСУ-358729
def color(code):
    return f"\u001b[{code}m"
White=color(47)
Black=color(40)
Blue=color(44)
end=color(0)
#Flag
for _ in range(2):
    print(White + '  '*10+Blue+'  '*5+White + '  '*15+end)
for _ in range(2):
    print(Blue+'  '*30+end)
for _ in range(2):
    print(White + '  '*10+Blue+'  '*5+White + '  '*15+end)
print()
#pattern
x=int(input())
print(((White + '  '*3+White + ' '+Black + '  '*2+White + '  '*3+White + ' '+end)*2)*x)
print(((White + '  '*2+White + ' '+Black + '  '*4+White + '  '*2+White + ' '+end)*2)*x)
print(((White + '   '+ Black + '  '*6+White + '  '*1+White + ' '+end)*2)*x)
print(((White + ' '+Black + '  '*8+White + ' '+end)*2)*x)
print(((White + '   '+ Black + '  '*6+White + '  '*1+White + ' '+end)*2)*x)
print(((White + '  '*2+White + ' '+Black + '  '*4+White + '  '*2+White + ' '+end)*2)*x)
print(((White + '  '*3+White + ' '+Black + '  '*2+White + '  '*3+White + ' '+end)*2)*x)

#grafic
count=20
count1=20
for i in (0,2,4,6,8,12,14,16,18,20):
    if count-i>10:
        print(count-i, Black + '  '*(count1-2) + Blue+'    '+end,end='')
    else:
        print('',count-i, Black + '  ' * (count1 - 2) + Blue + '    ' + end, end='')
    if count1-i<20:
        print(Black+'  '*(20-count1)+end)
    else:
        print()
    count1-=2
print('   ', 0,'  ', 4,' ','', 8,'', 12,'',16,'',24,'',28,'',32,'',36,'',40)


