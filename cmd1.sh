virtualenv -p python3 venv
source venv/bin/activate

# airflow needs a home, ~/airflow is the default,
# but you can lay foundation somewhere else if you prefer
# (optional)
export AIRFLOW_HOME=~/Documents/training_assignment_2
export SLUGIFY_USES_TEXT_UNIDECODE=yes

# install from pypi using pip
pip install apache-airflow
pip install sklearn
pip install pandas
pip install jupyter

# initialize the database
airflow initdb

# start the web server, default port is 8080
airflow webserver -p 8080

# visit localhost:8080 in the browser and enable the example dag in the home page
