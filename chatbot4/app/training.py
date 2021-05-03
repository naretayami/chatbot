from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot(
        name='MyBot',
        
)

conversation = [
    "Hello", 
    "Hi there!"
    "How are you?",
    "I am good.", 
    "That is good to hear.",
    "Thank you", 
    "You are welcome.", 
]

trainer = ListTrainer(bot)
trainer.train(conversation)