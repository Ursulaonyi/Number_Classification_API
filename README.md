# **Number_Classification_API - README**

## **Introduction**
The **Number Classification API** is a simple RESTful API designed to classify a given number based on various mathematical properties. It determines whether a number is **prime**, **perfect**, **Armstrong**, and categorizes it as **odd** or **even**. Additionally, it calculates the sum of its digits and provides a fun fact about the number.

This API is built as an **AWS Lambda function**, which can be integrated with **AWS API Gateway** to make it accessible over the internet.

---

## **Features**
1. **Prime Number Check**: Determines if the number is a prime number.
2. **Perfect Number Check**: Identifies if the number is a perfect number.
3. **Armstrong Number Check**: Checks if the number is an Armstrong number.
4. **Odd/Even Classification**: Classifies the number as odd or even.
5. **Digit Sum Calculation**: Computes the sum of the digits of the number.
6. **Fun Fact Generator**: Provides a fun fact related to the number.
7. **Handles Negative and Floating-Point Numbers Gracefully**.
8. **Proper Error Handling and Response Formatting**.

---

## **API Endpoint**
```
GET /classify?number=<number>
```
This API expects a query parameter `number` and returns a JSON response with its classification.

---

## **Request Parameters**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `number`  | String | Yes | A number (integer or float) to classify |

---

## **Responses**
###  **Successful Response (`200 OK`)**
If a valid number is provided, the API will return the classification details.

#### **Example Request**
```
GET /classify?number=28
```

#### **Example Response**
```json
{
    "number": 28,
    "is_prime": false,
    "is_perfect": true,
    "properties": ["even"],
    "digit_sum": 10,
    "fun_fact": "28 is a fascinating number with unique properties."
}
```

---

###  **Invalid Input (`400 Bad Request`)**
If the input is missing or invalid (e.g., a non-numeric string), the API returns a **400 error**.

#### **Example Request**
```
GET /classify?number=abc
```

#### **Example Response**
```json
{
    "number": "abc",
    "error": "Invalid number format"
}
```

---

### **Internal Server Error (`500 Internal Server Error`)**
If an unexpected error occurs, the API gracefully handles it.

#### **Example Response**
```json
{
    "number": null,
    "error": "Internal server error",
    "message": "Error details"
}
```

---

## **Deployment Steps**
### **1. Create an AWS Lambda Function**
- Open AWS Lambda and create a new function.
- Choose **Python 3.x** as the runtime.
- Paste the API code into the function editor.

### **2. Configure API Gateway**
- Create an API in AWS API Gateway.
- Add a **GET method** for your API.
- Set up **Lambda Proxy Integration**.
- Deploy the API and note the endpoint URL.

### **3. Test the API**
- Use **Postman**, **cURL**, or a browser to send requests.
- Example:  
  ```
  curl -X GET "https://your-api-url/classify?number=153"
  ```

---

## **Implementation Details**
### **Code Breakdown**
- **Prime Number Check**  
  ```python
  def is_prime(n):
      if n < 2:
          return False
      for i in range(2, int(math.sqrt(n)) + 1):
          if n % i == 0:
              return False
      return True
  ```
- **Perfect Number Check**  
  ```python
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
  ```
- **Armstrong Number Check**  
  ```python
  def is_armstrong(n):
      digits = [int(d) for d in str(abs(n))]
      length = len(digits)
      return sum(d ** length for d in digits) == abs(n)
  ```

### **Error Handling**
- **Invalid numbers return `400 Bad Request`**  
- **Unexpected errors return `500 Internal Server Error`**  

---

## **Future Improvements**
- Add **more number properties** such as **palindrome check**, **Fibonacci check**, etc.
- Enhance **fun fact generation** with more mathematical insights.
- Improve **performance** using optimized algorithms.

---

## **Conclusion**
This API provides an easy way to analyze numbers with multiple classifications. It follows best practices with **proper error handling, structured responses, and efficient computations**.

---

## **License**
This project is open-source and free to use. 
