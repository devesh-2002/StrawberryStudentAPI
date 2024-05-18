# StrawberryStudentAPI
This is a Strawberry (Python based GraphQL) API for managing Student data in a DynamoDB database.

## Setting up the Repo
1. Fork and Clone the Repository.
2. Create Access Key in AWS by clicking on Profile Name at Top-Right, then Security Credentials. Save the Credentials. Configure AWS CLI.
3. Create table, 'studentTable' in DynamoDB.
4. Create virtual environment
```
virtualenv env
```
5. Activate virtual environment (Windows Powershell)
```
env/Scripts/activate
```
6. Install the requirements.txt
```
pip install -r requirements.txt
```
7. Run on `localhost:8000/graphql` by :
```
strawberry server schema
```
