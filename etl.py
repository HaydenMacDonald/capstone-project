import configparser
import psycopg2
from helpers.staging_queries import StagingQueries

def load_staging_tables(cur, conn):
    """Load staging tables with data via COPY commands"""
    print("Begin executing copy queries.")

    ## Extract copy table queries from StagingQueries class
    copy_table_queries = [a for a in dir(StagingQueries) if not a.startswith('__') and a.startswith('copy') and not callable(getattr(StagingQueries, a))]

    for query in copy_table_queries:
        cur.execute(getattr(StagingQueries, query))
        conn.commit()

    print("Completed copy queries.")


def insert_tables(cur, conn):
    """Insert data into fact/dimension tables via INSERT statements"""
    print("Begin executing insert queries.")

    ## Extract copy table queries from StagingQueries class
    insert_table_queries = [a for a in dir(StagingQueries) if not a.startswith('__') and a.startswith('insert') and not callable(getattr(StagingQueries, a))]

    for query in insert_table_queries:
        cur.execute(getattr(StagingQueries, query))
        conn.commit()

    print("Completed insert queries.")


def main():
    """Main program function"""
    ## Parse config file AWS details
    config = configparser.ConfigParser()
    config.read('dwh.cfg')
    
    ## Connect to Redshift instance
    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    ## Load staging tables and insert data into fact/dimension tables
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)
    
    ## Close connection
    conn.close()


if __name__ == "__main__":
    main()