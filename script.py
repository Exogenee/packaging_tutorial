import biketrauma_am

df = biketrauma_am.Load_db().save_as_df()
biketrauma_am.plot_location(biketrauma_am.get_accident(df))
