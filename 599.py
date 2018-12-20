
def l599(list1,list2):
    list3 = set(list1)& set(list2)
    b = []
    a = len(list1+list2)
    for v in list3:
        if a>list1.index(v)+list2.index(v):
            a = list1.index(v)+list2.index(v)
            b = []
            b.append(v)
        elif a==list1.index(v)+list2.index(v):
            b.append(v)


    return b


print(l599(["Shogun", "Tapioca Express", "Burger King", "KFC"],
           ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]))