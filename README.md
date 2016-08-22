Cachet Telegram Bot
===================
Bot for manage cachethq.io status pages

Setup
-----

You need to set following environment variables:
```
API_TOKEN    # Cachet API token
API_ENDPOINT # Cachet endpoint, i.e. http://status.domain.tld/api/v1

BOT_TOKEN    # Telegram Bot API token
```

If you want to use `docker-compose` to deploy your bot, then create appropriate `.env` file
in your environment. 

Run
---

```
docker-compose up
```

Logs
----
```
docker-compose logs
```

Commands
--------

```
/incidents   # Shows all registered (unclosed) incidents
```