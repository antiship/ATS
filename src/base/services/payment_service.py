import json
import requests
from src.base import logger
from src.base.utils.calculator import Calculator
from src.base.log_decorator import automation_logger
from src.base.services.service_route import ServiceRoute
from src.base.services.svc_requests.payment_requests import PaymentServiceRequest


class PaymentService(ServiceRoute):
    def __init__(self, auth_token=None):
        super(PaymentService, self).__init__()
        self.headers.update({'Authorization': auth_token})

    @automation_logger(logger)
    def get_credit_cards(self) -> object:
        """
        Sends HTTP POST request to PaymentServiceRequest to receive customer credit cards.
        :return: Response body as a JSON.
        """
        payload = PaymentServiceRequest().cards()
        try:
            _response = requests.post(self.api_url, data=payload, headers=self.headers)
            body = json.loads(_response.text)
            logger.logger.info("Service Response: {0}".format(body))
            return body
        except Exception as e:
            logger.logger.exception(F"{e.__class__.__name__} get_credit_cards failed with error: {e}")
            raise e

    @automation_logger(logger)
    def upload_credit_card_images(self, card_id: int, file_link: str) -> object:
        """

        :param card_id: Card ID- int 1 - Verified, 2- unverified, 3 - Deleted, 4 - Disabled, 5- expired.
        :param file_link: Link on to customer wallet- str.
        :return: Response body as a JSON.
        """
        payload = PaymentServiceRequest().upload_credit_card_images(card_id, file_link)
        try:
            _response = requests.post(self.api_url, data=payload, headers=self.headers)
            body = json.loads(_response.text)
            logger.logger.info("Service Response: {0}".format(body))
            return body
        except Exception as e:
            logger.logger.exception(F"{e.__class__.__name__} upload_credit_card_images failed with error: {e}")
            raise e

    @automation_logger(logger)
    def update_credit_card(self, card_id: int, status: int) -> object:
        """
        Sends HTTP POST request to PaymentServiceRequest to receive customer credit cards.
        :param card_id: Card ID- int 1 - Verified, 2- unverified, 3 - Deleted, 4 - Disabled, 5- expired.
        :param status: True if active and False otherwise.
        :return: Response body as a JSON.
        """
        payload = PaymentServiceRequest().update_credit_card_status(card_id, status)
        try:
            _response = requests.post(self.api_url, data=payload, headers=self.headers)
            body = json.loads(_response.text)
            logger.logger.info("Service Response: {0}".format(body))
            return body
        except Exception as e:
            logger.logger.exception(F"{e.__class__.__name__} update_credit_card failed with error: {e}")
            raise e

    @automation_logger(logger)
    def add_credit_card(self, credit_card: object) -> object :
        """
        Sends HTTP POST request to PaymentServiceRequest to store customer credit card onto Platform Server.
        :param credit_card: object of class CreditCard.
        :return: Response body as a JSON.
        """
        payload = PaymentServiceRequest().add_card(credit_card)
        try:
            _response = requests.post(self.api_url, data=payload, headers=self.headers)
            body = json.loads(_response.text)
            logger.logger.info("Service Response: {0}".format(body))
            if "id" in body.keys() and body['result']:
                credit_card.id = body['result']['card']['id']
            return body
        except Exception as e:
            logger.logger.exception(F"{e.__class__.__name__} add_credit_card failed with error: {e}")
            raise e

    @automation_logger(logger)
    def add_deposit_credit_card(self, credit_card: object, deposit_amount: float, currency_id: int) -> object:
        """
        Sends HTTP POST request to PaymentServiceRequest to add deposit onto customer credit card.
        :param credit_card: object of class CreditCard.
        :param deposit_amount: Amount-float.
        :param currency_id: Currency ID- int.
        :return: Response body as a JSON.
        """

        deposit_amount_value, deposit_amount_value_decimals = Calculator.calculate_decimals(deposit_amount)

        payload = PaymentServiceRequest().deposit_credit_card(
            credit_card, deposit_amount_value, deposit_amount_value_decimals, currency_id)
        try:
            _response = requests.post(self.api_url, data=payload, headers=self.headers)
            body = json.loads(_response.text)
            logger.logger.info("Service Response: {0}".format(body))
            return body
        except Exception as e:
            logger.logger.exception(F"{e.__class__.__name__} add_deposit_credit_card failed with error: {e}")
            raise e

    @automation_logger(logger)
    def withdrawal_credit_card(self, card_id: int, withdrawal_amount: float, currency: str) -> object:
        """
        Sends HTTP POST request to PaymentServiceRequest to perform withdrawal from customer credit card.
        :param card_id: Credit card ID- int.
        :param withdrawal_amount: Amount-float.
        :param currency: Currency code- str like "EUR".
        :return: Response body as a JSON.
        """
        payload = PaymentServiceRequest().withdrawal_credit_card(card_id, withdrawal_amount, currency)
        try:
            _response = requests.post(self.api_url, data=payload, headers=self.headers)
            body = json.loads(_response.text)
            logger.logger.info("Service Response: {0}".format(body))
            return body
        except Exception as e:
            logger.logger.exception(F"{e.__class__.__name__} withdrawal_credit_card failed with error: {e}")
            raise e

    @automation_logger(logger)
    def withdrawal_credit_card_sms_confirmation(self, withdrawal_token: str) -> object:
        """
        Sends HTTP POST request to PaymentServiceRequest to confirm withdrawal from customer credit card.
        :param withdrawal_token: Token- str.
        :return: Response body as a JSON.
        """
        payload = PaymentServiceRequest().withdrawal_credit_card_sms_confirmation(withdrawal_token)
        try:
            _response = requests.post(self.api_url, data=payload, headers=self.headers)
            body = json.loads(_response.text)
            logger.logger.info("Service Response: {0}".format(body))
            return body
        except Exception as e:
            logger.logger.exception(F"{e.__class__.__name__} withdrawal_credit_card_sms_confirmation failed with: {e}")
            raise e

    @automation_logger(logger)
    def withdrawal_credit_card_resend_sms(self, withdrawal_token: str) -> object:
        """
        Sends HTTP POST request to PaymentServiceRequest to request a new sms for requested withdrawal.
        :param withdrawal_token: Token- str.
        :return: Response body as a JSON.
        """
        payload = PaymentServiceRequest().withdrawal_credit_card_sms_confirmation(withdrawal_token)
        try:
            _response = requests.post(self.api_url, data=payload, headers=self.headers)
            body = json.loads(_response.text)
            logger.logger.info("Service Response: {0}".format(body))
            return body
        except Exception as e:
            logger.logger.exception(F"{e.__class__.__name__} withdrawal_credit_card_resend_sms failed with error: {e}")
            raise e

    @automation_logger(logger)
    def withdrawal_cancel(self, withdrawal_id: int) -> object:
        """
        Sends HTTP POST request to PaymentServiceRequest to cancel requested withdrawal.
        :param withdrawal_id: Withdrawal ID- int.
        :return: Response body as a JSON.
        """
        payload = PaymentServiceRequest().withdrawal_cancel(withdrawal_id)
        try:
            _response = requests.post(self.api_url, data=payload, headers=self.headers)
            body = json.loads(_response.text)
            logger.logger.info("Service Response: {0}".format(body))
            return body
        except Exception as e:
            logger.logger.exception(F"{e.__class__.__name__} withdrawal_cancel failed with error: {e}")
            raise e

    @automation_logger(logger)
    def add_deposit_crypto(self, currency_id: int) -> object:
        """
        Sends HTTP POST request to PaymentServiceRequest to add deposit crypto on customer account.
        :param currency_id: Currency ID- int.
        :return: Response body as a JSON.
        """
        payload = PaymentServiceRequest().deposit_crypto(currency_id)
        try:
            _response = requests.post(self.api_url, data=payload, headers=self.headers)
            body = json.loads(_response.text)
            logger.logger.info("Service Response: {0}".format(body))
            return body
        except Exception as e:
            logger.logger.exception(F"{e.__class__.__name__} add_deposit_crypto failed with error: {e}")
            raise e

    @automation_logger(logger)
    def withdrawal_crypto(self, currency_id: int, withdrawal_amount: float,
                          wallet_link: str = "bchtest:qrtr282l55cg94lkjcrykf9nzxh4j8hj95zmul7mwf") -> object:
        """
        Sends HTTP POST request to PaymentServiceRequest to perform withdrawal crypto from customer account.
        :param currency_id: Currency ID- int.
        :param withdrawal_amount: Amount-float.
        :param wallet_link: Link on to customer wallet- str.
        :return: Response body as a JSON.
        """

        withdrawal_amount_value, withdrawal_amount_value_decimals = Calculator.calculate_decimals(withdrawal_amount)

        payload = PaymentServiceRequest().withdrawal_crypto(currency_id, withdrawal_amount_value,withdrawal_amount_value_decimals , wallet_link)
        try:
            _response = requests.post(self.api_url, data=payload, headers=self.headers)
            body = json.loads(_response.text)
            logger.logger.info("Service Response: {0}".format(body))
            return body
        except Exception as e:
            logger.logger.exception(F"{e.__class__.__name__} withdrawal_crypto failed with error: {e}")
            raise e

    @automation_logger(logger)
    def withdrawal_crypto_sms_confirmation(self, withdrawal_token: str) -> object:
        """
        Sends HTTP POST request to PaymentServiceRequest to confirm withdrawal crypto via customer phone number.
        :param withdrawal_token: token received on WithdrawalCrypto request as str.
        :return: Response body as a JSON.
        """
        payload = PaymentServiceRequest().withdrawal_crypto_sms_confirmation(withdrawal_token)
        try:
            _response = requests.post(self.api_url, data=payload, headers=self.headers)
            body = json.loads(_response.text)
            logger.logger.info("Service Response: {0}".format(body))
            return body
        except Exception as e:
            logger.logger.exception(F"{e.__class__.__name__} withdrawal_crypto_sms_confirmation failed with error: {e}")
            raise e

    @automation_logger(logger)
    def withdrawal_crypto_resend_sms(self, withdrawal_token: str) -> object:
        """
        Sends HTTP POST request to PaymentServiceRequest to request a new sms for requested withdrawal.
        :param withdrawal_token: token received on WithdrawalCrypto request as str.
        :return: Response body as a JSON.
        """
        payload = PaymentServiceRequest().withdrawal_crypto_resend_sms(withdrawal_token)
        try:
            _response = requests.post(self.api_url, data=payload, headers=self.headers)
            body = json.loads(_response.text)
            logger.logger.info("Service Response: {0}".format(body))
            return body
        except Exception as e:
            logger.logger.exception(F"{e.__class__.__name__} withdrawal_crypto_resend_sms failed with error: {e}")
            raise e

    @automation_logger(logger)
    def withdrawal_wire(self, bank: object, currency_id: int, withdrawal_amount: float) -> object:
        """
        Sends HTTP POST request to PaymentServiceRequest to perform withdrawal crypto from customer account.
        :param bank: object of class Bank
        :param currency_id: Currency ID- int.
        :param withdrawal_amount: Amount-float.
        :return: Response body as a JSON.
        """

        withdrawal_amount_value, withdrawal_amount_value_decimals = Calculator.calculate_decimals(withdrawal_amount)

        payload = PaymentServiceRequest().withdrawal_wire(
            bank, currency_id, withdrawal_amount_value, withdrawal_amount_value_decimals)
        try:
            _response = requests.post(self.api_url, data=payload, headers=self.headers)
            body = json.loads(_response.text)
            logger.logger.info("Service Response: {0}".format(body))
            return body
        except Exception as e:
            logger.logger.exception(F"{e.__class__.__name__} withdrawal_wire failed with error: {e}")
            raise e

    @automation_logger(logger)
    def withdrawal_wire_sms_confirmation(self, withdrawal_token: str) -> object:
        """
        Sends HTTP POST request to PaymentServiceRequest to confirm withdrawal crypto via sms.
        :param withdrawal_token: Link on to customer wallet- str.
        :return: Response body as a JSON.
        """
        payload = PaymentServiceRequest().withdrawal_wire_sms_confirmation(withdrawal_token)
        try:
            _response = requests.post(self.api_url, data=payload, headers=self.headers)
            body = json.loads(_response.text)
            logger.logger.info("Service Response: {0}".format(body))
            return body
        except Exception as e:
            logger.logger.exception(F"{e.__class__.__name__} withdrawal_wire_sms_confirmation failed with error: {e}")
            raise e

    @automation_logger(logger)
    def withdrawal_wire_resend_sms(self, withdrawal_token: str) -> object:
        """
        Sends HTTP POST request to PaymentServiceRequest to request a new sms for requested withdrawal.
        :param withdrawal_token: Link on to customer wallet- str.
        :return: Response body as a JSON.
        """
        payload = PaymentServiceRequest().withdrawal_wire_resend_sms(withdrawal_token)
        try:
            _response = requests.post(self.api_url, data=payload, headers=self.headers)
            body = json.loads(_response.text)
            logger.logger.info("Service Response: {0}".format(body))
            return body
        except Exception as e:
            logger.logger.exception(F"{e.__class__.__name__} withdrawal_wire_resend_sms failed with error: {e}")
            raise e

    @automation_logger(logger)
    def withdrawal_sepa(self, bank: object, currency_id: int, withdrawal_amount: float) -> object:
        """
        Sends HTTP POST request to PaymentServiceRequest to perform withdrawal crypto from customer account.
        :param bank: object of class Bank
        :param currency_id: Currency ID- int.
        :param withdrawal_amount: Amount-float.
        :return: Response body as a JSON.
        """
        withdrawal_amount_value, withdrawal_amount_value_decimals = Calculator.calculate_decimals(withdrawal_amount)

        payload = PaymentServiceRequest().withdrawal_wire(
            bank, currency_id, withdrawal_amount_value, withdrawal_amount_value_decimals)
        try:
            _response = requests.post(self.api_url, data=payload, headers=self.headers)
            body = json.loads(_response.text)
            logger.logger.info("Service Response: {0}".format(body))
            return body
        except Exception as e:
            logger.logger.exception(F"{e.__class__.__name__} withdrawal_sepa failed with error: {e}")
            raise e

    @automation_logger(logger)
    def withdrawal_sepa_sms_confirmation(self, withdrawal_token: str) -> object:
        """
        Sends HTTP POST request to PaymentServiceRequest to confirm withdrawal crypto via customer phone number.
        :param withdrawal_token: Link on to customer wallet- str.
        :return: Response body as a JSON.
        """
        payload = PaymentServiceRequest().withdrawal_sepa_sms_confirmation(withdrawal_token)
        try:
            _response = requests.post(self.api_url, data=payload, headers=self.headers)
            body = json.loads(_response.text)
            logger.logger.info("Service Response: {0}".format(body))
            return body
        except Exception as e:
            logger.logger.exception(F"{e.__class__.__name__} withdrawal_sepa_sms_confirmation failed with error: {e}")
            raise e

    @automation_logger(logger)
    def withdrawal_sepa_resend_sms(self, withdrawal_token: str) -> object:
        """
        Sends HTTP POST request to PaymentServiceRequest to request a new sms for requested withdrawal.
        :param withdrawal_token: Link on to customer wallet- str.
        :return: Response body as a JSON.
        """
        payload = PaymentServiceRequest().withdrawal_sepa_resend_sms(withdrawal_token)
        try:
            _response = requests.post(self.api_url, data=payload, headers=self.headers)
            body = json.loads(_response.text)
            logger.logger.info("Service Response: {0}".format(body))
            return body
        except Exception as e:
            logger.logger.exception(F"{e.__class__.__name__} withdrawal_sepa_resend_sms failed with error: {e}")
            raise e

    @automation_logger(logger)
    def export_deposit_history(self, method_id=1) -> object:
        """
        Sends HTTP POST request to PaymentServiceRequest to deposit get_history.
        :return: Response body as a JSON.
        """
        payload = PaymentServiceRequest().export_deposit_history(method_id)
        try:
            _response = requests.post(self.api_url, data=payload, headers=self.headers)
            body = json.loads(_response.text)
            logger.logger.info("Service Response: {0}".format(body))
            return body
        except Exception as e:
            logger.logger.exception(F"{e.__class__.__name__} export_deposit_history failed with error: {e}")
            raise e

    @automation_logger(logger)
    def export_withdrawal_history(self, method_id=1) -> object:
        """
        Sends HTTP POST request to PaymentServiceRequest to withdrawal get_history.
        :return: Response body as a JSON.
        """
        payload = PaymentServiceRequest().export_withdrawal_history(method_id)
        try:
            _response = requests.post(self.api_url, data=payload, headers=self.headers)
            body = json.loads(_response.text)
            logger.logger.info("Service Response: {0}".format(body))
            return body
        except Exception as e:
            logger.logger.exception(F"{e.__class__.__name__} export_withdrawal_history failed with error: {e}")
            raise e

    @automation_logger(logger)
    def export_fee_history(self) -> object:
        """
        Sends HTTP POST request to PaymentServiceRequest to receive fee get_history.
        :return: Response body as a JSON.
        """
        payload = PaymentServiceRequest().export_fee_history()
        try:
            _response = requests.post(self.api_url, data=payload, headers=self.headers)
            body = json.loads(_response.text)
            logger.logger.info("Service Response: {0}".format(body))
            return body
        except Exception as e:
            logger.logger.exception(F"{e.__class__.__name__} export_fee_history failed with error: {e}")
            raise e

    @automation_logger(logger)
    def get_withdrawal_history(self, method_id=1, *args) -> object:
        """
        Sends HTTP POST request to PaymentServiceRequest to withdrawal get_history.
        :return: Response body as a JSON.
        """
        payload = PaymentServiceRequest().withdrawal_history(method_id, args)
        try:
            _response = requests.post(self.api_url, data=payload, headers=self.headers)
            body = json.loads(_response.text)
            logger.logger.info("Service Response: {0}".format(body))
            return body
        except Exception as e:
            logger.logger.exception(F"{e.__class__.__name__} get_withdrawal_history failed with error: {e}")
            raise e

    @automation_logger(logger)
    def get_deposit_history(self, method_id=1, *args) -> object:
        """
        Sends HTTP POST request to PaymentServiceRequest to deposit get_history.
        :return: Response body as a JSON.
        """
        payload = PaymentServiceRequest().deposit_history(method_id, args)
        try:
            _response = requests.post(self.api_url, data=payload, headers=self.headers)
            body = json.loads(_response.text)
            logger.logger.info("Service Response: {0}".format(body))
            return body
        except Exception as e:
            logger.logger.exception(F"{e.__class__.__name__} get_deposit_history failed with error: {e}")
            raise e

    @automation_logger(logger)
    def get_fee_history(self, *args) -> object:
        """
        Sends HTTP POST request to PaymentServiceRequest to receive fee get_history.
        :return: Response body as a JSON.
        """
        payload = PaymentServiceRequest().fee_history(args)
        try:
            _response = requests.post(self.api_url, data=payload, headers=self.headers)
            body = json.loads(_response.text)
            logger.logger.info("Service Response: {0}".format(body))
            return body
        except Exception as e:
            logger.logger.exception(F"{e.__class__.__name__} get_fee_history failed with error: {e}")
            raise e

    @automation_logger(logger)
    def get_portfolio_chat(self, currency_id: int) -> object:
        """
        Sends HTTP POST request to PaymentServiceRequest to receive portfolio chat data.
        :param currency_id: Currency ID- int
        :return: Response body as a JSON.
        """
        payload = PaymentServiceRequest().portfolio_chat(currency_id)
        try:
            _response = requests.post(self.api_url, data=payload, headers=self.headers)
            body = json.loads(_response.text)
            logger.logger.info("Service Response: {0}".format(body))
            return body
        except Exception as e:
            logger.logger.exception(F"{e.__class__.__name__} get_portfolio_chat failed with error: {e}")
            raise e


