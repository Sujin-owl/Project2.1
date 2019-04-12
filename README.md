## Project2 Team Members
Mark Yocum<br />
Hubert Cheng<br >
Charles Dixon<br />
Sujin Guo

## Extract:

#### State abbreviations

Collected the 2-letter abbreviations for states<br />
https://abbreviations.yourdictionary.com/articles/state-abbrev.html

#### Unemployment data (Website Scrape)
Unemployment Data was collected from scrape from the Bureau of Labor statistics.  Unemployment Rate was collected by state/month/year<br />
https://www.bls.gov/charts/state-employment-and-unemployment/state-unemployment-rates-animated.htm

#### Drug Death data (API)
Centers for Disease Control and Prevention provided an API for each state.  Data included, total deaths per state and deaths by indicator.<br />
https://data.cdc.gov/

## Process:

#### Tools: Jupyter Notebooks, Python, APIs, Splinter, ChromeDriver, Leaflet, HTML, Javascript, D3, Flask

Unemployment Scape
[Jupyter Notebook](https://github.com/Sujin-owl/Project2/blob/master/umployment_data.ipynb).

Combined data    
Please see this [Jupyter Notebook](https://github.com/Sujin-owl/Project2/blob/master/combined_drug_unemployment.ipynb).

Drug API
[Jupyter Notebook](https://github.com/Sujin-owl/Project2/blob/master/Drug_API_Scrape.ipynb)


## Deployment:

#### SQL

This database is utilizing a relational database.  All the information provided can be linked by state.  An empty database was created in MySQL workbench
Using SQLAlchemy, each set of data was loaded into SQL as it's own individual table and one combined table

#### HTML/JavaScript

To display the data collected, D3 was utilized to create a scatter graph displaying drug by death and unemployment rates by state.  Flask application was used to render a custom HTML to explain and display the scatter graph

#### Heroku:https://drug-project2.herokuapp.com/
