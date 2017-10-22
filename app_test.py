
from flask import Flask, request
import hashlib

@app.route('/create_new_task', methods=["POST"])
def create_new_task():
    if request.method == "POST":
        json_dict = request.json
    
    name = json_dict['name']
    location = json_dict['location']
    specialty = json_dict['specialty']
    description = json_dict['description']

    task_id = hashlib.md5(name.encode())

    try:
        con = psycopg2.connect("dbname='handyman' user='dubhacks' password='dubhacks'")
    except:
        print("Unable to connect to database.")
        
    cur = con.cursor()

    try:
        cur.execute("INSERT INTO worker (name, location, specialty, resolved, task_id, description) VALUES (name, location, specialty, false, task_id, description))")
    except:
        print("I can't input into worker")
                    
    data = con.commit()
    con.close()
    return jsonify(data);
                    
@app.route('/set_resolved', methods=["POST"])
def set_resolved():
   if request.method == "POST":
       json_dict = request.json
                               
   id = json_dict['task_id']
                               
   try:
           con = psycopg2.connect("dbname='handyman' user='dubhacks' password='dubhacks'")
   except:
           print("Unable to connect to database.")
                               
   cur = con.cursor()
   update = """ UPDATE workers
              SET resolved = %s
              WHERE task_id = %s"""
   try:
       cur.execute(update, (resolved, id))
   except:
       print("I can't input into worker")
   data = con.commit()
   con.close()
   return jsonify(data);

                               
                               
if __name__ == '__main__':
  app.run()
                               
