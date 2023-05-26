# circle-area
Exercício para nível iniciante ou intermediário de Python

A ideia deste exercício é apresentar o conceito de simulação estatística para cálcular a área de uma circunferência gerando números aleatórios a partir de uma distribuição de probabilidade Uniforme.

## Setup

Para executar os códigos é necessário instalar algumas bibliotecas, como: `numpy`, `pandas`, `matplotlib`. Para isso, basta executar o código abaixo com seu ambiente Python ativo:

```bash
$ pip install -r requirements.txt
```

## Organização do código

```
circle-area
├── area_circulo.py
├── area_cli.py
├── LICENSE
├── README.md
└── requirements.txt
```

`area_circulo.py` -> foi criado em live e sua gravação se encontra no canal do [CodeShow](colocar o link aqui).

`area_cli.py` -> Mesmo em live, utilizando os conceitos apresensatos, geramos um novo arquivo que pode ser utilizado para gerar diferentes cenários do mesmo problema. Isto é, circunferências e quantidade de amostras diferentes. Para brincar com este script, faça uso se seus parâmetros:

```bash
$ python area_cli.py --help
usage: area_cli.py [-h] [--diametro DIAMETRO] [--samples SAMPLES] [--plot]

options:
  -h, --help            show this help message and exit
  --diametro DIAMETRO, -d DIAMETRO
  --samples SAMPLES, -s SAMPLES
  --plot, -p
```