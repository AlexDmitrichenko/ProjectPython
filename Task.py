import json
from datetime import datetime

notes = []
path = "tasks/notes.json"

def loadNotes():
    global notes
    try:
        with open(path, 'r') as f:
            notes = json.load(f)
    except FileNotFoundError:
        pass

def saveNotes():
    with open(path, 'w') as f:
        json.dump(notes, f)

def addNote():
    title = input('Введите заголовок заметки: ')
    body = input('Введите текст заметки: ')
    createdAt = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
    noteId = 1
    for note in notes:
        if note["id"] == noteId:
            note_id += 1
    note = {'id': noteId, 'title': title, 'body': body, 'createdAt': createdAt, 'updatedAt': createdAt}
    notes.append(note)
    
    notes.sort(key= lambda x: x['id'])
    
    saveNotes()
    print('Заметка добавлена!')

def viewNotes():
    for note in notes:
        print(f"ID: {note['id']}, Заголовок: {note['title']}, Текст: {note['body']}, Создано: {note['createdAt']}, Обновлено: {note['updatedAt']}")
    if not notes:
        print('Заметок нет')

def editNote():
    noteId = int(input('Введите ID заметки, которую хотите отредактировать: '))
    for note in notes:
        if note['id'] == noteId:
            note['title'] = input('Введите новый заголовок заметки: ')
            note['body'] = input('Введите новый текст заметки: ')
            note['updatedAt'] = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
            saveNotes()
            print('Заметка отредактирована!')
            break
    else:
        print('Заметка не найдена')

def deleteNote():
    noteId = int(input('Введите ID заметки, которую хотите удалить: '))
    for note in notes:
        if note['id'] == noteId:
            notes.remove(note)
            saveNotes()
            print('Заметка удалена!')
            break
    else:
        print('Заметка не найдена')

loadNotes()

while True:
    print('\nМеню:')
    print('1. Просмотр заметок')
    print('2. Добавление заметки')
    print('3. Редактирование заметки')
    print('4. Удаление заметки')
    print('5. Выход')
    choice = input('\nВыберите пункт меню: ')
    print()
    if choice == '1':
        viewNotes()
    elif choice == '2':
        addNote()
    elif choice == '3':
        editNote()
    elif choice == '4':
        deleteNote()
    elif choice == '5':
        break
    else:
        print('Неверный пункт меню')