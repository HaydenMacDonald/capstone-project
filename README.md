# Capstone project for Udacity Data Engineering Nanodegree

## Step 1: Scope the Project and Gather Data
Since the scope of the project will be highly dependent on the data, these two things happen simultaneously. In this step, you’ll:
* Identify and gather the data you'll be using for your project (at least two sources and more than 1 million rows).
	- This capstone project is based on the [CS:GO Competitive Matchmaking Data](https://www.kaggle.com/skihikingkevin/csgo-matchmaking-damage) from Kaggle. Data files were downloaded directly from the repository.
* Explain what end use cases you'd like to prepare the data for (e.g., analytics table, app back-end, source-of-truth database, etc.)
	- In this project I aimed to prepare an analytics table with a fact table on rounds that occur in each game of CS:GO and dimension tables that contain additional information or could be used to link the rounds data to other data sources.

## Step 2: Explore and Assess the Data
* Explore the data to identify data quality issues, like missing values, duplicate data, etc.
	- The data do not seem to have duplicates at face value, but there are particular rows that will be excluded based on domain knowledge of the data set. For example, environmental damage caused by the world will be excluded from the damage dataset.
* Document steps necessary to clean the data
	- See `helpers/staging_queries.py` for cleaning steps.

## Step 3: Define the Data Model
* Map out the conceptual data model and explain why you chose that model
	- A star model was used to model the data in order to optimize the data for queries on rounds, which are captured in a fact table. Additional data related to the round is stored in dimension tables, including matches, teams, and maps. These tables together would allow analysts quick access to recent rounds data. This database would serve analytical purposes, but could also be used to serve data to a customer-facing product feature.
* List the steps necessary to pipeline the data into the chosen data model
	- Load relevant data into the correct S3 bucket
	- Add relevant credentials to your config file
	- Run `etl.bat` to create tables in Redshift, run the ETL process, and test the resulting records.

## Step 4: Run ETL to Model the Data
* Create the data pipelines and the data model
* Include a data dictionary
	- Please see the [data dictionary]().
* Run data quality checks to ensure the pipeline ran as expected
	- Integrity constraints on the relational database (e.g., unique key, data type, etc.)
	- Unit tests for the scripts to ensure they are doing the right thing
	- Source/count checks to ensure completeness

## Step 5: Complete Project Write Up
* What's the goal? What queries will you want to run? How would Spark or Airflow be incorporated? Why did you choose the model you chose?
	- The goal is to create a data warehouse for analytics on CS:GO rounds, either for use in analytics or in product features.
	- Analysts will run queries looking for specific types of rounds and could potentially use the data to build statistical models for predicting the dimensions of particular rounds.
	- Airflow could be incorporated by using a DAG to regularly update the warehouse and to provide more robust monitoring for the pipeline.
	- I chose this particular model because rounds are the most central aspect of any game of CS:GO. Winning rounds results in won matches and are essential to understanding how players and teams play the game. Therefore, I chose this model to optimize query performance on rounds data.
* Clearly state the rationale for the choice of tools and technologies for the project.
	- ...
* Document the steps of the process.
	- ...
* Propose how often the data should be updated and why.
	- ...
* If the data was increased by 100x, I would...
* If the pipelines were run on a daily basis by 7am, I would...
* If the database needed to be accessed by 100+ people, I would...
