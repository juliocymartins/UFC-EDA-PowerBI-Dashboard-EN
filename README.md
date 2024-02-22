# UFC EDA Dashboard
Project of Exploratory Data Analysis - Ultimate UFC Dataset

## This was my inaugural project intended to enrich my portfolio.

## The project also has a version in Power BI with 2 pages, which can be accessed through the link: https://app.powerbi.com/view?r=eyJrIjoiOGI0ODc5ZWYtMmVhZC00MzU5LTlhMDMtMzgzOWNlNzYwNTgwIiwidCI6IjE3NGZkYjA3LWY1YjYtNDc4Zi05MDdmLTY4NWY3ZDVkMGRhNCJ9 Note: It contains two pages. One for the fighters and another for the fights/events.

Project Description: This project utilizes the "Ultimate UFC Dataset" available on Kaggle, which contains comprehensive information about all UFC fights from mid-2010 to mid-2021. The analysis focused on extracting relevant information about the events and the fighters.

Based on the insights obtained, new tables were created in Excel format:

ufc_fighters.xlsx: Contains comprehensive data about the fighters, consolidating crucial information for future analyses. ufc_fights.xlsx: Contains detailed information about the fights, allowing for a complete view of the statistics and results. Additionally, a file called ufc_fighters_all.xlsx was generated, which analyzes the fighters individually, providing a detailed view of each one.

Dashboard: An interactive dashboard was developed in Python called ufc_dashboard.py, which provides an overview of the most relevant statistics and insights extracted from the UFC dataset.

Repository Contents:

ufc_fighters.py: Initial development of the project, where the files R_fighters.xlsx and B_fighters.xlsx were created. From them, the ufc_fighters.xlsx file was created.

ufc_fighters_all.py: Stage of creating a dataframe containing summarized data of each separate fighter. Created from the ufc_fighters.xlsx file.

ufc_fights.py: Responsible for creating the 'ufc_fights.xlsx' file, containing UFC fight/event statistics.

ufc_functions.py: Creation of functions related to fighters (dataframes: ufc_fighters and ufc_fighters_all) that will be plotted on the dashboard.

ufc_functions2.py: Creation of functions related to fights and events (dataframe: ufc_fights) that will be plotted on the dashboard.

ufc_dashboard.py: Creation and development of an interactive dashboard containing analyses and insights of the data obtained throughout the project.

Others: I also posted screenshots of the dashboard in .png format and also the xlsx files generated throughout the project.

The original dataset is also included in the project (ufc-master(DATASET ORIGINAL).csv).

Contributing: I am open to contributions and suggestions for improvements to the project. Feel free to contact and share your ideas.

Contact: For more information or questions, please contact via email [yamashitajulio@hotmail.com].
