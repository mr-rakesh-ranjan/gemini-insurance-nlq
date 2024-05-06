from static.generate_sql import generate_SQL_2_NL
from static.filter_SQL import parse_runable_query
from run_sql import execute_query_df_no_json, execute_query_df
# geting output from db

def getting_data_from_db(user_input):
    gen_sql = generate_SQL_2_NL(user_prompt=user_input)
    run_sql = parse_runable_query(gen_sql=gen_sql)
    # print(execute_query_df(run_sql))
    return execute_query_df(run_sql)
    

res = getting_data_from_db("List all policies and their effective dates whose Account number=10001")

# print(type(res))
print(res)