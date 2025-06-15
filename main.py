

from src.camada1_fisica import CamadaFisica
from src.camada2_enlace import CamadaEnlace
from src.camada3_rede import CamadaRede
from src.camada4_transporte import CamadaTransporte
from src.camada5_sessao import CamadaSessao
from src.camada6_apresentacao import CamadaApresentacao
from src.camada7_aplicacao import CamadaAplicacao


if __name__ == "__main__":
    mensagem = "O"
    print("Mensagem original:", mensagem)

    dados = CamadaAplicacao().processar(mensagem)
    dados = CamadaApresentacao().processar(dados)
    dados = CamadaSessao().processar(dados)
    dados = CamadaTransporte().processar(dados)
    dados = CamadaRede().processar(dados)
    dados = CamadaEnlace().processar(dados)
    sinal = CamadaFisica().processar(dados)

    print("\nSinal transmitido:", sinal)
