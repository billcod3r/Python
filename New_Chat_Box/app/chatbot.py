import os
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer


# Create chatbot Instance

chatbot = ChatBot(
    'Chatty',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand. I am still learning.',
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///database.sqlite3'
)

# Training with Personal Ques & Ans

training_data_quesans = open('training_data/crime.txt').read().splitlines()
training_data_personal = open('training_data/simple.txt').read().splitlines()
training_data_conv = open('training_data/more.txt').read().splitlines()

training_data = training_data_quesans + training_data_personal + training_data_conv

trainer = ListTrainer(chatbot)
trainer.train(training_data)

# Training with English Corpus Data
trainer_corpus = ChatterBotCorpusTrainer(chatbot)