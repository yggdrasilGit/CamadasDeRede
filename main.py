

from src.camada3_rede import CamadaRede
from src.camada4_transporte import CamadaTransporte
from src.camada5_sessao import CamadaSessao
from src.camada6_apresentacao import CamadaApresentacao


def main():
    # Camada de Apresentação
    camada_apresentacao = CamadaApresentacao()

    # Camada de Sessão
    camada_sessao = CamadaSessao(session_id="sessaoABC")
    camada_apresentacao.camada_sessao = camada_sessao

    # Camada de Transporte
    camada_transporte = CamadaTransporte(porta_origem=1234, porta_destino=80)
    camada_sessao.camada_transporte = camada_transporte

    # Camada de Rede
    camada_rede = CamadaRede(ip_origem="192.168.1.1", ip_destino="192.168.1.2")
    camada_transporte.camada_rede = camada_rede

    # Enlace está dentro da Rede, com Física embutida

    camada_sessao.iniciar_sessao()

    mensagem = "Olá, camada de apresentação!"
    print("\n=== TRANSMISSÃO ===")
    camada_apresentacao.transmitir(mensagem)

    print("\n=== RECEPÇÃO ===")
    dados_recebidos = camada_apresentacao.receber()

    camada_sessao.encerrar_sessao()

    print(f"\n[Aplicação] Dados recebidos: {dados_recebidos}")






if __name__ == "__main__":
    main()
