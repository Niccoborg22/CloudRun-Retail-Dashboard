# REST API Documentation
---
This folder includes all the files used to build and deploy the REST API using Flask-RESTx for a web application that manages articles, transactions, customers, and alldata.
## Overview
---
This REST API has been designed to provide access to the following resources stored in the following databases: 
- Customers: Google Cloud MySql database
- Articles: Google Cloud MySql database
- Transactions: Google Cloud MySql database
- AllData: Google Cloud MySql database
The main purpose of the API is to retrieve the data in JSON format. The API uses authentication

## Demo Images
---
![image](https://github.com/Niccoborg22/CloudRun-Retail-Dashboard/assets/114749413/362be93f-acba-4c93-909f-be4f4d26d786)

## Required Modules
---
The modules required to run the API are the following: 
- Flask: pip install Flask
- Flask-RESTx: pip install flask-restx
- SQLAlchemy: pip install SQLAlchemy
- Pandas: pip install pandas
## Functions
--- 
### Connect()
- *Description*: Connect to the MySQL Google Cloud Database
- *Input*: /
- *Output*: variable 'conn', represents a connection to the database

### Disconnect(conn)
- *Description*: Disconnect to the MySQL Google Cloud Database
- *Input*: variable 'conn', represents a connection to the database
- *Output*: /

## Endpoints
---
### Namespace Customers
#### GET customers/customers
- *Description*: Fethces all the customers dataset
- *Authorization*: /

### Namespace Articles
#### GET articles/articles
- *Description*: Fethces all the articles dataset
- *Authorization*: /

### Namespace Transactions
#### GET transactions/transactions
- *Description*: Fethces all the transaction dataset
- *Authorization*: /

### Namespace Alldata
#### GET alldata/alldata
- *Description*: Fethces all the alldata dataset
- *Authorization*: /

## Error Handling
---
In case of unathorized requests or errors, the API will return a JSON object containing an error message and an appropriate HTTP status code.

## Deployment
---
The API has been deployed in the Cloud Run in Google Cloud. In order to do so the following additional files have been created: 
- Dockerfile: Dockerfile necessary to create a container
- requirements.txt: txt file with all the requirements for the app engine to deploy the application

