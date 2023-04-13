class person: 
    id_person = 0 
    person_type = ''
    name = '' # full name
    document = '' # identification number
    entrance = '' # date
    exit_ = '' # date
    early_exit = '' # three options

    def  __init__(self,id_person, name, document, person_type ): 
        self.id_person = id_person
        self.name = name
        self.document = document
        self.person_type = person_type

