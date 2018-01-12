## use chunk for large data set
chunksize = 5000
out = None
for data in pd.read_csv('data/test.csv', engine='python', encoding="utf-8", chunksize=chunksize):
    if out is None:
        out = data.copy()
    else:
        out.append(data)
test = out.copy()