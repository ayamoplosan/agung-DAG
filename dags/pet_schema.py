create_pet_table = PostgresOperator(
    task_id="create_pet_table",
    postgres_conn_id="postgres_default",
    sql="pet_schema.sql",
)
populate_pet_table = PostgresOperator(
    task_id="populate_pet_table",
    postgres_conn_id="postgres_default",
    sql="pet_schema.sql",
)
get_all_pets = PostgresOperator(
    task_id="get_all_pets",
    postgres_conn_id="postgres_default",
    sql="SELECT * FROM pet;",
)