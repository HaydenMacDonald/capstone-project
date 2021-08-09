import configparser
import psycopg2
from helpers import DropQueries, CreateQueries


def drop_tables(cur, conn):
    """Drop all specified tables"""
    
    ## Extract drop table queries from DropQueries class
    drop_table_queries = [a for a in dir(DropQueries) if not a.startswith('__') and not callable(getattr(DropQueries, a))]
    
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """ Create tables in Redshift cluster """

    ## Extract create table queries from CreateQueries class
    create_table_queries = [a for a in dir(CreateQueries) if not a.startswith('__') and not callable(getattr(CreateQueries, a))]

    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """ Main program function """
    ## Parse config file AWS details
    config = configparser.ConfigParser()
    config.read('dwh.cfg')
    
    ## Connect to Redshift instance
    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    ## Drop tables then create tables
    drop_tables(cur, conn)
    create_tables(cur, conn)
    
    ## Close connection
    conn.close()


if __name__ == "__main__":
    main()