class List(object):
    def remove_(self, integer_list, values_list):
        # #your code here

        for i in values_list:
            integer_list = [x for x in integer_list if x != i]
        return integer_list


integer_list = [1, 1, 2 ,3 ,1 ,2 ,3 ,4, 4, 3 ,5, 6, 7, 2, 8]
values_list  = [1, 3, 4, 2]


li = List()
print(li.remove_(integer_list, values_list))

class List2(object):
    def remove_(self, integer_list, values_list):
        return [i for i in integer_list if i not in values_list]