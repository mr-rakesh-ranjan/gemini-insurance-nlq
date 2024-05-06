# from static.generate_sql import generate_SQL_2_NL #for debugging only

# for debugging only
# gen_sql = generate_SQL_2_NL("List all policies for Account number=10000 and their effective dates")
# print(gen_sql)

def parse_runable_query(gen_sql):
    # finding the position of '```' and removing the '```' and the newlines
    start = gen_sql.find("```") + len("```\n")
    # finding position of ending '```' and removing the '```'
    end = gen_sql.rfind("```")
    # apply strip method on input_string
    out_string = gen_sql[start:end].strip()
    # print(f"OUTPUT STRING {out_string}") # for debugging only
    return out_string