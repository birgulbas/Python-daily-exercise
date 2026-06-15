from Notebook import *

my_notebook=Notebook()  # create an instance


while True:
    print("\n*** Notebook Menu ***\n")
    print("*"*30)
    print("1. Add a Note")
    print("2. Show All Notes")
    print("3. Delete a Note")
    print("4. Update a Note")
    print("Q. Quit")
    print("*"*30)

    choice=input("Enter your choice: ")

    if choice=="1":
        note=input("Enter the note to add: ")
        my_notebook.add_notes(note)

    elif choice=="2":
        my_notebook.show_notes()

    elif choice=="3":
        my_notebook.show_notes()  # to see notes before deleting

        if my_notebook.notes:
            index=int(input("Enter the index of the note to delete: "))-1  # for lists starts from 0
            my_notebook.delete_note(index)
        else:
            print("No notes found!")

    elif choice=="4":
        my_notebook.show_notes()

        if my_notebook.notes:
            # GÖZDEN KAÇAN HATA DÜZELTİLDİ: Güncelleme yaparken de index'i int() yapıp 1 çıkarmalıyız!
            index=int(input("Enter the index of the note to update: "))-1
            new_note=input("Enter the new note to update: ")
            my_notebook.update_note(index,new_note)

        else:
            print("No notes found!")

    elif choice=="Q" or choice=="q":
        print("Exiting...")
        break

    else:
        print("invalid choice!")