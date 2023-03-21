from model import NotesDatabase
import datetime

now = datetime.datetime.now()

methods = NotesDatabase()

while True:
    print("Нажмите 1, чтобы создать заметку   \n  Нажмите 2, чтобы обновить заметку \n Нажмите 3, чтобы удалить заметку  \n Нажмите 4 чтобы прочитать заметки \n  Нажмите 5 для выхода")
    try:
        number = int(input('Введите номер : '))
        if number == 1:
            id = int(input('Введите номер заметки : '))

            notes_name = input('Введите название заметки : ')
            notes_subject = input('Введите тему заметки : ')
            notes_content = input('Введите содержание заметки : ')
            time = now.strftime("%d-%m-%Y %H:%M")
            methods.createNote(id, notes_name, notes_subject, notes_content, time)
        elif number == 2:
            id = int(input('Введите номер заметки для редактирования : '))

            methods.updateNotes(id)
        elif number == 3:
            id = int(input('Введите номер заметки : '))
            methods.deleteNotes(id)
        elif number == 4:
            methods.showAllNotes()
        elif number == 5:
            break
    except Exception as e:
            print(e)