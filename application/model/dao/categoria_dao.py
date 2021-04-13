from application.model.entity.categoria import Categoria
from application.model.entity.video import Video
import os
from typing import List

class CategoriaDAO():
    """
    def inserir(self, categoria) -> None:
        categoria_list = self.listarTodos()
        categoria.setId(len(categoria_list) + 1)
        categoria_list.append(categoria)
        dict_list = self.converterToDictlist(categoria_list)
 
    def listarTodos(self) -> List[Categoria]:
        resultado = []
        resultado = self.converterToCategoriaList(categoria_list)
        return resultado
 
    def converterToDictlist(self, categoria_list: List[Categoria]) -> List:
        resultado = []
        for categoria in categoria_list:
            resultado.append(categoria.toDict())
        return resultado
 
    def buscarPorId(self, categoria_id: int) -> Categoria:
        for categoria in self.converterToCategoriaList(categoria_list):
            if categoria.getId() == categoriaId:
                return categoria
 
    def converterToCategoriaList(self, categoria_list: List) -> List[Categoria]:
        resultado = []
        for categoria_dict in categoria_list:
            categoria = Categoria()
            categoria.setId(categoria_dict['id'])
            categoria.setTitle(categoria_dict['title'])
            categoria.setCapa(categoria_dict['capa'])
            categoria.setDescription(categoria_dict['description'])
            video_list = []
            for video_dict in categoria_dict['videos']:
                video = Video()
                video.setId(video_dict['id'])
                video.setVideo(video_dict['video'])
                video.setTitle(video_dict['title'])
                video.setDescription(video_dict['description'])
                video.setDate(video_dict['date'])
                video.setLikes(video_dict['likes'])
                video.setViews(video_dict['views'])
            categoria.setVideo(video_list)
            resultado.append(categoria)
        return resultado
    """