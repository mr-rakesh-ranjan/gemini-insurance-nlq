import replicate # type: ignore
from dotenv import load_dotenv # type: ignore
from SQL_prompt import sql_prompt
from pathlib import Path
import os

# load .env and replicate token
env_path = Path('.', '.env')
load_dotenv(dotenv_path=env_path)
replicate_token = os.getenv('REPLICATE_API_TOKEN')

# configure  the replicate with its token
replicate = replicate.Client(api_token=replicate_token)

# for debugging only
user_prompt = "List all policies for Account number=10000 and their effective dates"

def generate_SQL_2_NL(user_prompt) -> str:
    input ={
        "prompt": f" {sql_prompt} Work through this problem step by step: \n\nQ: , {user_prompt} ?",
        "prompt_template": "<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\nYou are a helpful assistant<|eot_id|><|start_header_id|>user<|end_header_id|>\n\n{prompt}<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n"
    }
    temp : str = ""
    # for event in replicate.run(
    #     "meta/meta-llama-3-70b-instruct",
    #     input=input
    # ):
    #     print(event, end="")
    #     temp.join(event)
        
    res = replicate.run(
        "meta/meta-llama-3-70b-instruct",
        input=input
    )
    
    temp = ''.join([str(element) for element in res])
    # print(temp)
    return temp

# print(generate_SQL_2_NL(user_prompt=user_prompt))

    
