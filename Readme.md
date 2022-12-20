## Rasa Healthcare chatbot

train model :
```
docker run -it -v $(pwd):/app rasa/rasa:2.2.8-full train --out models
```
in case model saving error :
```
sudo chgrp -R root models && sudo chmod -R 770 models
sudo chgrp -R root . && sudo chmod -R 770 .
```
deploy bot :
```
docker-compose up -d
```
view logs :
```
docker-compose logs
```
shutdown service :
```
docker-compose down
```