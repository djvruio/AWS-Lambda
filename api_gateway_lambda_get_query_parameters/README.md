# Hands-on Description
- Create a simple GET demo API with Query Parameter in API Gateway.
    - Add a required URL Query string parameter (Method Execution)
    - In Settings select option **Request Validator** to ```Validate query string parameters and headers```
- Integrate Lambda as the backend of the API (with Python).
    - Add a Map Template application/json (Integration Request)
- Test the  API in API Gateway Console.
- Deploy the API in a Stage (DEVEL).
- Invoking the API Method from Internet (with browser).

## Notes
[API Gateway mapping template](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-mapping-template-reference.html#input-variable-reference)