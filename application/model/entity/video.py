class Video:
    def __init__(self, id, title, urlVideo, capa, description, date, category):
        self._id = id
        self._title = title
        self._urlVideo = urlVideo
        self._capa = capa
        self._description = description
        self._date = date
        self._category = category
        self._views = None
        self._likes = None

    def getId(self):
        return self._id
    
    def setId(self, id):
        self._id = id

    def getTitle(self):
        return self._title
    
    def setTitle(self, title):
        self._title = title

    def getUrlVideo(self):
        return self._urlVideo

    def setUrlVideo(self, urlVideo):
        self._urlVideo = urlVideo
    
    def getCapa(self):
        return self._capa
    
    def setCapa(self, capa):
        self._capa = capa

    def getDescription(self):
        return self._description

    def setDescription(self, description):
        self._description = description

    def getDate(self):
        return self._date

    def setDate(self, date):
        self._date = date

    def getCategory(self):
        return self._category 

    def setCategory(self, category):
        self._category = category
    
    def getViews(self):
        if self._views != None:
            return self._views
        else:
            return 'Ainda não há visualizações neste vídeo.'

    def setViews(self, views):
        self._views = views

    def getLikes(self):
        if self._likes != None:
            return self._likes
        else:
            return 'Ainda não há likes neste vídeo.'

    def setLikes(self, likes):
        self._likes = likes