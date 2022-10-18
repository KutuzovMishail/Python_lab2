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

