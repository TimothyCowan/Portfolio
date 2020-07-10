import requests
import hashlib
import sys

#Function to pass 1st 5 char's from encypted password to api.
def request_api_data(encrypted_characters):
    url = 'https://api.pwnedpasswords.com/range/' + encrypted_characters
    resp = requests.get(url)
    if resp.status_code != 200: #apr2020 this link works for api if error is raised consider looking at api link
        raise RuntimeError(f'Error returning: {resp.status_code}, Check API {url}')
    return resp

#dump of matching full sha1 encyptions and there total count
def get_password_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines()) #cleaning up given format
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0 #if 0 is returned we will use this as a flag to show the password was not found in the list.

# creating sha1 encyption and assigning the 1st 5 characters to a var tht is passed through api   
def password_check(password):
    to_be_checked = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = to_be_checked[:5], to_be_checked[5:] 
    response = request_api_data(first5_char)
    return get_password_count(response, tail)

#passing ea password given through the terminal through functions: password_check -> request_api_data -> get_password_count
def main(args):
    for password in args:
        total_finds = password_check(password)
        if total_finds:
            print(f'{password} was found {total_finds} time(s)')
        else:
            print(f'{password} is good')

if __name__ == "__main__":
    main(sys.argv[1:])