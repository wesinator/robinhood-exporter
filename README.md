# robinhood-exporter

#### Usage:

No API auth required:
1. Browse https://robinhood.com/ (logged in), open developer tools
2. Look for request to `https://api.robinhood.com/midlands/lists/default/`
3. Save raw response from this request to .json
4. Run Python script taking json filename as argument to function.

You can alternatively get `https://api.robinhood.com/midlands/lists/default/`
from API when authenticated, using a robinhood API client such as https://github.com/jmfernandes/robin_stocks

I didn't want to mess with that here if account has 2FA, and this is meant to be a one-time operation.

_#DeleteRobinhood_

#### License

Licensed under 4-clause BSD
