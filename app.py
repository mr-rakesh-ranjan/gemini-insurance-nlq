

# flask APP
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin # type: ignore
from dotenv import load_dotenv, find_dotenv # type: ignore
from run_sql import execute_query_df
from static.generate_sql import generate_SQL_2_NL
from static.filter_SQL import parse_runable_query
import datetime as dt

# load .env and replicate token
load_dotenv(find_dotenv())

app = Flask(__name__)
cors = CORS(app=app)
app.config['CORS_HEADERS'] = 'Content-Type'

# for debugging only
@app.route('/', methods = ['GET', 'POST'])
def home():
    if(request.method == 'GET'):
        data = "Hello world"
        return jsonify({'data' : data})

# api for getting customer details
@app.route('/api/v1/get-customer-details/<accountNumber>', methods = ['GET'])
@cross_origin()
def getAccountDetails(accountNumber):
    query = f"SELECT * FROM [dbo].[customer] WHERE account_number = {int(accountNumber)} "
    res = execute_query_df(query)
    return res

# api for valid customer via DOB
def isValidCustomer(accountNumber, dob):
    if type(accountNumber) != int and type(dob) != dt.date:
        return TypeError("Account Number is ")
    pass

# api for getting policy details with there respective customer details
@app.route('/api/v1/getAll-policy-details/<accountNumber>', methods = ['GET','POST'])
@cross_origin()
def getAllPolicyDetails(accountNumber):
    if request.method == 'POST':
        request_data = request.get_json(force=True)
        print(request_data['customer_query']) # for debugging only
        requested_query = f"{request_data['customer_query']} whose Account number is {int(accountNumber)}"
        return generatingResponseLLM(requested_query)
    else:
        return jsonify({
            "Wroning" : "Please write a proper query!!!"
        })

# api for getting policy details with there policy number
# @app.route('/api/v1/get-policy-details/<accountNumber>/<policyNumber>', methods = ['GET'])
@app.route('/api/v1/get-policy-details')
@cross_origin
def getPolicyDetails(self):
    if request.method == 'GET':
        # query = f"SELECT * FROM [dbo].[PolicyDetails] WHERE PolicyNumber = {str(policyNumber)} and AccountNumber = {int(accountNumber)};"
        query = "SELECT * FROM [dbo].[PolicyDetails] WHERE PolicyNumber = 'mdy-3402747' and AccountNumber = 10001; "
        res = execute_query_df(query)
        return res


# method for generating response from AI assistant
def generatingResponseLLM(user_input):
    gen_sql = generate_SQL_2_NL(user_prompt=user_input)
    run_sql = parse_runable_query(gen_sql=gen_sql)
    # print(execute_query_df(run_sql))
    return execute_query_df(run_sql)
if __name__ == '__main__':
    app.run(debug = True)