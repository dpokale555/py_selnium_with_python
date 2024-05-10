import mysql.connector

try:
    con1 = mysql.connector.connect(host='127.0.0.1', port=3319, user="link_qa_read", passwd="linkqa@1234",
                                   database="inqa_merchant_onboarding")
    curs = con1.cursor()
    curs.execute("SELECT * FROM inqa_merchant_onboarding.merchant where external_id in ('HBri0464','HDel0095','LJIO0728')")

    for row in curs:
       print(row[0],row[1],row[2],row[3],row[4],row[5],row[6])

    con1.close()
except:
    print("Error found")

print("Finished..")





