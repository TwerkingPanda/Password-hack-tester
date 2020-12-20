import requests
import hashlib

# k-anonymity : text is passed through a hash function (indempotent; same input - always the same output).
# A hashed version is created and only first 5 characters are shared. In response, all the hashe tails with the same initial 5 are 
# returned. The system then matches the original hash with the list received and authenticates.

def api_call(head,tail):		#hash_password_K-Anonimised
	resp = requests.get('https://api.pwnedpasswords.com/range/' + head)		# returns a str object. hash:times\r\n format
	if resp.status_code != 200:
		raise ValueError('The query passed is not properly Hashed. Please verify again')
	haslist_and_times = (i.split(':') for i in resp.text.splitlines())
	for h,c in lst:
		if h == hashp_tail:
			return c
	return 0

def hashing(password):

	hash_object = hashlib.sha1(b'{password}')				#password.encode() would also work. Hash functions takes a sequence of bytes as input. 
	hashpass  =  hash_object.hexdigest().upper()
#hexdigest() returns a HEX string representing the hash. for sequence of bytes use digest() instead
	head, tail = hashpass[:5], hashpass[5:]
	times = api_call(head, tail)

	if times:
		print(f'The password {password} was found {times} times. You should cosider changing it.')
	else:
		print(f'No instance of {password} found. Carry on.')
	
if __name__ == '__main__':
	with open('passwords.txt', 'r') as p:
	for l in p:
		l=l.strip('\n')
		hashing(l)
