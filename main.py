from flask import Flask, render_template, redirect, url_for, request
from service import *

app = Flask(__name__)

'''
Login Handler
'''


@app.route('/', methods=['GET', 'POST'])
def login():
    response = validatelogin(request)
    if response == "Success":
        return redirect(url_for('menu'))
    else:
        return render_template('login.html')


'''
    Menu Creation Handler
'''


@app.route('/menu', methods=['GET', 'POST'])
def menu():
    menus, error, message, main_menus = addmenuitem(request)
    return render_template('menu.html', Menu_list=menus,error=error, message=message, Main_menus=main_menus)


'''
    Menu Edit Handler
'''


@app.route('/edit', methods=['POST', 'GET'])
def edit_menu():
    menus, error, message, main_menus = editmenuitem(request)
    return render_template('edit.html', Menu_list=menus, error=error, message=message, Main_menus=main_menus)


'''
    Roles Creation
'''


@app.route('/addrole', methods=['POST', 'GET'])
def addrole():
    message, error = addroledata(request)
    return render_template('createrole.html', error=error, message=message)


'''
    Role Privileges Handler
'''


@app.route('/role', methods=['POST', 'GET'])
def role():
    menus, roles, error, message, main_menus, sub_menus = setroleprivilegees(request)
    return render_template('role.html', Menu_list=menus, Roles=roles, error=error, Main_menus=main_menus, Sub_menus=sub_menus)


'''
    Role Edition Handler
'''


@app.route('/roleedit', methods=['POST', 'GET'])
def roleedit():
    menus, roles, error, message, main_menus, sub_menus = editroleprivileges(request)
    return render_template('editrole.html', Menu_list=menus, Roles=roles, error=error,
                           message=message, Main_menus=main_menus, Sub_menus=sub_menus)


'''
    User Setup Handler
'''


@app.route('/usersetup', methods=['POST', 'GET'])
def usersetup():
    roles, message = useradd(request)
    return render_template('usersetup.html', Roles=roles, message=message)


'''
    User Login Handler
'''


@app.route('/userlogin', methods=['POST', 'GET'])
def userlogin():
    response = validateuserlogin(request)
    if response == "Success":
        return redirect(url_for('user'))
    else:
        return render_template('userlogin.html')


'''
    Menu Deletion Handler
'''


@app.route('/delmenu', methods=['POST', 'GET'])
def delmenu():
    error, message, menus = deletemenu(request)
    return render_template('delmenu.html', error=error, messgae=message, Menus=menus)


'''
    Menu Deletion Handler
'''


@app.route('/delrole', methods=['POST', 'GET'])
def delrole():
    error, message, roles = deleterole(request)
    return render_template('delrole.html', error=error, message=message, Roles=roles)


'''
    Menu Display Handler
'''


@app.route('/user', methods=['POST', 'GET'])
def user():
    new_menu_list, all_roles, cur_user, new_sub_menu_list = menupage()
    return render_template('menubar.html', Menu_list=new_menu_list, All_roles=all_roles, Cur_user=cur_user, Sub_Menu_list=new_sub_menu_list)


if __name__ == '__main__':
    app.run(debug=True, port="8001")