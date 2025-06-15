class CamadaRede:
    def processar(self, dados):
        print("[3] Rede: adicionando endereço IP de origem e destino")
        return b"[IP origem: 192.168.0.1 | destino: 192.168.0.2]" + dados
