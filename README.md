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


mkdir actions-runner && cd actions-runner

curl -o actions-runner-linux-x64-2.319.1.tar.gz -L https://github.com/actions/runner/releases/download/v2.319.1/actions-runner-linux-x64-2.319.1.tar.gz

echo "3f6efb7488a183e291fc2c62876e14c9ee732864173734facc85a1bfb1744464  actions-runner-linux-x64-2.319.1.tar.gz" | shasum -a 256 -c

tar xzf ./actions-runner-linux-x64-2.319.1.tar.gz

./config.sh --url https://github.com/SAMANTA1401/end_to_end_deepl_chicken_disease --token AZIJMK6B2AXZXUSSZEOWIG3G4WICO


