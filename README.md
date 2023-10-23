## Arabic-Chatbot

### make Project ready
to run project download fast-text Arabic models: [Arabic](https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.ar.300.bin.gz), [Arabic Egypt](https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.arz.300.bin.gz) into vecs folder with exract the archive of downloaded gz file
create vecs folder in dosen`t created
note that you could change fast-text model with models into fast-text or another that defined in reading list, so check config.yml 

- name: rasa_nlu_examples.featurizers.dense.FastTextFeaturizer
     cache_path: vecs/cc.ar.300.bin

  for model customization and model path configurations as defined in config.yml

     [example](https://rasa.com/blog/enhancing-rasa-nlu-with-custom-components/)
### install python env
python venv with version <3.8, python >3.6 and [rasa_nlu_examples](https://github.com/RasaHQ/rasa-nlu-examples)
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
with webhooks examples go to [ngrok](https://ngrok.com/) webhook -- domain then create new run it into your machine
note that rasa working with local port 5005
### Issues
if you working with external models you should make installations og packages with these steps for avoid the error:
#### 1- using git or download https://github.com/RasaHQ/rasa-nlu-examples 
#### 2- install make from [Here]()
#### 3- make install
these steps makes the packages installed and rasa == 3 version also,
____________________________________________________________________________________________________________
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

## 🧪 Testing
- Train bot
```
rasa train
```
- Test bot on shell
```
rasa shell
```
- start `rasa` server
```bash
rasa run --enable-api --cors "*" --debug[Optional] -p {PORT}[optional]
```
- start `actions` server
```
rasa run actions -p {PORT}[Optional]
```


## 🛠 Features {Changable}
- [x] Basic E-commerce FAQ
- [x] Basic chitchats
- [x] Out of Scope
- [x] Contact us form
- [x] Send Emails

- [ ] 
### Tutorial links:
- [Build customer care chatbot from scratch](https://youtu.be/u6xOgR3jEMU)
- [Send email from Rasa chatbot](https://youtu.be/UcbNmZA65pw)
