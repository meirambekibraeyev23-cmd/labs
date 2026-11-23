file = open("mailbox.txt", "r")
domains = []

for line in file:
    if line.startswith("To:"):
        email = line[3:].strip()
        domain = email.split("@")[1]
        domains.append(domain)

file.close()

domains = sorted(set(domains))

file = open("output.txt", "w")

for domain in domains:
    file.write(domain + "\n")

file.close()