# .....................User-Agent information
import requests
import json
user_id = "100040000999000" # your user id
coo="#sb:......................."    # your cookie
url = 'https://web.facebook.com/api/graphql/'
file = open("log.html", "w")
headers = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "application/x-www-form-urlencoded",
    "sec-ch-ua": "\"Brave\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "\"\"",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"15.0.0\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "sec-gpc": "1",
    "x-asbd-id": "129477",
    "x-fb-friendly-name": "PokesMutatorPokeMutation",
    "x-fb-lsd": "JMAgV3hIY6U5HB_EYOwEhj",
    "Referrer-Policy": "strict-origin-when-cross-origin"
}

coo = {"cookies"}
new_body = f'av={user_id}&__aaid=0&__user={user_id}&__a=1&__req=1j&__hs=19809.HYP%3Acomet_pkg.2.1..2.1&dpr=1&__ccg=GOOD&__rev=1012350580&__s=8e96gz%3Ancl4kz%3A8njtlq&__hsi=7351090978894815231&__dyn=7AzHK4HwkEng5K8G6EjBAg2owIxu13wFwhUngS3q2ibwNw9G2Saw8i2S1DwUx60GE3Qwb-q7oc81xoswMwto886C11wBz83WwgEcEhwGxu782lwv89kbxS2218wc61awkovwRwlE-U2exi4UaEW2G1jxS6FobrwKxm5oe8464-5pUfEdbwxwjFovUaU3VBwFKq2-azo6O14wwwOg2cwMwhEkxebwHwNxe6Uak0zU8oC1hxB0qo4e16wWwjHDzUiwRxW&__csr=gaYtd7Tsc88slsZOA3Xsl5WtheBd9il9FlqiRrv8xJblaGERQ99mj-BWXRalppqJ5CXAGhaUGmA88hrGimVrhVu5-F9ebGjHWgDgg8HGGjAxe5rKEjjBy925xyEsxyWABDzEWEZ4wFz9UlxK4Eix68Gm5K9zRx2ifxW2K4Gx6UOexWaw4JBwAwaW2a9wTwvod8mwgpo9oiwb21Mwuo7-4Ulwbm0hW3K2i055o3uw2FE0Oa2y0KE07rW00PLU0Ge05vpUiJm0le1kw3So0DG0Jo0g6w2DE09xQ0D807k-1nCwj9ZG0mW032e&__comet_req=15&fb_dtsg=NAcNaCc1Ked3uHZbhy2fFMj-JcV3k_uOIZGoNjNmm1BcuIvsmma0GEw%3A21%3A1711551997&jazoest=25544&lsd=PcuM5h2BjPjy4sr5KXYRU9&__spin_r=1012350580&__spin_b=trunk&__spin_t=1711559244&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=PokesSurfaceQuery&variables=%7B%22scale%22%3A1%7D&server_timestamps=true&doc_id=6433741240081581'
response = requests.post(url, headers=headers, data=new_body, cookies=coo)

file.write(response.text)
file.close()


data=json.loads(response.text)


#............get pokeers id

poke_ids = []
pokes_list = data["data"]["viewer"]["incoming_pokes"]["edges"]

for poke in pokes_list:
    poke_status = poke["node"]["poker"]["poke_status"]
    if poke_status == "CAN_POKE":
        poke_id = poke["node"]["poker"]["id"]
        poke_ids.append(poke_id)
        
        
        
#............poke them      

for poke_id in poke_ids:
    body = f"av={user_id}&__aaid=0&__user={user_id}&__a=1&__req=1a&__hs=19809.HYP%3Acomet_pkg.2.1..2.1&dpr=1&__ccg=GOOD&__rev=1012348741&__s=2jwxqm%3A1jbp6v%3Alptkux&__hsi=7351061360227813138&__dyn=7AzHK4HwkEng5K8G6EjBAg2owIxu13wFwnUW3q2ibwNw9G2Sawba1DwUx60GE3Qwb-q7oc81xoswMwto886C11wBz83WwtohwGxu782lwv89kbxS2218wc61awkovwRwlE-U2exi4UaEW2G1jxS6FobrwKxm5o7G4-5pUfEe88o4Wm7-2K0-poarCwLyES1Iwh85d08O321LyUaUcojxK2B08-269wqQ1FwgU4q3G1eKufxa3m7E&__csr=iha79lPPq4mPmC-CgIy5FiPj9cAlNcgLnZn59XdQ89i4F4bXJ2ypBGOTv888ZqZXWJkKimFSGhWAQiFe8GGh4iGjGdjzUSiQqcAAyqxp2V8-8z4bByAQ8xu5F8qx52V9Eky9oqBz8y5E9UjzErwsohK2C2CbzUsUyU5W361Ywr8S9weu5F84e0TEuxSi0lm0KE15o0l0w1x60qS00kHm0azw1ox11dk0rV03M80DK0J80gpw2wE0ac807qO1cDSE1rE&__comet_req=15&fb_dtsg=NAcNe-1pwydeFU4u63EsVp76wubfc4ClSKUkVe70ghe-wcHsZMavAWw%3A21%3A1711551997&jazoest=25542&lsd=-n84iv0pEPWyMtByKf7paY&__spin_r=1012348741&__spin_b=trunk&__spin_t=1711552348&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=PokesMutatorPokeMutation&variables=%7B%22input%22%3A%7B%22client_mutation_id%22%3A%221%22%2C%22actor_id%22%3A%22{user_id}%22%2C%22user_id%22%3A%22{poke_id}%22%7D%7D&server_timestamps=true&doc_id=5028133957233114"
    response = requests.post(url, headers=headers, data=body, cookies=coo)
    print(response.text)
         
