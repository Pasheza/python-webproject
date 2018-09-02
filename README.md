# python-webproject

 Test python application which can load data from excel file to postgresql DB and visualize information from DB via web interface 
#### Instruction for launching this application

##### 1. Necessary requirements:
- Python 3.6
    - [Dash](https://plot.ly/products/dash/)
    - [SQLAlchemy](https://www.sqlalchemy.org/)
    - [PyYAML](https://pyyaml.org/wiki/PyYAMLDocumentation)
    - [Pandas](https://pandas.pydata.org/)
- Working PostgreSQL DB
##### 2. Clone this project to the folder of your choice
##### 3. Load data to DB from excel file
- Edit parameters in **dbdata.yml** file to configure connection to your DB (user, password, host, port, DB name)
- Copy excel file with to the folder of your choice
- Run **dbsetup.py** script with path to excel file as a parameter (example below for file in project root folder)
```shell
python dbsetup.py excel_data.xlsx
```
##### 4. Launch web application
- Run **app.py** script
```shell
python app.py
```
- Then you can access application at [127.0.0.1:8050](http://127.0.0.1:8050/)
##### 5. Choose index from dropdown list and enjoy plot related to chosen parameter