import turtle
import pandas
from unidecode import unidecode

estados_adivinhados = []

# configurando a tela
screen = turtle.Screen()
screen.title("Estados brasileiros")
imagem = "mapa_brasil.gif"
screen.addshape(imagem)
turtle.shape(imagem)
nome = turtle.Turtle()

# exibindo os nomes dos estados no mapa
nome.hideturtle()
nome.penup()

# carregando dados
data = pandas.read_csv("estados_brasileiros.csv")
estados = data.estado.to_list()

# encontrando as coordenadas do mouse na tela:
def clique(x,y):
    print (x,y)

turtle.onscreenclick(clique)

while len(estados_adivinhados) < 26:
    tentativa = screen.textinput(f"{len(estados_adivinhados)}/26 estados corretos", prompt="Adivinhe os estados brasileiros:")
    if tentativa == "Sair":
        estados_nao_adivinhados = []
        for estado in estados:
            if estado not in estados_adivinhados:
                estados_nao_adivinhados.append(estado)
        df = pandas.DataFrame(estados_nao_adivinhados)
        df.to_csv("estados_faltantes.csv")
        break
        
    # removendo acentos e caracteres especiais
    tentativa_normalizada = unidecode(tentativa).lower()
    estados_normalizados = []

    for estado in estados:
        estado_normalizado = unidecode(estado).lower()
        estados_normalizados.append(estado_normalizado)

    if tentativa_normalizada in estados_normalizados:
        estados_adivinhados.append(tentativa)
        indice_estado = estados_normalizados.index(tentativa_normalizada)
        estado_original = estados[indice_estado]
        dados_estado = data[data.estado == estado_original]

    if len(dados_estado) == 1: # garantindo que há apenas 1 linha
        x_coor = dados_estado.x.item()
        y_coor = dados_estado.y.item()
        nome.goto(x_coor, y_coor)
        nome.write(estado_original)

screen.mainloop()