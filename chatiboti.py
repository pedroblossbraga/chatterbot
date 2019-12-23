from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Boti')

trainer = ChatterBotCorpusTrainer(chatbot)
try:
        print('Selecione uma língua digitando-a, por obséquio.', '\n',
                      'Please select a language by typing it.', '\n', ' ')
        ling = str(input('Português / English '+'\n'))

        if ling == 'Português':
                trainer.train("chatterbot.corpus.portuguese.conversations")
                conv = str(input('O que desejas dizer? Insira as sentenças separadas por vírgulas'+'\n')).split(',')

        elif ling == 'English':
                trainer.train("chatterbot.corpus.english.conversations")
                conv = str(input('What do you want to say? Insert some sentences separated by commas'+'\n')).split(',')

        else:
                trainer.train("chatterbot.corpus.english.conversations")
                conv = str(input('What do you want to say? Insert some sentences separated by commas'+'\n')).split(',')

        #trainer.train("chatterbot.corpus.english")

        #conv = ['hello', 'how are you?']
        #conv = ['olá', 'tudo bem?', 'meu nome é Pedro e o seu?', 'gostas de chocolate?']
        for msg in conv:
                response = chatbot.get_response(msg)

                print('Response: ', response)
except Exceptiona as e:
        print('Erro: ', e)
