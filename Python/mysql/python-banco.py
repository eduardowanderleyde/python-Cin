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
        update_empregado = """UPDATE employee SET salary = 60000 WHERE sex = 'M' and ssn = 333445555 ;"""
        cursor.execute(update_empregado)
    elif a == "3":
        delete_dependente = """DELETE FROM dependent WHERE essn='123456789';"""
        cursor.execute(delete_dependente)
    elif a == "4":
        select_departament = """ SELECT dname, dnumber FROM department """""";"""
        cursor.execute(select_departament)
        b = cursor.fetchall()
    
        print()
    elif a == "5":
        select_join = """ SELECT ssn, dnumber FROM employee, department 
                               WHERE employee.dno = department.dnumber;"""
        cursor.execute(select_join)
        b = cursor.fetchall()
        c = cursor.fetchone()
        print(b)
    else:
        print("Escolha um opção valida!!!!!")