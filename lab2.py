#Кутузов Михаил Андреевич Группа-3140 ИСУ-358729
import pandas as pd
def color(code):
    return f"\u001b[{code}m"
White=color(47)
Black=color(40)
Blue=color(44)
Red=color(41)
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

#4
file = pd.read_csv('books.csv', encoding="windows-1251", delimiter=";")
df = file['Цена поступления']
befor2=0
after2=0
df=[float(x.replace(',', '.')) for x in df]
for i in (df):
    if float(i)<200:
        befor2+=1
    else:
        after2+=1


for i in (8109,8000,5000,2000,1300,1000,0):
    if i>1300:
        print(i, Black+'  ' + Red + '  ' + Black + ' ' * 3 + end)
    else:
        if i==0:
            print('   0', Black + '  ' + Red + '  ' + Black + ' ' + Blue + ' ' + Black + ' ' + end)
        else:
            print(i, Black + '  ' + Red + '  ' + Black + ' ' + Blue + ' ' + Black + ' ' + end)
