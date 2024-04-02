import os

import sentry_sdk

sentry_url = os.environ.get('SENTRY_URL', '')
sentry_sdk.init(
    dsn=sentry_url,
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)
