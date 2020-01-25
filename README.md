# Instill Bot
A chatbot/voice integration for [Instill Distilling](https://www.instilldistillingco.com/).

Runs off of [Rasa](www.rasa.com)

# Local Deployment
For local deployment I recommend just using [Rasa Open Source](https://rasa.com/docs/rasa/user-guide/installation/)

You can install this via `pip3 install rasa` (Recommended in a venv)

You will also need to install the pre-reqs with `pip3 install requirements-dev.txt` and `pip3 install requirements.txt`

1. Train the model - `rasa train`
2. Bring up action server - `rasa run actions --actions actions`
3. Then talk to it/test it via the CLI with - `rasa shell`

# Local Deployment
You can follow the normal [Rasa Open Source Install](https://rasa.com/docs/rasa/user-guide/installation/) instructions to install this project locally.

## Action Server
This assistant does require the action server to be running.  More information on what this is can be found at [Rasa Action Server](https://rasa.com/docs/rasa/api/rasa-sdk/#running-the-action-server)

If running locally you would need to run `rasa run actions --actions` before starting the assistant with the above Local Deployment instructions.

# Server Deployment
You can deploy on Gcloud Compute or AWS Ec2 for a good starting point.  Once you have your Ubuntu based OS/compute running the easiest process to follow is [Rasa X Quick Install](https://rasa.com/docs/rasa-x/installation-and-setup/docker-compose-script/)

After you follow this you can [Enable SSL](https://rasa.com/docs/rasa-x/installation-and-setup/docker-compose-manual/#securing-with-ssl) as well using Let's Encrypt or your own certs. 
