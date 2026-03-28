from src.base import logger
from src.base.log_decorator import automation_logger
from src.base.services.svc_requests.request_constants import *
from src.base.services.svc_requests.request_schema import ApiRequestSchema


class ApiServiceRequest(ApiRequestSchema):
    def __init__(self):
        super(ApiServiceRequest, self).__init__()
        self.method = "Api."

    @automation_logger(logger)
    def create_api_token(self, token_name: str) -> str:
        """
        Builds request body for ApiService.create_api_token()
        :param token_name: Any string.
        :return: Request body as serialized ``obj`` into a JSON formatted ``str``.
        """
        self.method += "CreateApiToken"
        self.params.extend([
            {
                NAME: token_name,
                SMS_TYPE: 6,
                ACTION: "create",
                CODE: "123456"
            }
        ])
        body = self.to_json()
        logger.logger.info(REQUEST_BODY.format(body))
        return body

    @automation_logger(logger)
    def change_api_token_activation(self, token_id: int, token_state: bool) -> str:
        """
        Builds request body for ApiService.activate_api_token()
        :param token_id: ID to activate.
        :param token_state: True if active and False otherwise.
        :return: Request body as serialized ``obj`` into a JSON formatted ``str``.
        """
        self.method += "ChangeApiTokenActivation"
        self.params.extend([
            {
                ID: token_id,
                IS_ACTIVE: token_state
            }
        ])
        body = self.to_json()
        logger.logger.info(REQUEST_BODY.format(body))
        return body

    @automation_logger(logger)
    def delete_api_token(self, token_id: int) -> str:
        """
        Builds request body for ApiService.delete_api_token()
        :param token_id: ID to delete.
        :return: Request body as serialized ``obj`` into a JSON formatted ``str``.
        """
        self.method += "DeleteApiToken"
        self.params.extend([
            {
                ID: token_id
            }
        ])
        body = self.to_json()
        logger.logger.info(REQUEST_BODY.format(body))
        return body

    @automation_logger(logger)
    def update_api_token(self, token_id: int, token_name: str, ip_1: str, ip_2: str) -> str:
        """
        Builds request body for ApiService.update_api_token()
        :param token_id: Token ID to update.
        :param token_name: Token name to update.
        :param ip_1: IP.
        :param ip_2: IP.
        :return: Request body as serialized ``obj`` into a JSON formatted ``str``.
        """
        self.method += "UpdateApiToken"
        self.params.extend([
            {
                ID: token_id,
                NAME: token_name,
                IPS: [ip_1, ip_2]
            }
        ])
        body = self.to_json()
        logger.logger.info(REQUEST_BODY.format(body))
        return body

    @automation_logger(logger)
    def renew_api_token(self, api_key: str, token_id: int) -> str:
        """
        Builds request body for ApiService.renew_api_token()
        :param api_key: String (same as api token name).
        :param token_id: Token ID to renew.
        :return: Request body as serialized ``obj`` into a JSON formatted ``str``.
        """
        self.method += "RenewApiToken"
        self.params.extend([
            {
                ID: token_id,
                NAME: api_key,
                SMS_TYPE: 7,
                ACTION: "renew",
                CODE: "123456"
            }
        ])
        body = self.to_json()
        logger.logger.info(REQUEST_BODY.format(body))
        return body

    @automation_logger(logger)
    def get_api_tokens(self) -> str:
        """
        Builds request body for ApiService.get_api_token()
        :return: Request body as serialized ``obj`` into a JSON formatted ``str``.
        """
        self.method += "GetApiTokens"
        self.params.extend([{}])
        body = self.to_json()
        logger.logger.info(REQUEST_BODY.format(body))
        return body
