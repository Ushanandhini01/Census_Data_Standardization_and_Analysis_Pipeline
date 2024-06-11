import mysql.connector
import streamlit as st
import pandas as pd

def run_query(query):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    )
    print(mydb)
    cursor = mydb.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    return results
st.subheader(":blue[Population of each district]")

if st.button("Fetch Total Population Data"):
    # Define the query to calculate total population of each district
    query = """
    SELECT District, SUM(population) AS Total_Population
    FROM census_db.census_2011
    GROUP BY District
    """
    # Run the query
    results = run_query(query)
    st.table(results)

if st.button("Literate males and females of each district"):
    # Define the query to calculate total population of each district
    query = """
    select district,literate_male,literate_female from census_db.census_2011
    """
    # Run the query
    results = run_query(query)
    st.table(results)

if st.button("percentage of workers in each district"):
    # Define the query to calculate total population of each district
    query = """
    select district,avg(workers)*100 as workers_percent from census_db.census_2011 group by district
    """
    # Run the query
    results = run_query(query)
    st.table(results)

if st.button("households with access to lpg or png as cooking fuel"):
    # Define the query to calculate total population of each district
    query = """
    select district,lpg_or_png_households from census_db.census_2011
    """
    # Run the query
    results = run_query(query)
    st.table(results)

if st.button("Religious composition of each district"):
    # Define the query to calculate total population of each district
    query = """
    select district,(sum(hindus)+sum(muslims)+sum(christians)+sum(sikhs)+sum(jains)+sum(buddhists)+sum(others_religions)) as religious_composition from census_db.census_2011 group by district")
    """
    # Run the query
    results = run_query(query)
    st.table(results)

if st.button("households with internet access in each district"):
    # Define the query to calculate total population of each district
    query = """
    select district,households_with_internet from census_db.census_2011"
    """
    # Run the query
    results = run_query(query)
    st.table(results)

if st.button("education attainment in each district"):
    # Define the query to calculate total population of each district
    query = """
    select district,below_primary_education,primary_education,middle_education,secondary_education,higher_education,graduate_education from census_db.census_2011
    """
    # Run the query
    results = run_query(query)
    st.table(results)

if st.button("households with various transportation modes"):
    # Define the query to calculate total population of each district
    query = """
    select district,households_with_bicycle,households_with_car_jeep_van,households_with_scooter_motorcycle_moped from census_db.census_2011"
    """
    # Run the query
    results = run_query(query)
    st.table(results)


if st.button("condition of occupied census houses"):
    # Define the query to calculate total population of each district
    query = """
    select district,condition_of_occupied_census_houses_dilapidated_households,households_with_separate_kitchen_cooking_inside_house,having_bathing_facility_total_households,having_latrine_facility_within_the_premises_total_households from census_db.census_2011
    """
    # Run the query
    results = run_query(query)
    st.table(results)


if st.button("household size distribution in each district"):
    # Define the query to calculate total population of each district
    query = """
    select district,household_size_1_to_2_persons,household_size_3_to_5_persons_households from census_db.census_2011
    """
    # Run the query
    results = run_query(query)
    st.table(results)

if st.button("total no.of households in each state"):
    # Define the query to calculate total population of each district
    query = """
    select "state/ut",sum(households) from census_db.census_2011 group by "state/ut"
    """
    # Run the query
    results = run_query(query)
    st.table(results)

if st.button("households having access to latrine in each state"):
    # Define the query to calculate total population of each district
    query = """
    select "state/ut",sum(having_latrine_facility_within_the_premises_total_households) from census_db.census_2011 group by "state/ut"
    """
    # Run the query
    results = run_query(query)
    st.table(results)

if st.button("average household size in each state"):
    # Define the query to calculate total population of each district
    query = """
    select "state/ut",avg(households) as avg_household_size  from census_db.census_2011 group by "state/ut"
    """
    # Run the query
    results = run_query(query)
    st.table(results)

if st.button("own households vs rented households in each state"):
    # Define the query to calculate total population of each district
    query = """
    select "state/ut", sum(ownership_owned_households) as own_houses, sum(ownership_rented_households) as rent_houses from census_db.census_2011 group by "state/ut"
    """
    # Run the query
    results = run_query(query)
    st.table(results)

if st.button("distribution of different latrine types"):
    # Define the query to calculate total population of each district
    query = """
    select "state/ut", sum(type_of_latrine_facility_pit_latrine_households) as pit_larine_household,sum(type_of_latrine_facility_other_latrine_households) as other_larine_household from census_db.census_2011 group by "state/ut"
    """
    # Run the query
    results = run_query(query)
    st.table(results)

if st.button("Access to drinking water near premises in each state"):
    query = """
    select "state/ut",sum(location_of_drinking_water_source_near_the_premises_households) as Access_to_Drinking_near_Premises from census_db.census_2011 group by "state/ut"
    """
    # Run the query
    results = run_query(query)
    st.table(results)

if st.button("Avg Income distribution in each state based on power parity"):
    query = """
    select "state/ut",avg(total_power_parity) as Avg_Power_parity  from census_db.census_2011 group by "state/ut"
    """
    # Run the query
    results = run_query(query)
    st.table(results)

if st.button("percent of married couple with different household sizes"):
    query = """
    select "state/ut",avg(married_couples_1_households)*100 as one_household_size,avg(married_couples_2_households)*100 as two_household_size,avg(married_couples_3_households)*100 as three_household_size,avg(married_couples_3_or_more_households)*100 as three_or_more_household_size,avg(married_couples_4_households)*100 as four_households,avg(married_couples_5__households)*100 as five_households,avg(married_couples_none_households)*100 as none_households from census_db.census_2011 group by "state/ut"
    """
    # Run the query
    results = run_query(query)
    st.table(results)

if st.button("below poverty line based on power parity in each state"):
    query = """
    select "state/ut",sum(power_parity_less_than_rs_45000) as households_below_poverty_line from census_db.census_2011 group by "state/ut"
    """
    # Run the query
    results = run_query(query)
    st.table(results)

if st.button("percent of literacy rate in each state"):
    query = """
    select "state/ut",avg(literate)*100 as literacy_percent from census_db.census_2011 group by "state/ut"
    """
    # Run the query
    results = run_query(query)
    st.table(results)