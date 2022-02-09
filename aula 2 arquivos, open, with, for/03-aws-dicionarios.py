
# String em formato JSON
print(
'''

 .----------------.  .----------------.  .----------------.  .-----------------.   .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. |  | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |     _____    | || |    _______   | || |     ____     | || | ____  _____  | |  | |   _____      | || |     ____     | || |      __      | || |  ________    | || |    _______   | |
| |    |_   _|   | || |   /  ___  |  | || |   .'    `.   | || ||_   \|_   _| | |  | |  |_   _|     | || |   .'    `.   | || |     /  \     | || | |_   ___ `.  | || |   /  ___  |  | |
| |      | |     | || |  |  (__ \_|  | || |  /  .--.  \  | || |  |   \ | |   | |  | |    | |       | || |  /  .--.  \  | || |    / /\ \    | || |   | |   `. \ | || |  |  (__ \_|  | |
| |   _  | |     | || |   '.___`-.   | || |  | |    | |  | || |  | |\ \| |   | |  | |    | |   _   | || |  | |    | |  | || |   / ____ \   | || |   | |    | | | || |   '.___`-.   | |
| |  | |_' |     | || |  |`\____) |  | || |  \  `--'  /  | || | _| |_\   |_  | |  | |   _| |__/ |  | || |  \  `--'  /  | || | _/ /    \ \_ | || |  _| |___.' / | || |  |`\____) |  | |
| |  `.___.'     | || |  |_______.'  | || |   `.____.'   | || ||_____|\____| | |  | |  |________|  | || |   `.____.'   | || ||____|  |____|| || | |________.'  | || |  |_______.'  | |
| |              | || |              | || |              | || |              | |  | |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' |  | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'    '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 

''')

import json
clientes =  """
{
	"porte": "medio",
	"rendimento": "25",
	"tipos": ["alimenticio", "energia", "tecnologia"],
	"dados_cliente": {
		"name": "Julia LTDA",
		"phone": "117777-2347",
		"email": "email@email.com"
	}
}
"""


print("o tipo de clientes é : >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(type(clientes))
input( "tecle para continuar \n")


# Converter a string em JSON em um dicionário
clientes_dict = json.loads(clientes)
print("o tipo de clientes dict é : >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(type(clientes_dict))
input( "tecle para continuar \n")

print("print por casa : >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(clientes_dict["porte"])
print(clientes_dict["rendimento"])
print(clientes_dict["tipos"][0])
print(clientes_dict["dados_cliente"]['name'])
input( "tecle para continuar \n")

print("listando as chaves >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
for chave in clientes_dict.keys():
    print(chave)
print("listando os valores >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
for values in clientes_dict.values():
    print(values)
input( "tecle para continuar \n")

print("listando as chaves  e valores >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> \n")
from time import sleep
sleep(10)

for chave, valor in clientes_dict.items():
    print(chave,valor)
input("end dict ")


print(
'''


 .----------------.  .----------------.  .----------------.  .----------------.    .----------------.    .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. |  | .--------------. |  | .--------------. || .--------------. || .--------------. || .--------------. |
| |   _____      | || |     ____     | || |      __      | || |  ________    | |  | |              | |  | |  _________   | || |     _____    | || |   _____      | || |  _________   | |
| |  |_   _|     | || |   .'    `.   | || |     /  \     | || | |_   ___ `.  | |  | |              | |  | | |_   ___  |  | || |    |_   _|   | || |  |_   _|     | || | |_   ___  |  | |
| |    | |       | || |  /  .--.  \  | || |    / /\ \    | || |   | |   `. \ | |  | |    ______    | |  | |   | |_  \_|  | || |      | |     | || |    | |       | || |   | |_  \_|  | |
| |    | |   _   | || |  | |    | |  | || |   / ____ \   | || |   | |    | | | |  | |   |______|   | |  | |   |  _|      | || |      | |     | || |    | |   _   | || |   |  _|  _   | |
| |   _| |__/ |  | || |  \  `--'  /  | || | _/ /    \ \_ | || |  _| |___.' / | |  | |              | |  | |  _| |_       | || |     _| |_    | || |   _| |__/ |  | || |  _| |___/ |  | |
| |  |________|  | || |   `.____.'   | || ||____|  |____|| || | |________.'  | |  | |              | |  | | |_____|      | || |    |_____|   | || |  |________|  | || | |_________|  | |
| |              | || |              | || |              | || |              | |  | |              | |  | |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' |  | '--------------' |  | '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'    '----------------'    '----------------'  '----------------'  '----------------'  '----------------' 

''')


# Abrir o arquivo orders.json
with open("exemplo.json") as file:
    # Carregar seu conteúdo e torná-lo um novo dicionário
    data = json.load(file)

    # Excluir o par chave-valor "client" de cada pedido
    for clientinho in data["clients"]:
        del clientinho["dadosCliente"]

# Abrir (ou criar) um arquivo orders_new.json 
# e armazenar a nova versão dos dados.
with open("exemplo_novo.json", 'w') as file:
    json.dump(data, file)

# import boto3
# client = boto3.client('s3')
# response = client.list_buckets()
# print(type(response))
# for bucket in response['Buckets']:
#     print(bucket['Name'])

# #Exemplo pratico de dicionarios:
# import boto3
# region = 'sa-east-1'
# ec2 = boto3.client('ec2', region_name=region)


# #função, listar e parar todos as instancias t2.micro de uma vez e salvar log num json
# def pegar():
#     print('Into DescribeEc2Instance')
#     instances = ec2.describe_instances(Filters=[{'Name': 'instance-type', 'Values': ["t2.micro", "t3.micro"]}])
#     for ins_id in instances['Reservations']:
#                 print(type(ins_id))
#                 print(ins_id)
#                 input("continue")
#                 print('----- \n')
# pegar()

	