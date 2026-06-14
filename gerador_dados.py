import pandas as pd
import random
from faker import Faker
fake = Faker('pt_BR')
tipos_ocorrencia = [
    'Perturbação do Sossego', 'Apoio Comunitário', 
    'Averiguação de Atitude Suspeita', 'Ronda Preventiva', 
    'Mediação de Conflitos'
]
bairros = ['Messejana', 'Aldeota', 'Centro', 'Bom Jardim', 'Benfica', 'Parangaba']
status = ['Resolvido', 'Em Andamento', 'Pendente']

dados = []
for _ in range(500):
    dados.append({
        'Protocolo': fake.unique.random_number(digits=6),
        'Data': fake.date_between(start_date='-30d', end_date='today'),
        'Tipo_Ocorrencia': random.choice(tipos_ocorrencia),
        'Bairro': random.choice(bairros),
        'Status': random.choice(status)
    })
df = pd.DataFrame(dados)
df.to_csv('dados_defesa_social.csv', index=False)

print("Arquivo 'dados_defesa_social.csv' gerado com sucesso!")