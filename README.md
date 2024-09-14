# Deeplearning classification (chicken diseas predictiton)
 # used moduler component
## Workflows

1. Update config.yaml
2. update secrets.yaml[optional]
3. update params.yaml
4. update the entity
5. update the configaration manager in src config
6. update the components
7. update the pipelins
8. update the main.py
9. update the dvc.yaml

dvc init
dvc repro
dvc dag


sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker

setting>actions>runner>new self hosted runner> choose os> then run command one by one

