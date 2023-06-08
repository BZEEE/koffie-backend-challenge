
"""
General Logging utility class
currently just a stub, but the intent would be to
- allow the devs to view the logs locally for debugging purposes
- funnel the logs to a separate log monitoring service
  to support historical log retention for different environments,
  as well as possible event monitoring platforms for service reliability strategies
- Ultimately we want to control how the errors are show back to the consumer of this service
- Typically we would want to throw them some form of general error that is helpful to make
  them successfully call the service, but we want to encapsulate any domain or business logic
  of our API that users cannot find and exploit vulnerabilities
"""


class Logger:
    @staticmethod
    def log(exception: Exception):
        # For example if we use GCP or AWS to store our logs
        # Then we could use Splunk to monitor for events and setup alerts
        print(exception)


