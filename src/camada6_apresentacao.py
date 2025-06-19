import base64

class Rede:
    class CamadaFisica:
        def __init__(self):
            self.dados_recebidos = None

        def codificar(self, dados: str) -> str:
            """Codifica os dados em binário"""
            return ''.join(format(ord(c), '08b') for c in dados)

        def decodificar(self, bits: str) -> str:
            """Decodifica os dados binários para string"""
            caracteres = [chr(int(bits[i:i + 8], 2)) for i in range(0, len(bits), 8)]
            return ''.join(caracteres)

        def transmitir(self, dados: str):
            """Transmite os dados para a camada física, codificando para binário"""
            dados_binarios = self.codificar(dados)
            print(f"[Física] Codificando para binário: {dados_binarios}")
            print(f"[Física] Transmitindo bits pelo meio: {dados_binarios}")
            self.dados_recebidos = dados_binarios

        def receber(self):
            """Recebe e decodifica os dados"""
            if self.dados_recebidos:
                print(f"[Física] Recebido e decodificado: {self.dados_recebidos}")
                return self.decodificar(self.dados_recebidos)
            return None

    class CamadaEnlace:
        def __init__(self, camada_fisica):
            self.camada_fisica = camada_fisica

        def encapsular(self, dados: str) -> str:
            """Encapsula os dados no formato do enlace"""
            trailer = "0"  # Suponha que o trailer é sempre zero
            pacote_enlace = f"HEADER|{dados}|{trailer}"
            print(f"[Enlace] Dados encapsulados: {pacote_enlace}")
            return pacote_enlace

        def transmitir(self, dados: str):
            """Transmite os dados para a camada de física"""
            pacote_enlace = self.encapsular(dados)
            self.camada_fisica.transmitir(pacote_enlace)

        def receber(self) -> str:
            """Recebe os dados do enlace"""
            pacote = self.camada_fisica.receber() if self.camada_fisica else None
            if pacote:
                print(f"[Enlace] Pacote recebido: {pacote}")
                return pacote
            return None

    class CamadaRede:
        def __init__(self, ip_origem: str, ip_destino: str, camada_enlace):
            self.ip_origem = ip_origem
            self.ip_destino = ip_destino
            self.camada_enlace = camada_enlace

        def encapsular(self, dados: str) -> str:
            """Encapsula os dados com o endereço IP"""
            pacote_rede = f"{self.ip_origem}->{self.ip_destino}|{dados}"
            print(f"[Rede] Pacote encapsulado: {pacote_rede}")
            return pacote_rede

        def roteamento(self, pacote: str):
            """Roteia o pacote para a camada de enlace"""
            print(f"[Rede] Roteando para enlace: {pacote}")
            self.camada_enlace.transmitir(pacote)

        def receber(self) -> str:
            """Recebe o pacote da camada de enlace"""
            pacote = self.camada_enlace.receber() if self.camada_enlace else None
            if pacote:
                print(f"[Rede] Pacote recebido: {pacote}")
                return pacote
            return None

    class CamadaTransporte:
        def __init__(self, porta_origem: int, porta_destino: int, camada_rede):
            self.porta_origem = porta_origem
            self.porta_destino = porta_destino
            self.camada_rede = camada_rede

        def encapsular(self, dados: str) -> str:
            """Encapsula os dados com o cabeçalho da porta"""
            cabecalho = f"{self.porta_origem}:{self.porta_destino}"
            segmento = f"{cabecalho}|{dados}"
            print(f"[Transporte] Segmento criado: {segmento}")
            return segmento

        def transmitir(self, dados: str):
            """Transmite os dados para a camada de rede"""
            segmento = self.encapsular(dados)
            pacote = self.camada_rede.encapsular(segmento)
            self.camada_rede.roteamento(pacote)

        def receber(self) -> str:
            """Recebe os dados da camada de rede"""
            pacote = self.camada_rede.receber() if self.camada_rede else None
            if pacote:
                partes = pacote.split('|', 1)
                if len(partes) == 2:
                    cabecalho, dados = partes
                    print(f"[Transporte] Segmento recebido: {cabecalho} | Dados: {dados}")
                    return dados
            return None

    class CamadaSessao:
        def __init__(self, session_id: str, camada_transporte):
            self.session_id = session_id
            self.camada_transporte = camada_transporte

        def iniciar_sessao(self):
            """Inicia a sessão"""
            print(f"[Sessão] Sessão '{self.session_id}' iniciada.")

        def encapsular(self, dados: str) -> str:
            """Encapsula os dados com o ID da sessão"""
            pacote = f"{self.session_id}|{dados}"
            print(f"[Sessão] Dados com sessão: {pacote}")
            return pacote

        def transmitir(self, dados: str):
            """Transmite os dados para a camada de transporte"""
            pacote = self.encapsular(dados)
            self.camada_transporte.transmitir(pacote)

        def receber(self) -> str:
            """Recebe os dados da camada de transporte"""
            dados = self.camada_transporte.receber()
            if dados:
                print(f"[Sessão] Dados recebidos: {dados}")
                return dados
            return None

        def encerrar_sessao(self):
            """Encerra a sessão"""
            print(f"[Sessão] Sessão '{self.session_id}' encerrada.")

    class CamadaApresentacao:
        def __init__(self, camada_sessao):
            self.camada_sessao = camada_sessao

        def codificar(self, dados: str) -> str:
            """Codifica os dados em base64"""
            codificado = base64.b64encode(dados.encode()).decode()
            print(f"[Apresentação] Dados codificados (base64): {codificado}")
            return codificado

        def transmitir(self, dados: str):
            """Transmite os dados codificados para a camada de sessão"""
            dados_codificados = self.codificar(dados)
            self.camada_sessao.transmitir(dados_codificados)

        def receber(self) -> str:
            """Recebe e decodifica os dados"""
            if self.camada_sessao:
                return self.camada_sessao.receber()
            return None

# Função Principal (Interativa)
def main():
    # Criando as camadas dentro da classe Rede
    camada_fisica = Rede.CamadaFisica()
    camada_enlace = Rede.CamadaEnlace(camada_fisica)
    camada_rede = Rede.CamadaRede(ip_origem="192.168.1.1", ip_destino="192.168.1.2", camada_enlace=camada_enlace)
    camada_transporte = Rede.CamadaTransporte(porta_origem=1234, porta_destino=80, camada_rede=camada_rede)
    camada_sessao = Rede.CamadaSessao(session_id="sessaoABC", camada_transporte=camada_transporte)
    camada_apresentacao = Rede.CamadaApresentacao(camada_sessao)

    # Iniciar sessão
    camada_sessao.iniciar_sessao()

    while True:
        # Solicitar entrada de dados do usuário
        mensagem = input("\nDigite sua mensagem (ou 'sair' para encerrar): ")
        
        if mensagem.lower() == 'sair':
            # Se o usuário digitar "sair", encerramos a sessão e saímos do loop
            camada_sessao.encerrar_sessao()
            print("[Aplicação] Sessão encerrada. Até logo!")
            break

        # Enviar dados (passo a passo)
        input("\nPressione Enter para enviar para a Camada de Apresentação...")
        camada_apresentacao.transmitir(mensagem)

        input("\nPressione Enter para enviar para a Camada de Sessão...")
        camada_sessao.transmitir(mensagem)

        input("\nPressione Enter para enviar para a Camada de Transporte...")
        camada_transporte.transmitir(mensagem)

        input("\nPressione Enter para enviar para a Camada de Rede...")
        camada_rede.roteamento(camada_rede.encapsular(mensagem))

        input("\nPressione Enter para enviar para a Camada de Enlace...")
        camada_enlace.transmitir(mensagem)

        input("\nPressione Enter para enviar para a Camada Física...")
        camada_fisica.transmitir(mensagem)

        input("\nPressione Enter para concluir a recepção...")
        camada_fisica.receber()
        camada_enlace.receber()
        camada_rede.receber()
        camada_transporte.receber()
        camada_sessao.receber()

# Rodar o script
if __name__ == "__main__":
    main()
