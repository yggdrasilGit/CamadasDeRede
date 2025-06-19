class CamadaSessao:
    def __init__(self, session_id: str):
        self.session_id = session_id
        self.camada_transporte = None

    def iniciar_sessao(self):
        print(f"[Sessão] Sessão '{self.session_id}' iniciada.")

    def encapsular(self, dados: str) -> str:
        # A sessão vem primeiro, depois os dados
        pacote = f"{self.session_id}|{dados}"
        print(f"[Sessão] Dados com sessão: {pacote}")
        return pacote

    def transmitir(self, dados: str):
        if not self.camada_transporte:
            print("[Sessão] Camada de transporte não conectada.")
            return
        pacote = self.encapsular(dados)
        self.camada_transporte.transmitir(pacote)

    def receber(self) -> str:
        dados = self.camada_transporte.receber() if self.camada_transporte else None
        if dados:
            # Separando os dados corretamente
            partes = dados.split('|', 1)
            if len(partes) == 2:
                session_id, payload = partes
                if session_id == self.session_id:
                    print(f"[Sessão] Sessão válida '{session_id}'. Dados: {payload}")
                    return payload
                else:
                    print(f"[Sessão] Sessão inválida: {session_id}")
        return None

    def encerrar_sessao(self):
        print(f"[Sessão] Sessão '{self.session_id}' encerrada.")
