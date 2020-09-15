# Weatherbot_Sunny
This bot is trained to tell you the weather in your city.

Requirements installed:
- Python3
- pip
- Rasa X or Rasa OpenSource
- separate virtual environment like anaconda

Next steps:
- Clone the project from Git: https://github.com/Thessa1/weatherbot_sunny
- Switch from base to virtual environment
- Install the request package in your current rasa environment with<br>
<i>$ pip install requests</i><br>
This will install the requests package in the rasa environment so we can call the weather API in rasa chatbot.
- To train and run the model use<br>
<i>$ rasa train && rasa shell –debug</i><br>
or with Rasa X<br>
<i>$ rasa train && rasa x</i><br>
- parellelly run the actions server in new terminal,<br>
<i>$ rasa run actions</i>
