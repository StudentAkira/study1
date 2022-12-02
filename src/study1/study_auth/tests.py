import json

with open('keys.json', 'r+') as keys_file:
    keys = ''.join([item.strip('\t').strip('\n') for item in keys_file.readlines()])
    print(keys)
    keys = json.loads(keys)

"""
{
	"secret_django_key":"django-insecure-p*2fxw8o)%(#(uou@xog2c754rjoz+s*p=wsl1=x+t!b2+%+*w",
	"database_name":"study1",
	"database_user":"study_admin",
	"database_password":"study",
	"database_host":"localhost",
	"database_port":"5432",

	"vk_app_id":"8210508",
	"vk_app_secret":"edU3gRwxDig958p6n6yM",
	"vk_app_key":"1152a30d1152a30d1152a30d61112feb41111521152a30d73905f2eaccdd1ce20e1bb7e",
	
	"gmail_smpt_login":"yapakira82@gmail.com",
	"gmail_smtp_password":"akmmulwzqjtrghls",
}	

"""