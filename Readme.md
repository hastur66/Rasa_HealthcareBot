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
bash docker_up.sh
```
view logs :
```
bash docker_logs.sh
```
shutdown service :
```
bash docker_down.sh
```