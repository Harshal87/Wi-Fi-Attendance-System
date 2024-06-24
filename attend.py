import os
from getmac import get_mac_address
import pymysql as mdb


def upd(count,per,name,subject):
    
    mydb = mdb.connect(
      host="127.0.0.1",
      user="root",
      passwd="",
      database="apsystem"
    )

    mycursor = mydb.cursor()

   

    sql = "UPDATE report SET total = %s,per = %s WHERE name=%s AND subject=%s"
    val = (count,per,name,subject)

    mycursor.execute(sql, val)

    mydb.commit()
    mydb.close()
mydb = mdb.connect(
          host="127.0.0.1",
          user="root",
          passwd="",
          database="apsystem"
        )

mycursor = mydb.cursor()

sql = "SELECT name,subject,mac,total FROM report"


mycursor.execute(sql)
fine=0
myresult = mycursor.fetchall()
mydb.close()
#print (myresult)
for x in myresult:
  name= str(x[0])
  subject=str(x[1])
  mac=str(x[2])
  total=str(x[3])
  if total=='':
    print ('find')
    mydb = mdb.connect(
      host="127.0.0.1",
      user="root",
      passwd="",
      database="apsystem"
    )

    mycursor = mydb.cursor()

    sql = "SELECT mac FROM report WHERE name=%s AND subject=%s"


    mycursor.execute(sql,(name,subject))
    fine=0
    myresult = mycursor.fetchall()
    mydb.close()
    #print (myresult)
    count=0
    for x in myresult:
        mc=str(x[0])
        print(mc)
        if mac==mc:
            count=count+1
    per1=(count/5)*100
    per = "{:.2f}".format(per1)
    print(per)
    upd(count,per,name,subject)
#####################################################33
    
#def upd(name,mac,count,per,ids):
    
    #con = mdb.connect('localhost', \
    #                          'root', \
    #                          '', \
     #                         'apsystem' );
    #cur = con.cursor()
    #cur.execute("TRUNCATE TABLE `report`")
    #cur.execute("""INSERT INTO report(name,mac,total,per,ids) \
                       #VALUES(%s,%s,%s,%s,%s)""", (name,mac,count,per,ids))
    """     
    con.commit()
mydb = mdb.connect(
          host="127.0.0.1",
          user="root",
          passwd="",
          database="apsystem"
        )

mycursor = mydb.cursor()

sql = "SELECT id,name,mac,total FROM report"


mycursor.execute(sql)
fine=0
myresult = mycursor.fetchall()
mydb.close()
#print (myresult)
for x in myresult:
  ids= str(x[0])
  name=str(x[1])
  mac=str(x[2])
  total=str(x[3])
  if total=='':
    print ('find')
    mydb = mdb.connect(
      host="127.0.0.1",
      user="root",
      passwd="",
      database="apsystem"
    )

    mycursor = mydb.cursor()

    sql = "SELECT mac FROM student"


    mycursor.execute(sql)
    fine=0
    myresult = mycursor.fetchall()
    mydb.close()
    #print (myresult)
    count=0
    for x in myresult:
        mc=str(x[0])
        print(mc)
        if mac==mc:
            count=count+1
    per=(count/7)*100
    print(per)
    upd(name,mac,count,per,ids)
    """
####   ##################################################### 
subject=str(input('Enter Subject='))
for i in range(0,10):
    ii=str(i)
    ips='192.168.43.3'+ii
    response = os.popen(f"ping {ips}").read()
    print(i)
    if "host unreachable." in response:
        k=1
    else:        
        ip_mac = get_mac_address(ip=ips)
        print(ips,ip_mac)
        mydb = mdb.connect(
          host="127.0.0.1",
          user="root",
          passwd="",
          database="apsystem"
        )

        mycursor = mydb.cursor()

        sql = "SELECT student FROM student WHERE mac=%s"


        mycursor.execute(sql,(ip_mac,))
        myresult = mycursor.fetchall()
        mydb.close()
        try:
            v= (myresult[0])
            v=v[0]
            print(v)
            con = mdb.connect('localhost', \
                                  'root', \
                                  '', \
                                  'apsystem' );
            cur = con.cursor()
                    #cur.execute("TRUNCATE TABLE `sens`")
            cur.execute("""INSERT INTO attendance(student,subject) \
                               VALUES(%s,%s)""", (v,subject))

            cur.execute("""INSERT INTO report(name,mac,subject) \
                               VALUES(%s,%s,%s)""", (v,ip_mac,subject))

            #upd()

            con.commit()
            mydb = mdb.connect(
              host="127.0.0.1",
              user="root",
              passwd="",
              database="apsystem"
                )
            mycursor = mydb.cursor()

            
            sql="SELECT total FROM `report` WHERE name=%s AND subject=%s "
            mycursor.execute(sql,(v,subject))
            myresult1=mycursor.fetchall()
            v1=(myresult1[0])
            v1=v1[0]
            print(v1)

            if(v1>0):
                v2=int(v1)
                v2+=1
                v1=v2
                
            else:
                ct1=1
                v1=ct1

            print(v1,v,subject)
            sql = "UPDATE report SET total = %s WHERE name= %s ,subject= %s"
            val1 = (v1,v,subject)

            mycursor.execute(sql, val1)

            mydb.commit()
            mydb.close()    
            
    
                    
            #con.commit()
        except:
            print('e')
       
