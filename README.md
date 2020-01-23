# Instill Bot
A chatbot/voice integration for [Instill Distilling](https://www.instilldistillingco.com/).

Runs off of [Rasa](www.rasa.com)

# Local Deployment
For local deployment I recommend just using [Rasa Open Source](https://rasa.com/docs/rasa/user-guide/installation/)

You can install this via `pip3 install rasa` (Recommended in a venv)

1. Train the model - `rasa train`
2. Then talk to it/test it via the CLI with - `rasa shell`

# Server Deployment
Uses [Terraform](https://www.terraform.io) to deploy resources, right now only example is AWS EC2 instance.  Will have it fully automated soon but for now it sets up a EC2 instance and pulls the Rasa X automated install script down and then you can run it at your leisure to setup your assistant.

## Pre-Reqs For Server Deployment
You need to ensure you have the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv1.html) installed and configured.

`deployment/aws` folder has the terraform files.  Right now the only file you have to change is the section:

`private_key = file("~/.ssh/rasa-chatbot.pem")` and replace this with whatever your key pair file is from your AWS key pair used.  This is the same name you will be asked when deploying.

To deploy simply run `terraform apply` and you will be asked for the name of the key pair name to be used for the instance as well as what size instance to be used like `t2.small` etc.

After a few minutes when terraform is complete you will have a ec2 instance you can then login to it and run the `sudo bash ./install.sh` from the home directory of the `ubuntu` user.

After this is complete you will have a docker-compose file you can bring up, basically you are following the instructions for [Rasa X Automated Install](https://rasa.com/docs/rasa-x/installation-and-setup/docker-compose-script/)

## What it Deploys
This will deploy a ec2 instance of your size choosing along with the security group allowing SSH and Port 80 access to everywhere.

## Deployment TODO
Once I get the proper env vars needed add back in the `sudo bash ./install.sh` step to auto create the env as needed and then run `sudo docker-compose up -d` to bring the bot up.