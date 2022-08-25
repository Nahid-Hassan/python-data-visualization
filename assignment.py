================================
def convert(column_name):
  return column_name.lower().replace(' ', '_')

# df.columns = [col.lower().replace(' ', '_') for col in df.columns]
# df.columns



df.columns = [convert(col) for col in df.columns]
df.columns


df['name'] = df['name'].apply(lambda name : name.title())
df.head()


# write your code here.......
def under_eighteen(age):
  if age < 18:
    return True
  else:
    return False

df['age'].apply(under_eighteen)


flag = df['age'].apply(under_eighteen)
df.drop(index=df[flag]index)
