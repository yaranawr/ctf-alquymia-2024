import pandas as pd

df = pd.read_parquet('5640483420244_vpcflowlogs.log.parquet')

df_validos = df[df['srcaddr'] != "-"]
ip_origem_mais_frequente = df_validos['srcaddr'].value_counts().idxmax()
frequencia_ip_origem = df_validos['srcaddr'].value_counts().max()
ips_destino_na_rede = df[df['dstaddr'].str.startswith('10.0.0.')]['dstaddr'].nunique()
tcp_count = df[df['protocol'] == 6.0].shape[0]

print(f"IP de Origem mais frequente: {ip_origem_mais_frequente} com {frequencia_ip_origem} ocorrências")

print(f"Quantidade de pacotes TCP: {tcp_count}")

print(f"Quantidade de IPs de destino na rede 10.0.0.0/24: {ips_destino_na_rede}")

# print(df)