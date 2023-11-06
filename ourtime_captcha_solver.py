import capsolver
from urllib.parse import urlparse

# Change this information
capsolver.api_key = "Your pay per usage key"

def solve_funcaptcha_ourtime():
    solution = capsolver.solve({
    "type": "FunCaptchaTaskProxyLess",
        "websiteURL": "https://ourtime.com",
        "websitePublicKey": "85800716-F435-4981-864C-8B90602D10F7",
        "funcaptchaApiJSSubdomain": "https://client-api.arkoselabs.com"
    })
    return solution

def main():
    
    print("Solving ourtime captcha")
    solution = solve_funcaptcha_ourtime()
    
    token = solution["token"]
    
    print("Token Solution " + token)
    
if __name__ == "__main__":
    main()
