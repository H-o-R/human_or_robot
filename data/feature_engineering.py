
#merging bids and train dataframe to create a new_train data frame
bids_unique= bids_df.groupby('bidder_id').nunique()
bids_unique = bids_unique.drop(["bid_id"],axis = 1)
join_result= df_train.merge(bids_unique, how= 'left', on = 'bidder_id')
join_result.fillna(0,inplace = True)
bids_df_count= bids_df.groupby("bidder_id")
counts= bids_df_count['url'].count().reset_index().rename(columns = {'url':'num_bids'})
new_train= join_result.merge(counts, how= 'left')

#drop null values
new_train.dropna(inplace=True)

#dropping categorical data columns
new_train.drop(['bidder_id','payment_account','address'],axis=1,inplace = True)

#one hot encoding on merchandise (from brennan)
from sklearn.preprocessing import OneHotEncoder
one_hot = pd.get_dummies(new_train['merchandise'])
new_train.drop('merchandise',axis=1,inplace= True)
new_train= new_train.join(one_hot)
new_train = new_train.rename(columns={1.0:'merchandise=1.0',2.0:'merchandise=2.0'})
