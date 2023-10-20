# Arabic-Chatbot

## make it ready
to run project download [fast-text](https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.ar.300.bin.gz) cc.ar.300.bin model for into vecs folder with exract the archive of downloaded file 
create vecs folder in dosen`t created
as defiend in config.yml
## install python env
install python 3.8 and [rasa_nlu_examples](https://github.com/RasaHQ/rasa-nlu-examples)
find fast-text module for rasa

## start train and run
into terminal/cmd in the project folder
to train the module with implemented text domain & NLU:  
rasa train
so to run the bot into cmd/commands:
rasa shell

to think with api:
rasa run actions
## working with chat platforms 
to configure the model to answer as a bot on telegram bot channel created channel then put bot name and auth token into cradentials.yml
with webhooks examples go to [ngrok]() webhook -- domain then create new run it into your machine
note that rasa working with local port 5005

for work with telegram [API](https://medium.com/devops-dev/free-hosting-for-your-telegram-bot-its-easier-than-you-think-66a5e5c000bb)
