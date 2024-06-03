# Query to select all female bears, returning their names and ages
select_all_female_bears_return_name_and_age = """
    SELECT name, age
    FROM bears
    WHERE sex = 'F';
"""

# Query to select all bears' names and ages ordered by age
select_all_bears_names_and_ages_ordered_by_age = """
    SELECT name, age
    FROM bears
    ORDER BY age;
"""

# Query to select the youngest bear's name and age
select_youngest_bear = """
    SELECT name, age
    FROM bears
    ORDER BY age ASC
    LIMIT 1;
"""

# Query to select the oldest bear's name and age
select_oldest_bear = """
    SELECT name, age
    FROM bears
    ORDER BY age DESC
    LIMIT 1;
"""

# Query to select all bears' names and ages that are still alive
select_all_alive_bears = """
    SELECT name, age
    FROM bears
    WHERE alive = 1;
"""
