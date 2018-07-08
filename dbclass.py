import pymysql


class dbbase:
    def __init__(self):
        self.db = pymysql.connect(host="192.168.0.80", user="duvuser01", passwd="Dev@123", db="leave_module",
                                  cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.db.cursor()

    def insert(self, query, parameters):
        self.cursor.execute(query, parameters)
        self.db.commit()

    def read(self, query):
        self.cursor.execute(query)
        menus = self.cursor.fetchall()
        return menus

    def update(self, query, parameters):
        self.cursor.execute(query, parameters)
        self.db.commit()

    def delete(self, query, parameters):
        self.cursor.execute(query, parameters)
        self.db.commit()

    def close(self):
        self.cursor.close()
        self.db.close()

query1 = "SELECT * FROM tbl_menus"
query2 = "SELECT * FROM tbl_roles"
query3 = "SELECT * FROM tbl_role_privileges"
query4 = "SELECT * FROM tbl_user"
query5 = "INSERT INTO tbl_menus (menu_name, if_main_menu, main_menu, display_order) VALUES (%s,%s,%s,%s)"
query6 = "UPDATE tbl_menus SET menu_name=%s, if_main_menu=%s, main_menu=%s, display_order=%s WHERE menu_ID=%s"
query7 = "INSERT INTO tbl_roles (role) VALUES (%s)"
query8 = "INSERT INTO tbl_role_privileges (menu_ID, role_ID, access) VALUES (%s,%s,%s)"
query9 = "DELETE FROM tbl_menus WHERE menu_ID=%s"
query10 = "DELETE FROM tbl_role_privileges WHERE menu_ID=%s"
query11 = "DELETE FROM tbl_roles WHERE role_ID=%s"
query12 = "DELETE FROM tbl_role_privileges WHERE role_ID=%s"
query13 = "UPDATE tbl_role_privileges SET access=%s WHERE (menu_ID=%s AND role_ID=%s)"
query14 = "INSERT INTO tbl_user (username, password, role_ID) VALUES (%s,%s,%s)"
query15 = "SELECT DISTINCT a.menu_id, a.access, a.role_ID, b.menu_name, b.if_main_menu, b.main_menu, b.display_order " \
          "FROM tbl_role_privileges a, tbl_menus b where (a.menu_id = b.menu_id AND b.if_main_menu = 1 AND a.access=1)"
query16 = "SELECT distinct a.menu_id, a.access, a.role_ID, b.menu_name, b.if_main_menu, b.main_menu, b.display_order " \
          "FROM tbl_role_privileges a, tbl_menus b where (a.menu_id = b.menu_id AND b.if_main_menu = 0 AND a.access=1)"
query17 = "SELECT * FROM tbl_menus WHERE if_main_menu=1"
query18 = "SELECT DISTINCT p.role_ID, q.role from tbl_role_privileges p, tbl_roles q WHERE p.role_ID = q.role_ID"
query19 = "UPDATE tbl_user SET username=%s, password=%s WHERE role_ID=%s"
query20 = "DELETE FROM tbl_user WHERE role_ID=%s"
query21 = "SELECT a.menu_id, a.access, a.role_ID, b.menu_name, c.role " \
          "FROM tbl_role_privileges a, tbl_menus b, tbl_roles c WHERE (a.menu_id = b.menu_id AND a.role_ID = c.role_ID)"
query22 = "SELECT * FROM tbl_menus WHERE if_main_menu=0"
