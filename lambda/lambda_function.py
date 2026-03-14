import json
import boto3
import uuid

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("DynamoDB")


def response(status, body):
    return {
        "statusCode": status,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body)
    }


def lambda_handler(event, context):

    method = event["requestContext"]["http"]["method"]
    path = event.get("rawPath") or event["requestContext"]["http"].get("path", "")

    # GET /hello
    if path.endswith("/hello") and method == "GET":
        return response(200, {"message": "Hello from Lambda"})


    # POST /echo
    if path.endswith("/echo") and method == "POST":

        body = json.loads(event.get("body") or "{}")

        item = {
            "id": str(uuid.uuid4()),
            **body
        }

        table.put_item(Item=item)

        return response(201, item)


    # GET /echo
    if path.endswith("/echo") and method == "GET":

        result = table.scan()

        return response(200, result.get("Items", []))


    # DELETE /echo
    if path.endswith("/echo") and method == "DELETE":

        items = table.scan().get("Items", [])

        for item in items:
            table.delete_item(Key={"id": item["id"]})

        return response(200, {"deleted": len(items)})


    return response(404, {"message": "Not Found"})