# -*- coding: utf-8 -*-
"""Update response to contain web service info"""

import json
from ga4gh.refget.middleware.media_type import MediaTypeMidware
from ga4gh.refget.config.service_info import SERVICE_INFO


def get_service_info(properties, request, response):
    """Refget function, get web service info

    The get_service_info function corresponds to the /sequence/service-info
    endpoint described in the refget API specification. First performs media
    type validation, then returns service info object

    Arguments:
        properties (Properties): runtime properties
        request (Request): generic refget request
        response (Response): modifiable, generic refget response
    """

    @MediaTypeMidware(properties, request, response)
    def worker(properties, request, response):
        service_info = SERVICE_INFO
        service_info["id"] = properties.get("source.service_id")
        service_info["name"] = properties.get("source.service_name")
        service_info["organization"]["name"] = properties.get("source.organization")
        service_info["organization"]["url"] = properties.get("source.organization_url")
        response.set_body(json.dumps(
            service_info
            ))
    worker(properties, request, response)