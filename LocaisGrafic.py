"""
- Perguntar ao usuário localização que vai viajar
- Verificar na lista da região e sortear um estado
- Apresentar ao usuário essa localização
"""
from random import choice
from PySimpleGUI import PySimpleGUI as sg

norte = ['Acre', 'Amapá', 'Amazonas', 'Pará', 'Rondônia', 'Roraima', 'Tocantins']

sul = ['Paraná', 'Santa Catarina', 'Rio Grande do Sul']

nordeste = ['Bahia', 'Alagoas', 'Rio grande do Norte', 'Pernambuco', 'Paraíba', 'Ceará', 'Sergipe', 'Piauí']

sudeste = ['Minas Gerais', 'Espirito Santo', 'São Paulo', 'Rio de Janeiro']

CentroOeste = ['Mato Grosso do Sul', 'Goiania', 'Mato Grosso']

class apresentandoEstados:
    def __init__(self):
        sg.theme('LightGrey')
        layout = [
            [sg.Text('Para onde você deseja viajar? ')],
            [sg.Radio('Norte', 1, key='norte'), sg.Radio('Sul', 1, key='sul'), sg.Radio('Centro Oeste', 1, key='centro'), sg.Radio('Sudeste', 1, key='sudeste'), sg.Radio('Nordeste', 1, key='nordeste')],
            [sg.Text(' '*40), sg.Button('Start')],
            [sg.Output(size=(54, 3), )]
        ]

        self.janela = sg.Window('Sua viagem perfeita!', layout)

    def cidade(self):
        while True:
            evento, valores = self.janela.read()
            self.norte = valores['norte']
            self.sul = valores['sul']
            self.centroOeste = valores['centro']
            self.sudeste = valores['sudeste']
            self.nordeste = valores['nordeste']
            if evento == sg.WINDOW_CLOSED:
                break
            if evento == 'Start':
                cidade = self.randomCity()
                print(' ')
                print(cidade)
                

    def randomCity(self):
        if self.norte == True:
            randomNorte = choice(norte)
            return randomNorte
        if self.centroOeste == True:
            randomCentro = choice(CentroOeste)
            return randomCentro
        if self.sul == True:
            randomSul = choice(sul)
            return randomSul
        if self.sudeste == True:
            randomSudeste = choice(sudeste)
            return randomSudeste
        if self.nordeste == True:
            randomNordeste = choice(nordeste)
            return randomNordeste

localização = apresentandoEstados()
localização.cidade()