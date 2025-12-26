log = []
max_tries = 3
attempt = 0
success = False

def mock_api():
    return "fail" if attempt < 2 else "success"

try:
    while attempt < max_tries and not success:
        attempt += 1
        response = mock_api()

        if response == "success":
            log.append(f"Success on attempt {attempt}")
            success = True
        else:
            log.append(f"Attempt {attempt} failed")
except Exception as e:
    log.append(f"An error occurred: {str(e)}")



print(log)
