from jsonrpc import ServiceProxy
access = ServiceProxy("http://127.0.0.1:4316")
pwd = raw_input("Enter wallet passphrase: ")
access.walletpassphrase(pwd, 60)
