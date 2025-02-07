import json
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    if n < 2:
        return False
    sum_divisors = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            sum_divisors += i
            if i != n // i:
                sum_divisors += n // i
    return sum_divisors == n

def is_armstrong(n):
    digits = [int(d) for d in str(abs(n))]
    length = len(digits)
    return sum(d ** length for d in digits) == abs(n)

def digit_sum(n):
    return sum(int(d) for d in str(abs(n)))

def get_fun_fact(n):
    if is_armstrong(n):
        return f"{n} is an Armstrong number because {' + '.join([f'{d}^{len(str(abs(n)))}' for d in str(abs(n))])} = {n}"
    return f"{n} is a fascinating number with unique properties."

def classify_properties(n):
    properties = []
    if is_armstrong(n):
        properties.append("armstrong")
    if n % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")
    return properties

def lambda_handler(event, context):
    try:
        # Extract the number from query parameters
        query_params = event.get("queryStringParameters", {})
        number_str = query_params.get("number")

        # Validate input
        if not number_str:
            return create_response(400, {"number": None, "error": "Missing number parameter"})

        try:
            number = float(number_str)  # Support floating-point and integers
        except ValueError:
            return create_response(400, {"number": number_str, "error": "Invalid number format"})  # ✅ Include invalid input

        is_whole = number.is_integer()
        int_number = int(number) if is_whole else None

        properties = classify_properties(int_number) if is_whole else []

        response = {
            "number": number,
            "is_prime": is_prime(int_number) if is_whole else False,
            "is_perfect": is_perfect(int_number) if is_whole else False,
            "properties": properties,
            "digit_sum": digit_sum(int_number) if is_whole else None,
            "fun_fact": get_fun_fact(int_number) if is_whole else f"{number} is a real number with unique properties."
        }

        return create_response(200, response)

    except Exception as e:
        return create_response(500, {"number": None, "error": "Internal server error", "message": str(e)})

# Function to ensure all responses have correct headers
def create_response(status_code, body):
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Allow-Methods": "GET"
        },
        "body": json.dumps(body)
    }