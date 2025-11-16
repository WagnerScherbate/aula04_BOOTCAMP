import csv


def ler_arquivo_csv(caminho_do_arquivo: str) -> None:
    arquivo_csv: list = []

    with open (file=caminho_do_arquivo, mode="r", encoding="utf-8") as arquivo:
        leitor_csv = csv.DictReader(arquivo)
    for linha in leitor_csv:
        arquivo_csv.append(linha)

    return arquivo_csv

arquivo = ler_arquivo_csv(r"E:\jornadadedados\aula04_BOOTCAMP\exemplo.csv")
print(arquivo)

