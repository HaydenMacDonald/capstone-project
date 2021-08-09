import configparser
import psycopg2
from helpers import TestQueries


def test_tables(cur):
    """Insert data into fact/dimension tables via INSERT statements"""

    ## Extract copy table queries from StagingQueries class
    test_table_queries = [a for a in dir(TestQueries) if not a.startswith('__') and not callable(getattr(TestQueries, a))]

    ## Create error_count
    error_count = 0

    for check in test_table_queries:
        query = check.get('query')
        expected = check.get('expected')
        cur.execute(query)
        cur.execute()
        results = cur.fetchall()

        if expected != results[0][0]:
            error_count += 1

    return error_count


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
    
    ## Close connection
    conn.close()


if __name__ == "__main__":
    main()