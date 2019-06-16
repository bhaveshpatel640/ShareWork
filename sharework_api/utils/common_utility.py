# -*- coding: utf-8 -*-
__author__ = " Bhavesh Patel"

# python dependencies
import string
import random


class CommonUtility:
    """
    CommonUtility is a class which provide basic functionality for Business Logic service
    """
    @staticmethod
    def generate_short_url(size):
        """ generate_short_url function is used to generate short_url of length `size` with Uppercase and Lowercase characters

        @returns:
            This will return 32 character uuid
        """
        chars = string.ascii_lowercase + string.digits + string.ascii_uppercase
        return ''.join(random.choice(chars) for _ in range(size))
