import qrcode

# Função para gerar o QR code a partir de um link
def gerar_qr_code(link, nome_arquivo):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=6,
    )
    qr.add_data(link)
    qr.make(fit=True)

    qr_code = qr.make_image(fill_color="black", back_color="white")
    qr_code.save(nome_arquivo)

if __name__ == "__main__":
    # Digitando o link 
    link_acesso = input("Digite o link que deseja converter em um QR code: ")
    # Dando nome ao Arquivo 
    nome_do_arquivo = input("De um nome ao seu Arquivo (por exemplo, 'meu_Qr_Code.png'): ")

    gerar_qr_code(link_acesso, nome_do_arquivo)
    print(f"QR code gerado e salvo como {nome_do_arquivo}")