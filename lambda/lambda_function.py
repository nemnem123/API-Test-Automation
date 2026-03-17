import json
import boto3
import uuid

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("DynamoDB")

def lambda_handler(event, context):
    try:
        print("EVENT:", event)

        method = event["requestContext"]["http"]["method"]
        path = event["rawPath"]

        # ===== HELLO =====
        if path == "/hello" and method == "GET":
            return {
                "statusCode": 200,
                "body": json.dumps({"message": "hello world"})
            }

        # ===== POST =====
        if path == "/echo" and method == "POST":
            body = json.loads(event["body"])

            item = {
                "id": str(uuid.uuid4()),
                "name": body.get("name"),
                "role": body.get("role")
            }

            table.put_item(Item=item)

            return {
                "statusCode": 201,
                "body": json.dumps(item)
            }

        # ===== GET =====
        if path == "/echo" and method == "GET":
            response = table.scan()

            return {
                "statusCode": 200,
                "body": json.dumps(response.get("Items", []))
            }

        # ===== DELETE =====
        if path == "/echo" and method == "DELETE":
            items = table.scan().get("Items", [])

            for item in items:
                table.delete_item(Key={"id": item["id"]})

            return {
                "statusCode": 200,
                "body": json.dumps({"message": "deleted"})
            }

        return {
            "statusCode": 404,
            "body": json.dumps({"message": "Not Found"})
        }

    except Exception as e:
        print("ERROR:", str(e))
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }