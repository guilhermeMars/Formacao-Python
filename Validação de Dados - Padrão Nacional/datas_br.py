from datetime import datetime, timedelta

class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        # strftime - Transforma em uma string os dias (perde todos os métodos), logo é utilizado só no final da exibição
        return self.momento_cadastro.strftime("%d/%m/%Y %H:%M")

    def mes_cadastro(self):
        meses_ano = [
            "janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
        ]
        mes_cadastro = self.momento_cadastro.month - 1
        return meses_ano[mes_cadastro]

    def dia_semana(self):
        dias_semana = [
            "segunda", "terça", "quarta", "quinta", "sexta", "sabado", "domingo"
        ]
        dia_semana = self.momento_cadastro.weekday()
        return dias_semana[dia_semana]
    
    def tempo_cadastro(self):
        tempo_cadastro = (datetime.today() + timedelta(days=30)) - self.momento_cadastro
        return tempo_cadastro
    