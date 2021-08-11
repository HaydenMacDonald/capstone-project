import os
import csv
import configparser
import psycopg2
from helpers.test_queries import TestQueries
from helpers.sample_queries import SampleQueries


def test_tables(cur):
    """Insert data into fact/dimension tables via INSERT statements"""

    ## Extract copy table queries from StagingQueries class
    test_table_queries = [a for a in dir(TestQueries) if not a.startswith('__') and not callable(getattr(TestQueries, a))]

    ## Create error_count
    error_count = 0

    for attr in test_table_queries:
        check = getattr(TestQueries, attr)
        query = check.get('query')
        expected = check.get('expected')
        cur.execute(query)
        results = cur.fetchall()

        if expected != results[0][0]:
            error_count += 1

    return error_count

def sample_tables(cur):
    """Sample data from each fact/dimension tables via SELECT statements"""

    ## Extract copy table queries from StagingQueries class
    sample_table_queries = [a for a in dir(SampleQueries) if not a.startswith('__') and not callable(getattr(SampleQueries, a))]

    for attr in sample_table_queries:
        check = getattr(SampleQueries, attr)
        query = check.get('query')
        table_name = check.get('table')
        cur.execute(query)
        results = cur.fetchall()

        ## Write csv        
        fp = open(f"{os.getcwd()}\\data\\csgo-data\\sample-data\\{table_name}.csv", 'w')
        myFile = csv.writer(fp)
        myFile.writerows(results)
        fp.close()

def main():
    """Main program function"""
    ## Parse config file for AWS details
    config = configparser.ConfigParser()
    config.read('dwh.cfg')
    
    ## Connect to Redshift instance
    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    ## Test fact/dimension tables
    checks = test_tables(cur)

    if checks > 0:
        raise ValueError('Data quality checks failed.')
    elif checks == 0:
        print("Data quality checks passed.")
        sample_tables(cur)
    
    ## Close connection
    conn.close()


if __name__ == "__main__":
    main()