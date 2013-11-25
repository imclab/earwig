import uuid

import boto.ses

<<<<<<< HEAD
from ..utils import template_to_string
from .models import SESDeliveryMeta
from .. import EmailContactPlugin
=======
from ..utils import body_template_to_string, subject_template_to_string
from .models import SESEmailStatus
from .. import ContactPlugin
>>>>>>> fd0edb7e78dddc1fe927534aa30d977618c59280


class SESContact(EmailContactPlugin):
    '''Amazon SES contact plugin.

    Bounce requests would be configured with SNS:
    http://aws.amazon.com/about-aws/whats-new/2012/06/26/amazon-ses-announces-bounce-and-complaint-notifications/

    The alternative is setting up a special address to reveive them
    by email, which would suck.
    '''
    medium = 'email'

    def send_message(self, attempt, extra_context=None):
        self.check_contact_detail(attempt)
        contact_detail = attempt.contact
        email_address = contact_detail.value

        message = body_template_to_string('default', 'email', attempt)
        subject = subject_template_to_string('default', 'email', attempt)

        conn = boto.ses.connect_to_region()
        resp = conn.send_email(
             source=self.get_sender_address(attempt),
             subject=subject,
             body=body,
             to_addresses=[email_address],
             reply_addresses=self.get_reply_addreses(attempt))

        request_id = resp['SendEmailResponse']['ResponseMetadata']['RequestID']
        message_id = resp['SendEmailResult']['MessageId']
        obj = SentEmailStatus.create(
            attempt=attempt, request_id=request_id, message_id=message_id)

    def check_message_status(self, attempt):
        '''This function depends on shape of SNS notifactions and
        the output we want from this funtion.
        '''
        obj = SESDeliveryMetadata.get(attempt=attempt)
        raise NotImplementedError()
