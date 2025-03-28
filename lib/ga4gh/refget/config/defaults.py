# -*- coding: utf-8 -*-
"""Default values for modifiable server properties"""

DEFAULT_SOURCE_BASE_URL = "http://insdc-mirror.s3-website-us-west-2.amazonaws.com"
"""Refget server points to INSDC AWS S3 bucket by default"""

DEFAULT_SOURCE_SEQUENCE_PATH = "/sequence/{seqid}"
"""Refget server resolves sequence requests to specified dir in S3 bucket"""

DEFAULT_SOURCE_METADATA_PATH = "/metadata/json/{seqid}.json"
"""Refget server resolves metadata requests to specified dir in S3 bucket"""

DEFAULT_SERVER_PORT = 8888
"""Default port server runs on"""

DEFAULT_LOCAL_OPENAPI_FILE = None
"""By default, no openapi file provided, server will not serve Swagger UI"""

DEFAULT_SERVICE_NAME = "Refget Service"
"""Service name. Should be human readable."""

DEFAULT_SERVICE_ID = "refget.server.v2"
"""Unique ID of this service. Reverse domain name notation is recommended, though not required."""

DEFAULT_ORGANIZATION = "Example Org"
"""By default, the organization is Example Org. Outside tests this should be overwritten."""

DEFAULT_ORGANIZATION_URL = "https://www.examples.com"
"""By default, the organization url is https://www.examples.com. Outside tests this should be overwritten."""

DEFAULT_ALLOWED_PROPERTY_KEYS = {
    "source.base_url",
    "source.sequence_path",
    "source.metadata_path",
    "source.service_id",
    "source.service_name",
    "source.organization",
    "source.organization",
    "source.organization_url",
    "server.port",
    "local.openapi_file"
}
"""Allowed modifiable properties in properties file"""

DEFAULT_PROPERTIES = {
    "source.base_url": DEFAULT_SOURCE_BASE_URL,
    "source.sequence_path": DEFAULT_SOURCE_SEQUENCE_PATH,
    "source.metadata_path": DEFAULT_SOURCE_METADATA_PATH,
    "source.service_id": DEFAULT_SERVICE_ID,
    "source.service_name": DEFAULT_SERVICE_NAME,
    "source.organization": DEFAULT_ORGANIZATION,
    "source.organization_url": DEFAULT_ORGANIZATION_URL,
    "server.port": DEFAULT_SERVER_PORT,
    "local.openapi_file": DEFAULT_LOCAL_OPENAPI_FILE
}
"""Default properties for each property key"""