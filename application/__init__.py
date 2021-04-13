from flask import Flask
import os
from application.model.entity.video import Video
from application.model.entity.categoria import Categoria
from application.model.dao.categoria_dao import CategoriaDAO

app = Flask(__name__, static_folder=os.path.abspath('application/view/static'), template_folder=os.path.abspath('application/view/templates'))

"""
categorias = CategoriaDAO()

video1 = Video()
video1.setId(1)
video1.setTitle("You Say")
video1.setVideo("{{url_for('static', filename='video/you-say.mp4')}}")
video1.setCapa("{{url_for('static', filename='image/categoria_musica.png')}}")
video1.setDescription("By Lauren Daigle")
video1.setLikes("421")
video1.setViews("1202")
video1.setDate("12/04/2021")
 
video2 = Video()
video2.setId(2)
video2.setTitle("Enough")
video2.setVideo("{{url_for('static', filename='video/enough.mp4')}}")
video2.setCapa("{{url_for('static', filename='image/categoria_musica.png')}}")
video2.setDescription("By Koryn Hawthorne")
video2.setLikes("320")
video2.setViews("932")
video2.setDate("12/04/2021")
 
video3 = Video()
video3.setId(3)
video3.setTitle("Além do Rio Azul")
video3.setVideo("{{url_for('static', filename='video/alem-do-rio-azul.mp4')}}")
video3.setCapa("{{url_for('static', filename='image/categoria_musica.png')}}")
video3.setDescription("Cover by Júlia Vitória")
video3.setLikes("470")
video3.setViews("522")
video3.setDate("12/04/2021")

idMusica = 1
titleCategory1 = "Músicas"
description1 = "O melhor som para você!"
capa1 = "{{url_for('static', filename='image/categoria_musica.png')}}"
musicas = [video1, video2, video3]
primeira_categoria = Categoria(idMusica, titleCategory1, description1, capa1)
primeira_categoria.setVideo(musicas)
 
categorias.inserir(primeira_categoria)
 
video4 = Video()
video4.setId(4)
video4.setTitle("Zootopia")
video4.setVideo("{{url_for('static', filename='video/zootopia.mp4')}}")
video4.setCapa("{{url_for('static', filename='image/categoria_musica.png')}}")
video4.setDescription("Zootopia é uma cidade diferente de tudo o que você já viu. Formada por “bairros-habitat”, como a elegante Praça Sahara  e a gelada Tundralândia, essa metrópole abriga uma grande diversidade de animais irreverentes sempre prontos para encarar uma nova e divertida aventura.")
video4.setLikes("453")
video4.setViews("900")
video4.setDate("12/04/2021")
 
video5 = Video()
video5.setId(5)
video5.setTitle("Detona Ralph - Wifi Ralph")
video5.setVideo("{{url_for('static', filename='video/detona-ralph.mp4')}}")
video5.setCapa("{{url_for('static', filename='image/categoria_musica.png')}}")
video5.setDescription("Embarque nessa aventura emocionante!")
video5.setLikes("864")
video5.setViews("912")
video5.setDate("12/04/2021")
 
video6 = Video()
video6.setId(6)
video6.setTitle("Desafiando Gigantes")
video6.setVideo("{{url_for('static', filename='video/desafiando-gigantes.mp4')}}")
video6.setCapa("{{url_for('static', filename='image/categoria_musica.png')}}")
video6.setDescription("Cultivando Valores - União Comprometer-se com o único propósito, reconhecendo que precisamos uns dos outros para entregar tudo com excelência")
video6.setLikes("640")
video6.setViews("1000")
video6.setDate("12/04/2021")
 
idFilme = 2
titleCategory2 = "Filme"
description2 = "O melhor do cinema para você!"
capa2 = "{{url_for('static', filename='image/categoria_filme.png')}}"
filmes = [video4, video5, video6]
segunda_categoria = Categoria(idFilme, titleCategory2, description2, capa2)
 
categorias.inserir(segunda_categoria)
 
video7 = Video()
video7.setId(7)
video7.setTitle("Mr Sunshine")
video7.setVideo("{{url_for('static', filename='video/mr-sunshine.mp4')}}")
video7.setCapa("{{url_for('static', filename='image/categoria_musica.png')}}")
video7.setDescription("Miseuteo Syeonsyain é uma série de televisão sul-coreana exibida pela emissora tvN entre 7 de julho a 30 de setembro de 2018, com um total de 24 episódios, a série também estreou internacionalmente pela plataforma Netflix.")
video7.setLikes("940")
video7.setViews("1320")
video7.setDate("12/04/2021")
 
video8 = Video()
video8.setId(8)
video8.setTitle("Pousando no Amor")
video8.setVideo("{{url_for('static', filename='video/pousando-no-amor.mp4')}}")
video8.setCapa("{{url_for('static', filename='image/categoria_musica.png')}}")
video8.setDescription("O drama é sobre uma herdeira rica chamada Yoon Se Ri, que, enquanto voava de parapente, é forçada a aterrissar na Coreia do Norte por causa dos ventos fortes. Um oficial norte-coreano chamado Ri Jung Hyuk a esconde e protege, assim, começando a amá-la")
video8.setLikes("649")
video8.setViews("1500")
video8.setDate("12/04/2021")
 
video9 = Video()
video9.setId(9)
video9.setTitle("Descendentes do Sol")
video9.setVideo("{{url_for('static', filename='video/descendentes-do-sol.mp4')}}")
video9.setCapa("{{url_for('static', filename='image/categoria_musica.png')}}")
video9.setDescription("O capitão Yoo Shi Jin das forças especiais se apaixona pela cirurgiã Kang Mo Yeon. Os dois lutam para viver um romance em meio a um país devastado pela guerra.")
video9.setLikes("989")
video9.setViews("1520")
video9.setDate("12/04/2021")
 
idDrama = 3
titleCategory3 = "Drama"
description3 = "Para você se divertir e se emocionar!"
capa3 = "{{url_for('static', filename='image/categoria_drama.png')}}"
dramas = [video7, video8, video9]
 
terceira_categoria = Categoria(idDrama, titleCategory3, description3, capa3)
 
 
categorias.inserir(terceira_categoria)
"""

from application.controller import home_controller
from application.controller import video_controller