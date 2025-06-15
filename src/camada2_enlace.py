class CamadaEnlace:
    def processar(self, dados):
        print("[2] Enlace: adicionando endereço MAC")
        return b"[MAC origem: AA:BB:CC:DD:EE:FF | destino: FF:EE:DD:CC:BB:AA]" + dados
