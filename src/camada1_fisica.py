class CamadaFisica:
    def processar(self, dados):
        print("[1] Física: transmitindo bits pelo meio físico")
        binario = ' '.join(format(byte, '08b') for byte in dados)
        return binario
