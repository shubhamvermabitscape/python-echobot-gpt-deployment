#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
    APP_TYPE = os.environ.get("MicrosoftAppType", "MultiTenant")
    APP_TENANTID = os.environ.get("MicrosoftAppTenantId", "")

    AZURE_OPENAI_ENDPOINT = "https://openaiinstance11052024.openai.azure.com/"
    AZURE_OPENAI_API_KEY = "aaaad9493f9246538886b1a3eb7f3f34"
    AZURE_OPENAI_API_VERSION = "2024-02-15-preview"
    AZURE_OPENAI_MODEL = "gpt-4"
    

    