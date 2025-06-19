from src.camada1_fisica import CamadaFisica


class CamadaEnlace:
    def __init__(self):
        self.camada_fisica = CamadaFisica()

    def encapsular(self, dados: str) -> str:
        cabecalho = "HEADER"
        trailer = self.calcular_paridade(dados)
        pacote = f"{cabecalho}|{dados}|{trailer}"
        print(f"[Enlace] Dados encapsulados: {pacote}")
        return pacote

    def calcular_paridade(self, dados: str) -> str:
        binario = ''.join(format(ord(c), '08b') for c in dados)
        return '1' if binario.count('1') % 2 != 0 else '0'

    def transmitir(self, dados: str):
        pacote = self.encapsular(dados)
        partes = pacote.split('|')
        dados_extraidos = '|'.join(partes[1:-1])
        dados_binarios = self.camada_fisica.codificar_binario(dados_extraidos)
        print(f"[Enlace] Transmitindo para a camada física: {dados_binarios}")
        self.camada_fisica.transmitir(dados_binarios)

    def verificar_erro(self, dados: str) -> bool:
        paridade = self.calcular_paridade(dados)
        print(f"[Enlace] Trailer calculado: {paridade}")
        return True  # simplificado

    def receber(self) -> str:
        dados_recebidos = self.camada_fisica.receber()
        if dados_recebidos and self.verificar_erro(dados_recebidos):
            return dados_recebidos
        return None
