"""

In this kata you have to create a domain name validator mostly compliant with RFC 1035, RFC 1123, and RFC 2181

For purposes of this kata, following rules apply:

Domain name may contain subdomains (levels), hierarchically separated by . (period) character
Domain name must not contain more than 127 levels, including top level (TLD)
Domain name must not be longer than 253 characters (RFC specifies 255, but 2 characters are reserved for trailing dot and null character for root level)
Level names must be composed out of lowercase and uppercase ASCII letters, digits and - (minus sign) character
Level names must not start or end with - (minus sign) character
Level names must not be longer than 63 characters
Top level (TLD) must not be fully numerical
Additionally, in this kata

Domain name must contain at least one subdomain (level) apart from TLD
Top level validation must be naive - ie. TLDs nonexistent in IANA register are still considered valid as long as they adhere to the rules given above.
The validation function accepts string with the full domain name and returns boolean value indicating whether the domain name is valid or not.

Examples:

validate('codewars') == False
validate('g.co') == True
validate('codewars.com') == True
validate('CODEWARS.COM') == True
validate('sub.codewars.com') == True
validate('codewars.com-') == False
validate('.codewars.com') == False
validate('example@codewars.com') == False
validate('127.0.0.1') == False

"""

#My solution: Still needs love, not passing dot tests.  I feel like I'm getting better. Even though I can solve the problems, I need to work on more effiecient code and best practices.

def validate(domain):
#     if (domain[0]) == '.':
#         return False
    if len(domain) > 253:
        return False
    dot_count = 0
    for char in domain:
        if char == ".":
            dot_count = dot_count + 1
    if dot_count == 0:
        return False
        
    d = domain.split('.')
    for part in d:

        try:
            first_p = part[0] 
            last_p = part[-1] 
            if first_p is '-':
                return False
            elif last_p is '-':
                return False
        except:
            pass

    try:
        first = d[0][0]
        
        last = d[-1][-1]
    except:
        pass
        
    try:
        if first is '-':
          return False
        elif last is '-':
          return False
    except:
        pass
    
    for part in d:
      if len(part) > 63:
          return False
        
      if part is 'com' or 'co':
        return True
      else:
      
          return False
