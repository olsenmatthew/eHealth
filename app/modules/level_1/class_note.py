from app.modules.level_0.class_system import *

class Note:

    def __init__(self, notesID, provider, patient, time_view, epoch_time, body):
        self.notesID = notesID
        self.provider = provider
        self.patient = patient
        self.time_view = time_view
        self.epoch_time = epoch_time
        self.body = body
    
    def set_note(self):
        system = System
        dict_notes = system.get_notes()
        for key in dict_notes:
            if self.notesID == key:
                dict_notes[key] = self
                system.set_notes(dict_notes)
        dict_notes.update({self.notesID:self})
        system.set_notes(dict_notes)
    
    def delete_note(self):
        system = System
        dict_notes = system.get_notes()
        for key in dict_notes:
            if self.notesID == key:
                del dict_notes[key]
                break 
        system.set_notes(dict_notes)
    
    def __lt__(self, other):
        return self.epoch_time > other.epoch_time
        
