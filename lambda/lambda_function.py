import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('DynamoDB')

def response(status, body):
    return {
        "statusCode": status,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(body)
    }

def lambda_handler(event, context):

    path = event.get("rawPath", "")
    method = event.get("requestContext", {}).get("http", {}).get("method")

    # fix /dev
    if path.startswith("/dev"):
        path = path.replace("/dev", "")

    print("PATH:", path)
    print("METHOD:", method)

    # HELLO
    if path == "/hello" and method == "GET":
        return response(200, {"message": "hello"})

    # POST
    if path == "/echo" and method == "POST":
        body = json.loads(event.get("body", "{}"))

        item = {
            "id": str(uuid.uuid4()),
            "name": body.get("name"),
            "role": body.get("role")
        }

        table.put_item(Item=item)

        return response(201, item)

    # GET
    if path == "/echo" and method == "GET":
        res = table.scan()
        return response(200, res.get("Items", []))

    # DELETE
    if path == "/echo" and method == "DELETE":
        res = table.scan()

        for item in res.get("Items", []):
            table.delete_item(Key={"id": item["id"]})

        return response(200, {"message": "deleted"})

    return response(404, {"message": "Not found"})