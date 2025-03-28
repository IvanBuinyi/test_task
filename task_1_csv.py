import sqlite3
import pandas as pd

csv_file = "test_files/2017.csv"

df = pd.read_csv(csv_file)

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

df.to_sql("dog", conn, if_exists="replace", index=False)

query = "SELECT distinct lower(trim(Breed)) as Breed FROM dog"
result_1_1 = pd.read_sql(query, conn)

print(result_1_1)

result_1_1.to_csv("test_files/test_task_1_1.csv", index=False)

query = ("SELECT lower(trim(Breed)) as Breed, LicenseType, count(*) as number FROM dog group by lower(trim(Breed)), LicenseType order by 1, 2 ")
result_1_2 = pd.read_sql(query, conn)

print(result_1_2)

result_1_2.to_csv("test_files/test_task_1_2.csv", index=False)

query = ("SELECT lower(trim(DogName)) as DogName, count(*) as cnt FROM dog group by lower(trim(DogName)) order by 2 desc limit 5 ")
result_1_3 = pd.read_sql(query, conn)

print(result_1_3)

result_1_3.to_csv("test_files/test_task_1_3.csv", index=False)

conn.close()
