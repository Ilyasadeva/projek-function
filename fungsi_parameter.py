def selamat_datang(nama):
    print('halo', nama, 'apa kabar?')
    
selamat_datang('budi')
def greetings(nama, waktu):
    print('hello',nama , 'sudah datang' ,waktu, 'ini?')
greetings('andi' ,'pagi')
greetings('rudy' ,'siang')
greetings('wahyu' ,'malam')


greetings('malam', 'wahyu') # positional parameter
greetings(waktu='malam', nama='wahyu') # fixed parameter