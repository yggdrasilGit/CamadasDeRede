from src.camada2_enlace import CamadaEnlace


class CamadaRede:
    def __init__(self, ip_origem: str, ip_destino: str):
        self.ip_origem = ip_origem
        self.ip_destino = ip_destino
        self.camada_enlace = CamadaEnlace()

    def encapsular(self, dados: str) -> str:
        cabecalho = f"{self.ip_origem}->{self.ip_destino}"
        pacote = f"{cabecalho}|{dados}"
        print(f"[Rede] Pacote encapsulado: {pacote}")
        return pacote

    def rotear(self, pacote: str):
        print(f"[Rede] Roteando para enlace: {pacote}")
        self.camada_enlace.transmitir(pacote)

    def receber(self) -> str:
        dados = self.camada_enlace.receber()
        if dados:
            print(f"[Rede] Pacote recebido: {dados}")
            return dados
        return None
