from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from datasets import dialogs

print('Running...')
chatbot = ChatBot('对话机器人')

print('Making datasets...')
conversation = []
for line in dialogs:
    for item in line:
        conversation.append(item)
    conversation.append('')
print('Datasets size:', len(conversation))

print("\nTraining...")
trainer = ListTrainer(chatbot)
trainer.train(conversation)
print("Train finished.\n")
