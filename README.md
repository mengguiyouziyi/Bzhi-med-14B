模型 API 文档
API 终端地址 (Endpoint)

URL: https://861-pcp.proxy.hz.gpuez.com/v1/chat/completions
方法: POST
认证: 需要 API Key
请求格式
请求体采用JSON格式，包含以下字段：
{
    "model": "qwen2.5-14b-instruct",
    "messages": [
        {"role": "user", "content": "<你的问题>"}
    ],
    "temperature": 0.7,
    "max_tokens": 1000
}
- model: 使用的模型名称，这里为qwen2.5-14b-instruct
- messages: 输入的消息，包含用户的输入内容
- temperature: 控制生成文本的多样性，值越高生成的内容越随机，推荐0.7
- max_tokens: 生成的最大Token数量

响应格式

成功请求将返回以下JSON格式的响应：
{
    "id": "chatcmpl-xxxxxxx",
    "object": "chat.completion",
    "created": 1698987187,
    "model": "qwen2.5-14b-instruct",
    "choices": [
        {
            "message": {
                "role": "assistant",
                "content": "<模型回答>"
            }
        }
    ]
}
示例代码
你可以使用Python进行调用，以下是一个Python的示例代码：
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
