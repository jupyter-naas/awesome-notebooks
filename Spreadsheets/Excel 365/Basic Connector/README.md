# Excel 365 driver

Make Excel 365 spreadsheet ready to sync with Bob.


## Overview 

**Context** 

Excel is the most business tool on the planet. We love and Excel and use it a lot. It's most likely the only tool we are still using on our local drive.. 

Though, getting data from excel is very complicated and we have very little ressources available on the web making it simple to understand the different ways of accessing the data. 


**Problems**

- No proper documentation on the internet
- Complicated setup if you follow the Microsoft procedure.


**Solution**

Naas allows you to customize how and when your data syncs with Excel 365:

- username - username of sharepoint account
- password - password of sharepoint account
- domain - domain of sharepont account (eg mysite.sharepoint.com)
- file_path - its a full path of file in sharepoint . it can get from sharepoint dashbord by right click on file and select detail. then path can copy from right panel in dashboard
- export - it is an optional parameter. it can be csv or xlsx. file will be exported to data_output folder based on this variable. set export as empty string or False if no need to export the file

**How to use it?**

For the Excel connector, please use the following formula :

```python
df = naas.excel365.connect('username','password','domain','path','sheet','export')
```
Note : we suggest to put the argument of the function as variables.



### Permissions 

This connector requires the following permissions on your account.

- username - username of sharepoint account
- password - password of sharepoint account


## Credits 

- Data hack article : https://www.mydatahack.com/how-to-get-data-from-sharepoint-with-python/
  - Very usefull because it goes straight to the point 
- Microsoft API documentation (😎)


