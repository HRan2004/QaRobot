from chatterbot import ChatBot

print('Starting...')
chatbot = ChatBot('对话机器人')

# 跟你的机器人对话
while True:
    text = input("You: ")
    if len(text) == 0:
        break
    response = chatbot.get_response(text)
    print("Robot:", response)
