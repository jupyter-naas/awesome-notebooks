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
* [Read dataframe from S3](https://github.com/jupyter-naas/awesome-notebooks/tree/master/AWS/AWS_Read_dataframe_from_S3.ipynb)
* [Send dataframe to S3](https://github.com/jupyter-naas/awesome-notebooks/tree/master/AWS/AWS_Send_dataframe_to_S3.ipynb)
* [Upload file to S3 bucket](https://github.com/jupyter-naas/awesome-notebooks/tree/master/AWS/AWS_Upload_file_to_S3_bucket.ipynb)

## Airtable
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
* [Send data](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Bubble/Bubble_Send_data.ipynb)

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

## D-Tale
* [Visualize dataframe](https://github.com/jupyter-naas/awesome-notebooks/tree/master/D-Tale/D-Tale_Visualize_dataframe.ipynb)

## Dask
* [Parallelize operations on multiple csvs](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Dask/Dask_parallelize_operations_on_multiple_csvs.ipynb)

## Data.gouv.fr
* [COVID19 -  FR - Entrées et sorties par région pour 1 million d'hab.](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Data.gouv.fr/COVID19%20-%20%20FR%20-%20Entr%C3%A9es%20et%20sorties%20par%20r%C3%A9gion%20pour%201%20million%20d%27hab..ipynb)
* [Récupération données légales entreprise](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Data.gouv.fr/Data.gouv.fr_R%C3%A9cup%C3%A9ration_donn%C3%A9es_l%C3%A9gales_entreprise.ipynb)

## Draft Kings
* [Get NBA Moneylines](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Draft%20Kings/Draft_Kings_Get_NBA_Moneylines.ipynb)

## EM-DAT
* [Natural disasters](https://github.com/jupyter-naas/awesome-notebooks/tree/master/EM-DAT/EM-DAT_natural_disasters.ipynb)

## Elasticsearch
* [Connect to server](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Elasticsearch/Elasticsearch_Connect_to_server.ipynb)

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

## GitHub
* [Add new issues as page in Notion database](https://github.com/jupyter-naas/awesome-notebooks/tree/master/GitHub/GitHub_Add_new_issues_as_page_in_Notion_database.ipynb)
* [Add new member to team](https://github.com/jupyter-naas/awesome-notebooks/tree/master/GitHub/GitHub_Add_new_member_to_team.ipynb)
* [Close issue](https://github.com/jupyter-naas/awesome-notebooks/tree/master/GitHub/GitHub_Close_issue.ipynb)
* [Create issue](https://github.com/jupyter-naas/awesome-notebooks/tree/master/GitHub/GitHub_Create_issue.ipynb)
* [Download file from url](https://github.com/jupyter-naas/awesome-notebooks/tree/master/GitHub/GitHub_Download_file_from_url.ipynb)
* [Get active projects](https://github.com/jupyter-naas/awesome-notebooks/tree/master/GitHub/GitHub_Get_active_projects.ipynb)
* [Get commits ranking from repository](https://github.com/jupyter-naas/awesome-notebooks/tree/master/GitHub/GitHub_Get_commits_ranking_from_repository.ipynb)
* [Get issues from repo](https://github.com/jupyter-naas/awesome-notebooks/tree/master/GitHub/GitHub_Get_issues_from_repo.ipynb)
* [Get profile from user](https://github.com/jupyter-naas/awesome-notebooks/tree/master/GitHub/GitHub_Get_profile_from_user.ipynb)
* [Get profiles from teams](https://github.com/jupyter-naas/awesome-notebooks/tree/master/GitHub/GitHub_Get_profiles_from_teams.ipynb)
* [Get pull requests from repository](https://github.com/jupyter-naas/awesome-notebooks/tree/master/GitHub/GitHub_Get_pull_requests_from_repository.ipynb)
* [Get stargazers from repository](https://github.com/jupyter-naas/awesome-notebooks/tree/master/GitHub/GitHub_Get_stargazers_from_repository.ipynb)
* [Get weekly commits from repository](https://github.com/jupyter-naas/awesome-notebooks/tree/master/GitHub/GitHub_Get_weekly_commits_from_repository.ipynb)
* [Peform basic actions](https://github.com/jupyter-naas/awesome-notebooks/tree/master/GitHub/GitHub_Peform_basic_actions.ipynb)
* [Read issue](https://github.com/jupyter-naas/awesome-notebooks/tree/master/GitHub/GitHub_Read_issue.ipynb)
* [Track issues on projects](https://github.com/jupyter-naas/awesome-notebooks/tree/master/GitHub/GitHub_Track_issues_on_projects.ipynb)
* [Track notebooks created over time](https://github.com/jupyter-naas/awesome-notebooks/tree/master/GitHub/GitHub_Track_notebooks_created_over_time.ipynb)

## Gmail
* [Automate response from keywords in mailbox](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Gmail/Gmail_Automate_response_from_keywords_in_mailbox.ipynb)
* [Clean mailbox](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Gmail/Gmail_Clean_mailbox.ipynb)
* [Read mailbox](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Gmail/Gmail_Read_mailbox.ipynb)
* [Schedule mailbox cleaning](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Gmail/Gmail_Schedule_mailbox_cleaning.ipynb)
* [Send emails from Gsheet classic](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Gmail/Gmail_Send_emails_from_Gsheet_classic.ipynb)
* [Send emails from Gsheet specific](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Gmail/Gmail_Send_emails_from_Gsheet_specific.ipynb)

## Google Analytics
* [Follow average session duration daily](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Google%20Analytics/Google_Analytics_Follow_average_session_duration_daily.ipynb)
* [Follow number of new visitors daily](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Google%20Analytics/Google_Analytics_Follow_number_of_new_visitors_daily.ipynb)
* [Follow number of sessions daily](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Google%20Analytics/Google_Analytics_Follow_number_of_sessions_daily.ipynb)
* [Follow number of visitors daily](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Google%20Analytics/Google_Analytics_Follow_number_of_visitors_daily.ipynb)
* [Get bounce rate](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Google%20Analytics/Google_Analytics_Get_bounce_rate.ipynb)
* [Get pageview ranking](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Google%20Analytics/Google_Analytics_Get_pageview_ranking.ipynb)
* [Get stats per country](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Google%20Analytics/Google_Analytics_Get_stats_per_country.ipynb)
* [Get time on landing page](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Google%20Analytics/Google_Analytics_Get_time_on_landing_page.ipynb)
* [Get unique visitors](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Google%20Analytics/Google_Analytics_Get_unique_visitors.ipynb)
* [Get unique visitors by country](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Google%20Analytics/Google_Analytics_Get_unique_visitors_by_country.ipynb)

## Google Drive
* [Download file](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Google%20Drive/Google_Drive_Download_file.ipynb)

## Google Search
* [Get LinkedIn company url from name](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Google%20Search/Google_Search_Get_LinkedIn_company_url_from_name.ipynb)
* [Get LinkedIn profile url from name](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Google%20Search/Google_Search_Get_LinkedIn_profile_url_from_name.ipynb)
* [Perform search](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Google%20Search/Google_Search_Perform_search.ipynb)

## Google Sheets
* [Add items to Notion databases from new rows in](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Google%20Sheets/Google_Sheets_Add_items_to_Notion_databases_from_new_rows_in_Google_Sheets.ipynb)
* [Get data](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Google%20Sheets/Google_Sheets_Get_data.ipynb)
* [Send LinkedIn invitations from spreadsheet](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Google%20Sheets/Google_Sheets_Send_LinkedIn_invitations_from_spreadsheet.ipynb)
* [Send data](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Google%20Sheets/Google_Sheets_Send_data.ipynb)
* [Send data to MongoDB](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Google%20Sheets/Google_Sheets_Send_data_to_MongoDB.ipynb)
* [Send emails from sheet](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Google%20Sheets/Google_Sheets_Send_emails_from_sheet.ipynb)

## HTML
* [Create a website](https://github.com/jupyter-naas/awesome-notebooks/tree/master/HTML/HTML_Create_a_website.ipynb)

## Healthchecks
* [Perfom basic actions](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Healthchecks/Healthchecks_Perfom_basic_actions.ipynb)

## HubSpot
* [Associate contact to deal](https://github.com/jupyter-naas/awesome-notebooks/tree/master/HubSpot/HubSpot_Associate_contact_to_deal.ipynb)
* [Create Task](https://github.com/jupyter-naas/awesome-notebooks/tree/master/HubSpot/HubSpot_Create_Task.ipynb)
* [Create contact](https://github.com/jupyter-naas/awesome-notebooks/tree/master/HubSpot/HubSpot_Create_contact.ipynb)
* [Create contacts from linkedin post likes](https://github.com/jupyter-naas/awesome-notebooks/tree/master/HubSpot/HubSpot_Create_contacts_from_linkedin_post_likes.ipynb)
* [Create deal](https://github.com/jupyter-naas/awesome-notebooks/tree/master/HubSpot/HubSpot_Create_deal.ipynb)
* [Delete Task](https://github.com/jupyter-naas/awesome-notebooks/tree/master/HubSpot/HubSpot_Delete_Task.ipynb)
* [Delete contact](https://github.com/jupyter-naas/awesome-notebooks/tree/master/HubSpot/HubSpot_Delete_contact.ipynb)
* [Delete deal](https://github.com/jupyter-naas/awesome-notebooks/tree/master/HubSpot/HubSpot_Delete_deal.ipynb)
* [Get Task](https://github.com/jupyter-naas/awesome-notebooks/tree/master/HubSpot/HubSpot_Get_Task.ipynb)
* [Get all contacts](https://github.com/jupyter-naas/awesome-notebooks/tree/master/HubSpot/HubSpot_Get_all_contacts.ipynb)
* [Get all deals](https://github.com/jupyter-naas/awesome-notebooks/tree/master/HubSpot/HubSpot_Get_all_deals.ipynb)
* [Get all pipelines and dealstages](https://github.com/jupyter-naas/awesome-notebooks/tree/master/HubSpot/HubSpot_Get_all_pipelines_and_dealstages.ipynb)
* [Get closed deals weekly](https://github.com/jupyter-naas/awesome-notebooks/tree/master/HubSpot/HubSpot_Get_closed_deals_weekly.ipynb)
* [Get contact](https://github.com/jupyter-naas/awesome-notebooks/tree/master/HubSpot/HubSpot_Get_contact.ipynb)
* [Get contacts associated to deal](https://github.com/jupyter-naas/awesome-notebooks/tree/master/HubSpot/HubSpot_Get_contacts_associated_to_deal.ipynb)
* [Get deal](https://github.com/jupyter-naas/awesome-notebooks/tree/master/HubSpot/HubSpot_Get_deal.ipynb)
* [Get new deals created weekly](https://github.com/jupyter-naas/awesome-notebooks/tree/master/HubSpot/HubSpot_Get_new_deals_created_weekly.ipynb)
* [Send LinkedIn invitations from contacts](https://github.com/jupyter-naas/awesome-notebooks/tree/master/HubSpot/HubSpot_Send_LinkedIn_invitations_from_contacts.ipynb)
* [Send contacts to gsheet](https://github.com/jupyter-naas/awesome-notebooks/tree/master/HubSpot/HubSpot_Send_contacts_to_gsheet.ipynb)
* [Send deals to gsheet](https://github.com/jupyter-naas/awesome-notebooks/tree/master/HubSpot/HubSpot_Send_deals_to_gsheet.ipynb)
* [Send sales brief](https://github.com/jupyter-naas/awesome-notebooks/tree/master/HubSpot/HubSpot_Send_sales_brief.ipynb)
* [Update Task](https://github.com/jupyter-naas/awesome-notebooks/tree/master/HubSpot/HubSpot_Update_Task.ipynb)
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

## INPI
* [Download PDF recap](https://github.com/jupyter-naas/awesome-notebooks/tree/master/INPI/INPI_Download_PDF_recap.ipynb)

## IUCN
* [Extinct species](https://github.com/jupyter-naas/awesome-notebooks/tree/master/IUCN/IUCN_Extinct_species.ipynb)

## Insee
* [Download PDF recap](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Insee/Insee_Download_PDF_recap.ipynb)

## Instagram
* [Get stats from posts](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Instagram/Instagram_Get_stats_from_posts.ipynb)
* [Post image and caption](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Instagram/Instagram_Post_image_and_caption.ipynb)

## Integromat
* [Trigger workflow](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Integromat/Integromat_Trigger_workflow.ipynb)

## Johns Hopkins
* [Covid19 Active Cases](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Johns%20Hopkins/Johns_Hopkins_Covid19_Active_Cases.ipynb)
* [Get Covid19 data](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Johns%20Hopkins/Johns_Hopkins_Get_Covid19_data.ipynb)

## Jupyter Notebooks
* [Add cells in notebook json](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Jupyter%20Notebooks/Jupyter_Notebooks_Add_cells_in_notebook_json.ipynb)
* [Add tags in cells](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Jupyter%20Notebooks/Jupyter_Notebooks_Add_tags_in_cells.ipynb)
* [Count code characters](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Jupyter%20Notebooks/Jupyter_Notebooks_Count_code_characters.ipynb)
* [Count code lines](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Jupyter%20Notebooks/Jupyter_Notebooks_Count_code_lines.ipynb)
* [Get installs](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Jupyter%20Notebooks/Jupyter_Notebooks_Get_installs.ipynb)
* [Get libraries](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Jupyter%20Notebooks/Jupyter_Notebooks_Get_libraries.ipynb)
* [Read file json](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Jupyter%20Notebooks/Jupyter_Notebooks_Read_file_json.ipynb)
* [Save file ipynb](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Jupyter%20Notebooks/Jupyter_Notebooks_Save_file_ipynb.ipynb)

## Jupyter
* [Get server uptime](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Jupyter/Jupyter_Get_server_uptime.ipynb)
* [Get user information](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Jupyter/Jupyter_Get_user_information.ipynb)
* [Get user session](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Jupyter/Jupyter_Get_user_session.ipynb)
* [Get user terminal](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Jupyter/Jupyter_Get_user_terminal.ipynb)
* [Restart server](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Jupyter/Jupyter_Restart_server.ipynb)

## LinkedIn
* [Accept all invitations and send first message](https://github.com/jupyter-naas/awesome-notebooks/tree/master/LinkedIn/LinkedIn_Accept_all_invitations_and_send_first_message.ipynb)
* [Accept invitation received](https://github.com/jupyter-naas/awesome-notebooks/tree/master/LinkedIn/LinkedIn_Accept_invitation_received.ipynb)
* [Follow company followers](https://github.com/jupyter-naas/awesome-notebooks/tree/master/LinkedIn/LinkedIn_Follow_company_followers.ipynb)
* [Generate leads from posts](https://github.com/jupyter-naas/awesome-notebooks/tree/master/LinkedIn/LinkedIn_Generate_leads_from_posts.ipynb)
* [Get comments from post](https://github.com/jupyter-naas/awesome-notebooks/tree/master/LinkedIn/LinkedIn_Get_comments_from_post.ipynb)
* [Get company followers](https://github.com/jupyter-naas/awesome-notebooks/tree/master/LinkedIn/LinkedIn_Get_company_followers.ipynb)
* [Get connections from network](https://github.com/jupyter-naas/awesome-notebooks/tree/master/LinkedIn/LinkedIn_Get_connections_from_network.ipynb)
* [Get contact from profile](https://github.com/jupyter-naas/awesome-notebooks/tree/master/LinkedIn/LinkedIn_Get_contact_from_profile.ipynb)
* [Get conversations](https://github.com/jupyter-naas/awesome-notebooks/tree/master/LinkedIn/LinkedIn_Get_conversations.ipynb)
* [Get followers from network](https://github.com/jupyter-naas/awesome-notebooks/tree/master/LinkedIn/LinkedIn_Get_followers_from_network.ipynb)
* [Get guests from event](https://github.com/jupyter-naas/awesome-notebooks/tree/master/LinkedIn/LinkedIn_Get_guests_from_event.ipynb)
* [Get identity from profile](https://github.com/jupyter-naas/awesome-notebooks/tree/master/LinkedIn/LinkedIn_Get_identity_from_profile.ipynb)
* [Get info from company](https://github.com/jupyter-naas/awesome-notebooks/tree/master/LinkedIn/LinkedIn_Get_info_from_company.ipynb)
* [Get invitations received](https://github.com/jupyter-naas/awesome-notebooks/tree/master/LinkedIn/LinkedIn_Get_invitations_received.ipynb)
* [Get invitations sent](https://github.com/jupyter-naas/awesome-notebooks/tree/master/LinkedIn/LinkedIn_Get_invitations_sent.ipynb)
* [Get likes from post](https://github.com/jupyter-naas/awesome-notebooks/tree/master/LinkedIn/LinkedIn_Get_likes_from_post.ipynb)
* [Get messages from profile](https://github.com/jupyter-naas/awesome-notebooks/tree/master/LinkedIn/LinkedIn_Get_messages_from_profile.ipynb)
* [Get network from profile](https://github.com/jupyter-naas/awesome-notebooks/tree/master/LinkedIn/LinkedIn_Get_network_from_profile.ipynb)
* [Get polls from post](https://github.com/jupyter-naas/awesome-notebooks/tree/master/LinkedIn/LinkedIn_Get_polls_from_post.ipynb)
* [Get posts stats from profile](https://github.com/jupyter-naas/awesome-notebooks/tree/master/LinkedIn/LinkedIn_Get_posts_stats_from_profile.ipynb)
* [Get resume from profile](https://github.com/jupyter-naas/awesome-notebooks/tree/master/LinkedIn/LinkedIn_Get_resume_from_profile.ipynb)
* [Get stats from post](https://github.com/jupyter-naas/awesome-notebooks/tree/master/LinkedIn/LinkedIn_Get_stats_from_post.ipynb)
* [Ignore invitation received](https://github.com/jupyter-naas/awesome-notebooks/tree/master/LinkedIn/LinkedIn_Ignore_invitation_received.ipynb)
* [Send comments from post to gsheet](https://github.com/jupyter-naas/awesome-notebooks/tree/master/LinkedIn/LinkedIn_Send_comments_from_post_to_gsheet.ipynb)
* [Send company followers to Google Sheets](https://github.com/jupyter-naas/awesome-notebooks/tree/master/LinkedIn/LinkedIn_Send_company_followers_to_Google_Sheets.ipynb)
* [Send connections from network to gsheet](https://github.com/jupyter-naas/awesome-notebooks/tree/master/LinkedIn/LinkedIn_Send_connections_from_network_to_gsheet.ipynb)
* [Send invitation to company followers](https://github.com/jupyter-naas/awesome-notebooks/tree/master/LinkedIn/LinkedIn_Send_invitation_to_company_followers.ipynb)
* [Send invitation to profile](https://github.com/jupyter-naas/awesome-notebooks/tree/master/LinkedIn/LinkedIn_Send_invitation_to_profile.ipynb)
* [Send invitation to profile from post likes](https://github.com/jupyter-naas/awesome-notebooks/tree/master/LinkedIn/LinkedIn_Send_invitation_to_profile_from_post_likes.ipynb)
* [Send likes from post to gsheet](https://github.com/jupyter-naas/awesome-notebooks/tree/master/LinkedIn/LinkedIn_Send_likes_from_post_to_gsheet.ipynb)
* [Send message to profile](https://github.com/jupyter-naas/awesome-notebooks/tree/master/LinkedIn/LinkedIn_Send_message_to_profile.ipynb)
* [Send message to profile from post likes](https://github.com/jupyter-naas/awesome-notebooks/tree/master/LinkedIn/LinkedIn_Send_message_to_profile_from_post_likes.ipynb)
* [Send posts feed to gsheet](https://github.com/jupyter-naas/awesome-notebooks/tree/master/LinkedIn/LinkedIn_Send_posts_feed_to_gsheet.ipynb)
* [Send weekly post engagement metrics by email](https://github.com/jupyter-naas/awesome-notebooks/tree/master/LinkedIn/LinkedIn_Send_weekly_post_engagement_metrics_by_email.ipynb)
* [Update metrics from posts in Notion content calendar](https://github.com/jupyter-naas/awesome-notebooks/tree/master/LinkedIn/LinkedIn_Update_metrics_from_posts_in_Notion_content_calendar.ipynb)
* [Linkedin Follow number of content published](https://github.com/jupyter-naas/awesome-notebooks/tree/master/LinkedIn/Linkedin_Follow_number_of_content_published.ipynb)
* [Linkedin Follow total content views](https://github.com/jupyter-naas/awesome-notebooks/tree/master/LinkedIn/Linkedin_Follow_total_content_views.ipynb)

## Matplotlib
* [Create Waterfall chart](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Matplotlib/Matplotlib_Create_Waterfall_chart.ipynb)

## Metrics Store
* [Content creation Track connections](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Metrics%20Store/Content_creation_Track_connections.ipynb)

## Microsoft Teams
* [Send message](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Microsoft%20Teams/Microsoft_Teams_Send_message.ipynb)

## Microsoft Word
* [Convert to HMTL](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Microsoft%20Word/Microsoft_Word_Convert_to_HMTL.ipynb)

## MongoDB
* [Get data](https://github.com/jupyter-naas/awesome-notebooks/tree/master/MongoDB/MongoDB_Get_data.ipynb)
* [Send data](https://github.com/jupyter-naas/awesome-notebooks/tree/master/MongoDB/MongoDB_Send_data.ipynb)
* [Send data to Google Sheets](https://github.com/jupyter-naas/awesome-notebooks/tree/master/MongoDB/MongoDB_Send_data_to_Google_Sheets.ipynb)

## MySQL
* [Query database](https://github.com/jupyter-naas/awesome-notebooks/tree/master/MySQL/MySQL_Query_database.ipynb)

## NASA
* [Artic sea ice](https://github.com/jupyter-naas/awesome-notebooks/tree/master/NASA/NASA_Artic_sea_ice.ipynb)
* [Global temperature](https://github.com/jupyter-naas/awesome-notebooks/tree/master/NASA/NASA_Global_temperature.ipynb)
* [Sea level](https://github.com/jupyter-naas/awesome-notebooks/tree/master/NASA/NASA_Sea_level.ipynb)

## Naas Auth
* [Bearer validate](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Naas%20Auth/Naas_Auth_bearer_validate.ipynb)
* [Connect](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Naas%20Auth/Naas_Auth_connect.ipynb)
* [Users me](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Naas%20Auth/Naas_Auth_users_me.ipynb)

## Naas
* [Asset demo](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Naas/Naas_Asset_demo.ipynb)
* [Automate GitHub Auth](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Naas/Naas_Automate_GitHub_Auth.ipynb)
* [Configure Github with ssh](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Naas/Naas_Configure_Github_with_ssh.ipynb)
* [Credits Get Balance](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Naas/Naas_Credits_Get_Balance.ipynb)
* [Dependency demo](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Naas/Naas_Dependency_demo.ipynb)
* [Doc demo](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Naas/Naas_Doc_demo.ipynb)
* [Domain demo](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Naas/Naas_Domain_demo.ipynb)
* [Emailbuilder demo](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Naas/Naas_Emailbuilder_demo.ipynb)
* [Get Transactions](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Naas/Naas_Get_Transactions.ipynb)
* [Get help](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Naas/Naas_Get_help.ipynb)
* [Get number of downloads naas drivers package](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Naas/Naas_Get_number_of_downloads_naas_drivers_package.ipynb)
* [Get number of downloads naas package](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Naas/Naas_Get_number_of_downloads_naas_package.ipynb)
* [Get total downloads naas libraries](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Naas/Naas_Get_total_downloads_naas_libraries.ipynb)
* [NLP Examples](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Naas/Naas_NLP_Examples.ipynb)
* [Notification demo](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Naas/Naas_Notification_demo.ipynb)
* [Remove Scheduler Outputs](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Naas/Naas_Remove_Scheduler_Outputs.ipynb)
* [Reset Instance](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Naas/Naas_Reset_Instance.ipynb)
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
* [Add paragraph with link in page](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Notion/Notion_Add_paragraph_with_link_in_page.ipynb)
* [Create page](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Notion/Notion_Create_page.ipynb)
* [Explore API](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Notion/Notion_Explore_API.ipynb)
* [Generate Google Sheets rows for new items in  database](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Notion/Notion_Generate_Google_Sheets_rows_for_new_items_in_Notion_database.ipynb)
* [Get database](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Notion/Notion_Get_database.ipynb)
* [Get users](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Notion/Notion_Get_users.ipynb)
* [Send LinkedIn invitations from database](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Notion/Notion_Send_LinkedIn_invitations_from_database.ipynb)
* [Send Slack Messages For New  Database Items](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Notion/Notion_Send_Slack_Messages_For_New_Notion_Database_Items.ipynb)
* [Sent Gmail On New Item](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Notion/Notion_Sent_Gmail_On_New_Item.ipynb)
* [Update page](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Notion/Notion_Update_page.ipynb)
* [Update pages from database](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Notion/Notion_Update_pages_from_database.ipynb)

## OpenWeatherMap
* [Get City Weather](https://github.com/jupyter-naas/awesome-notebooks/tree/master/OpenWeatherMap/OpenWeatherMap_Get_City_Weather.ipynb)
* [Send daily email with predictions](https://github.com/jupyter-naas/awesome-notebooks/tree/master/OpenWeatherMap/OpenWeatherMap_Send_daily_email_with_predictions.ipynb)

## OwnCloud
* [Download file](https://github.com/jupyter-naas/awesome-notebooks/tree/master/OwnCloud/OwnCloud_Download_file.ipynb)
* [Upload file](https://github.com/jupyter-naas/awesome-notebooks/tree/master/OwnCloud/OwnCloud_Upload_file.ipynb)

## PDF
* [Transform to MP3](https://github.com/jupyter-naas/awesome-notebooks/tree/master/PDF/PDF_Transform_to_MP3.ipynb)

## Pandas
* [Create Pivot Table](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Pandas/Pandas_Create_Pivot_Table.ipynb)
* [Create dataframe from dict](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Pandas/Pandas_Create_dataframe_from_dict.ipynb)
* [Format number to string](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Pandas/Pandas_Format_number_to_string.ipynb)
* [ISO Date Conversion](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Pandas/Pandas_ISO_Date_Conversion.ipynb)
* [Merge Dataframes](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Pandas/Pandas_Merge_Dataframes.ipynb)
* [Transform dataframe to dict](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Pandas/Pandas_Transform_dataframe_to_dict.ipynb)

## Pillow
* [Add data to image](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Pillow/Pillow_Add_data_to_image.ipynb)

## Pipedrive
* [Get contact](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Pipedrive/Pipedrive_Get_contact.ipynb)

## Plaid
* [Get accounts](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Plaid/Plaid_Get_accounts.ipynb)
* [Get transactions](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Plaid/Plaid_Get_transactions.ipynb)

## Plotly
* [Create Bubblechart](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Plotly/Plotly_Create_Bubblechart.ipynb)
* [Create Candlestick](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Plotly/Plotly_Create_Candlestick.ipynb)
* [Create Gantt chart](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Plotly/Plotly_Create_Gantt_chart.ipynb)
* [Create Heatmap](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Plotly/Plotly_Create_Heatmap.ipynb)
* [Create Horizontal Barchart](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Plotly/Plotly_Create_Horizontal_Barchart.ipynb)
* [Create Leaderboard](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Plotly/Plotly_Create_Leaderboard.ipynb)
* [Create Leaderboard stacked](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Plotly/Plotly_Create_Leaderboard_stacked.ipynb)
* [Create Linechart](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Plotly/Plotly_Create_Linechart.ipynb)
* [Create Mapchart world](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Plotly/Plotly_Create_Mapchart_world.ipynb)
* [Create Vertical Barchart](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Plotly/Plotly_Create_Vertical_Barchart.ipynb)
* [Create Vertical Barchart group](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Plotly/Plotly_Create_Vertical_Barchart_group.ipynb)
* [Create Vertical Barchart stacked](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Plotly/Plotly_Create_Vertical_Barchart_stacked.ipynb)
* [Create Waterfall chart](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Plotly/Plotly_Create_Waterfall_chart.ipynb)

## PostgresSQL
* [Get data from database](https://github.com/jupyter-naas/awesome-notebooks/tree/master/PostgresSQL/PostgresSQL_Get_data_from_database.ipynb)

## PyPI
* [- Get number of downloads any package](https://github.com/jupyter-naas/awesome-notebooks/tree/master/PyPI/PyPI%20-%20Get_number_of_downloads_any_package.ipynb)

## Python
* [Consolidate Excel files](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Python/Python_Consolidate_Excel_files.ipynb)
* [Create dataframe from lists](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Python/Python_Create_dataframe_from_lists.ipynb)
* [Create dict from lists](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Python/Python_Create_dict_from_lists.ipynb)
* [Download PDF from URL](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Python/Python_Download_PDF_from_URL.ipynb)
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

## SendGrid
* [Get all messages](https://github.com/jupyter-naas/awesome-notebooks/tree/master/SendGrid/SendGrid_Get_all_messages.ipynb)
* [Send message](https://github.com/jupyter-naas/awesome-notebooks/tree/master/SendGrid/SendGrid_Send_message.ipynb)

## Slack
* [Add new user to Google Sheets](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Slack/Slack_Add_new_user_to_Google_Sheets.ipynb)
* [Follow number of users in workspace](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Slack/Slack_Follow_number_of_users_in_workspace.ipynb)
* [Send message](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Slack/Slack_Send_message.ipynb)

## Snowflake
* [Create table from csv](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Snowflake/Snowflake_Create_table_from_csv.ipynb)
* [Delete table](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Snowflake/Snowflake_Delete_table.ipynb)
* [Read Table](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Snowflake/Snowflake_Read_Table.ipynb)
* [Update table](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Snowflake/Snowflake_Update_table.ipynb)

## Societe.com
* [Get company details](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Societe.com/Societe.com_Get_company_details.ipynb)
* [Get verif.com](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Societe.com/Societe.com_Get_verif.com.ipynb)

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

## TikTok
* [Get user stats](https://github.com/jupyter-naas/awesome-notebooks/tree/master/TikTok/TikTok_Get_user_stats.ipynb)
* [Get videos stats](https://github.com/jupyter-naas/awesome-notebooks/tree/master/TikTok/TikTok_Get_videos_stats.ipynb)

## Trello
* [Get board data](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Trello/Trello_Get_board_data.ipynb)

## Twilio
* [Send SMS](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Twilio/Twilio_Send_SMS.ipynb)

## Twitter
* [Get posts stats](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Twitter/Twitter_Get_posts_stats.ipynb)
* [Get tweets from search](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Twitter/Twitter_Get_tweets_from_search.ipynb)
* [Get tweets stats from profile](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Twitter/Twitter_Get_tweets_stats_from_profile.ipynb)
* [Get user data](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Twitter/Twitter_Get_user_data.ipynb)
* [Post text and image](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Twitter/Twitter_Post_text_and_image.ipynb)
* [Schedule posts](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Twitter/Twitter_Schedule_posts.ipynb)

## WSR
* [WHI Create indicator](https://github.com/jupyter-naas/awesome-notebooks/tree/master/WSR/WHI_Create_indicator.ipynb)
* [Get daily Covid19 active cases trend JHU](https://github.com/jupyter-naas/awesome-notebooks/tree/master/WSR/WSR_Get_daily_Covid19_active_cases_trend_JHU.ipynb)
* [Get daily Covid19 active cases worldmap JHU](https://github.com/jupyter-naas/awesome-notebooks/tree/master/WSR/WSR_Get_daily_Covid19_active_cases_worldmap_JHU.ipynb)

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
* [Send daily prediction to Notion](https://github.com/jupyter-naas/awesome-notebooks/tree/master/YahooFinance/YahooFinance_Send_daily_prediction_to_Notion.ipynb)
* [Send daily prediction to Slack](https://github.com/jupyter-naas/awesome-notebooks/tree/master/YahooFinance/YahooFinance_Send_daily_prediction_to_Slack.ipynb)

## YouTube
* [Download video](https://github.com/jupyter-naas/awesome-notebooks/tree/master/YouTube/YouTube_Download_video.ipynb)
* [Extract and summarize transcript](https://github.com/jupyter-naas/awesome-notebooks/tree/master/YouTube/YouTube_Extract_and_summarize_transcript.ipynb)
* [Extract transcript from video](https://github.com/jupyter-naas/awesome-notebooks/tree/master/YouTube/YouTube_Extract_transcript_from_video.ipynb)
* [Get statistics from channel](https://github.com/jupyter-naas/awesome-notebooks/tree/master/YouTube/YouTube_Get_statistics_from_channel.ipynb)
* [Get statistics from video](https://github.com/jupyter-naas/awesome-notebooks/tree/master/YouTube/YouTube_Get_statistics_from_video.ipynb)
* [Get uploads from channel](https://github.com/jupyter-naas/awesome-notebooks/tree/master/YouTube/YouTube_Get_uploads_from_channel.ipynb)
* [Summarize video](https://github.com/jupyter-naas/awesome-notebooks/tree/master/YouTube/YouTube_Summarize_video.ipynb)

## ZIP
* [Extract files](https://github.com/jupyter-naas/awesome-notebooks/tree/master/ZIP/ZIP_Extract_files.ipynb)

## Zapier
* [Trigger workflow](https://github.com/jupyter-naas/awesome-notebooks/tree/master/Zapier/Zapier_Trigger_workflow.ipynb)

## spaCy
* [SpaCy Build a sentiment analysis model using Twitter](https://github.com/jupyter-naas/awesome-notebooks/tree/master/spaCy/SpaCy_Build_a_sentiment_analysis_model_using_Twitter.ipynb)


<br/>
Maintained by CashStory SAS (Naas mother company).
<br/>
Contact us to learn more on our website chat : https://naas.ai

