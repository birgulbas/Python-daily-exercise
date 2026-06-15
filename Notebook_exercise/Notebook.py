class Notebook:
    def __init__(self):
        self.notes = [] #list for store notes

    def add_notes(self,note):
        self.notes.append(note)
        print("Note added successfully!")

    def show_notes(self):
        if not self.notes:
            print("Have no notes yet.")
        else:
            for x, note in enumerate(self.notes):
                print(f"{x+1}: {note}") #shows notes of index and allignment


    def delete_notes(self,index):
        if 0 <= index < len(self.notes): #check to find index
            deleted_note = self.notes.pop(index) #delete select one
            print(f"Deleted note: {deleted_note}")
        else:
            print("invalid index!")

    def update_note(self,index,new_note):
        if 0 <= index < len(self.notes):
            self.notes[index] = new_note #defined note change eith new one
            print(f"Note is updated. {new_note}")
        else:
            print("invalid index!")
