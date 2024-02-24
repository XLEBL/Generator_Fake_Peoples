from util import helpers
import time
text = f"""
\t======GENERAL INFO======
\tYour name and etc. >> {helpers.gen_name()}
\tYour age >> {helpers.age()}
\tYour phone number >> {helpers.generate_phone_number()}

\t========BANK INFO======
\tYour credit card >> {helpers.credit_card()}
\tYour"""""
def main():
    print("\tOkay, let`s go!")
    print(f"{text}")
if __name__ == "__main__":
    main()