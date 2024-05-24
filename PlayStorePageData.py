# -*- coding: utf-8 -*-
"""
Created on Tue May 14 13:19:06 2024

@author: Sven
"""


import requests
import datetime
import json

language = 'en'
country = 'us'
header = {
    'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
}
date = str(datetime.datetime.now())
bundle_name = 'com.king.candycrushsaga'


data = f"""f.req=[[["Ws7gDc", "[null,null,[[1,9,10,11,13,14,19,20,38,43,47,49,52,58,59,63,69,70,73,74,75,78,79,80,91,92,95,96,97,100,101,103,106,112,119,129,137,139,141,145,146]],[[[true],null,[[null,[]]],null,null,null,null,[null,2],null,null,null,null,null,null,null,null,null,null,null,null,null,null,[1]],[null,[[null,[]]]],[null,[[null,[]]],null,[true]],[null,[[null,[]]]],null,null,null,null,[[[null,[]]]],[[[null,[]]]]],null,[[\\"{bundle_name}\\",7]]]", null, "7"],]]"""
res = requests.post(
    f'https://play.google.com/_/PlayStoreUi/data/batchexecute?hl={language}&gl={country}',
    headers=header, data=data)

try:
    app = json.loads(json.loads(res.text.splitlines()[-1])[0][2])[1][2]
except:
    app = None
try:
    total_install = app[13][2]
except:
    total_install = None
    
try:
    release_date = app[10][0]
except:
    release_date = None
try:
    update_date = app[145][0][0]
except:
    update_date = None
try:
    version = app[140][0][0][0]
except:
    version = None
try:
    update_description = app[144][1][1]
except:
    update_description = None
try:
    category_tags = []
    for tag_arr in list(filter(lambda item: item is not None, app[118])):
        for tag_arr2 in tag_arr[0]:
            if isinstance(tag_arr2[0], str):
                category_tags.append(tag_arr2[0])
            else:
                category_tags.append(tag_arr2[0][0])
except:
    category_tags = []
try:
    one_star_review_count = int(app[51][1][1][1])
except:
    one_star_review_count = None
try:
    two_star_review_count = int(app[51][1][2][1])
except:
    two_star_review_count = None
try:
    three_star_review_count = int(app[51][1][3][1])
except:
    three_star_review_count = None
try:
    four_star_review_count = int(app[51][1][4][1])
except:
    four_star_review_count = None
try:
    five_star_review_count = int(app[51][1][5][1])
except:
    five_star_review_count = None
try:
    icon_link = app[95][0][3][2]
except:
    icon_link = None
try:
    store_video_link = app[100][0][0][3][2]
except:
    store_video_link = None
try:
    store_video_thumbnail_link = app[100][0][1][3][2]
except:
    store_video_thumbnail_link = None
try:
    ss_links = app[78][0]
    screenshot_links = []
    for ss_link in ss_links:
        screenshot_links.append(ss_link[3][2])
except:
    screenshot_links = []
try:
    page_description = app[72][0][1]
except:
    page_description = None
try:
    rating = app[51][0][1]
except:
    rating = None
try:
    trunc_install = app[13][0]
except:
    trunc_install = None

play_store_page = {
    'bundle_name': bundle_name,
    'release_date': release_date,
    'scrape_time': date,
    'country_code': 'us',
    'avg_rating': rating,
    'description': page_description,
    'trunc_install': trunc_install,
    'last_update_date': update_date,
    'version': version,
    'update_description': update_description,
    'category_tags': [str(category_tags)],
    'total_install': total_install,
    'icon_link': icon_link,
    'screenshot_links': [str(screenshot_links)],
    'store_video_link': store_video_link,
    'store_video_thumbnail_link': store_video_thumbnail_link,
    'one_star_review_count': one_star_review_count,
    'two_star_review_count': two_star_review_count,
    'three_star_review_count': three_star_review_count,
    'four_star_review_count': four_star_review_count,
    'five_star_review_count': five_star_review_count
}

print("App ID")
print(bundle_name)
print("TOTAL INSTALLS (all geos up to this day)")
print(total_install)





















