
bids_unique= bids_df.groupby('bidder_id').nunique()
bids_unique = bids_unique.drop(["bid_id"],axis = 1)
join_result= df_train.merge(bids_unique, how= 'left', on = 'bidder_id')
join_result.fillna(0,inplace = True)
bids_df_count= bids_df.groupby("bidder_id")
counts= bids_df_count['url'].count().reset_index().rename(columns = {'url':'num_bids'})
new_train= join_result.merge(counts, how= 'left')
