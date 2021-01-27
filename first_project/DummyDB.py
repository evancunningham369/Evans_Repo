import mysql.connector
import pandas as pd
from pandas import DataFrame

# Create the database

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="The_Sims_3_Cheats")
cursor = mydb.cursor()
#cursor.execute("CREATE DATABASE The_Sims_3_Cheats")

# create the table


# def create_The_Sims_3_Table():
#cursor.execute("CREATE TABLE The_Sims_3 (Title VARCHAR(50), Release_Year INT, Platform VARCHAR(50), Cheat_Code VARCHAR(100), Cheat_Code_Description VARCHAR(100))")

# populate the table


def populate_The_Sims_3_Table():

    cheat_data = [('The Sims 3', 2009, 'PC', 'CNTRL + SHFT + C', 'Open Cheat Console'),
                  ('The Sims 3', 2009, 'PC',
                   'fullscreen on/off', 'Adjust the game screen'),
                  ('The Sims 3', 2009, 'PC', 'constrainFloorElevation true/false',
                   'Unrestrict Terrain adjustments'),
                  ('The Sims 3', 2009, 'PC', 'freerealestate', 'Buy any house'),
                  ('The Sims 3', 2009, 'PC',
                   'enableLlamas on/off', 'Llamas message'),
                  ('The Sims 3', 2009, 'PC', 'jokePlease', 'Joke message'),
                  ('The Sims 3', 2009, 'PC', 'hideHeadlineEffects on/off',
                   'Hides all meters like the skill meter'),
                  ('The Sims 3', 2009, 'PC', 'quit', 'Quits the game'),
                  ('The Sims 3', 2009, 'PC', 'help', 'Help menu'),
                  ('The Sims 3', 2009, 'PC',
                   'slowMotionViz <0 to 8>', 'Slow motion mode'),
                  ('The Sims 3', 2009, 'PC',
                   'ResetLifetimeHappiness', 'Reset sims happiness'),
                  ('The Sims 3', 2009, 'PC',
                   'resetSim <firstname> <lastname>', 'Reset the Sims settings'),
                  ('The Sims 3', 2009, 'PC', 'buydebug on/off',
                   'Display hidden items in buy mode after testingcheats is used'),
                  ('The Sims 3', 2009, 'PC', 'fps on/off',
                   'Displays Frames per Second'),
                  ('The Sims 3', 2009, 'PC',
                   'HideHeadlineEffects on/off', 'Modifies thought balloons'),
                  ('The Sims 3', 2009, 'PC', 'fadeObjects on/off',
                   'Objects fade with camera zoom'),
                  ('The Sims 3', 2009, 'PC', 'testingcheatsenabled true',
                   'Activate Testing cheats, shift click a Sim'),
                  ('The Sims 3', 2009, 'PC', 'unlockOutfits on/off',
                   'Unlocks outfits in Create a Sim'),
                  ('The Sims 3', 2009, 'PC', 'moveobjects on/off',
                   'Move anything including your Sim'),
                  ('The Sims 3', 2009, 'PC', 'AlwaysAllowBuildBuy true/false',
                   'Modes are always available'),
                  ('The Sims 3', 2009, 'PC', 'familyfunds <familys last name> <amount over 0>',
                   'Modify familys bank account balance to number set'),
                  ('The Sims 3', 2009, 'PC', 'kaching', 'Gives $1000'),
                  ('The Sims 3', 2009, 'PC', 'motherlode', 'Gives $50000')
                  ]

    cursor.executemany(
        'INSERT IGNORE into The_Sims_3 VALUES(%s, %s, %s, %s, %s)', cheat_data)
    mydb.commit()

# print the tables data into a Pandas DataFrame to be sent to the HTML code


def print_sql_data_as_Pandas_DF():
    query = 'SELECT * FROM The_Sims_3'
    df = pd.read_sql(query, mydb)
    print(df)

# run main


def main():
    cursor.execute('DROP TABLE The_Sims_3')
    create_The_Sims_3_Table()
    populate_The_Sims_3_Table()
    # print_sql_data_as_Pandas_DF()


if __name__ == '__main__':
    main()
