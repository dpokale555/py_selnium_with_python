import mysql.connector

update_query="UPDATE `inqa_merchant_onboarding`.`merchant` SET `name` = 'Britannia_industries_pvt' WHERE (`id` = '6')"
delete_query="delete from `inqa_merchant_onboarding`.`merchant` where id = 6"
insert_query="INSERT INTO `inqa_merchant_onboarding`.`merchant` (created_at) VALUES ('2022-05-28 11:25:34.848196')"


try:
    con1 = mysql.connector.connect(host='127.0.0.1', port=3319, user="link_qa_read", passwd="linkqa@1234",
                                   database="inqa_merchant_onboarding")
    curs = con1.cursor()
    curs.execute(delete_query)
    con1.commit()
    con1.close()
except:
    print("Error found")

print("Finished..")





