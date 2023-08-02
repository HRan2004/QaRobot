from robot import chatbot

while True:
    try:
        user_input = input("You: ")
        response = chatbot.get_response(user_input)
        print("Robot: ", response)

    except (KeyboardInterrupt, EOFError, SystemExit):
        break
