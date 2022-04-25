class vigenere:

	def __init__(self,keyt,alphabet="abcdefghijklmnopqrstuvwxyz"):
		self.point = 0
		self.keyt = keyt
		self.keytLens = len(self.keyt)
		self.alphabet = alphabet
		self.alphabetLens = len(self.alphabet)

	def reset(self):
		self.point = 0

	def encrypt(self,plainElement):
		PlainNum = self.alphabet.find(plainElement)
		KeyNum = self.alphabet.find(self.keyt[self.point])
		EncPlain = self.alphabet[(PlainNum+KeyNum)%self.alphabetLens]
		self.point = (self.point+1)%self.keytLens 
		return EncPlain

	def decrypt(self,plainElement):
		PlainNum = self.alphabet.find(plainElement)
		KeyNum = self.alphabet.find(self.keyt[self.point])
		EncPlain = self.alphabet[(PlainNum-KeyNum)%self.alphabetLens]
		self.point = (self.point+1)%self.keytLens 
		return EncPlain

def decode(keyt,alphabet,ciphertext):
	maker = vigenere(keyt.lower(),alphabet)
	plaintext = ""
	for i in ciphertext:
		if i == " ":
			plaintext += i
		else:
			plaintext += maker.decrypt(i)
	return plaintext

alphabet = "abcdefghijklmnopqrstuvwxyz0123456789,.!{}\""
keyt = "welcometocvvd"

ciphertext1 = '4x 7c6 mr {1h9!j0x4cpxi 76ev! q4ksv 2z w{1fvd l9 pzu ozkxzg{ 0r{ env23 01zn {7l"lg'
ciphertext2 = '{snm6 vs3s tz6d"io v2 1m6yg}} v8m4j6 te15nz{v 3ilfj 1m6yg}} v8m4j vmw t 0gy3fwp nq1pm!wq8 }kwx lhtqg!6 jv3u 2vzy7t"'
ciphertext3 = '}qtvvmhwsf}2d"jlo26w8sq,6haw5czx20oxz}rvxlmsmf{6gqq}}qtnsmrw3tz}h9hwkyqx0ov{9nw2k{'
ciphertext4 = '4q oc1 rv1sfz6or'
ciphertext5 = '1plil"!vo5zzhi!b,t{9ge6in,lh!.db7mshxt'

print(decode(keyt,alphabet,ciphertext2))
print(decode(keyt,alphabet,ciphertext2))
print(decode(keyt,alphabet,ciphertext3))
print(decode(keyt,alphabet,ciphertext4))
print(decode(keyt,alphabet,ciphertext5))
