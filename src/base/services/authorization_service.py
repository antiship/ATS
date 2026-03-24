import json
import requests
from src.base import logger
from src.base.log_decorator import automation_logger
from src.base.services.service_route import ServiceRoute
from src.base.services.svc_requests.authorization_requests import AuthorizationServiceRequest


class AuthorizationService(ServiceRoute):
    def __init__(self, auth_token=None):
        super(AuthorizationService, self).__init__()
        self.headers.update({'Authorization': auth_token})

    @automation_logger(logger)
    def get_session_data(self) -> object:
        """

        :return:
        """
        payload = AuthorizationServiceRequest().session_data()
        try:
            _response = requests.post(self.api_url, data=payload, headers=self.headers)
            body = json.loads(_response.text)
            logger.logger.info("Service Response: {0}".format(body))
            return body
        except Exception as e:
            logger.logger.exception(F"{e.__class__.__name__} get_session_data failed with error: {e}")
            raise e

    @automation_logger(logger)
    def sign_up_step_1(self, customer) -> object:
        """
        Registration- step 1
        Sends HTTP POST request to AuthorizationService to fill registration form.
        :param customer: Customer object.
        :return: Response body as a JSON.
        """
        # MailGun.get_logs(customer.email)
        payload = AuthorizationServiceRequest().step_one(customer)
        try:
            _response = requests.post(self.api_url, data=payload, headers=self.headers)
            body = json.loads(_response.text)
            logger.logger.info("Service Response: {0}".format(body))
            return body
        except Exception as e:
            logger.logger.exception(F"{e.__class__.__name__} sign_up_step_1 failed with error: {e}")
            raise e

    @automation_logger(logger)
    def log_in_by_tfa_token(self, tfa_token: str) -> object:
        payload = AuthorizationServiceRequest().login_by_tfa_token(tfa_token)
        try:
            _response = requests.post(self.api_url, data=payload, headers=self.headers)
            body = json.loads(_response.text)
            logger.logger.info("Service Response: {0}".format(body))
            return body
        except Exception as e:
            logger.logger.exception(F"{e.__class__.__name__} log_in_by_tfa_token failed with error: {e}")
            raise e

    @automation_logger(logger)
    def enable_tfa_step_1(self, password: str) -> object:
        """
        Enables TFA - customer must be logged in.
        First step required to enable the tfa verification.
        :param password: Password of the customer used for this test
        :return:
        """
        payload = AuthorizationServiceRequest().enable_tfa_step_1(password)
        try:
            _response = requests.post(self.api_url, data=payload, headers=self.headers)
            body = json.loads(_response.text)
            logger.logger.info("Service Response: {0}".format(body))
            return body
        except Exception as e:
            logger.logger.exception(F"{e.__class__.__name__} enable_tfa_step_1 failed with error: {e}")
            raise e

    @automation_logger(logger)
    def enable_tfa_step_2(self, code) -> object:
        """
        Second step required to enable the tfa verification
        :param code: Code sent to customer's phone for tfa verification. Hardcoded.
        :return:
        """
        payload = AuthorizationServiceRequest().enable_tfa_step_2(code)
        try:
            _response = requests.post(self.api_url, data=payload, headers=self.headers)
            body = json.loads(_response.text)
            logger.logger.info("Service Response: {0}".format(body))
            return body
        except Exception as e:
            logger.logger.exception(F"{e.__class__.__name__} enable_tfa_step_2 failed with error: {e}")
            raise e

    @automation_logger(logger)
    def verify_email_step_2(self, email: str, ver_token: str) -> object:
        """
        Registration- step 2
        Sends HTTP POST request to AuthorizationService to validate token via customer email.
        :param email: Customer email.
        :param ver_token: Verification token as str.
        :return: Response body as a JSON.
        """
        payload = AuthorizationServiceRequest().step_two(email, ver_token)
        try:
            _response = requests.post(self.api_url, data=payload, headers=self.headers)
            body = json.loads(_response.text)
            logger.logger.info("Service Response: {0}".format(body))
            return body
        except Exception as e:
            logger.logger.exception(F"{e.__class__.__name__} verify_email_step_2 failed with error: {e}")
            raise e

    @automation_logger(logger)
    def add_phone_step_3(self, customer) -> object:
        """
        Registration- step 3
        Sends HTTP POST request to AuthorizationService to add customer phone number.
        :param customer: Customer object.
        :return: Response body as a JSON.
        """
        # 1- method, 2- phone, 3- country_code, 4- language
        payload = AuthorizationServiceRequest().step_three(customer)
        try:
            _response = requests.post(self.api_url, data=payload, headers=self.headers)
            body = json.loads(_response.text)
            logger.logger.info("Service Response: {0}".format(body))
            return body
        except Exception as e:
            logger.logger.exception(F"{e.__class__.__name__} add_phone_step_3 failed with error: {e}")
            raise e

    @automation_logger(logger)
    def verify_phone_step_4(self) -> object:
        """
        Registration- step 4
        Sends HTTP POST request to AuthorizationService to validate phone number.
        :return: Response body as a JSON.
        """
        payload = AuthorizationServiceRequest().step_four()
        try:
            _response = requests.post(self.api_url, data=payload, headers=self.headers)
            body = json.loads(_response.text)
            logger.logger.info("Service Response: {0}".format(body))
            return body
        except Exception as e:
            logger.logger.exception(F"{e.__class__.__name__} verify_phone_step_4 failed with error: {e}")
            raise e

    @automation_logger(logger)
    def update_personal_details_step_5(self, customer) -> object:
        """
        Registration- step 5
        Sends HTTP POST request to AuthorizationService to update customer account details.
        :param customer: Customer object.
        :return: Response body as a JSON.
        """
        payload = AuthorizationServiceRequest().step_five(customer)
        try:
            _response = requests.post(self.api_url, data=payload, headers=self.headers)
            body = json.loads(_response.text)
            logger.logger.info("Service Response: {0}".format(body))
            return body
        except Exception as e:
            logger.logger.exception(F"{e.__class__.__name__} update_personal_details_step_5 failed with error: {e}")
            raise e

    @automation_logger(logger)
    def client_checklist_step6(self) -> object:
        payload = AuthorizationServiceRequest().step_six()
        try:
            _response = requests.post(self.api_url, data=payload, headers=self.headers)
            body = json.loads(_response.text)
            logger.logger.info("Service Response: {0}".format(body))
            return body
        except Exception as e:
            logger.logger.exception(F"{e.__class__.__name__} client_checklist_step6 failed with error: {e}")
            raise e

    @automation_logger(logger)
    def upload_documents_step_7(self, link1: str, link2: str, link3: str) -> object:
        """
        Registration- step 7
        Sends HTTP POST request to AuthorizationService to upload documents.
        :param link1: Link to file provided from FileService.
        :param link2: Link to file provided from FileService.
        :param link3: Link to file provided from FileService.
        :return: Response body as a JSON.
        """
        payload = AuthorizationServiceRequest().step_seven(link1, link2, link3)
        try:
            _response = requests.post(self.api_url, data=payload, headers=self.headers)
            body = json.loads(_response.text)
            logger.logger.info("Service Response: {0}".format(body))
            return body
        except Exception as e:
            logger.logger.exception(F"{e.__class__.__name__} upload_documents_step_7 failed with error: {e}")
            raise e

    @automation_logger(logger)
    def login_by_credentials(self, email: str, password: str) -> object:
        """
        Sends HTTP POST request to AuthorizationService to log in and receive auth_token.
        :param email: Customer email.
        :param password: Customer password.
        :return: Response body as a JSON.
        """
        payload = AuthorizationServiceRequest().login_by_credentials(email, password)
        try:
            _response = requests.post(self.api_url, data=payload, headers=self.headers)
            body = json.loads(_response.text)
            logger.logger.info("Service Response: {0}".format(body))
            return body
        except Exception as e:
            logger.logger.exception(F"{e.__class__.__name__} login_by_credentials failed with error: {e}")
            raise e

    @automation_logger(logger)
    def login_by_token(self, api_token: str, secret: str) -> object:
        """
        Sends HTTP POST request to AuthorizationService to log in by api_token and receive auth_token.
        :param api_token: Customer api_token- str.
        :param secret: Customer secret- str.
        :return: Response body as a JSON.
        """
        payload = AuthorizationServiceRequest().login_by_token(api_token, secret)
        try:
            _response = requests.post(self.api_url, data=payload, headers=self.headers)
            body = json.loads(_response.text)
            logger.logger.info("Service Response: {0}".format(body))
            return body
        except Exception as e:
            logger.logger.exception(F"{e.__class__.__name__} login_by_token failed with error: {e}")
            raise e

    @automation_logger(logger)
    def log_out(self) -> object:
        """
        Sends HTTP POST request to AuthorizationService to log out and invalidate auth_token.
        :return: Response body as a JSON.
        """
        payload = AuthorizationServiceRequest().log_out()
        try:
            _response = requests.post(self.api_url, data=payload, headers=self.headers)
            body = json.loads(_response.text)
            logger.logger.info("Service Response: {0}".format(body))
            return body
        except Exception as e:
            logger.logger.exception(F"{e.__class__.__name__} log_out failed with error: {e}")
            raise e

    @automation_logger(logger)
    def generate_password_hash(self, email: str, password: str) -> object:
        """
        Sends HTTP POST request to AuthorizationService to receive hashed password.
        :param email: Customer email.
        :param password: Customer password.
        :return: Response body as a JSON.
        """
        payload = AuthorizationServiceRequest().generate_password_hash(email, password)
        try:
            _response = requests.post(self.api_url, data=payload, headers=self.headers)
            body = json.loads(_response.text)
            logger.logger.info("Service Response: {0}".format(body))
            return body
        except Exception as e:
            logger.logger.exception(F"{e.__class__.__name__} generate_password_hash failed with error: {e}")
            raise e

    @automation_logger(logger)
    def update_personal_details(self, customer: object) -> object:
        """
        Sends HTTP POST request to AuthorizationService to update customer details.
        :param customer: Customer object.
        :return: Response body as a JSON.
        """
        payload = AuthorizationServiceRequest().update_personal_details(customer)
        try:
            _response = requests.post(self.api_url, data=payload, headers=self.headers)
            body = json.loads(_response.text)
            logger.logger.info("Service Response: {0}".format(body))
            return body
        except Exception as e:
            logger.logger.exception(F"{e.__class__.__name__} update_personal_details failed with error: {e}")
            raise e

    @automation_logger(logger)
    def validate_token(self, auth_token: str) -> object:
        """

        :param auth_token:
        :return:
        """
        payload = AuthorizationServiceRequest().validate_token(auth_token)
        try:
            _response = requests.post(self.api_url, data=payload, headers=self.headers)
            body = json.loads(_response.text)
            logger.logger.info("Service Response: {0}".format(body))
            return body
        except Exception as e:
            logger.logger.exception(F"{e.__class__.__name__} validate_token failed with error: {e}")
            raise e

    @automation_logger(logger)
    def get_needed_files(self) -> object:
        """

        :return:
        """
        payload = AuthorizationServiceRequest().get_needed_files()
        try:
            _response = requests.post(self.api_url, data=payload, headers=self.headers)
            body = json.loads(_response.text)
            logger.logger.info("Service Response: {0}".format(body))
            return body
        except Exception as e:
            logger.logger.exception(F"{e.__class__.__name__} get_needed_files failed with error: {e}")
            raise e

    @automation_logger(logger)
    def get_questionnaire(self) -> object:
        """

        :return:
        """
        payload = AuthorizationServiceRequest().get_questionnaire()
        try:
            _response = requests.post(self.api_url, data=payload, headers=self.headers)
            body = json.loads(_response.text)
            logger.logger.info("Service Response: {0}".format(body))
            return body
        except Exception as e:
            logger.logger.exception(F"{e.__class__.__name__} get_questionnaire failed with error: {e}")
            raise e

    @automation_logger(logger)
    def change_email_step1(self) -> object:
        """

        :return:
        """
        payload = AuthorizationServiceRequest().change_email_step1()
        try:
            _response = requests.post(self.api_url, data=payload, headers=self.headers)
            body = json.loads(_response.text)
            logger.logger.info("Service Response: {0}".format(body))
            return body
        except Exception as e:
            logger.logger.exception(F"{e.__class__.__name__} change_email_step1 failed with error: {e}")
            raise e

    @automation_logger(logger)
    def change_email_step2(self) -> object:
        """

        :return:
        """
        payload = AuthorizationServiceRequest().change_email_step2()
        try:
            _response = requests.post(self.api_url, data=payload, headers=self.headers)
            body = json.loads(_response.text)
            logger.logger.info("Service Response: {0}".format(body))
            return body
        except Exception as e:
            logger.logger.exception(F"{e.__class__.__name__} change_email_step2 failed with error: {e}")
            raise e

    @automation_logger(logger)
    def change_email_step3(self, mail_token=None, email=None) -> object:
        """

        :param mail_token:
        :param email:
        :return:
        """
        payload = AuthorizationServiceRequest().change_email_step3(mail_token, email)
        try:
            _response = requests.post(self.api_url, data=payload, headers=self.headers)
            body = json.loads(_response.text)
            logger.logger.info("Service Response: {0}".format(body))
            return body
        except Exception as e:
            logger.logger.exception(F"{e.__class__.__name__} change_email_step3 failed with error: {e}")
            raise e

    @automation_logger(logger)
    def change_email_step4(self, ver_token: str) -> object:
        """

        :param ver_token:
        :return:
        """
        payload = AuthorizationServiceRequest().change_email_step4(ver_token)
        try:
            _response = requests.post(self.api_url, data=payload, headers=self.headers)
            body = json.loads(_response.text)
            logger.logger.info("Service Response: {0}".format(body))
            return body
        except Exception as e:
            logger.logger.exception(F"{e.__class__.__name__} change_email_step4 failed with error: {e}")
            raise e

    @automation_logger(logger)
    def change_phone_step1(self) -> object:
        """

        :return:
        """
        payload = AuthorizationServiceRequest().change_phone_step1()
        try:
            _response = requests.post(self.api_url, data=payload, headers=self.headers)
            body = json.loads(_response.text)
            logger.logger.info("Service Response: {0}".format(body))
            return body
        except Exception as e:
            logger.logger.exception(F"{e.__class__.__name__} change_phone_step1 failed with error: {e}")
            raise e

    @automation_logger(logger)
    def change_phone_step2(self) -> object:
        """

        :return:
        """
        payload = AuthorizationServiceRequest().change_phone_step2()
        try:
            _response = requests.post(self.api_url, data=payload, headers=self.headers)
            body = json.loads(_response.text)
            logger.logger.info("Service Response: {0}".format(body))
            return body
        except Exception as e:
            logger.logger.exception(F"{e.__class__.__name__} change_phone_step2 failed with error: {e}")
            raise e

    @automation_logger(logger)
    def change_phone_step3(self, phone_token: str, full_phone: str) -> object:
        """

        :param phone_token:
        :param full_phone:
        :return:
        """
        payload = AuthorizationServiceRequest().change_phone_step3(phone_token, full_phone)
        try:
            _response = requests.post(self.api_url, data=payload, headers=self.headers)
            body = json.loads(_response.text)
            logger.logger.info("Service Response: {0}".format(body))
            return body
        except Exception as e:
            logger.logger.exception(F"{e.__class__.__name__} change_phone_step3 failed with error: {e}")
            raise e

    @automation_logger(logger)
    def change_phone_step4(self) -> object:
        """

        :return:
        """
        payload = AuthorizationServiceRequest().change_phone_step4()
        try:
            _response = requests.post(self.api_url, data=payload, headers=self.headers)
            body = json.loads(_response.text)
            logger.logger.info("Service Response: {0}".format(body))
            return body
        except Exception as e:
            logger.logger.exception(F"{e.__class__.__name__} change_phone_step4 failed with error: {e}")
            raise e

    @automation_logger(logger)
    def resend_sms(self) -> object:
        """

        :return:
        """
        payload = AuthorizationServiceRequest().resend_sms()
        try:
            _response = requests.post(self.api_url, data=payload, headers=self.headers)
            body = json.loads(_response.text)
            logger.logger.info("Service Response: {0}".format(body))
            return body
        except Exception as e:
            logger.logger.exception(F"{e.__class__.__name__} resend_sms failed with error: {e}")
            raise e

    @automation_logger(logger)
    def resend_email(self) -> object:
        """

        :return:
        """
        payload = AuthorizationServiceRequest().resend_email()
        try:
            _response = requests.post(self.api_url, data=payload, headers=self.headers)
            body = json.loads(_response.text)
            logger.logger.info("Service Response: {0}".format(body))
            return body
        except Exception as e:
            logger.logger.exception(F"{e.__class__.__name__} resend_email failed with error: {e}")
            raise e

    @automation_logger(logger)
    def forgot_password_step1(self, email) -> object:
        """

        :return:
        """
        payload = AuthorizationServiceRequest().forgot_password_step1(email)
        try:
            _response = requests.post(self.api_url, data=payload, headers=self.headers)
            body = json.loads(_response.text)
            logger.logger.info("Service Response: {0}".format(body))
            return body
        except Exception as e:
            logger.logger.exception(F"{e.__class__.__name__} forgot_password_step1 failed with error: {e}")
            raise e

    @automation_logger(logger)
    def forgot_password_step2(self, email, ver_token, new_password) -> object:
        """

        :return:
        """
        payload = AuthorizationServiceRequest().forgot_password_step2(email, ver_token, new_password)
        try:
            _response = requests.post(self.api_url, data=payload, headers=self.headers)
            body = json.loads(_response.text)
            logger.logger.info("Service Response: {0}".format(body))
            return body
        except Exception as e:
            logger.logger.exception(F"{e.__class__.__name__} forgot_password_step2 failed with error: {e}")
            raise e

    @automation_logger(logger)
    def reset_password(self) -> object:
        """

        :return:
        """
        payload = AuthorizationServiceRequest().reset_password()
        try:
            _response = requests.post(self.api_url, data=payload, headers=self.headers)
            body = json.loads(_response.text)
            logger.logger.info("Service Response: {0}".format(body))
            return body
        except Exception as e:
            logger.logger.exception(F"{e.__class__.__name__} reset_password failed with error: {e}")
            raise e

    @automation_logger(logger)
    def change_password(self, password, new_password) -> object:
        """

        :return:
        """
        payload = AuthorizationServiceRequest().change_password(password, new_password)
        try:
            _response = requests.post(self.api_url, data=payload, headers=self.headers)
            body = json.loads(_response.text)
            logger.logger.info("Service Response: {0}".format(body))
            return body
        except Exception as e:
            logger.logger.exception(F"{e.__class__.__name__} change_password failed with error: {e}")
            raise e


    @automation_logger(logger)
    def change_subscriptions(self, email_option, sms_option, mobile_option) -> object:
        """
        Changes customer's subscriptions.
        Customer can be subscribed to email, sms and mobile adds and updates
        Existing customer subscriptions are saved in DB - "customers" table
        and provided in Customer Data (Trade Service).

        :return:
        """
        payload = AuthorizationServiceRequest().change_subscriptions(email_option, sms_option, mobile_option)
        try:
            _response = requests.post(self.api_url, data=payload, headers=self.headers)
            body = json.loads(_response.text)
            logger.logger.info("Service Response: {0}".format(body))
            return body
        except Exception as e:
            logger.logger.exception(F"{e.__class__.__name__} change_subscriptions failed with error: {e}")
            raise e

    @automation_logger(logger)
    def get_login_logs(self) -> object:

        """

        :return:
        """
        payload = AuthorizationServiceRequest().get_login_logs()
        try:
            _response = requests.post(self.api_url, data=payload, headers=self.headers)
            body = json.loads(_response.text)
            logger.logger.info("Service Response: {0}".format(body))
            return body
        except Exception as e:
            logger.logger.exception(F"{e.__class__.__name__} get_login_logs failed with error: {e}")
            raise e

    @automation_logger(logger)
    def reset_phone(self) -> object:

        """

        :return:
        """
        payload = AuthorizationServiceRequest().reset_phone()
        try:
            _response = requests.post(self.api_url, data=payload, headers=self.headers)
            body = json.loads(_response.text)
            logger.logger.info("Service Response: {0}".format(body))
            return body
        except Exception as e:
            logger.logger.exception(F"{e.__class__.__name__} reset_phone failed with error: {e}")
            raise e

    @automation_logger(logger)
    def sign_up_step_back(self) -> object:
        """

        :return:
        """
        payload = AuthorizationServiceRequest().signup_step_back()
        try:
            _response = requests.post(self.api_url, data=payload, headers=self.headers)
            body = json.loads(_response.text)
            logger.logger.info("Service Response: {0}".format(body))
            return body
        except Exception as e:
            logger.logger.exception(F"{e.__class__.__name__} sign_up_step_back failed with error: {e}")
            raise e
