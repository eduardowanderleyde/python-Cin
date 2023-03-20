from mysql.connector import Error
import mysql.connector as MC

try:
    
    connect = MC.connect(
    host="localhost",
    user="root",
    passwd="Softex2023",
    database="company")
    
    print("MySQL Database connection successful")
except Error as err:
    print("Error: {}".format(err))

cursor = connect.cursor()

query_update='''UPDATE employee SET fname = 'Eduardo' WHERE ssn=123456789 ;'''

query_delete='''DELETE FROM dept_locations WHERE dnumber=4;'''

query_select='''SELECT essn, pno FROM works_on;'''

query_join='''SELECT dnum, dnumber
FROM project, department
WHERE project.dnum = department.dnumber;
'''



while True:
    a = input("""o que vc quer fazer:
        1 - inserir algum departamento
        2 - atualizar algum departamento
        3 - deletar algum dependente
        4 - pesquisar nome e numero de todos os departamentos
        5 - pesquisar ssn dos empregados e seus departamentos
    """)

    if a == "1":
        nome = input("nome do departamento")
        numero = input("numero do departamento")
        mgrssn = input("digite o ssn do supervisor desse departamento: ")
        mgrstartdate = input("digite a data do de inciio do supervisor: obs: a data é para estar assim aaaa-mm-dd: ")
        query_department = """ INSERT INTO department(dname, dnumber, mgrssn, mgrstartdate )
                                   VALUES('""" + nome + """','""" + numero + """','""" + mgrssn + """','""" + mgrstartdate + """' ); """
        cursor.execute(query_department)
    elif a == "2":
    
        cursor.execute(query_update)
        
    elif a == "3":

        cursor.execute(query_delete)
        
    elif a == "4":
        query_select = """ SELECT * FROM employee ;"""
        cursor.execute(query_select)
        b = cursor.fetchall()
    
        print(b)
    elif a == "5":

        cursor.execute(query_join)
        b = cursor.fetchall()
        c = cursor.fetchone()
        print(b)
    else:
        print("Escolha um opção valida!!!!!")

    connect.commit()