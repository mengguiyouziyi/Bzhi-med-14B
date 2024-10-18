import requests

def generate(question: str, api_key: str) -> str:
    """调用模型API生成回答."""
    url = 'https://861-pcp.proxy.hz.gpuez.com/v1/chat/completions'
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    data = {
        "model": "qwen2.5-14b-instruct",
        "messages": [{"role": "user", "content": question}],
        "temperature": 0.7,
        "max_tokens": 1000
    }

    response = requests.post(url, json=data, headers=headers)
    response.raise_for_status()
    
    return response.json()['choices'][0]['message']['content']

# 示例调用
api_key = "<你的API Key>"
question = "什么是机器学习？"
answer = generate(question, api_key)
print(answer)
