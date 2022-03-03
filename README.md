# Naas Templates [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
(aka the "awesome-notebooks") 


## About Naas
Naas is a data platform that enable anyone with minimal technical knowledge to turn  <a href="https://jupyter.org" target="_blank">Jupyter Notebooks</a> into powerful automation, analytical and AI engines thanks to <a href="https://docs.naas.ai/" target="_blank">low-code formulas</a>.<br>

The platform is based on 3 elements:<br>
- The **templates** enable anyone to use data engines on all kind of subjects in minutes.
- The low-code **drivers** act as connectors to facilitate access to tools, and complex libraries (database, API, ML algorithm...)
- The low-code **features** (scheduling, asset sharing, notifications...) turns Notebooks into production ready data engines.<br>

Naas is forever free to use with 100 credits/month.<br>
<a href="https://www.naas.ai/free-forever" target="_blank">Open your account</a><br>


## Naas Templates
The aim of this repository is to be the largest aggregator of production ready Jupyter Notebooks templates.
To do so, we have defined a framework that enable easy understanding and scaling of Notebooks: 
Each notebook is organized with the following msections:  
- Title: "Tool - Action of the notebook"
- Description: a one-liner explaining the benefits of the notebooks for the user 
- Tags: hastags of the topics the notebook is about
- Input: list of all the variables, credentials, that needs to be setup 
- Model: list the functions applied to the data 
- Output: list the assets to be used by the user and its distribution channels if any.

The repository is organized by source/tools.
Managed by Naas core-team and community ⭐️.

→ Feel free to use the Issues tab to add any templates you would like to see, or contribute to.


## How to contribute ?
- Step 1: Open free account on <a href="https://www.naas.ai/" target="_blank">Naas.ai</a>
- Step 2: Clone awesome-notebooks repo
- Step 3: Change status of this Issue to “In progress” so we can know you are working on it
- Step 4: Create new branch with a short name of the issue (ex: “gsheet-notion”)
- Step 5: Create folder named with the source tool (if it does not already exist in the awesome-notebooks folder), and adapt notebook template to the current use case.
- Step 6: Once you are happy with the result, commit to the branch
- Step 7: Open a pull request and tag me as a reviewer with a little comment on what you have done, but most of the explanations should be in the notebook itself
- Step 8: Change status of this Issue to “Review” so we can know a review is pending
- Step 9: Link the PR to this issue for tracking in the backlog
- Step 10:  Expect a feedback and merge in the next 48h-72h


✅ Apply to our <a href="https://join.slack.com/t/aiclub-hq/shared_invite/zt-iqkuwq7m-zvdxYYbGLVVcIKuB2vg3pA" target="_blank">Open Source Contributor Program</a> for guidance and mentorship.

✅ Join our <a href="https://join.slack.com/t/aiclub-hq/shared_invite/zt-iqkuwq7m-zvdxYYbGLVVcIKuB2vg3pA" target="_blank">Slack Community</a> to present yourself, ask questions, learn about our latest news.

✅ Follow us on social medias:
- [Twitter: @naas.ai ](https://twitter.com/JupyterNaas)<br>
- [Linkedin: @JupyterNaas](https://www.linkedin.com/company/naas-ai/)<br>
- [Youtube: @naas](https://www.youtube.com/channel/UCKKG5hzjXXU_rRdHHWQ8JHQ/videos)<br>

<br>

# Templates list


## AWS
* [Daily biling notification to slack](https://github.com/jupyter-naas/awesome-notebooks/tree/master/AWS/AWS_Daily_biling_notification_to_slack.ipynb)
* [Get files from S3 bucket](https://github.com/jupyter-naas/awesome-notebooks/tree/master/AWS/AWS_Get_files_from_S3_bucket.ipynb)
* [Upload file to S3 bucket](https://github.com/jupyter-naas/awesome-notebooks/tree/master/AWS/AWS_Upload_file_to_S3_bucket.ipynb)

## Airtable
* [Connect](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Airtable/Airtable_Connect.ipynb)
* [Delete data](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Airtable/Airtable_Delete_data.ipynb)
* [Get data](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Airtable/Airtable_Get_data.ipynb)
* [Insert data](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Airtable/Airtable_Insert_data.ipynb)
* [Search data](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Airtable/Airtable_Search_data.ipynb)

## AlphaVantage
* [Get balance sheet](https://github.com/jupyter-naas/awesome-notebooks/tree/master/AlphaVantage/AlphaVantage_Get_balance_sheet.ipynb)
* [Get cashflow statement](https://github.com/jupyter-naas/awesome-notebooks/tree/master/AlphaVantage/AlphaVantage_Get_cashflow_statement.ipynb)
* [Get company overview](https://github.com/jupyter-naas/awesome-notebooks/tree/master/AlphaVantage/AlphaVantage_Get_company_overview.ipynb)
* [Get income statement](https://github.com/jupyter-naas/awesome-notebooks/tree/master/AlphaVantage/AlphaVantage_Get_income_statement.ipynb)

## Bazimo
* [Get export Actifs](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Bazimo/Bazimo_Get_export_Actifs.ipynb)
* [Get export Baux](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Bazimo/Bazimo_Get_export_Baux.ipynb)
* [Get export Factures](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Bazimo/Bazimo_Get_export_Factures.ipynb)
* [Get export Locataires](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Bazimo/Bazimo_Get_export_Locataires.ipynb)
* [Get export Lots](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Bazimo/Bazimo_Get_export_Lots.ipynb)

## Boursorama
* [Get CDS](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Boursorama/Boursorama_Get_CDS.ipynb)

## Bubble
* [Trigger workflow](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Bubble/Bubble_Trigger_workflow.ipynb)

## CCXT
* [Calculate Support and Resistance](https://github.com/jupyter-naas/awesome-notebooks/tree/master/CCXT/CCXT_Calculate_Support_and_Resistance.ipynb)
* [Predict Bitcoin from Binance](https://github.com/jupyter-naas/awesome-notebooks/tree/master/CCXT/CCXT_Predict_Bitcoin_from_Binance.ipynb)

## CSV
* [Read file](https://github.com/jupyter-naas/awesome-notebooks/tree/master/CSV/CSV_Read_file.ipynb)
* [Save file](https://github.com/jupyter-naas/awesome-notebooks/tree/master/CSV/CSV_Save_file.ipynb)

## Canny
* [Create](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Canny/Canny_Create.ipynb)
* [Github issue update](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Canny/Canny_Github_issue_update.ipynb)
* [Read](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Canny/Canny_Read.ipynb)

## Celestrak
* [Satellites over time](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Celestrak/Celestrak_Satellites_over_time.ipynb)

## Cityfalcon
* [Get data from API](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Cityfalcon/Cityfalcon_Get_data_from_API.ipynb)

## Data.gouv.fr
* [COVID19 -  FR - Entrées et sorties par région pour 1 million d'hab.](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Data.gouv.fr/COVID19%20-%20%20FR%20-%20Entr%C3%A9es%20et%20sorties%20par%20r%C3%A9gion%20pour%201%20million%20d%27hab..ipynb)

## EM-DAT
* [Natural disasters](https://github.com/jupyter-naas/awesome-notebooks/tree/master/EM-DAT/EM-DAT_natural_disasters.ipynb)

## Elastic Search
* [Connect to server](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Elastic%20Search/Elastic%20Search_Connect_to_server.ipynb)

## Excel 365
* [Access  sheet](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Excel%20365/Access%20Excel%20365%20sheet.ipynb)

## Excel
* [Consolidate files](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Excel/Excel_Consolidate_files.ipynb)
* [Custom sheet](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Excel/Excel_Custom_sheet.ipynb)
* [Get dynamic active range](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Excel/Excel_Get_dynamic_active_range.ipynb)
* [Read file](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Excel/Excel_Read_file.ipynb)
* [Save file](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Excel/Excel_Save_file.ipynb)

## FAO
* [Consumer price indice](https://github.com/jupyter-naas/awesome-notebooks/tree/master/FAO/FAO_Consumer_price_indice.ipynb)

## FEC
* [Creer un dashboard PowerBI](https://github.com/jupyter-naas/awesome-notebooks/tree/master/FEC/FEC_Creer_un_dashboard_PowerBI.ipynb)

## FTP
* [S Connect](https://github.com/jupyter-naas/awesome-notebooks/tree/master/FTP/FTPS_Connect.ipynb)
* [Connect](https://github.com/jupyter-naas/awesome-notebooks/tree/master/FTP/FTP_Connect.ipynb)
* [Get file](https://github.com/jupyter-naas/awesome-notebooks/tree/master/FTP/FTP_Get_file.ipynb)
* [Send file](https://github.com/jupyter-naas/awesome-notebooks/tree/master/FTP/FTP_Send_file.ipynb)

## Github
* [Close issue](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Github/Github_Close_issue.ipynb)
* [Create issue](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Github/Github_Create_issue.ipynb)
* [Download file from url](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Github/Github_Download_file_from_url.ipynb)
* [Get active projects](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Github/Github_Get_active_projects.ipynb)
* [Get commits ranking from repository](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Github/Github_Get_commits_ranking_from_repository.ipynb)
* [Get issues from repo](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Github/Github_Get_issues_from_repo.ipynb)
* [Get profile from user](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Github/Github_Get_profile_from_user.ipynb)
* [Get profiles from teams](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Github/Github_Get_profiles_from_teams.ipynb)
* [Get pull requests from repository](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Github/Github_Get_pull_requests_from_repository.ipynb)
* [Get stargazers from repository](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Github/Github_Get_stargazers_from_repository.ipynb)
* [Get weekly commits from repository](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Github/Github_Get_weekly_commits_from_repository.ipynb)
* [Peform basic actions](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Github/Github_Peform_basic_actions.ipynb)
* [Read issue](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Github/Github_Read_issue.ipynb)
* [Track notebooks created over time](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Github/Github_Track_notebooks_created_over_time.ipynb)
* [Track open issues roadmap](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Github/Github_Track_open_issues_roadmap.ipynb)

## Gmail
* [Automate response from keywords in mailbox](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Gmail/Gmail_Automate_response_from_keywords_in_mailbox.ipynb)
* [Clean mailbox](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Gmail/Gmail_Clean_mailbox.ipynb)
* [Read mailbox](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Gmail/Gmail_Read_mailbox.ipynb)
* [Schedule mailbox cleaning](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Gmail/Gmail_Schedule_mailbox_cleaning.ipynb)
* [Send emails from Gsheet classic](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Gmail/Gmail_Send_emails_from_Gsheet_classic.ipynb)
* [Send emails from Gsheet specific](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Gmail/Gmail_Send_emails_from_Gsheet_specific.ipynb)

## Google Analytics
* [GoogleAnalytics Get bounce rate](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Google%20Analytics/GoogleAnalytics_Get_bounce_rate.ipynb)
* [GoogleAnalytics Get pageview ranking](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Google%20Analytics/GoogleAnalytics_Get_pageview_ranking.ipynb)
* [GoogleAnalytics Get stats per country](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Google%20Analytics/GoogleAnalytics_Get_stats_per_country.ipynb)
* [GoogleAnalytics Get time on landing page](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Google%20Analytics/GoogleAnalytics_Get_time_on_landing_page.ipynb)
* [GoogleAnalytics Get unique visitors](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Google%20Analytics/GoogleAnalytics_Get_unique_visitors.ipynb)

## Google Drive
* [Download file](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Google%20Drive/Google_Drive_Download_file.ipynb)

## Google Search
* [Perform search](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Google%20Search/Google_Search_Perform_search.ipynb)

## Google Sheets
* [Gsheets Get data](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Google%20Sheets/Gsheets_Get_data.ipynb)
* [Gsheets Send data](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Google%20Sheets/Gsheets_Send_data.ipynb)
* [Gsheets Send emails from sheet](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Google%20Sheets/Gsheets_Send_emails_from_sheet.ipynb)

## HTML
* [Create a website](https://github.com/jupyter-naas/awesome-notebooks/tree/master/HTML/HTML_Create_a_website.ipynb)

## Healthchecks
* [Healthcheks Perfom basic actions](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Healthchecks/Healthcheks_Perfom_basic_actions.ipynb)

## HubSpot
* [Associate contact to deal](https://github.com/jupyter-naas/awesome-notebooks/tree/master/HubSpot/HubSpot_Associate_contact_to_deal.ipynb)
* [Create Task](https://github.com/jupyter-naas/awesome-notebooks/tree/master/HubSpot/HubSpot_Create_Task.ipynb)
* [Create contact](https://github.com/jupyter-naas/awesome-notebooks/tree/master/HubSpot/HubSpot_Create_contact.ipynb)
* [Create contacts from linkedin post likes](https://github.com/jupyter-naas/awesome-notebooks/tree/master/HubSpot/HubSpot_Create_contacts_from_linkedin_post_likes.ipynb)
* [Create deal](https://github.com/jupyter-naas/awesome-notebooks/tree/master/HubSpot/HubSpot_Create_deal.ipynb)
* [Delete contact](https://github.com/jupyter-naas/awesome-notebooks/tree/master/HubSpot/HubSpot_Delete_contact.ipynb)
* [Delete deal](https://github.com/jupyter-naas/awesome-notebooks/tree/master/HubSpot/HubSpot_Delete_deal.ipynb)
* [Get all contacts](https://github.com/jupyter-naas/awesome-notebooks/tree/master/HubSpot/HubSpot_Get_all_contacts.ipynb)
* [Get all deals](https://github.com/jupyter-naas/awesome-notebooks/tree/master/HubSpot/HubSpot_Get_all_deals.ipynb)
* [Get all pipelines and dealstages](https://github.com/jupyter-naas/awesome-notebooks/tree/master/HubSpot/HubSpot_Get_all_pipelines_and_dealstages.ipynb)
* [Get closed deals weekly](https://github.com/jupyter-naas/awesome-notebooks/tree/master/HubSpot/HubSpot_Get_closed_deals_weekly.ipynb)
* [Get contact](https://github.com/jupyter-naas/awesome-notebooks/tree/master/HubSpot/HubSpot_Get_contact.ipynb)
* [Get contacts associated to deal](https://github.com/jupyter-naas/awesome-notebooks/tree/master/HubSpot/HubSpot_Get_contacts_associated_to_deal.ipynb)
* [Get deal](https://github.com/jupyter-naas/awesome-notebooks/tree/master/HubSpot/HubSpot_Get_deal.ipynb)
* [Get new deals created weekly](https://github.com/jupyter-naas/awesome-notebooks/tree/master/HubSpot/HubSpot_Get_new_deals_created_weekly.ipynb)
* [Send contacts to gsheet](https://github.com/jupyter-naas/awesome-notebooks/tree/master/HubSpot/HubSpot_Send_contacts_to_gsheet.ipynb)
* [Send deals to gsheet](https://github.com/jupyter-naas/awesome-notebooks/tree/master/HubSpot/HubSpot_Send_deals_to_gsheet.ipynb)
* [Send sales brief](https://github.com/jupyter-naas/awesome-notebooks/tree/master/HubSpot/HubSpot_Send_sales_brief.ipynb)
* [Update contact](https://github.com/jupyter-naas/awesome-notebooks/tree/master/HubSpot/HubSpot_Update_contact.ipynb)
* [Update deal](https://github.com/jupyter-naas/awesome-notebooks/tree/master/HubSpot/HubSpot_Update_deal.ipynb)
* [Update followers from linkedin](https://github.com/jupyter-naas/awesome-notebooks/tree/master/HubSpot/HubSpot_Update_followers_from_linkedin.ipynb)
* [Update jobtitle country industry from linkedin](https://github.com/jupyter-naas/awesome-notebooks/tree/master/HubSpot/HubSpot_Update_jobtitle_country_industry_from_linkedin.ipynb)
* [Update linkedinbio from google](https://github.com/jupyter-naas/awesome-notebooks/tree/master/HubSpot/HubSpot_Update_linkedinbio_from_google.ipynb)

## Hugging Face
* [Ask boolean question to T5](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Hugging%20Face/Hugging_Face_Ask_boolean_question_to_T5.ipynb)
* [Naas drivers integration](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Hugging%20Face/Hugging_Face_Naas_drivers_integration.ipynb)

## IFTTT
* [Post on Twitter](https://github.com/jupyter-naas/awesome-notebooks/tree/master/IFTTT/IFTTT_Post_on_Twitter.ipynb)
* [Trigger workflow](https://github.com/jupyter-naas/awesome-notebooks/tree/master/IFTTT/IFTTT_Trigger_workflow.ipynb)

## IMDB
* [Top  Movie](https://github.com/jupyter-naas/awesome-notebooks/tree/master/IMDB/Top_IMDB_Movie.ipynb)

## IUCN
* [Extinct species](https://github.com/jupyter-naas/awesome-notebooks/tree/master/IUCN/IUCN_Extinct_species.ipynb)

## Instagram
* [Post image and caption](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Instagram/Instagram_Post_image_and_caption.ipynb)

## Integromat
* [Trigger workflow](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Integromat/Integromat_Trigger_workflow.ipynb)

## Johns Hopkins
* [Covid19 Active Cases](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Johns%20Hopkins/Johns_Hopkins_Covid19_Active_Cases.ipynb)

## Jupyter Notebooks
* [JupyterNotebooks Add cells code](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Jupyter%20Notebooks/JupyterNotebooks_Add_cells_code.ipynb)

## Jupyter
* [Get user information](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Jupyter/Jupyter_Get_user_information.ipynb)

## LinkedIn
* [+Notion Update metrics in content calendar from posts](https://github.com/jupyter-naas/awesome-notebooks/tree/master/LinkedIn/LinkedIn%2BNotion_Update_metrics_in_content_calendar_from_posts.ipynb)
* [Get comments from post](https://github.com/jupyter-naas/awesome-notebooks/tree/master/LinkedIn/LinkedIn_Get_comments_from_post.ipynb)
* [Get connections from network](https://github.com/jupyter-naas/awesome-notebooks/tree/master/LinkedIn/LinkedIn_Get_connections_from_network.ipynb)
* [Get contact from profile](https://github.com/jupyter-naas/awesome-notebooks/tree/master/LinkedIn/LinkedIn_Get_contact_from_profile.ipynb)
* [Get conversations](https://github.com/jupyter-naas/awesome-notebooks/tree/master/LinkedIn/LinkedIn_Get_conversations.ipynb)
* [Get followers from network](https://github.com/jupyter-naas/awesome-notebooks/tree/master/LinkedIn/LinkedIn_Get_followers_from_network.ipynb)
* [Get guests from event](https://github.com/jupyter-naas/awesome-notebooks/tree/master/LinkedIn/LinkedIn_Get_guests_from_event.ipynb)
* [Get identity from profile](https://github.com/jupyter-naas/awesome-notebooks/tree/master/LinkedIn/LinkedIn_Get_identity_from_profile.ipynb)
* [Get likes from post](https://github.com/jupyter-naas/awesome-notebooks/tree/master/LinkedIn/LinkedIn_Get_likes_from_post.ipynb)
* [Get messages from profile](https://github.com/jupyter-naas/awesome-notebooks/tree/master/LinkedIn/LinkedIn_Get_messages_from_profile.ipynb)
* [Get network from profile](https://github.com/jupyter-naas/awesome-notebooks/tree/master/LinkedIn/LinkedIn_Get_network_from_profile.ipynb)
* [Get polls from post](https://github.com/jupyter-naas/awesome-notebooks/tree/master/LinkedIn/LinkedIn_Get_polls_from_post.ipynb)
* [Get posts feed from profile](https://github.com/jupyter-naas/awesome-notebooks/tree/master/LinkedIn/LinkedIn_Get_posts_feed_from_profile.ipynb)
* [Get posts stats from profile](https://github.com/jupyter-naas/awesome-notebooks/tree/master/LinkedIn/LinkedIn_Get_posts_stats_from_profile.ipynb)
* [Get resume from profile](https://github.com/jupyter-naas/awesome-notebooks/tree/master/LinkedIn/LinkedIn_Get_resume_from_profile.ipynb)
* [Get stats from post](https://github.com/jupyter-naas/awesome-notebooks/tree/master/LinkedIn/LinkedIn_Get_stats_from_post.ipynb)
* [Send comments from post in gsheet](https://github.com/jupyter-naas/awesome-notebooks/tree/master/LinkedIn/LinkedIn_Send_comments_from_post_in_gsheet.ipynb)
* [Send invitation from gsheet](https://github.com/jupyter-naas/awesome-notebooks/tree/master/LinkedIn/LinkedIn_Send_invitation_from_gsheet.ipynb)
* [Send invitation to profile](https://github.com/jupyter-naas/awesome-notebooks/tree/master/LinkedIn/LinkedIn_Send_invitation_to_profile.ipynb)
* [Send likes from post in gsheet](https://github.com/jupyter-naas/awesome-notebooks/tree/master/LinkedIn/LinkedIn_Send_likes_from_post_in_gsheet.ipynb)
* [Send message to profile](https://github.com/jupyter-naas/awesome-notebooks/tree/master/LinkedIn/LinkedIn_Send_message_to_profile.ipynb)
* [Linkedin Get info from company](https://github.com/jupyter-naas/awesome-notebooks/tree/master/LinkedIn/Linkedin_Get_info_from_company.ipynb)

## Metrics Store
* [Content creation Track connections](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Metrics%20Store/Content_creation_Track_connections.ipynb)
* [Template](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Metrics%20Store/Metrics_Store_Template.ipynb)

## Microsoft Teams
* [Send message](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Microsoft%20Teams/Microsoft%20Teams_Send_message.ipynb)

## Microsoft Word
* [Convert to HMTL](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Microsoft%20Word/Microsoft_Word_Convert_to_HMTL.ipynb)

## MongoDB
* [Get data](https://github.com/jupyter-naas/awesome-notebooks/tree/master/MongoDB/MongoDB_Get_data.ipynb)
* [Send data](https://github.com/jupyter-naas/awesome-notebooks/tree/master/MongoDB/MongoDB_Send_data.ipynb)

## MySQL
* [Query database](https://github.com/jupyter-naas/awesome-notebooks/tree/master/MySQL/MySQL_Query_database.ipynb)

## NASA
* [Artic sea ice](https://github.com/jupyter-naas/awesome-notebooks/tree/master/NASA/NASA_Artic_sea_ice.ipynb)
* [Global temperature](https://github.com/jupyter-naas/awesome-notebooks/tree/master/NASA/NASA_Global_temperature.ipynb)
* [Sea level](https://github.com/jupyter-naas/awesome-notebooks/tree/master/NASA/NASA_Sea_level.ipynb)
* [Indicate sealevel](https://github.com/jupyter-naas/awesome-notebooks/tree/master/NASA/NASA_indicate_sealevel.ipynb)
* [Sea-level-indicator](https://github.com/jupyter-naas/awesome-notebooks/tree/master/NASA/Sea-level-indicator.ipynb)

## Naas Auth
* [Bearer validate](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Naas%20Auth/Naas_Auth_bearer_validate.ipynb)
* [Connect](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Naas%20Auth/Naas_Auth_connect.ipynb)
* [Users me](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Naas%20Auth/Naas_Auth_users_me.ipynb)

## Naas
* [Asset demo](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Naas/Naas_Asset_demo.ipynb)
* [Credits Get Balance](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Naas/Naas_Credits_Get_Balance.ipynb)
* [Dependency demo](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Naas/Naas_Dependency_demo.ipynb)
* [Doc demo](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Naas/Naas_Doc_demo.ipynb)
* [Domain demo](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Naas/Naas_Domain_demo.ipynb)
* [Emailbuilder demo](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Naas/Naas_Emailbuilder_demo.ipynb)
* [Get Transactions](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Naas/Naas_Get_Transactions.ipynb)
* [Get help](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Naas/Naas_Get_help.ipynb)
* [NLP Examples](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Naas/Naas_NLP_Examples.ipynb)
* [Notification demo](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Naas/Naas_Notification_demo.ipynb)
* [Scheduler demo](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Naas/Naas_Scheduler_demo.ipynb)
* [Secret demo](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Naas/Naas_Secret_demo.ipynb)
* [Set timezone](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Naas/Naas_Set_timezone.ipynb)
* [Webhook demo](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Naas/Naas_Webhook_demo.ipynb)

## Neo
* [Get currencies live prices](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Neo/Neo_Get_currencies_live_prices.ipynb)

## Newsapi
* [Get data](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Newsapi/Newsapi_Get_data.ipynb)
* [Run sentiment analysis](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Newsapi/Newsapi_Run_sentiment_analysis.ipynb)
* [Send emails briefs](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Newsapi/Newsapi_Send_emails_briefs.ipynb)

## Notion
* [Create page](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Notion/Notion_Create_page.ipynb)
* [Explore API](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Notion/Notion_Explore_API.ipynb)
* [Get database](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Notion/Notion_Get_database.ipynb)
* [Get users](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Notion/Notion_Get_users.ipynb)
* [Push data from Gsheets](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Notion/Notion_Push_data_from_Gsheets.ipynb)
* [Scheduled Updates from Gsheets](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Notion/Notion_Scheduled_Updates_from_Gsheets.ipynb)
* [Sent Gmail On New Item](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Notion/Notion_Sent_Gmail_On_New_Item.ipynb)
* [Update page](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Notion/Notion_Update_page.ipynb)
* [Update pages from database](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Notion/Notion_Update_pages_from_database.ipynb)

## OpenWeatherMap
* [Get City Weather](https://github.com/jupyter-naas/awesome-notebooks/tree/master/OpenWeatherMap/OpenWeatherMap_Get_City_Weather.ipynb)

## OwnCloud
* [Download file](https://github.com/jupyter-naas/awesome-notebooks/tree/master/OwnCloud/OwnCloud_Download_file.ipynb)
* [Upload file](https://github.com/jupyter-naas/awesome-notebooks/tree/master/OwnCloud/OwnCloud_Upload_file.ipynb)

## PDF
* [Transform to MP3](https://github.com/jupyter-naas/awesome-notebooks/tree/master/PDF/PDF_Transform_to_MP3.ipynb)

## Pandas
* [Create Pivot Table](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Pandas/Pandas_Create_Pivot_Table.ipynb)
* [ISO Date Conversion](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Pandas/Pandas_ISO_Date_Conversion.ipynb)
* [Merge Dataframes](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Pandas/Pandas_Merge_Dataframes.ipynb)

## Pipedrive
* [Get contact](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Pipedrive/Pipedrive_Get_contact.ipynb)

## Plaid
* [Get accounts](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Plaid/Plaid_Get_accounts.ipynb)
* [Get transactions](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Plaid/Plaid_Get_transactions.ipynb)

## Plotly
* [Create Bubble chart](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Plotly/Create%20Bubble%20chart.ipynb)
* [Create Candlestick chart](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Plotly/Create%20Candlestick%20chart.ipynb)
* [Create Gantt chart](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Plotly/Create%20Gantt%20chart.ipynb)
* [Create Horizontal Bar Chart (Basic)](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Plotly/Create%20Horizontal%20Bar%20Chart%20%28Basic%29.ipynb)
* [Create Line Chart (Basic)](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Plotly/Create%20Line%20Chart%20%28Basic%29.ipynb)
* [Create Waterfall chart (Advanced)](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Plotly/Create%20Waterfall%20chart%20%28Advanced%29.ipynb)
* [Create Waterfall chart (Basic)](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Plotly/Create%20Waterfall%20chart%20%28Basic%29.ipynb)
* [Bubblechart](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Plotly/Plotly_Bubblechart.ipynb)
* [Candlestick](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Plotly/Plotly_Candlestick.ipynb)
* [Create Linechart](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Plotly/Plotly_Create_Linechart.ipynb)
* [Heatmap](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Plotly/Plotly_Heatmap.ipynb)
* [Mapchart world](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Plotly/Plotly_Mapchart_world.ipynb)
* [Vertical Barchart stacked](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Plotly/Plotly_Vertical_Barchart_stacked.ipynb)
* [Waterfall chart simple](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Plotly/Plotly_Waterfall_chart_simple.ipynb)

	### Pandas
	- [Looping Over Dataframe](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Python%20Snippets/Pandas/Looping_Over_Dataframe.ipynb)
	- [Pandas ISO Date Conversion](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Python%20Snippets/Pandas/Pandas_ISO_Date_Conversion.ipynb)

## Python
* [Consolidate Excel files](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Python/Python_Consolidate_Excel_files.ipynb)
* [Looping Over Dataframe](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Python/Python_Looping_Over_Dataframe.ipynb)

## Qonto
* [Get cash position trend](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Qonto/Qonto_Get_cash_position_trend.ipynb)
* [Get organizations](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Qonto/Qonto_Get_organizations.ipynb)
* [Get positions](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Qonto/Qonto_Get_positions.ipynb)
* [Get statement](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Qonto/Qonto_Get_statement.ipynb)
* [Get statement barline](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Qonto/Qonto_Get_statement_barline.ipynb)
* [Get statement ranking by category](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Qonto/Qonto_Get_statement_ranking_by_category.ipynb)
* [Get statement summary by operation type](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Qonto/Qonto_Get_statement_summary_by_operation_type.ipynb)
* [Get transactions](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Qonto/Qonto_Get_transactions.ipynb)
* [Releve de compte augmente](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Qonto/Qonto_Releve_de_compte_augmente.ipynb)

## Quandl
* [Get data from API](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Quandl/Quandl_Get_data_from_API.ipynb)
* [Get data from CSV](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Quandl/Quandl_Get_data_from_CSV.ipynb)

## Reddit
* [Get Hot Posts From Subreddit](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Reddit/Reddit_Get_Hot_Posts_From_Subreddit.ipynb)

## Redshift
* [Connect with SQL Magic and IAM Credentials](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Redshift/Redshift_Connect_with_SQL_Magic_and_IAM_Credentials.ipynb)

## Remoteok
* [Get jobs from categories](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Remoteok/Remoteok_Get_jobs_from_categories.ipynb)
* [Post daily jobs on slack](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Remoteok/Remoteok_Post_daily_jobs_on_slack.ipynb)

## Remotive
* [Get categories from job](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Remotive/Remotive_Get_categories_from_job.ipynb)
* [Get jobs from categories](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Remotive/Remotive_Get_jobs_from_categories.ipynb)
* [Post daily jobs on slack](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Remotive/Remotive_Post_daily_jobs_on_slack.ipynb)
* [Send jobs to gsheet](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Remotive/Remotive_Send_jobs_to_gsheet.ipynb)

## SAP-HANA
* [Query data](https://github.com/jupyter-naas/awesome-notebooks/tree/master/SAP-HANA/SAP-HANA_Query_data.ipynb)

## Slack
* [Send message](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Slack/Slack_Send_message.ipynb)

## Snowflake
* [Create table from csv](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Snowflake/Snowflake_Create_table_from_csv.ipynb)
* [Delete table](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Snowflake/Snowflake_Delete_table.ipynb)
* [Read Table](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Snowflake/Snowflake_Read_Table.ipynb)
* [Update table](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Snowflake/Snowflake_Update_table.ipynb)

## Societe.com
* [Get company details](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Societe.com/get_company_details.ipynb)
* [Get societe.ninja](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Societe.com/get_societe.ninja.ipynb)
* [Get verif.com](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Societe.com/get_verif.com.ipynb)

## Spotify
* [Create Radar Chart to analyze Playlist](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Spotify/Spotify_Create_Radar_Chart_to_analyze_Playlist.ipynb)

## Streamlit
* [Create prediction app](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Streamlit/Streamlit_Create_prediction_app.ipynb)

## Stripe
* [Get balances](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Stripe/Stripe_Get_balances.ipynb)
* [Get charges](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Stripe/Stripe_Get_charges.ipynb)
* [Get customers](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Stripe/Stripe_Get_customers.ipynb)

## Telegram
* [Create crypto sentiment bot](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Telegram/Telegram_Create_crypto_sentiment_bot.ipynb)

## Thinkific
* [Get users](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Thinkific/Thinkific_Get_users.ipynb)
* [Send users](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Thinkific/Thinkific_Send_users.ipynb)

## Trello
* [Get board data](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Trello/Trello_Get_board_data.ipynb)

## Twitter
* [Get tweets from search](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Twitter/Twitter_Get_tweets_from_search.ipynb)
* [Get tweets stats from profile](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Twitter/Twitter_Get_tweets_stats_from_profile.ipynb)
* [Get user data](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Twitter/Twitter_Get_user_data.ipynb)
* [Post text and image](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Twitter/Twitter_Post_text_and_image.ipynb)
* [Schedule posts](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Twitter/Twitter_Schedule_posts.ipynb)

## WHI
* [](https://github.com/jupyter-naas/awesome-notebooks/tree/master/WHI/WHI.ipynb)

	### indicators
	- [Johns Hopkins Covid19 Active Cases](https://github.com/jupyter-naas/awesome-notebooks/tree/master/WHI/indicators/Johns_Hopkins_Covid19_Active_Cases.ipynb)
	- [NASA Artic sea ice](https://github.com/jupyter-naas/awesome-notebooks/tree/master/WHI/indicators/NASA_Artic_sea_ice.ipynb)
	- [NASA Global temperature](https://github.com/jupyter-naas/awesome-notebooks/tree/master/WHI/indicators/NASA_Global_temperature.ipynb)
	- [NASA indicate sealevel](https://github.com/jupyter-naas/awesome-notebooks/tree/master/WHI/indicators/NASA_indicate_sealevel.ipynb)

## WSR
* [John Hopkins Active covid cases worldmap](https://github.com/jupyter-naas/awesome-notebooks/tree/master/WSR/John_Hopkins_Active_covid_cases_worldmap.ipynb)

## WorldBank
* [GDP contributors](https://github.com/jupyter-naas/awesome-notebooks/tree/master/WorldBank/WorldBank_GDP_contributors.ipynb)
* [GDP per capita and growth](https://github.com/jupyter-naas/awesome-notebooks/tree/master/WorldBank/WorldBank_GDP_per_capita_and_growth.ipynb)
* [GDP per country and evolution](https://github.com/jupyter-naas/awesome-notebooks/tree/master/WorldBank/WorldBank_GDP_per_country_and_evolution.ipynb)
* [Gini index](https://github.com/jupyter-naas/awesome-notebooks/tree/master/WorldBank/WorldBank_Gini_index.ipynb)
* [Most populated countries](https://github.com/jupyter-naas/awesome-notebooks/tree/master/WorldBank/WorldBank_Most_populated_countries.ipynb)
* [Richest countries top10](https://github.com/jupyter-naas/awesome-notebooks/tree/master/WorldBank/WorldBank_Richest_countries_top10.ipynb)
* [World employment by sector](https://github.com/jupyter-naas/awesome-notebooks/tree/master/WorldBank/WorldBank_World_employment_by_sector.ipynb)
* [World population and density](https://github.com/jupyter-naas/awesome-notebooks/tree/master/WorldBank/WorldBank_World_population_and_density.ipynb)

## Worldometer
* [World population evolution and projections](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Worldometer/Worldometer_World_population_evolution_and_projections.ipynb)

## XML
* [Transform sitemap to dataframe](https://github.com/jupyter-naas/awesome-notebooks/tree/master/XML/XML_Transform_sitemap_to_dataframe.ipynb)

## YahooFinance
* [Candlestick chart](https://github.com/jupyter-naas/awesome-notebooks/tree/master/YahooFinance/YahooFinance_Candlestick_chart.ipynb)
* [Cryptocurrencies heatmap correlation graph](https://github.com/jupyter-naas/awesome-notebooks/tree/master/YahooFinance/YahooFinance_Cryptocurrencies_heatmap_correlation_graph.ipynb)
* [Display chart from ticker](https://github.com/jupyter-naas/awesome-notebooks/tree/master/YahooFinance/YahooFinance_Display_chart_from_ticker.ipynb)
* [Get Stock Update](https://github.com/jupyter-naas/awesome-notebooks/tree/master/YahooFinance/YahooFinance_Get_Stock_Update.ipynb)
* [Get USDEUR data and chart](https://github.com/jupyter-naas/awesome-notebooks/tree/master/YahooFinance/YahooFinance_Get_USDEUR_data_and_chart.ipynb)
* [Get data from ticker](https://github.com/jupyter-naas/awesome-notebooks/tree/master/YahooFinance/YahooFinance_Get_data_from_ticker.ipynb)
* [Send daily prediction to Email](https://github.com/jupyter-naas/awesome-notebooks/tree/master/YahooFinance/YahooFinance_Send_daily_prediction_to_Email.ipynb)
* [Send daily prediction to Slack](https://github.com/jupyter-naas/awesome-notebooks/tree/master/YahooFinance/YahooFinance_Send_daily_prediction_to_Slack.ipynb)

## Youtube
* [Download video](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Youtube/Youtube_Download_video.ipynb)
* [Extract and summarize transcript](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Youtube/Youtube_Extract_and_summarize_transcript.ipynb)
* [Extract transcript from video](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Youtube/Youtube_Extract_transcript_from_video.ipynb)
* [Get statistics from channel](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Youtube/Youtube_Get_statistics_from_channel.ipynb)
* [Get statistics from video](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Youtube/Youtube_Get_statistics_from_video.ipynb)
* [Get uploads from channel](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Youtube/Youtube_Get_uploads_from_channel.ipynb)
* [Summarize video](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Youtube/Youtube_Summarize_video.ipynb)

## ZIP
* [Extract files](https://github.com/jupyter-naas/awesome-notebooks/tree/master/ZIP/ZIP_Extract_files.ipynb)

## Zapier
* [Trigger workflow](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Zapier/Zapier_Trigger_workflow.ipynb)


<br/>
Maintained by CashStory SAS (Naas mother company).
<br/>
Contact us to learn more on our website chat : https://naas.ai

