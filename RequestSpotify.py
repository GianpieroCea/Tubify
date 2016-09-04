import requests

client_id = 'INSERT_CLIENT_ID'
client_secret = 'INSERT_CLIENT_SECRET'

grant_type = 'client_credentials'

#Request based on Client Credentials Flow from https://developer.spotify.com/web-api/authorization-guide/

#Request body parameter: grant_type Value: Required. Set it to client_credentials
body_params = {'grant_type' : grant_type}

url='https://accounts.spotify.com/api/token'

response=requests.post(url, data=body_params, auth = (client_id, client_secret))

if __name__ == '__main__':
    print response.text
