import psycopg2
import json
import os

def handler(event, context):
    data = json.loads(event['body'])
    try:
        conn = psycopg2.connect(
            host=os.environ['POSTGRES_HOST'],
            port=os.environ['POSTGRES_PORT'],
            dbname=os.environ['POSTGRES_DB'],
            user=os.environ['POSTGRES_USER'],
            password=os.environ['POSTGRES_PASSWORD']
        )
        cursor = conn.cursor()
        query = "INSERT INTO shoppingcart.products(product_id, product_category, product_name, unit_price) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (data['id'], data['category'],data['name'], data['price']))
        conn.commit()
        response = {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Product added successfully"
            })
        }
    except Exception as e:
        response = {
            "statusCode": 500,
            "body": json.dumps({
                "message": f"Failed to add product: {e}"
            })
        }
    finally:
        cursor.close()
        conn.close()
        return response