from dbclass import *

Query = dbbase()
menu_dict = {}
cur_user = {}


def validatelogin(request):
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            return "Fail"
        else:
            return "Success"
    else:
        return "Fail"


def addmenuitem(request):
    if request.method == 'POST':
        menus = Query.read(query1)
        main_menus = Query.read(query17)
        menu_dict['menu_name'] = request.form['menu']
        menu_dict['display_order'] = int(request.form['order'])
        name = request.form.get('if_main_menu')
        if name:
            menu_dict['if_main_menu'] = 1
            menu_dict['main_menu'] = None
        else:
            menu_dict['if_main_menu'] = 0
            menu_dict['main_menu'] = request.form['main_menu']
        for each_menu in menus:
            if each_menu['menu_name'] == menu_dict['menu_name']:
                if menu_dict['main_menu'] == each_menu['menu_name'] or each_menu['main_menu'] == menu_dict['menu_name']:
                    break
                else:
                    error = 'Menu Present Already'
                return menus, error, "", main_menus
        Query.insert(query5, (menu_dict['menu_name'], menu_dict['if_main_menu'], menu_dict['main_menu'],
                              menu_dict['display_order']))
        roles = Query.read(query2)
        menus = Query.read(query1)
        for each_menu in menus:
            if menu_dict['menu_name'] == each_menu['menu_name']:
                menu_id = each_menu['menu_ID']
                for each_role in roles:
                    Query.insert(query8, (menu_id, each_role['role_ID'], False))
        message = 'Menu Created'
        if 'Create Menu' in request.form:
            return menus, "", message, main_menus
    else:
        menus = Query.read(query1)
        main_menus = Query.read(query17)
        return menus, "", "", main_menus


def editmenuitem(request):
    if request.method == 'POST':
        menus = Query.read(query1)
        main_menus = Query.read(query17)
        menu_dict['menu_name'] = request.form['menu']
        menu_dict['display_order'] = int(request.form['order'])
        for each_menu in menus:
            if each_menu['menu_name'] == menu_dict['menu_name']:
                menu_id = each_menu['menu_ID']
                name = request.form.get('if_main_menu')
                if name:
                    menu_dict['if_main_menu'] = 1
                    menu_dict['main_menu'] = None
                else:
                    menu_dict['if_main_menu'] = 0
                    menu_dict['main_menu'] = request.form['main_menu']
                Query.update(query6, (menu_dict['menu_name'], menu_dict['if_main_menu'], menu_dict['main_menu'],
                                      menu_dict['display_order'], menu_id))
                message = 'Menu Edited'
                return menus, "", message, main_menus
        error = 'Menu Not Present'
        return menus, error, "", main_menus
    else:
        menus = Query.read(query1)
        main_menus = Query.read(query17)
        return menus, "", "", main_menus


def addroledata(request):
    if request.method == 'POST':
        roles = Query.read(query2)
        new_role = request.form['roles']
        for role in roles:
            if role['role'] == new_role:
                error = 'Role Present Already'
                return "", error
        Query.insert(query7, new_role)
        message = 'Role Created'
        if 'add' in request.form:
            return message, ""
    else:
        return "", ""


def setroleprivilegees(request):
    if request.method == 'POST':
        roles = Query.read(query2)
        menus = Query.read(query1)
        main_menus = Query.read(query17)
        sub_menus = Query.read(query22)
        assigned = Query.read(query18)
        each_role = request.form['role']
        for role in assigned:
            if each_role == role['role']:
                error = 'Privileges Already Assigned'
                return menus, roles, error, "", main_menus, sub_menus
        for role in roles:
            if each_role == role['role']:
                role_id = role['role_ID']
                for each_menu in menus:
                    name = request.form.get(each_menu['menu_name'])
                    if name:
                        Query.insert(query8, (each_menu['menu_ID'], role_id, True))
                    else:
                        Query.insert(query8, (each_menu['menu_ID'], role_id, False))
                message = 'Role Privileges Set'
                if 'Assign Menus' in request.form:
                    return menus, roles, "", message, main_menus, sub_menus
        error = 'Role not Created'
        return menus, roles, error, "", main_menus, sub_menus
    else:
        menus = Query.read(query1)
        main_menus = Query.read(query17)
        roles = Query.read(query2)
        sub_menus = Query.read(query22)
        return menus, roles, "", "", main_menus, sub_menus


def editroleprivileges(request):
    if request.method == 'POST':
        menus = Query.read(query1)
        roles = Query.read(query2)
        assigned = Query.read(query18)
        main_menus = Query.read(query17)
        sub_menus = Query.read(query22)
        each_role = request.form['role']
        for role in assigned:
            if each_role == role['role']:
                role_id = role['role_ID']
                for each_menu in menus:
                    name = request.form.get(each_menu['menu_name'])
                    if name:
                        Query.update(query13, (True, each_menu['menu_ID'], role_id))
                    else:
                        Query.update(query13, (False, each_menu['menu_ID'], role_id))
                message = 'Role Edited'
                if 'Assign Menus' in request.form:
                    return  menus, roles, "", message, main_menus, sub_menus
        error = 'Role Not Assigned Earlier'
        if 'Assign Menus' in request.form:
            return menus, roles, error, "", main_menus, sub_menus
    else:
        menus = Query.read(query1)
        roles = Query.read(query2)
        main_menus = Query.read(query17)
        sub_menus = Query.read(query22)
        return menus, roles, "", "", main_menus, sub_menus


def useradd(request):
    if request.method == 'POST':
        new_role = request.form['role']
        username = request.form['username']
        password = request.form['password']
        roles = Query.read(query2)
        users = Query.read(query4)
        for one_role in roles:
            if one_role['role'] == new_role:
                role_id = one_role['role_ID']
                for each_user in users:
                    if each_user['role_ID'] == role_id:
                        Query.update(query19, (username, password, each_user['role_ID']))
                        message = 'Username and Password Set'
                        return roles, message
        for each_role in roles:
            if each_role['role'] == new_role:
                role_id = each_role['role_ID']
                Query.insert(query14, (username, password, role_id))
                message = 'Username and Password Set'
                return roles, message
    else:
        roles = Query.read(query2)
        return roles, ""


def validateuserlogin(request):
    if request.method == 'POST':
        users = Query.read(query4)
        username = request.form['username']
        password = request.form['password']
        for user in users:
            if user['username'] == username and user['password'] == password:
                cur_user['role_id'] = user['role_ID']
                return "Success"
        return "Fail"
    else:
        return "Fail"


def deletemenu(request):
    if request.method == 'POST':
        menus = Query.read(query17)
        sub_menus = Query.read(query22)
        name = request.form.get('if_main_menu')
        if name:
            for each_menu in menus:
                if each_menu['menu_name'] == request.form['menu_name']:
                    menu_id = each_menu['menu_ID']
                    Query.delete(query9, menu_id)
                    Query.delete(query10, menu_id)
                    message = 'Menu Deleted'
                    return "", message, menus
        for each_menu in sub_menus:
            if each_menu['menu_name'] == request.form['menu_name']:
                menu_id = each_menu['menu_ID']
                Query.delete(query9, menu_id)
                Query.delete(query10, menu_id)
                message = 'Menu Deleted'
                return "", message, menus
        error = 'No Menu Found'
        if 'Delete Menu' in request.form:
            return error, "", menus
    else:
        menus = Query.read(query1)
        return "", "", menus


def deleterole(request):
    if request.method == 'POST':
        roles = Query.read(query2)
        del_role = request.form['role_name']
        for role in roles:
            if role['role'] == del_role:
                role_id = role['role_ID']
                Query.delete(query11, role_id)
                Query.delete(query12, role_id)
                Query.delete(query20, role_id)
                message = 'Role Deleted'
                return "", message, roles
        error = 'Role Not Found'
        if 'Delete Role' in request.form:
            return error, "", roles
    else:
        roles = Query.read(query2)
        return "", "", roles


def menupage():
    all_roles = Query.read(query3)
    main_menu_list = Query.read(query15)
    sub_menu_list = Query.read(query16)
    new = main_menu_list
    new_menu_list = sorted(new, key=lambda k: k['display_order'])
    new_sub = sub_menu_list
    new_sub_menu_list = sorted(new_sub, key=lambda k: k['display_order'])
    return new_menu_list, all_roles, cur_user, new_sub_menu_list

