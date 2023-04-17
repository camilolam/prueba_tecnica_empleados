class person: 
    id_person = 0 
    name = '' # full name
    document = '' # identification number
    id_type = 0
    id_area = 0
    state = '' # into the company or out the company
    

    def  __init__(self,id_person, name, document, id_type, id_area): 
        self.id_person = id_person
        self.name = name
        self.document = document
        self.id_type = id_type
        self.id_area = id_area

