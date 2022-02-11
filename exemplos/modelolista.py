

import numpy as np
import random
import time
from datetime import datetime
from kafka import KafkaProducer
import pandas as pd
from pyspark.sql.functions import year, month
import json
import boto3
import datetime
from io import BytesIO
from email import message
from calendar import month_name
from pyspark.sql import SparkSession
from pyspark.sql.types import ArrayType, StructField, StructType, StringType, IntegerType
from pyspark.context import SparkContext
import sys
# from awsglue.transforms import *
# from awsglue.utils import getResolvedOptions
# from pyspark.context import SparkContext
# from awsglue.context import GlueContext
# from awsglue.job import Job

# sc.stop()

# @params: [JOB_NAME]
# args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext('local')
spark = SparkSession(sc)

# Create a schema in dataframe
schema = StructType([
    StructField('cnpj', StringType(), True),
    StructField('data_contratacao', StringType(), True),
    StructField('data_pagamento', StringType(), True),
    StructField('valor_operacao', StringType(), True),
    StructField('data_vencimento', StringType(), True),
    StructField('quantidade_parcelas_pagas', StringType(), True),
    StructField('pontuacao', StringType(), True),
    StructField('data_pgto_ultima_parcela', StringType(), True),
    StructField('adimplente', StringType(), True),
    StructField('valor_pago', StringType(), True),
    StructField('df1', StringType(), True),

])

# connection to s3 per resource and per client, via boto3 in bucket_name
s3 = boto3.resource('s3')
bucket = s3.Bucket('imobiliario')
s3_client = boto3.client('s3')
s3_bucket_name = 'imobiliario'
my_bucket = s3.Bucket(s3_bucket_name)
bucket_list = []

# iterates through the files in the bucket
for file in my_bucket.objects.filter(Delimiter='/', Prefix='pastaprincipal/input/'):
    file_name = file.key
    if file_name.find(".json") != -1:
        bucket_list.append(file)

# put here your logical
newJson = []
for obj in bucket_list:
    body = obj.get()['Body'].read()
    resp = json.loads(body)
    valor_pago = 0
    e_pagamento_nao_pactuado = 1
    for parcelas in resp['pagamentos']:
        if parcelas["codigo_pagamento"] == "LIQUIDACAO ANTECIPADA":
            continue
        parcela_valor = float(parcelas['valor_pagamento'])
        data_pagamento = parcelas['data_pagamento']
        valor_pago += parcela_valor
        data_pagamento = parcelas['data_pagamento']
        e_pagamento_nao_pactuado = parcelas['e_pagamento_nao_pactuado']
        if e_pagamento_nao_pactuado != 'false':
            print('desconsidera esse json e vai pro proximo!!!')
            e_pagamento_nao_pactuado = 1
            break

    if e_pagamento_nao_pactuado != 1:
        cnpj = resp['cnpj_empresa']
        valor_operacao = resp['valor_operacao']
        data_contratacao = resp['data_contratacao']
        data_vencimento = resp['data_vencimento']
        quantidade_parcelas_pagas = resp['quantidade_parcelas_pagas']
        pontuacao = 0

        # analisar a ultima parcela!!
        data_vericar = data_pagamento.split('T')[0]
        data_vericar = [int(add) for add in data_vericar.split('-')]

        data_vericar = datetime.datetime(
            data_vericar[0], data_vericar[2], data_vericar[1])

        year = datetime.datetime.now().year
        day = datetime.datetime.now().day
        month = datetime.datetime.now().month

        dia_hoje = datetime.datetime(year, month, day)
        print('cnpj', cnpj)
        print('data_pagamento', data_pagamento)
        print('dia_hoje', dia_hoje)
        print('data_vericar', data_vericar)
        print('data_vericar == dia_hoje', data_vericar == dia_hoje)

        ano = ""
        if data_vericar != dia_hoje:
            pontuacao = 1.5
            print('se a data for outro dia - desconsiderar!!!')

            newJson.append({
                "cnpj": f"{cnpj}",
                "valor_operacao": f"{valor_operacao}",
                "data_contratacao": f"{data_contratacao}",
                "data_vencimento": f"{data_vencimento}",
                "quantidade_parcelas_pagas": f"{quantidade_parcelas_pagas}",
                "pontuacao": f"{pontuacao}",
                "adimplente": "True",
                "data_pgto_ultima_parcela": f"{data_pagamento}",
                "valor_pago": f"{valor_pago}",
                "df1": f"{ano}"

            }
            )


# Create data frame
sc = SparkContext.getOrCreate('local')

# pip install kafka-python

KAFKA_TOPIC_NAME_CONS = "topicoimobi"
KAFKA_BOOTSTRAP_SERVERS_CONS = 'localhost:9092'

print("Kafka Producer Application Started ... ")

kafka_producer_obj = KafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS_CONS,
                                   value_serializer=lambda x: x.encode('utf-8'))


for message in df.collect():

    message_fields_value_list = []

    message_fields_value_list.append(message["cnpj"])
    message_fields_value_list.append(message["valor_operacao"])
    message_fields_value_list.append(message["data_contratacao"])
    message_fields_value_list.append(message["data_vencimento"])
    message_fields_value_list.append(message["quantidade_parcelas_pagas"])
    message_fields_value_list.append(message["pontuacao"])
    message_fields_value_list.append(message["adimplente"])
    message_fields_value_list.append(message["data_pgto_ultima_parcela"])
    message_fields_value_list.append(message["valor_pago"])
    message_fields_value_list.append(message["df1"])

    print(message_fields_value_list)

    message = ','.join(str(v) for v in message_fields_value_list)
    print("Message Type: ", type(message))
    print("Message: ", message)
    kafka_producer_obj.send(KAFKA_TOPIC_NAME_CONS, message)
    time.sleep(1)


print("Kafka Producer Application Completed. ")

# ////////---------------------------

#dyf = DynamicFrame.fromDF(dataframe=df, glue_ctx=glueContext, name="dyf")


# ---------------------
# IN AWS CONSOLE UNCOMMENT, IT WIL PERSISTS IN DATABAS
# convert to dynamic frame, save it to the bucket, and everything in it is automatically saved to the table because it is mapped in aws (see ddl.sql)
# from awsglue.dynamicframe import DynamicFrame
# dif = DynamicFrame.fromDF(df, glueContext, "test_nest")
# print(type(dif))
# dif.show()
