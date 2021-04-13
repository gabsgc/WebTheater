from typing import List
from application.model.entity.video import Video

class Categoria:
 
    def __init__(self, id, title, description, capa):
        self._id = id
        self._title = title
        self._description = description
        self._capa = capa
        self._video = None
 
    def setId(self, id:int) -> None:
        self._id = id
 
    def getId(self) -> int:
        return self._id
 
    def setTitle(self, title: str) -> None:
        self._title = title
    
    def getTitle(self) -> str:
        return self._title
 
    def setDescription(self, description: str) -> None:
        self._description = description
 
    def getDescription(self) -> str:
        return self._description
 
    def setCapa(self, capa: str) -> None:
        self._capa = capa
 
    def getCapa(self) -> str:
        return self._capa
 
    def getVideo(self) -> List[Video]:
        return self._video
 
    def setVideo(self, videos: List[Video]) -> None:
        self._video = videos
 
    def addVideo(self, video: Video) -> None:
        self._video.append(video)
 
    def toDict(self):
        videos = []
        for video in self._videos:
            videos.append(video.toDict())
        return {
            'id': self.getId(),
            'capa': self.getCapa(),
            'title': self.getTitle(),
            'description': self.getDescription(),
            'videos': self.getVideo(),
            'date': self.getDate(),
            'likes': self.getLikes(),
            'views': self.getViews()
        }
