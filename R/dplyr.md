df1 <- mutate_all(df, .funs=toupper)
df2 <- mutate_all(df, funs(toupper))
