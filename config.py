 API_ID    = os.environ.get("API_ID", "23990433")

    API_HASH  = os.environ.get("API_HASH", "e6c4b6ee1933711bc4da9d7d17e1eb20")

    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5992501587:AAHdDLpHnleGcpCQUizT1efHLhDNYUrtuYA") 

   

    # database config

    DB_NAME = os.environ.get("DB_NAME","pyro-botz")     

    DB_URL  = os.environ.get("DB_URL","mongodb+srv://nakflixbot:alpha3720@cluster0.qgybxbu.mongodb.net/?retryWrites=true&w=majority")

 

    # other configs

    BOT_UPTIME  = time.time()

    START_PIC   = os.environ.get("START_PIC", "")

    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]

    FORCE_SUB   = os.environ.get("FORCE_SUB", "5821871362") 

    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", None))
