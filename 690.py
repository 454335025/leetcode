def l690(employees,id):

    a = 0

    def find_id(e):
        b = 0
        for i in range(len(e)):
            for j in range(len(employees)):
                if employees[j][0] == e[i]:
                    b +=employees[j][1]
                if len(employees[j][2])>0:
                    b +=find_id(employees[j][2])

        return b

    for ii in range(len(employees)):
        if employees[ii][0] == id:
            a = employees[ii][1]
            a +=find_id(employees[ii][2])


    return a
print(l690([[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1))