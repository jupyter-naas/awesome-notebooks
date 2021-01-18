import snowflake.connector
import pandas as pd
import json
import os

class SnowflakeConnector:

    def __init__(self,user,password,account,database):
        """
            Description:
                        Accepts snowflake connection parameters and connects to snowflake database 
        """


        #Initializing parameters
        self.user = user 
        self.password = password
        self.account = account
        self.database = database

        print("Establishing connection to Snowflake")

        self.connection = self.get_connection()

    def get_connection(self):
        # Connecting to snowflake database
        try:
            ctx = snowflake.connector.connect(
                user=self.user,
                password=self.password,
                account=self.account,
                database=self.database
                )
            print("Connection established")
            return ctx
        except snowflake.connector.errors.DatabaseError as e:
            print('Snowflake Error {0} ({1}): {2} ({3})'.format(e.errno, e.sqlstate, e.msg, e.sfqid))

    def close_connection(self):
        #Closing snowflake database connection		
        print("\nClosing database connection")
        self.connection.close()
        print("Database connection closed!")

    def execute_query(self,query,query_type="pull"):
        """
            Executes the query passed as input
            Default query type is pull. Script will execute the query amd return a Dataframe.
            If query type is push. Query is executed and returns None.
        """
        print("Executing Query")
        try:
            cur = self.connection.cursor()
            cur.execute(query)
            if(str(query_type).lower()=="pull"):
                data = pd.DataFrame(cur.fetchall())
#                 print("Dataframe:\n",data)
                return data
            print("Query Successful!")
        except AttributeError as e:
            print("Query failed.Database connection error")
        except snowflake.connector.errors.ProgrammingError as e:
            # Error message
            print('Snowflake Error {0} ({1}): {2} ({3})'.format(e.errno, e.sqlstate, e.msg, e.sfqid))
        finally:
            cur.close()