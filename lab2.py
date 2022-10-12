#Кутузов Михаил Андреевич Группа-3140 ИСУ-358729
def color(code):
    return f"\u001b[{code}m"
White=color(47)
Blue=color(44)
end=color(0)
for i in range(2):
    print(White + '  '*10,Blue+'  '*5,White + '  '*15+end)
for i in range(2):
    print(Blue+'  '*31+end)
for i in range(2):
    print(White + '  '*10,Blue+'  '*5,White + '  '*15+end)
