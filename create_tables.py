import configparser
import psycopg2
from pprint import pprint
from helpers.drop_queries import DropQueries
from helpers.create_queries import CreateQueries


def drop_tables(cur, conn):
    """Drop all specified tables"""
    print("Begin executing drop queries.")

    ## Extract drop table queries from DropQueries class
    drop_table_queries = [a for a in dir(DropQueries) if not a.startswith('__') and not callable(getattr(DropQueries, a))]
    
    for query in drop_table_queries:
        cur.execute(getattr(DropQueries, query))
        conn.commit()

    print("Completed drop queries.")


def create_tables(cur, conn):
    """ Create tables in Redshift cluster """
    print("Begin executing create queries.")

    ## Extract create table queries from CreateQueries class
    create_table_queries = [a for a in dir(CreateQueries) if not a.startswith('__') and not callable(getattr(CreateQueries, a))]

    for query in create_table_queries:
        cur.execute(getattr(CreateQueries, query))
        conn.commit()

    print("Completed create queries.")


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