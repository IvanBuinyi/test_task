import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# database setup
DATABASE_URL = "sqlite:///etl_database.db"  # change to your DB
engine = create_engine(DATABASE_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# tables description
class Department(Base):
    __tablename__ = 'departments'
    department_id = Column(Integer, primary_key=True)
    name = Column(String)

class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    date_of_birth = Column(Date)
    salary = Column(Float)
    department_id = Column(Integer)

# tables creating
Base.metadata.create_all(engine)

# Extract data from CSV
csv_file = "test_files/emp.csv"  # change to your file
df = pd.read_csv(csv_file, encoding="utf-8")
print("headers in CSV:", df.columns.tolist())
# Data transformation
df.columns = df.columns.str.strip()  # removing spaces

#df['id'] = df['id'].astype(int)
df['name'] = df['name'].str.strip()
df['date_of_birth'] = pd.to_datetime(df['date_of_birth'], format='%d.%m.%Y', dayfirst=True).dt.date
df['salary'] = df['salary'].astype(float)
df['department_id'] = df['department_id'].astype(int)

#load data to employees
df.to_sql('employees', engine, if_exists='append', index=False)

# query = "SELECT * FROM employees"
# df_employees = pd.read_sql(query, engine)
#
# print(df_employees)

# creating departments table with unique department_id and name
# !!!!!! in the task not mentioned department_name so it is strange to take name looks like from employee !!!!!!
unique_departments = df[['department_id', 'name']].drop_duplicates()

# load to departments
unique_departments.to_sql('departments', engine, if_exists='append', index=False)

# query2 = "SELECT * FROM departments"
# df_departments = pd.read_sql(query2, engine)
#
# print(df_departments)

print("ETL completed!")