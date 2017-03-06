import uuid

class Project:
    __id = None
    __name = None
    __description = None
    __start_date = None
    __end_date = None

    def __init__(self, name, description, start_date, end_date):
        self.__id = uuid.uuid4()
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def description(self):
        return self.__description

    @name.setter
    def description(self, value):
        self.__description = value

    @property
    def start_date(self):
        return self.__start_date

    @name.setter
    def start_date(self, value):
        self._start_date = value

    @property
    def end_date(self):
        return self.__end_date

    @name.setter
    def end_date(self, value):
        self.__end_date = value

    def serialize(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "description" : self.description,
            "start_date" : self.start_date,
            "end_date" : self.end_date
        }