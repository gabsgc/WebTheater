from typing import List

class Video:
    _id: int
    _title: str
    _video: str
    _capa: str
    _description: str
    _date: str
    _views: int
    _likes: int
 
    def __init__(self):
        self._id = None
        self._title = None
        self._video = None
        self._capa = None
        self._date = None
        self._likes = None
        self._views = None
 
    def getId(self) -> int:
        return self._id
    
    def setId(self, id: int) -> None:
        self._id = id
 
    def getTitle(self) -> str:
        return self._title
    
    def setTitle(self, title: str) -> None:
        self._title = title
 
    def getVideo(self) -> str:
        return self._video
 
    def setVideo(self, video: str) -> None:
        self._video = video
    
    def getCapa(self) -> str:
        return self._capa
    
    def setCapa(self, capa: str) -> None:
        self._capa = capa
 
    def getDescription(self) -> str:
        return self._description
 
    def setDescription(self, description: str) -> None:
        self._description = description
 
    def getDate(self) -> int:
        return self._date
 
    def setDate(self, date: int) -> None:
        self._date = date
    
    def getViews(self) -> int:
        if self._views != None:
            return self._views
        else:
            return 'Ainda não há visualizações neste vídeo.'
 
    def setViews(self, views: int) -> None:
        self._views = views
 
    def getLikes(self) -> int:
        if self._likes != None:
            return self._likes
        else:
            return 'Ainda não há likes neste vídeo.'
 
    def setLikes(self, likes: int) -> None:
        self._likes = likes
 
    def toDict(self):
        return {
            'id': self.getId(),
            'video': self.getVideo(),
            'capa': self.getCapa(),
            'title': self.getTitle(),
            'description': self.getDescription(),
            'date': self.getDate(),
            'views': self.getViews(),
            'likes': self.getLikes()
        }
