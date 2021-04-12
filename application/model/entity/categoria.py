class Categoria:
    def __init__(self, id, title, description, capa):
        self._id = id
        self._title = title
        self._description = description
        self._capa = capa

    def setId(self, id):
        self._id = id

    def getId(self):
        return self._id

    def setTitle(self, title):
        self._title = title
    
    def getTitle(self):
        return self._title

    def setDescription(self, description):
        self._description = description

    def getDescription(self):
        return self._description

    def setCapa(self, capa):
        self._capa = capa

    def getCapa(self):
        return self._capa
