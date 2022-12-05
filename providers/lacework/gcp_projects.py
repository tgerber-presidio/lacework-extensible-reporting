import logging
logger = logging.getLogger(__name__)

from . import lw
from . import LWApiError

import json
   
def gcp_projects(org_id=''):
    results = []
    
    try:
        logger.info('Getting Projects for organizations: ' + org_id)
        a = lw().compliance.list_gcp_projects(gcp_organization_id=org_id)
        results.extend(a['data'][0]['projects'])
    except LWApiError:
        logger.warning('Could not get projects for organizations: ' + org_id)

    return results