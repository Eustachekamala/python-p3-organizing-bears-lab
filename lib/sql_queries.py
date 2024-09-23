select_all_female_bears_return_name_and_age = """
    SELECT name, bears.age
    FROM bears
    WHERE bears.sex = 'F'
    ORDER BY bears.age;
"""

select_all_bears_names_and_orders_in_alphabetical_order = """
    SELECT bears.name
    FROM bears
    ORDER BY bears.name ASC;
"""


select_all_bears_names_and_ages_that_are_alive_and_order_youngest_to_oldest = """
    SELECT bears.name, bears.age
    FROM bears
    WHERE bears.alive = true
    ORDER BY bears.age DESC;
"""

select_oldest_bear_and_returns_name_and_age = """
    SELECT bears.name, bears.age
    FROM bears
    WHERE bears.age = (SELECT MAX(bears.age) FROM bears)
    ORDER BY bears.age ASC;
"""
select_youngest_bear_and_returns_name_and_age = """
    SELECT bears.name, bears.age
    FROM bears
    WHERE bears.age = (SELECT MIN(bears.age) FROM bears)
    ORDER BY bears.age ASC;
"""