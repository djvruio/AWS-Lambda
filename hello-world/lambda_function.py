import json

def lambda_handler(event, context):
    # TODO implement
    print(f'event: {event}')
    print(f'context: {context}')
    print(f'memory limit: {context.memory_limit_in_mb}')
    print(f'function arn: {context.invoked_function_arn}')
    print(f'log group name: {context.log_group_name}')
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
