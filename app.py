from flask import Flask, jsonify, render_template
import numpy as np
import datetime as dt
import pandas as pd
from config import password

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import pymysql
pymysql.install_as_MySQLdb()


dbuser = 'root'
dbpassword = password
dbhost = 'localhost'
dbport = '3306'
dbname = 'Project2'

engine = create_engine(
    f"mysql://{dbuser}:{dbpassword}@{dbhost}:{dbport}/{dbname}")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/Drug_data.html")
def drugs():

    return render_template("Drug_data.html")


@app.route("/api/v1.0/drug_data")
def drug_data():
    """Return all database data on drug usage by state and year"""
    Drugs = engine.execute("SELECT * FROM drug").fetchall()

    return jsonify({'Drugs': [dict(row) for row in Drugs]})


@app.route("/api/v1.0/unemployment")
def unemployment():
    """Return all database data on unemployment by state and year"""
    Unemployment = engine.execute("SELECT * FROM unemployment").fetchall()

    return jsonify({'Unemployment': [dict(row) for row in Unemployment]})

@app.route("/api/v1.0/combined")
def combined():
    """Return all database data on drug use and unemployment by state and year"""
    Combined = engine.execute("SELECT * FROM combined").fetchall()
    test_df = pd.DataFrame(Combined)
    test_df = test_df.reset_index()
    test_df = test_df.rename(columns={0: 'state',
                                1: "month_year",
                                2: "cocaine",
                                3: "heroin",
                                4: "methadone",
                                5: "number_of_deaths",
                                6: "number_drug_overdose_death",
                                7: "opioids",
                                8: "percent_drugs_specified",
                                9: "psychostimulants",
                                10: "unemployment_data"})
    datagrouped = test_df.groupby(['state', 'month_year'])
    group_df = pd.DataFrame()
    columns = ['cocaine', 'heroin', 'methadone', 'number_of_deaths', 'number_drug_overdose_death', 'opioids', 'percent_drugs_specified', 'psychostimulants', "unemployment_data"]
    for column in columns:
        group_df[f"{column}"] = datagrouped[f"{column}"].sum()

    combined_dict = group_df.groupby(level=0).apply(lambda df: df.xs(df.name).to_dict()).to_dict()
    # print(combined_dict)
    
    return jsonify(combined_dict)

@app.route("/api/v1.0/states")
def states():
    """Return all state abbreviations"""
    Combined = engine.execute("SELECT * FROM combined").fetchall()
    test_df = pd.DataFrame(Combined)
    test_df = test_df.reset_index()
    test_df = test_df.rename(columns={0: 'state',
                                1: "month_year",
                                2: "cocaine",
                                3: "heroin",
                                4: "methadone",
                                5: "number_of_deaths",
                                6: "number_drug_overdose_death",
                                7: "opioids",
                                8: "percent_drugs_specified",
                                9: "psychostimulants",
                                10: "unemployment_data"})
    
    # print(test_df.state.unique())

    return jsonify(list(test_df.state.unique()))

@app.route("/api/v1.0/statedata/<state>")
def statedata(state):
    """Return all state abbreviations"""
    Combined = engine.execute("SELECT * FROM combined").fetchall()
    test_df = pd.DataFrame(Combined)
    test_df = test_df.reset_index()
    test_df = test_df.rename(columns={0: 'state',
                                1: "month_year",
                                2: "cocaine",
                                3: "heroin",
                                4: "methadone",
                                5: "number_of_deaths",
                                6: "number_drug_overdose_death",
                                7: "opioids",
                                8: "percent_drugs_specified",
                                9: "psychostimulants",
                                10: "unemployment_data"})
    
    # print(test_df.state.unique())
    datagrouped = test_df.groupby(['state', 'month_year'])
    group_df = pd.DataFrame()
    columns = ['cocaine', 'heroin', 'methadone', 'number_of_deaths', 'number_drug_overdose_death', 'opioids', 'percent_drugs_specified', 'psychostimulants', "unemployment_data"]
    for column in columns:
        group_df[f"{column}"] = datagrouped[f"{column}"].sum()

    combined_dict = group_df.groupby(level=0).apply(lambda df: df.xs(df.name).to_dict()).to_dict()
    # print(combined_dict)
    
    return jsonify(combined_dict[state])

if __name__ == '__main__':
    app.run(debug=True)