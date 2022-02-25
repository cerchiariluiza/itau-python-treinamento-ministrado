CREATE EXTERNAL TABLE `coostumers`(
  `customerid` bigint, 
  `customername` string, 
  `email` string, 
  `city` string, 
  `country` string, 
  `territory` string, 
  `contactfirstname` string, 
  `contactlastname` string)
ROW FORMAT DELIMITED 
  FIELDS TERMINATED BY ',' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://recebeevento/costumers/customers.csv'
TBLPROPERTIES (
  'CrawlerSchemaDeserializerVersion'='1.0', 
  'CrawlerSchemaSerializerVersion'='1.0', 
  'UPDATED_BY_CRAWLER'='crow', 
  'areColumnsQuoted'='false', 
  'averageRecordSize'='78', 
  'classification'='csv', 
  'columnsOrdered'='true', 
  'compressionType'='none', 
  'delimiter'=',', 
  'objectCount'='2', 
  'recordCount'='83', 
  'sizeKey'='6569', 
  'skip.header.line.count'='1', 
  'transient_lastDdlTime'='1645762964', 
  'typeOfData'='file')
