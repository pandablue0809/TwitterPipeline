sudo apt-get update
sudo apt install python3-pip
sudo pip install apache-airflow
sudo pip install pandas 
sudo pip install s3fs
sudo pip install tweepy

# Setting the Airflow Server
cd airflow
sudo nano airflow.cfg
# Change the dags_folder as /twitter_dag

mkdir twitter_dag
cd twitter_dag

# Copy the Codes on Server
sudo nano twitter_etl.py
sudo nano twitter_dag.py
