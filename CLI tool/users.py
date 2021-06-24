import pwd 

def fetch_users():
    users=[]
    for user in pwd.getpwall():
        if user.pwd_uid>=1000 and 'home' in user.pwd_dir:
            user.append({
                'name' : user.pw_name,
                'id' : user.pw_uid,
                'home' : user.pw_dir,
                'shell': user.pw_shell,
            })
    return users