import google.cloud.storage as storage
import os
import json
from imutils import paths
from datetime import datetime as dt
#from datetime import timedelta
import sqlite3
import pytz
tz = pytz.timezone("Asia/Calcutta")
import psycopg2

# conn = sqlite3.connect(database="db.sqlite3",check_same_thread=False)
# cur = conn.cursor()
#from django.core.serializers.json import DjangoJSONEncoder
#import schedule
import time

#from views import attribute
# data = []
# start_time = []
conn = psycopg2.connect(host="datavivservers.in", port = 5436, database="camerax", user="Dataviv", password="DatavivPostgreSQLSecurePassword!")
cur = conn.cursor()

def meta_data_store(feed_id,store_id, channel_no, module_name,url,status):
# cur.execute("""SELECT * FROM camera_modelanalysis""")
# img_url = "https://storage.googleapis.com/camerax-bucket/images/0/201001/14/Customer/fed2.jpg"
# timestamp ="2020-09-06T07:59:43.975597Z"
# classtype ="E"
# store_id = 9
    # try:
    #sql = "INSERT into camera_modelanalysis2(img_url,timestamp,classtype,store_id,owner_id,flag) values('%s', '%s', '%s',%d, %r)" % (img_url, timestamp, classtype, int(store_id),int(ownerid),False)
    sql = "INSERT into motion_event(feed_id,store_id, channel_no, module_name,url,status) values('%d','%d','%s','%s','%s','%r')" % (int(feed_id),int(store_id), channel_no, module_name,url,False)
    cur.execute(sql)
    conn.commit()

    # query_results = cur.fetchall()
    # print(query_results)

    # cur.close()
    # conn.close()
    return 0
    # except:
    #     return 1

#new_key = 'melodic-eye-296511-ce1ca7a5bc8e.json'
new_key = 'lockated-1174-10f37be0a591.json'
def store_image_bucket(module_name, channel_no,store_id,feed_id):
 
    storage_client = storage.Client.from_service_account_json(os.path.abspath(new_key))
    bucket = storage_client.get_bucket("camerax")
    _,FILENAME = os.path.split(imgname)
    datepath = dt.now(tz).strftime('%y%m%d')
    hour = dt.now(tz).hour
    timestamp = dt.now(tz)
    FILENAME = f"images/{storeid}/{datepath}/{hour}/{clas}/{FILENAME}"
    blob = bucket.blob(FILENAME)
    blob.upload_from_filename(imgname)
    blob.make_public()
    url = blob.public_url
    # meta = {'url':url, 'storeid':storeid, 'class':clas, 'timestamp': timestamp}
    # img_url, timestamp, classtype,store_id
    ret = meta_data_store(url,timestamp,clas,storeid,ownerid)
    print(url,ret)
    return url
def social_store_image_bucket(module_name, channel_no,store_id,feed_id,video_path):
    storage_client = storage.Client.from_service_account_json(os.path.abspath(new_key))
    bucket = storage_client.get_bucket("cameraxproject")
    #global data,start_time
    _,FILENAME = os.path.split(video_path)
    print(FILENAME)
    datepath = dt.now(tz).strftime('%y%m%d')
    print(datepath)
    hour = dt.now(tz).hour
    timestamp = dt.now(tz)
    print(hour)
    FILENAME = f"videos/md/{store_id}/{datepath}/{hour}/{FILENAME}"
    blob = bucket.blob(FILENAME)
    blob.upload_from_filename(video_path)
    blob.make_public()
    url = blob.public_url
    # meta = {'url':url, 'storeid':storeid, 'class':clas, 'timestamp': timestamp}
    # img_url, timestamp, classtype,store_id
    ret = meta_data_store(feed_id,store_id, channel_no, module_name,url,status='False')
    print(url,ret)
    print(url)
    return url
    # print(FILENAME)
    # url = FILENAME
    # print("file",url)
    # ret = meta_data_store(feed_id,store_id, channel_no, module_name,url,status='False')
    # print(url,ret)
    # #print(url)
    # return url
    # y = {'url':url, 'storeid':storeid, 'class':clas ,'timestamp': timestamp }
    # #z = json.loads(data)
     
    # data.append(y)
    # write_json(temp)
    #print(data)
    #print(type(data))
    #a = json.dumps(data,cls=DjangoJSONEncoder)
    #print(type(a))
        
    
    # blob = bucket.blob(FILENAME)
    # blob.upload_from_filename(imgname)
    # blob.make_public()
    
    # now = dt.now()
    # thres = '0:03:00'
    # format = "%H:%M:%S"
    # current_time = now.strftime("%H:%M:%S")    
    # start_time.append(current_time)
    # print(start_time[0])
    # time_diff = str(dt.strptime(current_time,format) - dt.strptime(start_time[0],format))
    # print(time_diff)
    # print(thres)
    # if time_diff > thres:
    #     for i,items in enumerate(data):
    #         #print(items['url'])
    #         ret = meta_data_store(items['url'],timestamp,clas,storeid,ownerid)
    #         print(ret,i)
    #         if i == len(data) - 1:
    #             data =[]
    #             start_time= []            
    # else:
    #     print('Less than thres')
        
   
    # meta = {'url':url, 'storeid':storeid, 'class':clas, 'timestamp': timestamp}
    # img_url, timestamp, classtype,store_id
    # ret = meta_data_store(url,timestamp,clas,storeid,ownerid)
    # print(url,ret)

    # print(url)
    # return url
def insert_analysis1(avg_male_count, avg_female_count, age_child, age_teenge, age_adult, age_old, total_in,total_out,customer_walkin, store_id):
    try:
        # print(avg_male_count, avg_female_count, age_child, age_teenge, age_adult, age_old, total_in,total_out,customer_walkin, store_id)
        timestamp = dt.now(tz)
        sql = "INSERT into camera_analysis1(avg_male_count, avg_female_count, age_child, age_teenge, age_adult, age_old, total_in,total_out,customer_walkin, timestamp, store_id) values( %d, %d, %d, %d, %d, %d, %d, %d, %d,'%s', %d)" % (int(avg_male_count), int(avg_female_count), int(age_child), int(age_teenge), int(age_adult), int(age_old), int(total_in),int(total_out),int(customer_walkin), timestamp, int(store_id))
        cur.execute(sql)
        conn.commit()
    # cur.close()
    # conn.close()
        return 1
    except:
        # cur.execute("ROLLBACK")
        # pass
        # conn.commit()
        # cur.execute(sql)s
        # conn.commit()
        return -1

def insert_analysis2(avg_purchased_visit,avg_linelength,timestamp,store_id):
    try:
        sql = "INSERT into camera_analysis2(avg_purchased_visit,avg_linelength,timestamp,store_id) values(%d, %d,'%s',%d )" % (int(avg_purchased_visit), int(avg_linelength), timestamp, int(store_id))
        cur.execute(sql)
        conn.commit()

        # cur.close()
        # conn.close()
        return 1
    except:
        return -1
# img = 'images/278775078_11142020231136403467.jpg'
# url = store_image_bucket(str(0),"O",img)
# print(url)
# path = 'data_dumps/employ_data'
# imagePaths = sorted(list(paths.list_images(path)))

# for imgpath in imagePaths:
#     print(imgpath)
#     ret = store_image_bucket(str(9),'E',imgpath)
#     print(ret)
# print(insert_analysis1(avg_male_count=10, avg_female_count=8, age_child=1, age_teenge=2, age_adult=16, age_old=0, total_in=14,total_out=11,customer_walkin=8, store_id=9))
# def where_json(file_name):
#     return os.path.exists(file_name)
# if where_json('data.json'):
#     pass

# else:

#     data = '{}'

#     with open('data.json', 'w') as outfile:  
#         json.dump(data, outfile)

# def write_json(data,filename='data.json'):
#     with open('data.json', 'w') as outfile:  
#         return json.dump(data, outfile,cls=DjangoJSONEncoder)
# Manual upload


# outpath = 'output/vid-17-02-371.avi'
# #entries = os.listdir(path_im)
# # img = 'images/customer_data/cust/19/C_11192020122627403448.jpg'

# # print(dt.fromtimestamp(os.path.getctime(img)).hour)
# ret = social_store_image_bucket("SD", "ch401",str(9),1,outpath) 
# print(ret)