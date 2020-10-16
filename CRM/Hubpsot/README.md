# Hubspot integration 

HubSpot is an inbound marketing software used in content management, SEO, and social media marketing campaigns. CashStory imports all of the HubSpot data directly into your own cloud-based Smart Data Warehouse without requiring an ETL process, giving your analysts a chance to immediately review your marketing data.

Finance professionals can generate custom reports and dashboards from within the platform, and use that information to <u>forecast sales</u>, <u>review exchanges</u> with customers, and learn more about the status of the sales deal pipeline. 

Reduce the time and cost of analyzing your HubSpot inbound marketing data with CashStory.



## Get the API key 

**To access your API key :**

1. In **your HubSpot** account, click the icon settings in the main navigation bar.

2. In the left sidebar menu, navigate to Integrations > **API key**.

3. If **a key** has never been generated for **your** account, click Generate **API key**.

4. If you've already generated an **API key**, click Show to display **your key**.


## Configure Bob to get the data

**To get the data from Bob **

1. In **your Bob** account, click the data science icon in the left side navigation bar.
2. In the left sidebar menu, navigate to Shared > **Hubspot driver**.
3. Take **your API key** and paste it in the **variables** section of the notebook, click on **Launch notebook**.
4. If you're **API key**, is correct you will be able to choose between diffrent outputs : 
   1. Deal output : consolidated table of your deals across pipelines 
   2. Contact output : consoldiated list of contacts



## Deal Output

| Key        | Value                | Description                                                  |
| ---------- | -------------------- | ------------------------------------------------------------ |
| PIPELINE   | BDR Jeremy           | Name of the pipeline (ex: named by the salesperson)          |
| DEAL_ID    | 1489973227           | Unique identifier of the deal                                |
| DEAL_NAME  | My Client            | Name of the deal                                             |
| DEAL_STAGE | Lead                 | Name of the stage in which the deal is                       |
| CLOSE_DATE | 31/03/2020  18:12:00 | Date when the deal has been closed / is supposed to be closed |
| DEAL_OWNER | Name Surname         | Name of the salesperson in charge of the deal                |
| AMOUNT     | 12000                | Amount of the deal                                           |
| COMPANY    | Associated company   | Name of the client company                                   |
| CONTACT    | Associated contact   |                                                              |



# References 

- Hubspot developpers guide on [deals](https://developers.hubspot.com/docs/methods/deals/deals_overview) 

