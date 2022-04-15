from urllib import response
from user_input import str_to_bool

def main():
    response = input("Would you like to continue?:")
    if str_to_bool(response):
        print("User wants to continue")
    else:
        print("User does not want to continue!")
    
# Make the func callable from the command line
# And don't run function if being imported elsewhere
if __name__ == '__main__':
    main()