from distutils.util import execute
from os import system
from secrets import choice
from turtle import clear
from unicodedata import name
import psycopg2
from tabulate import tabulate
import pwinput
    
class admin_page():
    
    def add_product():
            product_id=input("1:product_id:")
            product_name=input("2:product_name:")
            product_price=input("3:price:")
            product_quantity=input("4:number of new products:")    
            
            
            sql_q='INSERT INTO products(product_code,product_name,product_price,a_quantity) VALUES(%s,%s,%s,%s);'
            data=(product_id,product_name,product_price,product_quantity)
            cursor.execute(sql_q,data)
            connector.commit()
            return 1
        
    def view_products():
        
        cursor.execute("SELECT product_name, price FROM products;")
        products = cursor.fetchall()
        if not products:
            print("No products found.")
            return
        table_data = []
        for product in products:
            table_data.append([product[0], float(product[1])])

        headers = ["Product Name", "Price ($)"]
        print(tabulate(table_data, headers=headers, tablefmt="psql"))       


        
    def delete_product():
        
        q=str(input("Wanna delete products [y/n]:"))
        if q in ['y' or 'Y']:
            user=input("Username:")
            password=str(pwinput.pwinput(prompt="Password:",mask="*"))
            sql_q="SELECT password from authentication WHERE user like %s"
            cursor.execute(sql_q,user)
            password_d=cursor.fetchall()
            # out=password==password_d[0,0]
            if (password==password_d):
                query="DELETE * from table products where product_code=%s"
                code=input("Enter product id to be removed:")
                cursor.execute(query,code)
            else:
                print("Wrong password")
        connector.commit()
        choise=input("wanna remove multiple products[y/n]:")
        if choise in ['y' or 'Y']:
            admin_page.delete_product()
        else:
            work()
        
        if q in ['n' or 'N']:
            work()
        
        
class user_page():
    
    def view_products():
        
        # cursor.execute("SELECT product_name, price FROM products;")
        cursor.execute("SELECT * FROM products;")
        products = cursor.fetchall()
        if not products:
            print("No products found.")
            return
        table_data = []
        for product in products:
            table_data.append([product[0],product[1], float(product[2])])

        headers = ["Id" ,"Product Name", "Price ($)"]
        print(tabulate(table_data, headers=headers, tablefmt="psql"))       
        
    def place_order(self):
        
        # Check if the product exists and fetch its details
        user_page.view_products()
        po_product_id = int(input("Enter product id : "))
        quantity = int(input("Enter Quantity for order : "))
        cursor.execute("SELECT * FROM products WHERE product_id::integer = %s;", (po_product_id,))
        product = cursor.fetchall()
        
        if not product:
            print("Product not found.")
            return

        if quantity > product[0][2]:
            print("Insufficient stock.")
            return

        cursor.execute("INSERT INTO cart (product_id, quantity,username) VALUES (%s, %s, %s);",(po_product_id,quantity,username))
        print("Product added to cart !")

        new_stock = product[0][2] - quantity
        cursor.execute("UPDATE products SET quantity = %s WHERE product_id::integer = %s;", (new_stock, po_product_id))
        connector.commit() 

   
            
            
if __name__=="__main__":
    
    connector=psycopg2.connect(database="shopclassy",user='shopclassy',host="127.0.0.1",password="shopclassy",port="5432")
    cursor=connector.cursor()
    
    def access():
        global username 
        username = str(input("Enter username :"))
        password=pwinput.pwinput(prompt="password :", mask="*")
        sql_q= 'SELECT isadmin FROM Authentication where username like %s and password like %s'
        data=(username,password)
        cursor.execute(sql_q,data)
        isadmin=cursor.fetchall()
        
        if isadmin[0][0] == 0:
                print("1. View available products:\n2. Place your order\n3. Exit")
                op=int(input("Enter your choice:"))
                if op==1:
                    progres = user_page.view_products()
                elif op==2:
                    progres = user_page.place_order(username)    
                elif op==3:
                    exit()
        elif isadmin[0][0] == 1:
            work()
        
        else:
            print("Not an authorised user or admin:")
            
    def work():
            print("1. Add new product \n2. View existing products \n3. Delete existing product\n4. View specific table\n5. Exit")
            case=int(input("Enter your process:"))
            if case == 1:
                progres=admin_page.add_product()
                if progres == 1:
                    print("updated new products..")
                else:
                    print("failed during updation.(retry!)")
                    
            elif case == 2:
                admin_page.view_products()
                
            elif case==3:
                admin_page.delete_product()
            choise=input("wanna exit..(y/n)")
            if choise in ['Y' or 'y']:
                exit()
            elif choise in ['N' or 'n']:
                work()

    def exit():
        connector.close()
        print("Exitting")
    
    access()
