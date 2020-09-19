def my_list():
    while True:
        with open('shopping_list.txt','a+') as file:
            #print(file.tell())
            print("""type anytime
Exit: to quit
List: To Read and Delete
            
""")
            item = input('Enter item: ')
            if item == 'EXIT':
                break
            elif item == 'please tell':
                print(file.tell())
            elif item == 'LIST':
                 #print(file.tell())
                 file.seek(0)
                 #print(file.read())
                 items = list(enumerate(file.read().split(),1))
                 for count, item in items:
                     print("{:3d}) {}".format(count,item))
                 #remove = int(input("Enter number to delete or 0 to continue: "))
                 while True:
                     try:
                         remove = int(input("Enter number to delete or 0 to continue: "))
                         if remove == 0:
                             #continue
                             break
                         else:
                             del items[remove-1]
                             with open('shopping_list.txt','w') as file:
                                 for item in items:
                                     file.write(item[1] +'\n')
                     except ValueError:
                         print('If you don\'t want to delete please ener 0')

     

           


            else:
                file.write(item + '\n')
my_list()


print('jgkjfkg')