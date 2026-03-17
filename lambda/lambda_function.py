import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('DynamoDB')


def lambda_handler(event, context):

    path = event.get("rawPath")
    method = event.get("requestContext", {}).get("http", {}).get("method")

    # normalize path (bỏ /dev)
    if path.startswith("/dev"):
        path = path.replace("/dev", "")

    # ===== HELLO =====
    if path == "/hello" and method == "GET":
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "hello"})
        }

    # ===== POST =====
    if path == "/echo" and method == "POST":
        body = json.loads(event.get("body", "{}"))

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
        res = table.scan()

        return {
            "statusCode": 200,
            "body": json.dumps(res.get("Items", []))
        }

    # ===== DELETE =====
    if path == "/echo" and method == "DELETE":
        res = table.scan()

        for item in res.get("Items", []):
            table.delete_item(Key={"id": item["id"]})

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "deleted"})
        }

    return {
        "statusCode": 404,
        "body": json.dumps({"message": "Not found"})
    }