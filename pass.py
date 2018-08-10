
import md5
# import time

counter = 1

md5_hash = raw_input("Please enter your md5 Hash: ")
pwdfile = raw_input("Please enter the path to your wordlist file: ")

try:
    pwdfile = open(pwdfile, "r")
except:
    print "\nFile not found"
    quit()

for password in pwdfile:
    filemd5 = md5.new(password.strip()).hexdigest()
    # start = time.time()
    print "Trying passowrd %d: %s" % (counter, password.strip())

    counter += 1
    # end = time.time()
    # t_time = end - start

    if md5_hash == filemd5:
        print "\nPassword Cracked. \nThe Password is : %s" % password
        # print "Total runtime was -- ", t_time, "second"
        # time.sleep(10)
        break


else:
    print "\nPassword not Found."