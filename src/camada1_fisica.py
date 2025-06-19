class CamadaFisica:
    def __init__(self):
        self.meio_transmissao = []

    def codificar_binario(self, dados: str) -> str:
        binario = ''.join(format(ord(c), '08b') for c in dados)
        print(f"[Física] Codificando para binário: {binario}")
        return binario

    def transmitir(self, bits: str):
        self.meio_transmissao = list(bits)
        print(f"[Física] Transmitindo bits pelo meio: {''.join(self.meio_transmissao)}")

    def receber(self) -> str:
        if not self.meio_transmissao:
            print("[Física] Nenhum dado recebido.")
            return None
        bits_recebidos = ''.join(self.meio_transmissao)
        caracteres = [chr(int(bits_recebidos[i:i+8], 2)) for i in range(0, len(bits_recebidos), 8)]
        texto = ''.join(caracteres)
        print(f"[Física] Recebido e decodificado: {texto}")
        return texto
