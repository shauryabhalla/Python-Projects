lis = [7,15,6,8,90,56]

def bubble_sort(list_name):
    for i in range(len(list_name)):
        for j in range(0,len(list_name)-i-1):
            if list_name[j]>list_name[j+1]:
                list_name[j+1],list_name[j]=list_name[j],list_name[j+1]

    return list_name

print(bubble_sort(lis))