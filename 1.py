import re
import sys

# Question 1: Resume Information Extraction

print("RESUME INFORMATION EXTRACTION")

name = input("Enter name: ")
email = input("Enter email: ")
mobile = input("Enter mobile number: ")
skills = input("Enter skills: ")
experience = input("Enter years of experience: ")

if not re.fullmatch(r"[\w.-]+@[\w.-]+\.[A-Za-z]{2,}", email):
    print("Invalid email")
    print("NOT ELIGIBLE")
    sys.exit()

if not re.fullmatch(r"\d{10}", mobile):
    print("Invalid mobile number")
    print("NOT ELIGIBLE")
    sys.exit()

if not re.fullmatch(r"\d+", experience):
    print("Invalid experience")
    print("NOT ELIGIBLE")
    sys.exit()

experience = int(experience)

found = re.findall(
    r"Python|Java|SQL|Machine Learning|NLP", skills, re.I
)

if not found:
    print("Invalid skills")
    print("NOT ELIGIBLE")
    sys.exit()

print("\nResume Details")
print("Name:", name)
print("Email: Valid")
print("Mobile:", mobile)
print("Skills:", found)

if experience >= 2 and re.search(r"Python", skills, re.I):
    print("Eligible: Yes")
else:
    print("NOT ELIGIBLE")
    sys.exit()


# Question 2: Product Search System

print("\nPRODUCT SEARCH SYSTEM")

products = [
    "Python Book",
    "Java Book",
    "SQL Guide",
    "Python Course",
    "NLP Book"
]

keyword = input("Enter product keyword: ").strip()
choice = input(
    "Enter search type (exact/prefix/suffix/partial): "
).strip().lower()

if choice not in ["exact", "prefix", "suffix", "partial"]:
    print("Invalid search type")
    print("NOT ELIGIBLE")
    sys.exit()

if keyword == "":
    print("Invalid keyword")
    print("NOT ELIGIBLE")
    sys.exit()

count = 0

for product in products:
    if choice == "exact":
        match = product.lower() == keyword.lower()
    elif choice == "prefix":
        match = product.lower().startswith(keyword.lower())
    elif choice == "suffix":
        match = product.lower().endswith(keyword.lower())
    else:
        match = keyword.lower() in product.lower()

    if match:
        print("Match:", product)
        count += 1

print("Total matching products:", count)

if count == 0:
    print("No product found")
    print("NOT ELIGIBLE")
    sys.exit()


# Question 3: University Registration Validation

print("\nUNIVERSITY REGISTRATION")

reg = input("Enter register number: ").strip()
college_email = input("Enter university email: ").strip()
course = input("Enter course code: ").strip()
semester = input("Enter semester (1-8): ").strip()
phone = input("Enter mobile number: ").strip()

if not re.fullmatch(r"\d{9}", reg):
    print("Invalid register number")
    print("NOT ELIGIBLE")
    sys.exit()

if not re.fullmatch(
    r"\d{9}\.simats@saveetha\.com", college_email, re.I
):
    print("Invalid university email")
    print("NOT ELIGIBLE")
    sys.exit()

email_reg = college_email.split(".")[0]

if reg != email_reg:
    print("Register number and email do not match")
    print("NOT ELIGIBLE")
    sys.exit()

if not re.fullmatch(r"[A-Z]{2,4}\d{2,4}", course, re.I):
    print("Invalid course code")
    print("NOT ELIGIBLE")
    sys.exit()

if not re.fullmatch(r"[1-8]", semester):
    print("Invalid semester")
    print("NOT ELIGIBLE")
    sys.exit()

if not re.fullmatch(r"\d{10}", phone):
    print("Invalid mobile number")
    print("NOT ELIGIBLE")
    sys.exit()

if not re.fullmatch(r"\d{10}", mobile) or phone != mobile:
    print("Mobile number does not match Q1")
    print("NOT ELIGIBLE")
    sys.exit()



print("Register number: Valid")
print("University email: Valid")
print("Course code: Valid")
print("Semester: Valid")
print("Mobile number: Valid and matches Q1")
print("Registration Status: SUCCESSFUL")
print("ELIGIBLE")
