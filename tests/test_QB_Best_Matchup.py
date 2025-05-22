from pages.qbList import qb_and_stats_page
from pages.defList import def_Page

def test_QB_Best_Matchup(browser):
   qbsAndStats = qb_and_stats_page(browser)
   defandstats= def_Page(browser) 

   YEAR= input("What year would you like to check?" )

   # Given the NFL Stats website qblist
   qbsAndStats.load()

    #When the user selects A Year And Week
   qbsAndStats.filterByYear(YEAR)

    #THEN a list will contain all the QBs and there Stats
   assert YEAR in qbsAndStats.yearpage() 
   
    # and the Def they play that week 
    # TODO

    # and determine whos the best choice
    # TODO

    # and printed nicely 
    #TODO
    
    raise Exception("Incomplete test")