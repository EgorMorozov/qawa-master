from utilities import cli
import definitions

# REPORTING CONSTANTS
SCREENSHOT_DIR = definitions.ROOT_DIR + "/screenshots/"
REPORTS_DIR = definitions.ROOT_DIR + "/reports/"
PROJECT_NAME = "Egor_Inspect_shop_automation"
REPORT_NAME = "Egor_test_report"

# ENVIRONMENTS
DEV = "dev"
STAGING = "staging"

# ENVIRONMENT CONSTANTS
URLS = {DEV: "https://qaworkshop.netlify.app/", STAGING: "STAGING_URL"}

# DRIVER CONSTANTS
DRIVER_TIMEOUT = 30

# DERIVED CONSTANTS
ARGS = cli.get_cli_args()

BROWSER = ARGS.browser
ENV = ARGS.env
REPORT = ARGS.report
SCOPE = ARGS.scope

BASE_URL = URLS[ENV]
