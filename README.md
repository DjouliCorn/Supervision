# Supervision
A script which takes datas about your computer

## Content
Datas which are taken :
- percentage of the used cpu
- percentage of the used memory
- informations about the network that the computer used
- percentage of the space the disks uses (C and D)

## Features
__Text file:__ write all the informations taken into a texte file (info.txt). If the file doesn't exist, it's created automatically

__Database:__ write all the informations into a database

__Grafana:__ show the results into graphics with Grafana


## Usage

Prerequisite :
Install psutil, MariaDB, MySQL Connector (if needed)

1. Download the project
2. Open ``supervision.py`` in an IDE (PyCharm for example)
3. Create a database with create_bdd.sql

__Visual representation :__

4. Open a browser and go to ``http://localhost:3000/login``
5. For a first connection, enter "admin" and "admin" for username and password
6. Click on the ``+`` and import ``Create-Grafana-Monitoring-Ordinateur.json``

<p align = "center">
Graphic representation in Grafana
<img alt="graphic representation" src="https://user-images.githubusercontent.com/70654891/109171227-dbf9cd80-7781-11eb-998c-e950063ff5f5.JPG" width="75%"/>
</p>
