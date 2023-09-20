get_birth_date = PostgresOperator(
    task_id="get_birth_date",
    postgres_conn_id="postgres_default",
    sql="SELECT * FROM pet WHERE birth_date BETWEEN SYMMETRIC %(begin_date)s AND %(end_date)s",
    parameters={"begin_date": "2020-01-01", "end_date": "2020-12-31"},
)
-- dags/sql/birth_date.sql
SELECT * FROM pet WHERE birth_date BETWEEN SYMMETRIC {{ params.begin_date }} AND {{ params.end_date }}

get_birth_date = PostgresOperator(
    task_id="get_birth_date",
    postgres_conn_id="postgres_default",
    sql="sql/birth_date.sql",
    params={"begin_date": "2020-01-01", "end_date": "2020-12-31"},
)