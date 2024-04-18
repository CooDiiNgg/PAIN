from models import *
from plyer import notification

end = queue.Queue()
ai_response = queue.Queue()
get_users = queue.Queue()
put_users = queue.Queue()
flag = True

filters = {'number': 2, 'excluded_users': []}
load_dotenv()
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")


checker = Checker()
threading.Thread(target=checker.run, args=(end, filters, email, password, ai_response, )).start()
while flag:
    if not ai_response.empty():
        print(ai_response.get())
        percent = ai_response.get()
        if percent > 57:
            #print notification
            print("Phishing email")
            notification.notify(
                title='Phishing Email',
                message='This email is a phishing email',
                app_name='PAIN',
                timeout=10,
            )
    if not get_users.empty():
        users = reader.get_users()
        formated_users = {}
        for user in users:
            formated_users[user[1]].append({'id': user[0], 'username': user[3], 'active': user[4]}) if user[1] in formated_users else formated_users.update({user[1]: [{'id': user[0], 'username': user[3], 'active': user[4]}]})
        get_users.put(formated_users)
    if not put_users.empty():
        user = put_users.get()
        reader.put_user(user['service'], user['password'], user['email'], user['active'])
        threading.Thread(target=checker.run, args=(end, filters, user["email"], user["password"], ai_response, )).start()