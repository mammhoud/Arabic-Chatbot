## Arabic-Chatbot

### make it ready
to run project download [fast-text](https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.ar.300.bin.gz) cc.ar.300.bin model for into vecs folder with exract the archive of downloaded file 
create vecs folder in dosen`t created
as defiend in config.yml
### install python env
install python 3.8 and [rasa_nlu_examples](https://github.com/RasaHQ/rasa-nlu-examples)
find fast-text module for rasa

### start train and run
into terminal/cmd in the project folder
to train the module with implemented text domain & NLU:  
rasa train
so to run the bot into cmd/commands:
rasa shell

to think with api:
rasa run actions
### working with chat platforms 
to configure the model to answer as a bot on telegram bot channel created channel then put bot name and auth token into cradentials.yml
with webhooks examples go to [ngrok]() webhook -- domain then create new run it into your machine
note that rasa working with local port 5005

rasa project works with telegram, to know more about its [API](https://medium.com/devops-dev/free-hosting-for-your-telegram-bot-its-easier-than-you-think-66a5e5c000bb)

### Reading-list
#### [Events](https://rasa.com/docs/rasa/action-server/events#slot)
#### [Event Brokers](https://rasa.com/docs/rasa/event-brokers)
#### [Default Actions](https://rasa.com/docs/rasa/default-actions)
#### [Your Own Website](https://rasa.com/docs/rasa/connectors/your-own-website)
#### [Training Data Importers](https://rasa.com/docs/rasa/training-data-importers)
#### [Entity Recognition](https://rasa.com/blog/rasa-nlu-in-depth-part-2-entity-recognition/)
#### [How to run custom action in background?](https://forum.rasa.com/t/how-to-run-custom-action-in-background/49599)
#### [Connecting Rasa to a database to store responses](https://forum.rasa.com/t/connecting-rasa-to-a-database-to-store-responses/44998)
#### [Retrieving Data from Rasa Open Source into a database](https://forum.rasa.com/t/retrieving-data-from-rasa-open-source-into-a-database/57105)
#### [ValidationAction function not being read](https://forum.rasa.com/t/validationaction-function-not-being-read/56000)
#### [Custom paths](https://forum.rasa.com/t/custom-paths/56496)
#### [rasa blog](https://rasa.com/blog/)
#### []()
#### []()
#### []()
#### []()
#### []()
#### []()
#### []()
#### []()
