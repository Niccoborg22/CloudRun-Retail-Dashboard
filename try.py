#%%
import requests
url = 'https://retailback-m5kpcugzeq-ew.a.run.app/api/v1/alldata'
response = requests.get(url, headers={'Authorization': 'Bearer tokenMania'})

print(response)

# %%
