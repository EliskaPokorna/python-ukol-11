import re

def overeni_udaju(regex_jmeno, regex_email, regex_heslo):
    jmeno = input("Zadejte přihlašovací jméno: ")
    if regex_jmeno.match(jmeno):
        print("Přihlašovací jméno je platné.")
    else:
        print("Chyba: Přihlašovací jméno není platné.")
    
    email = input("Zadejte e-mailovou adresu: ")
    if regex_email.match(email):
        print("E-mailová adresa je platná.")
    else:
        print("Chyba: E-mailová adresa není platná.")

    heslo = input("Zadjte heslo: ")
    if regex_heslo.match(heslo):
        print("Heslo je platné.")
    else:
        print("Chyba: Heslo není platné.")

regex_jmeno = re.compile(r"^[\w]{6,10}$")
regex_email = re.compile(r"^[\w._+-]+@[\w.-]+\.[a-zA-Z]{2,}$")
regex_heslo = re.compile(r"^[\w\-+.=]{12,30}$")

print(overeni_udaju(regex_jmeno, regex_email, regex_heslo))