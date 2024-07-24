import os
from datetime import datetime


#cоздание класса библиотека
class Library:
    def __init__(self):
        #создание списка книг
        self.list_of_book = []

        # записывает из файла-txt данные, которые изначально (до запуска программы) там есть, в список
        self.download_from_txt_to_list()




    def download_from_txt_to_list(self):
        ''' загружает книги в список из файла-txt при запуске программы (функция срабатывает 1 раз при запуске) '''
        
        # открывает файл-txt в режиме чтения
        with open('library.txt', 'r') as file:
            lines = file.readlines()
            # читает файл построчно
            for line in lines:
                # разделяет строку по символу ';'
                every_parameter = line.strip().split(';')

                # присваивает значения переменным id, title, author, year, status 
                id = int(every_parameter[0])
                title = every_parameter[1]
                author = every_parameter[2]
                year = every_parameter[3]
                status = every_parameter[4]

                # добавляет данные в список
                self.list_of_book.append([id, title, author, year, status])






    def save_to_txt_from_list(self):  
        ''' записывает книги из списка в файл-txt для хранения '''

        # использует режим a для записи (создает и записывает или дозаписывает в существующий)
        with open('library.txt', 'w') as file:
            for book in self.list_of_book:    
                file.write(f'{book[0]};{book[1]};{book[2]};{book[3]};{book[4]} \n')




    def add_book(self, title, author, year): 
        ''' добавляет книгу в список, а потом записывает в файл-txt книги от пользователя (title, author, year - передаются от пользователя ) '''
        
        # добавляет книгу в список
        # если в списке еще нет книг, уникальный id = 1 
        if len(self.list_of_book) == 0:
            id = 1
            status = 'в наличии'
            self.list_of_book.append([id, title, author, year, status])
        else:
            # если в списке есть книги, уникальный id высчитывает, найдя максимальный сущствующий id и прибавляю 1
            id = max([elem[0] for elem in self.list_of_book])
            status = 'в наличии'
            self.list_of_book.append([id+1, title, author, year, status])
            
        #записывает обновление из списка в файл txt, применив сущетвующий метод добавения в файл-txt 
        self.save_to_txt_from_list() 





    def show_list_of_books(self):
        ''' показывает пользователю весь список книг с их параметрами id, title, author, year и status '''
        
        # выводит список f-строкой в консоль из списка
        for elem in self.list_of_book:
            id = elem[0]
            title = elem[1]
            author = elem[2]
            year = elem[3]
            status = elem[4]
            
            print(f'{id}, {title}, {author}, {year}, {status}')
    


        


    def del_book(self, whats_del): 
        ''' удаляет книгу по id по запросу пользователя '''
        
        #берет каждый список из списка списков и проверяю тот ли id 
        for elem in self.list_of_book:
            
            #конвертирует whats_del в int покольку elem[0] - это число, а whats_del изначально строка
            if elem[0] == int(whats_del):
                #при совпадении удаляет этот список из спсика 
                self.list_of_book.remove(elem)


        #перезаписывает измененный список списков в файл-txt
        self.save_to_txt_from_list()







    def search_the_book(self, parameter_for_search, whats_search):
        ''' пользователь ищет книги по title, author или year, вводит значение одного из этих параметров, программа показывает  книги по этому параметру  '''

        #ищет в списке по заданному параметру поиска и выводит все книги по этому парамертру и их статус
        if parameter_for_search == 'title':
            for elem in self.list_of_book:
                if elem[1] == whats_search:
                    print('--------------------------')
                    print(f'{elem[1]}, {elem[4]}')  
                    print('--------------------------') 

        elif parameter_for_search == 'author':
            for elem in self.list_of_book:
                if elem[2] == whats_search:
                    print('--------------------------')
                    print(f'{elem[2]}, {elem[4]}')
                    print('--------------------------')
    
        elif parameter_for_search == 'year':
            for elem in self.list_of_book:
                if elem[3] == whats_search:
                    print('--------------------------')
                    print(f'{elem[3]}, {elem[4]}')
                    print('--------------------------')
            



    def new_status_of_the_book(self, whats_id, whats_status): 
        ''' меняет статус книги '''

        #меняет статус. показывает, что изменилось
        for elem in self.list_of_book:
            #берет каждый список из списка списков и проверяет есть ли такой id 
            #конвертирует whats_id в int покольку elem[0] - это число, а whats_id изначально строка
            if elem[0] == int(whats_id):
                elem[4] = whats_status
                print('--------------------------------------------------------')
                print(f'{elem[0]}, {elem[1]}, {elem[2]}, {elem[3]}, {elem[4]}')
                print('--------------------------------------------------------')

    
        # перезаписывает в файл-txt 
        self.save_to_txt_from_list()







#проверка на число 
def try_int(value):
    try:
        your_num = int(value)
        return True
    except Exception as e:
        print('---------------------')
        print('Вы ввели не число')
        print('---------------------')
        return False



#проверка на корректный год
def try_year(value):
        try:
            year = int(value)
            if year <= 2024:
                return True
            else:
                print('----------------------------------------------------')
                print("Пожалуйста, введите год, который не превышает 2024")
                print('----------------------------------------------------')
                return False
        except ValueError:
            print("Введено не число! Пожалуйста, введите корректный год")
            return False
        


#проверка, что такое число есть в списке
def try_int_which_num(value):
    possible_num = range(1, 7)
    try:
        your_num = int(value)
        if your_num in possible_num:
            return True
        else:
            print('--------------------------------')
            print('Нужно ввести число от 1 до 6')
            print('--------------------------------')
            return False
    except Exception as e:
        print('Нужно ввести число от 1 до 6')
        return False





def which_operration():
    ''' создает пользовательское меню '''

    whats_the_operation = input('Какую операцию вы хотели бы выполнить?: \n'
                                '1. Добавить книгу в библиотеку \n'
                                '2. Удалить книгу из библиотеки \n'
                                '3. Найти книгу в библиотеке \n'
                                '4. Показать список книг \n'
                                '5. Изменить статус книги (в наличилии или выдана) \n'
                                '6. Выйти из меню \n'
                                'Выберете номер 1, 2, 3, 4, 5 или 6: \n')
    return whats_the_operation







def start_program():
    ''' запуск программы '''

    #вызываю экземпляр класса
    library1 = Library() 

    #прогамма работает пока пользователь не решит выйти
    while True:
        preferred_operation = which_operration()

        # проверяю число ли ввел пользователь
        check_int_num = try_int_which_num(preferred_operation)
        while check_int_num == False:
            preferred_operation = which_operration()
            check_int_num = try_int_which_num(preferred_operation)


        add_book = '1'
        del_book = '2'
        search_book = '3'
        show_list_of_book = '4'
        change_status_of_book = '5'
        exit_menu = '6'


        if preferred_operation == add_book:
            ''' добавляет новую книгу '''
            
            # очищает терминал
            clear = lambda: os.system('cls')
            clear()

            #запрашивает данные от пользователя
            your_title = input('Введите название книги: ')
            your_author = input('Введите автора книги: ')
            your_year = input('Введите год издания книги, который не превышает 2024 год: ')

            #проеряет ввел ли пользователь корректный год
            check_int = try_year(your_year)
            while check_int == False:
                your_year = input('Введите год издания книги, который не превышает 2024 год: ')
                check_int = try_year(your_year)

            #вызывает метод через экземпляр класса, передает в метод аргументы 
            library1.add_book(your_title, your_author, your_year)

            print('-----------------------------------------')
            print('Книга добавлена')
            print('-----------------------------------------')





        if preferred_operation == del_book:
            ''' удаляет книгу из бибилиотеки '''
            
            # очищает терминал
            clear = lambda: os.system('cls')
            clear()

            # показывает список книг
            library1.show_list_of_books()

            # делает проверку есть ли в библиотеке книги
            if len(library1.list_of_book) > 0: 

                #спрашивает, книгу по какому id пользователь хочет удалить
                to_del = input('Книгу под каким id вы хотите удалить: \n')

                # проверка на число
                check_int = try_int(to_del)
                while check_int == False:
                    to_del = input('Книгу под каким id вы хотите удалить: \n')
                    check_int = try_int(to_del)

                #проверка есть ли такой id книги в списке
                #создает тумблер для проверки, есть ли id в списке. если нет, то после цикла пишет, что книги нет
                is_have_id = False
                for elem in library1.list_of_book:
                    #берет каждый список из списка списков и проверяет, есть ли такой id 
                    #конвертируе to_del в int поскольку elem[0] - это число, а to_del изначально строка
                    if elem[0] == int(to_del):
                        # ставит тумблер, когда такой id в списке есть и книга удалилась
                        is_have_id = True 
                        library1.del_book(to_del)
                        print('-----------------------------------------')
                        print('Книга удалена')
                        print('-----------------------------------------')
                        
                # пишет пользователю, если книги с таким id нет
                if is_have_id == False:
                    print('-----------------------------------------')
                    print(f'Книги с id {to_del} в библиотеке нет')
                    print('-----------------------------------------')
 
            else:
                # пишет пользователю, если книг в библиотеке вообще нет 
                print('-----------------------------------------')
                print('Книг в библиотеке нет')
                print('-----------------------------------------')



 
        if preferred_operation == search_book:
            ''' поиск книги в бибилиотеке '''
            
            # очищает терминал
            clear = lambda: os.system('cls')
            clear()

            # показывает список книг
            library1.show_list_of_books()

            # если в библиотеке есть книги, спрашивает параметры поиска 
            if len(library1.list_of_book) > 0: 

                # просит пользователя ввести параметр поиска title, author или year
                whats_parameter = input('По какому из парамеров вы хотите найти книгу (title, author или year)?: \n')

                #просит ввести значение поиска
                whats_search = input('Введите значение поиска: \n')

                #если значение поиска - год. делает проверку
                if whats_parameter == 'year':
                    check_year = try_year(whats_search)
                    while check_year == False:
                        whats_search = input('Введите значение поиска: ')
                        check_year = try_int(whats_search)

                    #вызывает метод через экземпляр класса, передает в метод аргументы 
                    print('-----------------------------------------')
                    library1.search_the_book(whats_parameter, whats_search)
                    print('-----------------------------------------')    

                elif whats_parameter == 'author':
                    print('-----------------------------------------')
                    library1.search_the_book(whats_parameter, whats_search)
                    print('-----------------------------------------')

                elif whats_parameter == 'title':
                    print('-----------------------------------------')
                    library1.search_the_book(whats_parameter, whats_search)
                    print('-----------------------------------------')
            else:
                # пишет пользователю, если книг вообще нет 
                print('-----------------------------------------')
                print('Книг в библиотеке нет')
                print('-----------------------------------------')
                    
                    




        if preferred_operation == show_list_of_book:
            ''' показывает список книги '''
            
            # очищает терминал
            clear = lambda: os.system('cls')
            clear()
            #вызывает метод через экземпляр класса
            print('-----------------------------------------')
            library1.show_list_of_books()        
            print('-----------------------------------------')





        if preferred_operation == change_status_of_book:
            ''' меняет  статус книге по id '''
            
            # очищает терминал
            clear = lambda: os.system('cls')
            clear()

            #показывает пользователю весь список книг 
            library1.show_list_of_books()

            if len(library1.list_of_book) > 0: 

                #спрашивает у пользователя, книге по какому id он хочет изменить статус
                whats_id = input('У книги, по какому id вы хотите изменить статус? : \n')

                # проверка на число
                check_int = try_int(whats_id)
                while check_int == False:
                    whats_id = input('У книги, по какому id вы хотите изменить статус? : \n')
                    check_int = try_int(whats_id)

                #проверка, есть ли такой id книги в списке 
                for elem in library1.list_of_book:
                    #берет каждый список из списка списков и проверяет есть ли такой id 
                    #конвертирует whats_id в int поcкольку elem[0] - это число, а whats_id изначально строка
                    if elem[0] == int(whats_id):

                        #спрашивает у пользователя, какой новый статус он хочет задать книге
                        whats_status = input('Какой статус вы хотите задать книге (в наличии или выдана)? : \n')
                        while not whats_status in ['в наличии','выдана']:
                            print('Введите значение статуса правильно')
                            whats_status = input('Какой статус вы хотите задать книге (в наличии или выдана)? : \n')

                        #вызывает метод через экземпляр класса, передает в метод аргументы 
                        print('-----------------------------------------')
                        library1.new_status_of_the_book(whats_id, whats_status)
                        print('-----------------------------------------')
            else:
                #пишет пользователю, если книг вообще нет 
                print('-----------------------------------------')
                print('Книг в библиотеке нет')
                print('-----------------------------------------')



        if preferred_operation == exit_menu:
            ''' выход из меню  '''
            
            # очищает терминал
            clear = lambda: os.system('cls')
            clear()

            print('-----------------------------------------')
            print('До новых встреч!')  
            print('-----------------------------------------')
            break
    

start_program()     


