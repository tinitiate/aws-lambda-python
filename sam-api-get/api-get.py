import psycopg2
import json

def get_records(event, context):
    # Get the parameters from the API Gateway GET request
    parameters = event['queryStringParameters']

    # Connect to the PostgreSQL database
    conn = psycopg2.connect(
        host="tinitiate_postgres",
        database="tinitiate",
        user="tinitiate",
        password="tinitiate"
    )
    cursor = conn.cursor()
    
    # Execute a SQL query to retrieve the records
    query = "SELECT * FROM loans.customer WHERE customer_creditscore=%s AND customer_req_loanamount=%s"
    cursor.execute(query, (parameters['column1'], parameters['column2']))
    records = cursor.fetchall()
    print(records)
    
    # Close the connection to the database
    cursor.close()
    conn.close()
    
    # Return the records as a JSON response
    return {
        "statusCode": 200,
        "body": json.dumps(records,default=str)
    }
