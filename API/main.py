# Imports
from flask import Flask, jsonify, request
from sqlalchemy import create_engine, text
from flask_restx import Api, Namespace, Resource, reqparse, inputs, fields
import pandas as pd
import json
import os

# Create an app with Flask
app = Flask(__name__)

# Connect to the Google Cloud mySQL database
db_host = os.environ.get("MySQL_db_host")
db_user = os.environ.get("MySQL_db_user")
db_pass = os.environ.get("MySQL_db_pass")
db_name = os.environ.get("MySQL_db_name")

# Function to connect to the Google Cloud MySQL database
def connect():
    db = create_engine(
    'mysql+pymysql://{0}:{1}@{2}/{3}' \
        .format(db_user, db_pass, db_host, db_name), \
    connect_args = {'connect_timeout': 10})
    conn = db.connect()
    return conn

def disconnect(conn):
    conn.close()

# Create an API for our application
api = Api(app, version='1.0',
    title = 'KPIs H&M Retail Capstone Project',
    description = 'Set of JSON endpoint to get insightful data from the \'articles\', \'customers\' and \'transactions\' datasets',
    contact = 'nborgato2022@student.ie.edu',
    endpoint = '/api/v1'
)

# Create a namespace to group all the resources and routes related to customers
customers = Namespace('customers',
    description = 'All operations related to customers')
api.add_namespace(customers)

# Create an API to retrieve all the customers
@customers.route('/customers')
class get_all_users(Resource):
    def get(self):

            conn = connect()
            query = text("""
                SELECT *
                FROM customers
                LIMIT 1000
            """)
            result = conn.execute(query).fetchall()
            disconnect(conn)
            features = ["id", "customer_id",  "Active", "FN", "club_member_status", "fashion_news_frequency", "age", "postal_code"]
            data = [dict(zip(features, row)) for row in result]
            return jsonify({'result': data})


# Create a namespace to group all the resources and routes related to articles
articles = Namespace('articles',
    description = 'All operations related to articles')
api.add_namespace(articles)

# Create an API to retrieve all the articles
@articles.route('/articles')
class get_all_articles(Resource):
    def get(self):
            conn = connect()
            query = text("""
                SELECT *
                FROM articles
                LIMIT 1000
            """)
            result = conn.execute(query).fetchall()
            disconnect(conn)
            features = ["id","article_id","product_code","prod_name","product_type_no","product_type_name","product_group_name","graphical_appearance_no","graphical_appearance_name","colour_group_code","colour_group_name","perceived_colour_value_id","perceived_colour_value_name","perceived_colour_master_id","perceived_colour_master_name","department_no","department_name","index_code","index_name","index_group_no","index_group_name","section_no","section_name","garment_group_no","garment_group_name","detail_desc"]
            data = [dict(zip(features, row)) for row in result]
            return jsonify({'result': data})

# Create a namespace to group all the resources and routes related to transactions
transactions = Namespace('transactions',
    description = 'All operations related to transactions')
api.add_namespace(transactions)

# Create an API to retrieve data from the transactions
@transactions.route('/transactions')
class all_transactions(Resource):
    @api.response(404, "article not found")
    def get(self):
            conn = connect()
            query = text("""
                SELECT *
                FROM sampletransactions
                LIMIT 1000
            """)
            result = conn.execute(query).fetchall()
            disconnect(conn)
            features = ["index", "t_dat",  "customer_id", "article_id", "price", "sales_channel_id"]
            data = [dict(zip(features, row)) for row in result]
            return jsonify({'result': data})


# Create a namespace for retrieving the data all together
alldata = Namespace('alldata',
    description = 'The three datasets all together')
api.add_namespace(alldata)

# Create an API to retrieve all the data together
@alldata.route('/alldata')
class all_data(Resource):
    @api.response(404, "article not found")
    def get(self):
            conn = connect()
            query = text("""
                SELECT *
                FROM alldata
                LIMIT 1000
            """)
            result = conn.execute(query).fetchall()
            disconnect(conn)
            features = [
                "index",
                "t_dat",
                "customer_id",
                "article_id",
                "price",
                "sales_channel_id",
                "FN",
                "Active",
                "club_member_status",
                "fashion_news_frequency",
                "age",
                "postal_code",
                "product_code",
                "prod_name",
                "product_type_no",
                "product_type_name",
                "product_group_name",
                "graphical_appearance_no",
                "graphical_appearance_name",
                "colour_group_code",
                "colour_group_name",
                "perceived_colour_value_id",
                "perceived_colour_value_name",
                "perceived_colour_master_id",
                "perceived_colour_master_name",
                "department_no",
                "department_name",
                "index_code",
                "index_name",
                "index_group_no",
                "index_group_name",
                "section_no",
                "section_name",
                "garment_group_no",
                "garment_group_name",
                "detail_desc"
                ]
            data = [dict(zip(features, row)) for row in result]
            return jsonify({'result': data})

# Run the app
if __name__ == '__main__':
    app.run(
        host = '0.0.0.0', 
        port = 8080,
        debug = True)