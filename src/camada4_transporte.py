class CamadaTransporte:
    def __init__(self, porta_origem: int, porta_destino: int):
        self.porta_origem = porta_origem
        self.porta_destino = porta_destino
        self.camada_rede = None  # conectar depois

    def encapsular(self, dados: str) -> str:
        cabecalho = f"{self.porta_origem}:{self.porta_destino}"
        segmento = f"{cabecalho}|{dados}"
        print(f"[Transporte] Segmento criado: {segmento}")
        return segmento

    def transmitir(self, dados: str):
        segmento = self.encapsular(dados)
        if self.camada_rede:
            pacote = self.camada_rede.encapsular(segmento)
            self.camada_rede.rotear(pacote)
        else:
            print("[Transporte] Camada de rede não conectada.")

    def receber(self) -> str:
        pacote = self.camada_rede.receber() if self.camada_rede else None
        if pacote:
            partes = pacote.split('|', 1)
            if len(partes) == 2:
                cabecalho, dados = partes
                print(f"[Transporte] Segmento recebido: {cabecalho} | Dados: {dados}")
                return dados
        return None
