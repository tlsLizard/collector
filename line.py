#!/usr/bin/env python3
"""
      collector>line.py
      functions to get or set data in a table

      author: TlsLizard
                   
"""

import sqlite3


def count_items():
    item_counter = 0
    conn = sqlite3.connect('objects.db')
    c = conn.cursor()
    c.execute("SELECT * FROM objects")
    data = c.fetchall()
    for row in data:
        item_counter += 1
    print(str(item_counter) + ' objects in the table')
    c.close
    conn.close()
    return item_counter

def get_max_id():
    conn = sqlite3.connect('objects.db')
    c = conn.cursor()
    c.execute("SELECT MAX(id) FROM objects")
    data=int(c.fetchone()[0])
    print('max_id: {}'.format(data))
    c.close
    conn.close
    return(data)

def create_line(index,item_name):##Add other elements of the line
    conn = sqlite3.connect('objects.db')
    c = conn.cursor()
    
    c.execute("INSERT INTO objects (id, name) VALUES (?, ?)",
          (index, item_name))

    conn.commit()
    print(str(index)+" "+item_name+" created")
    c.close
    conn.close()

def delete_line(index):
    try:
        conn=sqlite3.connect('objects.db')
        c=conn.cursor()
        # Deleting single record now
        sql_delete_query = "DELETE from objects where id = {}".format(index)
        c.execute(sql_delete_query)
        conn.commit()
        print("Record deleted successfully ")
        c.close

    except sqlite3.Error as error:
        print("Failed to delete record from sqlite table", error)
    finally:
        if (conn):
            conn.close()
            print("the sqlite connection is closed")

def edit_line(index,x,x_unit,y,y_unit,z,z_unit,value,currency):
    try:
        conn=sqlite3.connect('objects.db')
        c=conn.cursor()
        # Editing single record now
        sql_edit_query = "UPDATE objects\
                          SET x={},length_unit_x='{}',\
                          y={},length_unit_y='{}',\
                          z={},length_unit_z='{}',\
                          value={},currency='{}'\
                          WHERE id={};\
                          ".format(x,x_unit,y,y_unit,z,z_unit,value,currency,index)
        c.execute(sql_edit_query)
        conn.commit()
        print("Record edited successfully ")
        c.close

    except sqlite3.Error as error:
        print("Failed to edit record in sqlite table", error)
    finally:
        if (conn):
            conn.close()
            print("the sqlite connection is closed")

def convertToBinaryData(filename):
    #Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

def insertBLOB(empId, photo):
    try:
        conn = sqlite3.connect('objects.db')
        c = conn.cursor()
        print("Connected to SQLite")
        sqlite_insert_blob_query = """ UPDATE objects
                                  SET bill= (?)
                                  WHERE id={}""".format(empId)

        empPhoto = convertToBinaryData(photo)
        # Convert data into tuple format
        data_tuple = (empPhoto,)
        c.execute(sqlite_insert_blob_query, data_tuple)
        conn.commit()
        print("Image inserted successfully as a BLOB into a table")
        c.close()

    except sqlite3.Error as error:
        print("Failed to insert blob data into sqlite table", error)
    finally:
        if (conn):
            conn.close()
            print("the sqlite connection is closed")

def get_name(id):
    try:
        conn = sqlite3.connect('objects.db')
        c = conn.cursor()
        sqlite_select_query="SELECT name from objects WHERE id={}".format(id)
        c.execute(sqlite_select_query)
        data=c.fetchall()
        print(data)
        c.close()

    except sqlite3.Error as error:
        print("Failed to retrieve name from id",error)
    finally:
        if (conn):
            conn.close()
            print("the sqlite connection is closed")
        return data[0]
'''
def insert_image_db(id,image):
    img_blob = sqlite3.Binary(image)
    try:
        conn = sqlite3.connect('objects.db')
        c = conn.cursor()
        sqlite_select_query = """ UPDATE objects
                                  SET bill= (?)
                                  WHERE id={}""".format(id)
        c.execute(sqlite_select_query,img_blob)
        conn.commit()
        conn.close()
    except sqlite3.Error as error:
        print("Failed to insert blob data into sqlite table", error)
    finally:
        if (conn):
            conn.close()
            print("the sqlite connection is closed")

def retrieve_image_db(id): #afficher la photo
    try:
        conn = sqlite3.connect("objects.db")
        c = conn.cursor()
        sqlite_select_query = """SELECT bill FROM WHERE id={}""".format(id)
        c.execute(sqlite_select_query)
        image = fetchone()
        image = np.array(image[0])
        conn.close()
        return image
    except sqlite3.Error as error:
        print("Failed to insert blob data into sqlite table", error)
    finally:
        if (conn):
            conn.close()
            print("the sqlite connection is closed")
    '''