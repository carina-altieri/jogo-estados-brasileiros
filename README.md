# Estados brasileiros - jogo Interativo

## Descrição do Projeto
Este é um jogo interativo desenvolvido em Python que desafia os jogadores a adivinhar todos os estados brasileiros. O jogador insere o nome dos estados e, ao acertar, o nome do estado é exibido na posição correta em um mapa do Brasil. Caso o jogador desista, é gerado um arquivo CSV com os estados que não foram adivinhados.

## Funcionalidades
* Visualizar um mapa do Brasil.
* Inserir nomes de estados brasileiros.
* Exibir os estados acertados no mapa, em suas respectivas coordenadas.
* Gerar um arquivo estados_faltantes.csv com os estados que não foram adivinhados.
* Capturar coordenadas do mouse no mapa para facilitar a configuração.

## Estrutura do projeto
```bash
📦 estados-brasileiros-jogo
 ┣ 📜 mapa_brasil.gif            # Imagem do mapa do Brasil
 ┣ 📜 estados_brasileiros.csv    # Arquivo com os estados e suas respectivas coordenadas
 ┣ 📜 estados_faltantes.csv      # Arquivo gerado ao sair do jogo (estados não adivinhados)
 ┣ 📜 main.py                    # Código principal do jogo
 ┗ 📜 README.md                  # Este arquivo
````

## Tecnologias Utilizadas
Python:
* turtle para criar a interface gráfica e exibir o mapa.
* pandas para manipular os dados dos estados e gerar arquivos CSV.
* unidecode para normalizar strings, removendo acentos e caracteres especiais.

## Pré-requisitos
Certifique-se de ter o seguinte instalado:

* Python 3.7 ou superior
* As bibliotecas listadas no arquivo requirements.txt

**Para instalar as bibliotecas:**
```bash
pip install -r requirements.txt
```

## Como Jogar
Execute o programa:
```bash
python main.py
```
1. Insira o nome de um estado brasileiro na caixa de texto que aparece.
2. Se acertar, o nome do estado será exibido no mapa na posição correta.
3. Digite "Sair" para encerrar o jogo e gerar o arquivo estados_faltantes.csv.

## Como o Jogo Funciona
* O jogo carrega os nomes dos estados brasileiros e suas coordenadas de um arquivo CSV (estados_brasileiros.csv).
* Quando o jogador digita:
  *  o nome de um estado o nome é normalizado (removendo acentos e caracteres especiais).
  * Se o estado estiver correto, ele é adicionado à lista de estados acertados e exibido no mapa.
* Ao encerrar o jogo, os estados não adivinhados são salvos em um arquivo CSV.

## Possíveis Melhorias
* Incluir um cronômetro para tornar o jogo mais desafiador.
* Melhorar a interface gráfica com botões e dicas visuais.

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.


