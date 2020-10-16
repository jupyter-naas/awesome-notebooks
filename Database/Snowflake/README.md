# Snowflake connector

### Pre-requisite:
- Snowflake account

### Credentials required to connect to Snowflake:

- username - Snowflake account username
- password - Snowflake account password
- account - Snowflake account ID
- database - Snowflake database you wish to connect

Note: Snowflake account ID can be found in the url ( e.g. cj50471.ap-southeast-1 )

## Sample Credentials JSON:

{
	"user": "< Your snowflake account username >",
	"password": "< Your snowflake account password >",
	"account": "< Your snowflake account ID >",
	"database": "< snowflake database name you wish to access >"
}

Note: credentials JSON file is passed as an mandatory parameter in "SnowflakeConnector" class

### Install dependency
```sh
$ sudo apt-get install -y libssl-dev libffi-dev
```

### Install PIP package inside virtual environment
```sh
$ pip install --upgrade snowflake-connector-python
```
### Executing Snowflake connector
```python
from snowflake import SnowflakeConnector
#Initialize SnowflakeConnector
instance = SnowflakeConnector('credentials.json')

#Fetch records from Snowflake database
instance.execute_query("< Your Select Query >",query_type="pull")

#Insert records into snowflake database
instance.execute_query("< Your insert query >",query_type="push")

#Close database connection (Mandatory)
instance.close_connection()
```

Note: Query of type pull will return a dataframe