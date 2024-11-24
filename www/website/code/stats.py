
def get_activity_stats():
    sql_query = f"select indicator_name, day, calculated_value \
                    from general_indicator \
                    where indicator_name in ('plankton_activity', \
                                            'shrimps_activity',\
                                            'crabs_activity',\
                                            'fish_activity',\
                                            'sharks_activity',\
                                            'whales_activity',\
                                            'humpbacks_activity'\
                                            ) \
                    and day in (current_date, current_date-30, current_date-60)"