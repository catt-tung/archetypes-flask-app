# Survival Archetypes Story Collector
A Python Flask Web App buit with Jinja with a PostgresSQL backend database. Styled with CSS and Bootstrap. A deployed version of this app can be found [here](https://archetypesstorycollector.herokuapp.com/).

![heroimage](./myapp/static/Untitled%20design.png)
## About this App
This app was created to build a treasure trove of stories about the survival archetypes from Caroline Myss' work in _Sacred Contracts_. According to Myss' work, each individual has twelve main archetypes that are always at work in our lives, four of which we all universally have, which are called the Survival Archetypes. 

Becoming aware of our archetypes and how they are at play in our lives is the first step to mastering the ability to make conscious choices. The survival archetypes help us grow and mature into individuals who know how to recognize the true lesson each experience that comes to us provides. 

My intention with building this app was to help us understand the survival archetypes through storytelling - both from writing out our own experiences, and learning from reading about the experiences of others. This has been the primary way I have come to understand archetypes - from sharing stories in my spiritual direction sessions and having my archetypes identified by my spiritual director. Slowly, I came to recognize and identify the survival archetypes when they showed up - allowing me to make conscious choices for change. It would have been incredibly useful for me at the time if there were more shared stories where I could learn about these archetypes, which is what this app intends to create.

## Technologies Used
The following technologies were used to build this app:

![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Jinja Badge](https://img.shields.io/badge/Jinja-B41717?logo=jinja&logoColor=fff&style=for-the-badge)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![Anaconda](https://img.shields.io/badge/Anaconda-%2344A833.svg?style=for-the-badge&logo=anaconda&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white)

## How to Use the App
To contribute and reflect on your own experiences encountering your survival archetypes, first register an account with the app and login with your credentials. From there, you can go to "Create Post" to add a story. Your stories will automatically be collected in "My Stories".

The published stories are available to be read without registering an account.

## Stretch Goals
Ideally I would like to have a different setup of the models where I could also have a favorite feature through a model that could link a profile model to a post, so that the stories could be re-read and absorbed. The ERD below shows an idea of what I was working toward. 

![ERD](myapp/static/Screen%20Shot%202022-04-15%20at%201.29.43%20AM.png)

In perhaps a different project, I would love for this to be extensible to _all_ the archetypes, and create an API database to be able to search them - however given that there are _hundreds_ of archetypes, this would really have to be a much more robust app, with API search functionalities and more filtering and display methods to make it practical and applicable. 

## Credits
+ This site's idea was inspired entirely by the works of Caroline Myss in Sacred Contracts, cited as follows: Myss, Caroline. Sacred Contracts: Awakening Your Divine Potential. Harmony, 2002.
+ Background photo by [Salvatore Andrea Santacroce](https://unsplash.com/@salcrocejpg?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/@salcrocejpg?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)
+ The favicon for this website came from [Story icons created by Freepik - Flaticon](https://www.flaticon.com/free-icons/story)
+ Badges for technologies were take from [Ileriayo's GH repo](https://github.com/Ileriayo/markdown-badges) using shields.io